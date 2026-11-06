#!/usr/bin/env python3
"""Resolve every physical key -> ZMK keymap position -> binding.

Re-implements ZMK v0.3's exact resolution chain so that "which binding does this
key press produce?" can be answered without a toolchain:

  1. `zmk,matrix-transform` builds a lookup table at compile time:
        lookup_table[ map[i].row * columns + map[i].col ] = i + 1
     (app/src/matrix_transform.c, TRANSFORM_LOOKUP_ENTRY)
  2. `zmk_matrix_transform_row_column_to_position()` adds col_offset/row_offset,
     looks the row/column up, and returns `value - 1` -> the keymap position.
  3. The keymap position indexes the layer's `bindings` array.

Usage:  python tools/verify_positions.py
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DTSI = ROOT / "boards" / "shields" / "ortho20_20" / "ortho20_20.dtsi"
KEYMAP = ROOT / "config" / "ortho20_20.keymap"

# Keycap legends as physically populated (Media/Studio unlock combo.png + user photo).
LEFT = [
    ["Esc", "Q", "W", "E", "R", "T"],
    ["F5", "A", "S", "D", "F", "G"],
    ["F6", "Z", "X", "C", "V", "B"],
    ["ScrLk", "F1", "F2", "F3", "PgOn", "F7"],
]
RIGHT = [
    ["Y", "U", "I", "O", "P", "Delete"],
    ["H", "J", "K", "L", ";", "End"],
    ["N", "M", "<", ">", "UP", "?/"],
    ["F8", "PgUp", "F4", "LEFT", "DOWN", "RIGHT"],
]

# Bindings that produce no visible character when tapped on their own.
NO_VISIBLE_OUTPUT = {
    "kp LCTRL", "kp LGUI", "kp LALT", "kp RGUI", "kp LSFT", "kp LSHFT", "trans",
}


def main():
    dtsi = DTSI.read_text(encoding="utf-8")
    keymap = KEYMAP.read_text(encoding="utf-8")

    cols = int(re.search(r"columns\s*=\s*<(\d+)>", dtsi).group(1))
    rows = int(re.search(r"rows\s*=\s*<(\d+)>", dtsi).group(1))
    mapcells = [(int(a), int(b)) for a, b in re.findall(r"RC\((\d+),(\d+)\)", dtsi)]
    print(f"transform: columns={cols} rows={rows} map entries={len(mapcells)}")

    lookup = {}
    for i, (r, c) in enumerate(mapcells):
        lookup[r * cols + c] = i + 1

    def position(row, col, col_offset=0):
        idx = (row * cols) + col + col_offset
        val = lookup.get(idx, 0)
        return None if val == 0 else val - 1

    layers = {}
    for name, body in re.findall(r"(\w+_layer)\s*\{(.*?)\n        \};", keymap, re.S):
        b = re.search(r"bindings\s*=\s*<(.*?)>;", body, re.S).group(1)
        layers[name] = [f"{m} {p}".strip() for m, p in re.findall(r"&(\w+)\s+([A-Z0-9_]+)?", b)]

    for name, bindings in layers.items():
        print(f"layer {name}: {len(bindings)} bindings")

    failures = 0
    for half, caps, off in (("LEFT", LEFT, 0), ("RIGHT", RIGHT, 6)):
        print(f"\n===== {half} HALF (col-offset={off}) =====")
        for r in range(4):
            cells = []
            for c in range(6):
                p = position(r, c, off)
                if p is None:
                    failures += 1
                    cells.append(f"{caps[r][c]:>6}->UNMAPPED")
                    continue
                cells.append(f"{caps[r][c]:>6}->p{p:<3}{layers['default_layer'][p]}")
            print("  " + " | ".join(cells))

    print("\n===== positions with no visible output on layer 0 (modifier / trans) =====")
    for i, b in enumerate(layers["default_layer"]):
        if b in NO_VISIBLE_OUTPUT:
            print(f"  pos {i}: {b}")

    print("\n===== positions that are &trans on every layer (never produce anything) =====")
    dead = [
        i
        for i in range(len(layers["default_layer"]))
        if all(l[i] == "trans" for l in layers.values())
    ]
    print("  " + (", ".join(str(i) for i in dead) if dead else "(none)"))

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
