# 20/20 Split Keyboard

A wireless, hotswap, ortholinear split keyboard powered by [ZMK firmware](https://zmk.dev/).

<p align="center">
  <img src="Media/real pic together.jpg" alt="20/20 Split — Together" width="720" />
</p>

<p align="center">
  <img src="Media/real pic split.jpg" alt="20/20 Split — Split Mode" width="720" />
</p>

---

## Features

| | |
|---|---|
| **Layout** | Plank-ish 40 % when magnetically attached · Ortholinear 24 + 24 when split |
| **Hotswap** | Cherry MX compatible hotswap sockets — swap switches without soldering |
| **Wireless** | Bluetooth Low Energy via dual Nice!Nano v2 Clones (nRF52840)  |
| **Customizable** | Remap keys live with [ZMK Studio](https://zmk.studio/) — no reflashing required |
| **Battery** | 801350 3.7 V Li-Po per half with on/off slide switch |
| **3D Printed** | Fully printable case with magnet attachment system |

---

## Links

| Resource | URL |
|---|---|
| **Build Video** | [YouTube](https://www.youtube.com/watch?v=XWv2SwuP9wc) |
| **PDF Manual** | [20_20 split keyboard BOM and instructions.pdf](Media/20_20%20split%20keyboard%20BOM%20and%20instructions.pdf) |
| **ZMK Studio** | [zmk.studio](https://zmk.studio/) |
| **3D Printable Files** | [MakerWorld](https://makerworld.com/en/models/2563301/)|
| **ZMK Docs** | [zmk.dev](https://zmk.dev/) |

---

## Tools Used

| Tool | Purpose |
|---|---|
| [Keyboard Layout Editor](https://www.keyboard-layout-editor.com/#/) | Layout creation |
| [Swillkb Plate Builder](http://builder.swillkb.com/) | Plate DXF generation |
| [ZMK Shield Wizard](https://shield-wizard.genteure.workers.dev/) | ZMK shield configuration |
| [Keymap Drawer](https://keymap-drawer.streamlit.app/) | Keymap visualization |

---

## Default Keymap



<p align="center">
  <img src="Media/Full layout.png" alt="Full keyboard layout" width="640" />
</p>

User keymap is located at [`config/ortho20_20.keymap`](config/ortho20_20.keymap). You can also remap keys live via [ZMK Studio](https://zmk.studio/) — no reflashing needed.

---

## Combos

### ZMK Studio Unlock

Hold two bottom-row keys simultaneously to unlock ZMK Studio:

<p align="center">
  <img src="Media/Studio unlock combo.png" alt="ZMK Studio unlock combo" width="480" />
</p>

### Bluetooth Profile Combos

<p align="center">
  <img src="Media/Bluetooth combos.png" alt="Bluetooth combos" width="480" />
</p>

---

## Bill of Materials

> [!NOTE]
> **Additionally required (not listed below):** soldering iron, solder, [hookup wires](https://www.aliexpress.com/item/1005005048098404.html), [rubber feet](https://www.aliexpress.com/item/1005002705337380.html), heatshrink tubing, hot glue, and superglue.

| # | Item | Qty | Link |
|:-:|------|:---:|:----:|
| 1 | **Cherry MX Switches** | 48 | [AliExpress](https://www.aliexpress.com/item/1005007345651159.html) |
| 2 | **Pro Micro nRF52840** (Nice!Nano v2 clone) | 2 | [AliExpress](https://www.aliexpress.com/item/1005006995289476.html) |
| 3 | **MX Hotswap Sockets** | 48 | [AliExpress](https://www.aliexpress.com/item/1005004290562374.html) |
| 4 | **1N4148 Diodes** | 48 | [AliExpress](https://www.aliexpress.com/item/1005006245109375.html) |
| 5 | **M2 × 10 mm SHCS Screws** | 4 | [Bambu Lab](https://eu.store.bambulab.com/products/m2-socket-head-cap-machine-screws-shcs?id=48672759054684) |
| 6 | **M2 × 4 mm SHCS Screws** | 4 | [Bambu Lab](https://eu.store.bambulab.com/products/m2-socket-head-cap-machine-screws-shcs?id=48672758923612) |
| 7 | **M2 × 6 mm Standoffs** | 4 | [AliExpress](https://www.aliexpress.com/item/1005006049595637.html) |
| 8 | **4 × 2 mm Round Magnets** | 6 | [Bambu Lab](https://eu.store.bambulab.com/products/round-magnet?id=47966966579548) |
| 9 | **Kapton Tape** | 1 | [AliExpress](https://www.aliexpress.com/item/1005007518587827.html) |
| 10 | **Copper Wire** | 1 | [AliExpress](https://www.aliexpress.com/item/1005009078359338.html) |
| 11 | **801350 3.7 V Li-Po Battery** | 2 | [AliExpress](https://www.aliexpress.com/item/1005007117105334.html) |
| 12 | **Slide Switch** (on/off) | 2 | [AliExpress](https://www.aliexpress.com/item/33013437240.html) |
| 13 | **EVA Foam** *(optional, recommended)* | — | [AliExpress](https://www.aliexpress.com/item/1005002621956105.html) |
| 14 | **JST Battery Connectors** *(optional, recommended)* | — | [AliExpress](https://www.aliexpress.com/item/1005003390942788.html) |

---

## Build Instructions

> [!TIP]
> Watch the full **[Build Video on YouTube](https://www.youtube.com/watch?v=XWv2SwuP9wc)** for a detailed wiring walkthrough.

1. **Prepare everything** — Print the case parts and gather all BOM materials.
2. **Insert hotswap sockets** into the hotswap plate.
3. **Assemble plates** — Attach the hotswap plate to the switch plate using **M2 × 10 mm screws** and **6 mm standoffs**.
4. **Insert the switches** into the assembled plate.
5. **Solder diodes** — Solder the 1N4148 diodes to the hotswap sockets, placing them in their slots in the hotswap plate.
6. **Wire the rows** — Connect the other legs of the diodes together to form rows.
7. **Insulate rows** — Cover row wiring with **kapton tape** to prevent shorts.
8. **Wire the columns** — Cut copper wire to length and solder to the second hotswap contact to form columns.
9. **Connect to controller** — Wire rows and columns to the Nice!Nano v2 (see [Pinout](#-pinout) below).
10. **Solder power circuit** — Wire the slide switch, battery, and controller together.
11. **Flash firmware** — Flash the firmware and test all keys.

    > ⚠️ The **right half will not work** unless the left half is powered on.

12. **Final assembly** — Seat the controller in the case, secure with hot glue, insert switches into sockets, and screw on the bottom plate with **M2 × 4 mm screws**.
13. **Finishing touches** — Add keycaps and glue the magnets into the case.
14. **Repeat** for the second half — enjoy your new keyboard! 🎉

---

## Pinout

<p align="center">
  <img src="Media/pinout.png" alt="Wiring pinout diagram" width="720" />
</p>

> [!NOTE]
> All columns and all rows use the same pins on both halves — columns `106`, `104`, `011`, `100`, `024`, `022` and rows `113`, `111`, `010`, `009`.

---

## Firmware

Firmware is built automatically via GitHub Actions. To install:

1. Go to the **[Actions](../../actions)** tab on this repo.
2. Click the latest successful workflow run.
3. Download the firmware `.uf2` files from the **Artifacts** section.
4. Put each Nice!Nano v2 into bootloader mode (double-tap reset) and copy the corresponding `.uf2` file.

For more details see the [ZMK firmware installation guide](https://zmk.dev/docs/user-setup#installing-the-firmware).

### Build Artifacts

| Artifact | Description |
|---|---|
| `ortho20_20_left_with_studio` | Left half — includes ZMK Studio support |
| `ortho20_20_right` | Right half (peripheral) |
| `settings_reset` | Flash to either half to factory-reset stored settings |

### Premade Firmware

For convenience, you can download the premade firmware here:
- [firmware .zip](Premade%20Firmware/firmware%20.zip)

> [!WARNING]
> This bundle was published **before** the left half was re-wired to `024`/`022`, so its left-half
> firmware still drives columns 4–5 on `002`/`115`. If your board is wired with `024`/`022`,
> flash the **freshly built** firmware from the Actions tab instead.

### ZMK Studio

This firmware ships with **ZMK Studio** enabled on the left half. Connect via USB, open [zmk.studio](https://zmk.studio/), and remap your keys on the fly.

---

<p align="center">
  <em>Designed & built by <a href="https://github.com/vostoklabs">Vostok Labs</a></em>
</p>
