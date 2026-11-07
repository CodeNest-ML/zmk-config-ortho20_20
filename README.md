# 20/20 分体键盘
一款采用 [ZMK 固件](https://zmk.dev/) 的无线、热插拔、正交分体键盘。

<p align="center">
  <img src="Media/real pic together.jpg" alt="20/20 分体键盘 — 合并状态" width="720" />
</p>

<p align="center">
  <img src="Media/real pic split.jpg" alt="20/20 分体键盘 — 分体状态" width="720" />
</p>

---

## 特性

| | |
|---|---|
| **布局** | 磁吸合并时为 Plank 式 40% 配列 · 分体时为正交 24 + 24 配列 |
| **热插拔** | 兼容 Cherry MX 的热插拔轴座 —— 免焊接更换轴体 |
| **无线** | 双 Nice!Nano v2 克隆版 (nRF52840) 支持 Bluetooth Low Energy  |
| **可自定义** | 通过 [ZMK Studio](https://zmk.studio/) 在线改键 —— 无需重新烧录固件 |
| **电池** | 每半区一块 801350 3.7 V 锂聚合物电池，配滑动开关 |
| **3D 打印** | 外壳可完整打印，采用磁吸固定结构 |

---

## 相关链接

| 资源 | 链接 |
|---|---|
| **组装视频** | [YouTube](https://www.youtube.com/watch?v=XWv2SwuP9wc) |
| **PDF 手册** | [20_20 split keyboard BOM and instructions.pdf](Media/20_20%20split%20keyboard%20BOM%20and%20instructions.pdf) |
| **ZMK Studio** | [zmk.studio](https://zmk.studio/) |
| **3D 打印文件** | [MakerWorld](https://makerworld.com/en/models/2563301/) |
| **ZMK 文档** | [zmk.dev](https://zmk.dev/) |

---

## 使用到的工具

| 工具 | 用途 |
|---|---|
| [Keyboard Layout Editor](https://www.keyboard-layout-editor.com/#/) | 布局设计 |
| [Swillkb Plate Builder](http://builder.swillkb.com/) | 定位板 DXF 生成 |
| [ZMK Shield Wizard](https://shield-wizard.genteure.workers.dev/) | ZMK shield 配置 |
| [Keymap Drawer](https://keymap-drawer.streamlit.app/) | 键位可视化 |

---

## 默认键位



<p align="center">
  <img src="Media/Full layout.png" alt="完整键盘布局" width="640" />
</p>

用户键位表位于 [`config/ortho20_20.keymap`](config/ortho20_20.keymap)。你也可以通过 [ZMK Studio](https://zmk.studio/) 在线改键 —— 无需重新烧录固件。

---

## 组合键

### ZMK Studio 解锁

同时按住底排的两个按键即可解锁 ZMK Studio：

<p align="center">
  <img src="Media/Studio unlock combo.png" alt="ZMK Studio 解锁组合键" width="480" />
</p>

### 蓝牙配置组合键

<p align="center">
  <img src="Media/Bluetooth combos.png" alt="蓝牙组合键" width="480" />
</p>

---

## 物料清单

> [!NOTE]
> **另需准备（未列于下表）：** 烙铁、焊锡、[接线](https://www.aliexpress.com/item/1005005048098404.html)、[橡胶脚垫](https://www.aliexpress.com/item/1005002705337380.html)、热缩管、热熔胶和瞬干胶。

| # | 物料 | 数量 | 链接 |
|:-:|------|:---:|:----:|
| 1 | **Cherry MX 轴体** | 48 | [AliExpress](https://www.aliexpress.com/item/1005007345651159.html) |
| 2 | **Pro Micro nRF52840** (Nice!Nano v2 克隆版) | 2 | [AliExpress](https://www.aliexpress.com/item/1005006995289476.html) |
| 3 | **MX 热插拔轴座** | 48 | [AliExpress](https://www.aliexpress.com/item/1005004290562374.html) |
| 4 | **1N4148 二极管** | 48 | [AliExpress](https://www.aliexpress.com/item/1005006245109375.html) |
| 5 | **M2 × 10 mm 内六角圆柱头螺钉 (SHCS)** | 4 | [Bambu Lab](https://eu.store.bambulab.com/products/m2-socket-head-cap-machine-screws-shcs?id=48672759054684) |
| 6 | **M2 × 4 mm 内六角圆柱头螺钉 (SHCS)** | 4 | [Bambu Lab](https://eu.store.bambulab.com/products/m2-socket-head-cap-machine-screws-shcs?id=48672758923612) |
| 7 | **M2 × 6 mm 铜柱** | 4 | [AliExpress](https://www.aliexpress.com/item/1005006049595637.html) |
| 8 | **4 × 2 mm 圆形磁铁** | 6 | [Bambu Lab](https://eu.store.bambulab.com/products/round-magnet?id=47966966579548) |
| 9 | **Kapton 胶带** | 1 | [AliExpress](https://www.aliexpress.com/item/1005007518587827.html) |
| 10 | **铜线** | 1 | [AliExpress](https://www.aliexpress.com/item/1005009078359338.html) |
| 11 | **801350 3.7 V 锂聚合物电池** | 2 | [AliExpress](https://www.aliexpress.com/item/1005007117105334.html) |
| 12 | **滑动开关**（开/关） | 2 | [AliExpress](https://www.aliexpress.com/item/33013437240.html) |
| 13 | **EVA 泡棉** *(可选，推荐)* | — | [AliExpress](https://www.aliexpress.com/item/1005002621956105.html) |
| 14 | **JST 电池连接器** *(可选，推荐)* | — | [AliExpress](https://www.aliexpress.com/item/1005003390942788.html) |

---

## 组装说明

> [!TIP]
> 观看完整的 **[YouTube 组装视频](https://www.youtube.com/watch?v=XWv2SwuP9wc)**，了解详细接线流程。

1. **准备所有材料** —— 打印外壳零件并备齐全部物料。
2. **安装热插拔轴座** —— 把热插拔轴座压入热插拔定位板。
3. **组装定位板** —— 用 **M2 × 10 mm 螺钉** 和 **6 mm 铜柱** 把热插拔定位板与轴体定位板固定在一起。
4. **安装轴体** —— 把轴体插入组装好的定位板。
5. **焊接二极管** —— 将 1N4148 二极管焊到热插拔轴座上，放进热插拔定位板对应的槽位。
6. **连接行线** —— 把二极管剩余的引脚焊接在一起，构成行线。
7. **绝缘行线** —— 用 **Kapton 胶带** 包覆行线，防止短路。
8. **连接列线** —— 将铜线剪到所需长度，焊到热插拔轴座的第二触点，构成列线。
9. **连接主控** —— 把行线和列线接到 Nice!Nano v2（见下方 [引脚定义](#引脚定义)）。
10. **焊接电源电路** —— 把滑动开关、电池和主控连接在一起。
11. **烧录固件** —— 烧录固件并测试所有按键。

    > ⚠️ **除非左半区已上电，否则右半区无法工作。**

12. **最终组装** —— 把主控放进外壳，用热熔胶固定，将轴体压入轴座，再用 **M2 × 4 mm 螺钉** 拧上底板。
13. **收尾工作** —— 装上键帽，并把磁铁粘进外壳。
14. **另一半重复上述步骤** —— 享受你的新键盘！🎉

---

## 引脚定义

左右两半区接线完全相同 —— 同一个 MCU 引脚在左半区和右半区对应相同的列 / 行。

**列** —— 通往热插拔轴座第二触点的铜线：

| 半区 | 列 0 | 列 1 | 列 2 | 列 3 | 列 4 | 列 5 |
|------|-------|-------|-------|-------|-------|-------|
| 左 | `106` (P1.06) | `104` (P1.04) | `011` (P0.11) | `100` (P1.00) | `024` (P0.24) | `022` (P0.22) |
| 右 | `106` (P1.06) | `104` (P1.04) | `011` (P0.11) | `100` (P1.00) | `024` (P0.24) | `022` (P0.22) |

**行** —— 焊接在一起的二极管引脚：

| 半区 | 行 0 | 行 1 | 行 2 | 行 3 |
|------|-------|-------|-------|-------|
| 左 | `113` (P1.13) | `111` (P1.11) | `010` (P0.10) | `009` (P0.09) |
| 右 | `113` (P1.13) | `111` (P1.11) | `010` (P0.10) | `009` (P0.09) |

> [!NOTE]
> 手册中的编号是 Nice!Nano v2 / nRF52840 端口针脚名去掉小数点后的形式 ——
> `P1.06` → `106`，`P0.24` → `024`。第 4–5 列在**左右两半区**都是 `024` / `022`。

---

## 固件

固件通过 GitHub Actions 自动构建。安装步骤：

1. 进入本仓库的 **[Actions](../../actions)** 标签页。
2. 点击最近一次成功的构建记录。
3. 从 **Artifacts** 区域下载固件 `.uf2` 文件。
4. 让每块 Nice!Nano v2 进入 bootloader 模式（双击复位），然后复制对应的 `.uf2` 文件。

更多细节请参阅 [ZMK 固件安装指南](https://zmk.dev/docs/user-setup#installing-the-firmware)。

### 构建产物

| 产物 | 说明 |
|---|---|
| `ortho20_20_left_with_studio` | 左半区 —— 包含 ZMK Studio 支持 |
| `ortho20_20_right` | 右半区（外设） |
| `settings_reset` | 刷入任意一半区即可恢复出厂设置 |

### 预编译固件

为方便使用，可以直接下载预编译固件：
- [firmware.zip](Premade%20Firmware/firmware.zip)

> [!NOTE]
> 该固件包于 2026-11-07 重新构建，左半区第 4–5 列已改为 `024`/`022`，
> 与本文档的[引脚定义](#引脚定义)及 BOM 手册一致，可直接刷写。

### ZMK Studio

本固件在左半区启用了 **ZMK Studio**。通过 USB 连接，打开 [zmk.studio](https://zmk.studio/)，即可实时改键。

---

<p align="center">
  <em>由 <a href="https://github.com/vostoklabs">Vostok Labs</a> 设计并制作</em>
</p>
