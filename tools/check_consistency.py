#!/usr/bin/env python3
"""Static consistency checker for zmk-config-ortho20_20.

Verifies matrix geometry, keymap layer sizes, the ZMK Studio layout JSON, the
left/right kscan wiring against the project's own BOM manual, the split matrix
transform offset, and the ZMK build inputs -- without needing a Zephyr toolchain.

Usage:  python tools/check_consistency.py
Exit code 0 = all checks passed, 1 = at least one failure.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DTS = ROOT / "boards" / "shields" / "ortho20_20"
CONFIG = ROOT / "config"

# nice!nano v2 pro_micro index -> raw nRF52840 pin
# Source: zmk/app/boards/arm/nice_nano/arduino_pro_micro_pins.dtsi (ZMK v0.3)
PM = {
    0: "P0.08", 1: "P0.06", 2: "P0.17", 3: "P0.20", 4: "P0.22", 5: "P0.24",
    6: "P1.00", 7: "P0.11", 8: "P1.04", 9: "P1.06", 10: "P0.09",
    14: "P1.11", 15: "P1.13", 16: "P0.10", 18: "P1.15", 19: "P0.02",
    20: "P0.29", 21: "P0.31",
}

# Expected wiring, from Media/20_20 split keyboard BOM and manual.md
# Both halves are wired identically: columns 106/104/011/100/024/022, rows 113/111/010/009.
EXPECT = {
    "left": {
        "cols": ["P1.06", "P1.04", "P0.11", "P1.00", "P0.24", "P0.22"],
        "rows": ["P1.13", "P1.11", "P0.10", "P0.09"],
    },
    "right": {
        "cols": ["P1.06", "P1.04", "P0.11", "P1.00", "P0.24", "P0.22"],
        "rows": ["P1.13", "P1.11", "P0.10", "P0.09"],
    },
}

failures = 0


def chk(cond, msg):
    global failures
    print(("  PASS  " if cond else "  FAIL  ") + msg)
    if not cond:
        failures += 1


def resolve_pins(block):
    """Resolve '<&pro_micro N ...>' / '<&gpioX Y ...>' entries to raw pin names."""
    pins = []
    for node, idx in re.findall(r"<&(pro_micro|gpio[01])\s+(\d+)", block):
        idx = int(idx)
        if node == "pro_micro":
            pins.append(PM.get(idx, f"?pro_micro{idx}"))
        else:
            pins.append(f"P{node[-1]}.{idx:02d}")
    return pins


def main():
    print("== 1. matrix geometry ==")
    dtsi = (DTS / "ortho20_20.dtsi").read_text(encoding="utf-8")
    cols = int(re.search(r"columns\s*=\s*<(\d+)>", dtsi).group(1))
    rows = int(re.search(r"rows\s*=\s*<(\d+)>", dtsi).group(1))
    total = cols * rows
    map_cells = re.findall(r"RC\(\d+,\d+\)", dtsi)
    layouts = (DTS / "ortho20_20-layouts.dtsi").read_text(encoding="utf-8")
    keys_attr = re.findall(r"&key_physical_attrs", layouts)
    chk(total == 48, f"transform grid {cols}x{rows} = {total} positions")
    chk(len(map_cells) == total, f"transform map entries = {len(map_cells)} (expected {total})")
    chk(len(keys_attr) == total, f"physical-layout keys = {len(keys_attr)} (expected {total})")

    keymap = (CONFIG / "ortho20_20.keymap").read_text(encoding="utf-8")
    for layer, body in re.findall(r"(\w+_layer)\s*\{(.*?)\n        \};", keymap, re.S):
        bindings = re.search(r"bindings\s*=\s*<(.*?)>;", body, re.S).group(1)
        n = len(re.findall(r"&(?:kp|mo|trans|bt|out)\b", bindings))
        chk(n == total, f"keymap layer '{layer}' bindings = {n} (expected {total})")

    lay = json.loads((CONFIG / "ortho20_20.json").read_text(encoding="utf-8"))
    lay = lay["layouts"]["ortho20_20"]["layout"]
    chk(len(lay) == total, f"studio json layout entries = {len(lay)} (expected {total})")
    attrs = re.findall(r"&key_physical_attrs\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", layouts)
    bad = [i for i, (_, _, x, y) in enumerate(attrs)
           if int(x) != lay[i]["x"] * 100 or int(y) != lay[i]["y"] * 100]
    chk(not bad, f"studio json x/y matches devicetree physical layout ({len(bad)} mismatches)")

    print("== 2. kscan wiring vs BOM manual ==")
    for half in ("left", "right"):
        ov = (DTS / f"ortho20_20_{half}.overlay").read_text(encoding="utf-8")
        cblk = re.search(r"col-gpios(.*?);", ov, re.S).group(1)
        rblk = re.search(r"row-gpios(.*?);", ov, re.S).group(1)
        active = "\n".join(l for l in cblk.splitlines() if not l.strip().startswith("//"))
        col_pins = resolve_pins(active)
        row_pins = resolve_pins(rblk)
        print(f"  [{half}] cols={col_pins}")
        print(f"  [{half}] rows={row_pins}")
        chk(col_pins == EXPECT[half]["cols"],
            f"{half} column pins == manual table {EXPECT[half]['cols']}")
        chk(row_pins == EXPECT[half]["rows"],
            f"{half} row pins == manual table {EXPECT[half]['rows']}")
        chk(len(col_pins) == 6 and len(row_pins) == 4,
            f"{half} matrix = {len(col_pins)}x{len(row_pins)} (expected 6x4)")

    print("== 3. split transform ==")
    right = (DTS / "ortho20_20_right.overlay").read_text(encoding="utf-8")
    m = re.search(r"col-offset\s*=\s*<(\d+)>", right)
    chk(bool(m) and int(m.group(1)) == 6,
        f"right half col-offset = {m.group(1) if m else None} (expected 6)")

    print("== 4. combo positions ==")
    cp = [int(x) for x in re.search(r"key-positions\s*=\s*<([^>]+)>", keymap).group(1).split()]
    for p in cp:
        r, c = divmod(p, cols)
        print(f"  combo pos {p} -> row {r}, col {c} ({'left' if c < 6 else 'right'} half)")
    chk(all(0 <= p < total for p in cp), "combo key-positions inside keymap range")

    print("== 5. ZMK build inputs ==")
    by = (ROOT / "build.yaml").read_text(encoding="utf-8")
    chk("board: nice_nano_v2" in by, "build.yaml board target nice_nano_v2 (valid in ZMK v0.3)")
    chk("ortho20_20_left" in by and "ortho20_20_right" in by, "both halves present in build matrix")
    chk("settings_reset" in by, "settings_reset artifact present (shield ships its own keymap)")
    west = (CONFIG / "west.yml").read_text(encoding="utf-8")
    chk("revision: v0.3" in west, "west.yml pins ZMK revision v0.3 (tag exists)")
    chk(re.search(r"self:\s*\n\s*path:\s*config", west) is not None,
        "west.yml self path = config (so ZMK_CONFIG=<repo>/config)")

    print()
    print("RESULT:", "ALL CHECKS PASSED" if not failures else f"{failures} CHECK(S) FAILED")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
