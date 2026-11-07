# ortho20/20 项目检测报告

- 检测对象：`zmk-config-ortho20_20`（ZMK 用户配置仓库，ZMK v0.3 / nice!nano v2）
- 检测提交：`905ffb3` "添加项目检测报告与一致性校验脚本"（2026-10-26）
- 修订日期：2026-11-07 —— **第二节结论方向已更正，详见下方修订说明**

---

## 〇、修订说明（2026-11-07）

首版报告把左半区 col4/col5 判为"固件写错了、文档才对"，**结论方向反了**。

实测**左半区实物已改线**：第 4、5 列现在接在 **P0.24 / P0.22**（与右半区相同），
而不是 P0.02 / P1.15。因此：

| | 首版判断（错误） | 修订后（正确） |
| --- | --- | --- |
| 左半区 col4/col5 实物接线 | P0.02 / P1.15（002 / 115） | **P0.24 / P0.22（024 / 022）** |
| 谁错了 | 固件 | **文档**（BOM 手册 / README / PDF 手册） |
| 处理方式 | 改固件 | **回滚固件 + 同步文档** |

已按"回滚固件 + 同步文档"处理完毕：固件回到 `pro_micro 5` / `pro_micro 4`，
BOM 手册（md + PDF）与 README 三处接线表全部改为 024 / 022，
`Media/pinout.png` 实拍标注图已删除（只能像素级修补、无法长期维护），
`python tools/check_consistency.py` 通过。

---

## 一、结论

**项目结构完整、编译链是绿的，左/右半区接线完全一致，固件与文档现已对齐。**

| 项目 | 结果 |
| --- | --- |
| 编译 / CI | ✅ 通过 |
| 矩阵几何（transform / 物理布局 / 三层 keymap / Studio JSON） | ✅ 全部一致，48 键位 |
| 分体映射（右半区 `col-offset = <6>`） | ✅ 正确 |
| 左半区 kscan 列引脚 | ✅ 106 / 104 / 011 / 100 / **024 / 022** |
| 右半区 kscan 列引脚 | ✅ 106 / 104 / 011 / 100 / **024 / 022** |
| 行线（两半区） | ✅ 113 / 111 / 010 / 009 |
| 文档接线表（BOM 手册 / README / PDF 手册） | ✅ 已与固件对齐 |
| 组合键（Studio 解锁） | ✅ 与文档图片一致 |

---

## 二、P0：左半区 col4/col5 曾被误改，现已回滚

### 2.1 现象

`11c9e5c` 把左半区 col4/col5 从 `pro_micro 5` / `pro_micro 4`（P0.24 / P0.22）
改成了 `pro_micro 19` / `pro_micro 18`（P0.02 / P1.15）：

```dts
// 误改后（11c9e5c）
col-gpios
    = <&pro_micro 9 GPIO_ACTIVE_HIGH>    // col0 -> P1.06
    , <&pro_micro 8 GPIO_ACTIVE_HIGH>    // col1 -> P1.04
    , <&pro_micro 7 GPIO_ACTIVE_HIGH>    // col2 -> P0.11
    , <&pro_micro 6 GPIO_ACTIVE_HIGH>    // col3 -> P1.00
    , <&pro_micro 19 GPIO_ACTIVE_HIGH>   // col4 -> P0.02  (left half only)
    , <&pro_micro 18 GPIO_ACTIVE_HIGH>   // col5 -> P1.15  (left half only)
    ;
```

### 2.2 证据链

| 来源 | 左半区 col4 / col5 | 右半区 col4 / col5 |
| --- | --- | --- |
| **实物接线（改线后的板子）** | **024 / 022** | 024 / 022 |
| `Media/20_20 split keyboard BOM and manual.md` 接线表 | 002 / 115 ❌（已改为 024 / 022） | 024 / 022 |
| `Media/pinout.png` 实物接线图 | 002 / 115 ❌（**已删除**） | 024 / 022 |
| `Media/20_20 split keyboard BOM and instructions.pdf` 第 2 页 | 002 / 115 ❌（已改为 024 / 022） | 024 / 022 |
| `README.md` Pinout 说明 | 002 / 115 ❌（已改为 024 / 022） | 024 / 022 |
| `boards/shields/ortho20_20/ortho20_20_left.overlay` | 024 / 022 ✅（回滚后） | 024 / 022 ✅ |

即：**BOM 手册（md + PDF）与 README 三处一直停留在改线前的旧值**，首版报告误把文档当成了权威来源。
（`Media/pinout.png` 实拍标注图同样是旧值的来源，现已删除，见 2.5。）

引脚换算依据：ZMK v0.3 `app/boards/arm/nice_nano/arduino_pro_micro_pins.dtsi`
（`pro_micro 4`=P0.22、`5`=P0.24、`18`=P1.15、`19`=P0.02）。

### 2.3 成因（git 历史）

```
bf422ea  初始版本                    ← 左半区 19/18（P0.02/P1.15），此时文档也是 002/115
e8650f0  19 -> pro_micro 2           ← 引脚编号写错（P0.17），同一根线的两种写法
f0fc407  pro_micro 2 -> gpio0 2     ← 换写法，物理引脚不变（P0.02）
76fad1f  Readme remap               ← 发布 Premade Firmware 用的就是 002/115
9a13604  left中将002、115改成024、022 ← 【改线】左半区改成 024/022；写成 24/22 非法编号 → CI 失败
19b4ee4  修正Pro Micro 编号          ← 24/22 改成合法的 5/4（即 P0.24/P0.22）→ CI 转绿
11c9e5c  修正左半区 col4/col5 引脚   ← 【误改】又改回 19/18（依据是未更新的旧文档）
本次修订  回滚                        ← 恢复 5/4（P0.24/P0.22），并同步四处文档
```

关键点：`9a13604` / `19b4ee4` 是**跟着实物改线**走的，改完 CI 变绿、固件正确；
`11c9e5c` 依据的是**没有跟着改的旧文档**，把正确的固件改回了旧引脚。

### 2.4 影响面（误改期间）

- 左半区 4 行 × 2 列 = **8 个键位失效**：`R` `T` / `F` `G` / `V` `B` / `Lower` `SPACE`。
- 实际接在 P0.24、P0.22 上的两根列线变为悬空；而 col-gpios 没有配上下拉（只有行配了 `GPIO_PULL_DOWN`）
  → 这两列可能出现**幽灵键 / 随机误触**。
- `Lower` 键失效连带影响：Left 的 `Lower`（位置 40）与 Right 的 `Raise`（位置 43）组成的
  **Studio 解锁组合键将无法触发**（组合键跨半区，需要两边同时按下）。
- 右半区不受影响。
- **连带效应**：右半区 `PgUp`（位置 43）虽然引脚正确，但它是上述组合键的成员之一。
  按 ZMK v0.3 `app/src/combo.c`，组合键成员在被按下后会先被 *captured*，只有
  `timeout-ms = 50` 超时后才会通过 `cleanup() → release_pressed_keys() → ZMK_EVENT_RELEASE`
  交还给 keymap；因此位置 43 的按下会被吞掉最多 50 ms。在位置 40 已死、组合键永远凑不齐的情况下：
  - 轻点 `PgUp`（按下后很快松开）→ 按下与松开几乎同时到达 `&mo RAISE`，层切换瞬间生效又失效，
    **看起来就是"完全没反应"**；
  - 长按 `PgUp` → 要等组合键超时后才会切到 Raise 层，有明显延迟。
  这就是用户观察到 "V / PgOn / PgUp 三个位置没反应" 的完整成因。
- 回滚后以上全部消失。

### 2.5 修复（✅ 已应用）

```diff
--- a/boards/shields/ortho20_20/ortho20_20_left.overlay
+++ b/boards/shields/ortho20_20/ortho20_20_left.overlay
@@ -10,8 +10,8 @@
             = <&pro_micro 9 GPIO_ACTIVE_HIGH>    // col0 -> P1.06
             , <&pro_micro 8 GPIO_ACTIVE_HIGH>    // col1 -> P1.04
             , <&pro_micro 7 GPIO_ACTIVE_HIGH>    // col2 -> P0.11
             , <&pro_micro 6 GPIO_ACTIVE_HIGH>    // col3 -> P1.00
-            , <&pro_micro 19 GPIO_ACTIVE_HIGH>   // col4 -> P0.02  (left half only)
-            , <&pro_micro 18 GPIO_ACTIVE_HIGH>   // col5 -> P1.15  (left half only)
+            , <&pro_micro 5 GPIO_ACTIVE_HIGH>    // col4 -> P0.24
+            , <&pro_micro 4 GPIO_ACTIVE_HIGH>    // col5 -> P0.22
             ;
```

- `pro_micro 5` = P0.24、`pro_micro 4` = P0.22，与右半区（`<&gpio0 24>` / `<&gpio0 22>`）指向同一对物理引脚。
- 同步更新的文档：

  | 文件 | 改动 |
  | --- | --- |
  | `Media/20_20 split keyboard BOM and manual.md` | 接线表左半区 `4 - 002 5 - 115` → `4 - 024 5 - 022` |
  | `Media/20_20 split keyboard BOM and instructions.pdf` | 第 2 页左半区表格 `4 - 002 / 5 - 115` → `4 - 024 / 5 - 022`（内容流定点替换，字形与位置不变） |
  | `README.md` | Pinout 章节改为两半区共用的**文字接线表**（列 `106`/`104`/`011`/`100`/`024`/`022`，行 `113`/`111`/`010`/`009`，并标注 nRF52840 端口针脚名） |
  | `Media/pinout.png` | **删除** —— 实拍图上手工画的标注只能像素级修补、无法长期维护，接线信息改由 README 文字表承载 |

- 应用后 `python tools/check_consistency.py` → **ALL CHECKS PASSED**。

### 2.6 引脚冲突复核（已确认无冲突）

nice!nano v2 板级占用：LED=P0.15、电源开关=P0.13、uart0=P0.08/P0.06、i2c0=P0.17/P0.20、spi1=P1.13/P0.10/P1.11。

- **P0.24 / P0.22 未被板级占用** ✅（右半区一直在用，可作佐证）
- 注意：行线 P1.13 / P1.11 / P0.10 与 spi1 复用，但 spi1 在 Zephyr 中默认 disabled、pinctrl 不生效，因此无冲突
  —— 仅提醒：**不要在该键盘上启用 SPI1**。

---

## 三、已验证通过的检查项

| # | 检查项 | 结果 |
| --- | --- | --- |
| 1 | 矩阵 transform：`columns=12` × `rows=4` = 48 位，map 恰好 48 个 `RC()` | ✅ |
| 2 | 物理布局 `keys` 属性 48 项，与 transform 顺序一致 | ✅ |
| 3 | 三层 keymap（base / lower / raise）每层恰好 48 个绑定 | ✅ |
| 4 | `config/ortho20_20.json`（Studio 布局）48 项，x/y 与 devicetree 物理布局逐项吻合 | ✅ |
| 5 | 左右半区 kscan 均为 6 列 × 4 行 = 24 键/半区，合计 48 | ✅ |
| 6 | 右半区 `col-offset = <6>`（ZMK 先加偏移再查 map，右半区本地 col0→全局 col6） | ✅ |
| 7 | 行线左右半区完全一致（P1.13 / P1.11 / P0.10 / P0.09），与手册一致 | ✅ |
| 8 | **左右半区列线完全一致**：P1.06 / P1.04 / P0.11 / P1.00 / P0.24 / P0.22，与手册一致 | ✅ |
| 9 | 组合键 `key-positions = <40 43>` = 左半区 `Lower` + 右半区 `Raise`，与 `Media/Studio unlock combo.png` 一致 | ✅ |
| 10 | `config/ortho20_20.conf` / `.keymap` 能被 ZMK 找到（shield 名 `ortho20_20_left/right` 会派生出候选名 `ortho20_20`） | ✅ |
| 11 | `board: nice_nano_v2` 在 ZMK v0.3 中有效（`app/boards/arm/nice_nano/nice_nano_v2.dts`） | ✅ |
| 12 | `revision: v0.3` 是 ZMK 真实存在的 tag；`self: path: config` 使 `ZMK_CONFIG=<repo>/config` | ✅ |
| 13 | `settings_reset` shield 自带 keymap，单独构建不会因找不到 keymap 而失败 | ✅ |
| 14 | Kconfig：`ZMK_SPLIT` 两半区开启、左半区 central、名称只给 central —— 与 ZMK 官方 new-shield 规范一致 | ✅ |
| 15 | Studio 用法：仅 central（左半区）加 `studio-rpc-usb-uart` snippet —— 符合 ZMK 官方文档 | ✅ |
| 16 | `Media/Full layout.png` 与 keymap 实际绑定完全对应 | ✅ |
| 17 | BOM 手册（md + PDF）/ README 三处接线表与固件一致 | ✅ |

---

## 四、次要问题与改进建议

1. **Premade Firmware 与当前固件不同步**
   `Premade Firmware/firmware .zip` 在 `76fad1f`（2026-03-23）发布，早于左半区改线，
   其左半区固件仍是 `002`/`115`。**已改线成 `024`/`022` 的板子不能用它**，
   应从 Actions 页下载当前源码构建的固件。README 已加警告。

2. **README 的构建产物名不准确**
   README「Build Artifacts」表写的是 `ortho20_20_left_with_studio` / `ortho20_20_right` / `settings_reset`，
   但 ZMK 的 `build-user-config.yml` 实际产物是 `artifact-<name>.uf2`（`settings_reset` 未指定 `artifact-name`，
   实际为 `artifact-settings_reset-nice_nano_v2-zmk.uf2`），最终合并包名为 `firmware`。建议按实际产物名修正。

3. **缺少 shield 元数据文件**
   ZMK 官方 new-shield 规范建议为每个 part 提供 `ortho20_20_left.zmk.yml` / `ortho20_20_right.zmk.yml`
   （含 `features: [keys, studio]`、`siblings` 等）。缺失不影响编译，但会让键盘无法出现在 ZMK 官方硬件列表 /
   Studio 的键盘目录里。

4. **右半区也被打上了 Studio 开关**
   `config/ortho20_20.conf` 对两个半区同时生效，`CONFIG_ZMK_STUDIO=y` 会连带编译进右半区固件。
   右半区本不需要 Studio（ZMK 文档明确只给 central 加），会白白占用 flash/RAM。
   建议拆成 `ortho20_20.conf`（共享）+ `ortho20_20_left.conf`（Studio 相关）两个文件。

5. **Studio 可用层数受限**
   keymap 只定义了 3 层。若希望在 Studio 里新增层，需在 keymap 中追加 `status = "reserved";` 的空层，
   否则 Studio 无法增加/启用新层。

6. **keymap 注释与实际绑定不符（小）**
   base 层底排注释写的是 `| CTL | WIN| ALT| WIN| ...`，实际第 4 位绑定为 `&kp RGUI`（与 `Full layout.png` 一致，
   注释里的 "WIN" 应改成 "RGUI"），第 9 位也是 `&kp RGUI`。功能无误，仅注释误导。

7. **列线建议加上 `GPIO_PULL_DOWN`**
   行线已配 `GPIO_PULL_DOWN`，列线未配。若某根列线接触不良/悬空，容易产生幽灵键；两半区对齐配置更稳妥。

8. **CI 触发时机**
   `.github/workflows/build.yml` 是 `on: [push, pull_request, workflow_dispatch]`，
   建议改成仅对 `boards/`、`config/`、`build.yaml` 等相关路径触发，避免改 README 也重跑一次全量构建。

---

## 五、如何复检

```bash
# 静态一致性检查（不需要 Zephyr 工具链）
python tools/check_consistency.py

# 真实编译（需要 west + Zephyr SDK）
west init -l config && west update
west build -d build/left -b nice_nano_v2 -s studio-rpc-usb-uart -- -DSHIELD=ortho20_20_left -DZMK_CONFIG=$PWD/config -DCONFIG_ZMK_STUDIO=y
west build -d build/right -b nice_nano_v2 -- -DSHIELD=ortho20_20_right -DZMK_CONFIG=$PWD/config
```

`tools/check_consistency.py` 已内置本报告的全部断言（矩阵几何、keymap 绑定数、Studio JSON 对齐、
左右半区引脚与 BOM 手册比对、transform 偏移、build.yaml / west.yml 有效性），修复后可一键回归。

刷机后自测建议（对应第 2.4 节）：

1. 左半区依次按 `R T F G V B`，确认 6 个键都有响应；
2. 左半区 `SPACE` 应可用（且不产生多余键）；
3. 同时按住左半区 `Lower` + 右半区 `Raise`，应弹出 ZMK Studio 解锁提示；
4. 右半区按 `P` `BSPC`，确认不受影响。
