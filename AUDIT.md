# ortho20/20 项目检测报告

- 检测对象：`zmk-config-ortho20_20`（ZMK 用户配置仓库，ZMK v0.3 / nice!nano v2）
- 检测提交：`19b4ee4` "修正Pro Micro 编号"（2026-10-16 15:37）
- 检测日期：2026-10-26

---

## 一、结论

**项目结构完整、编译链是绿的，但存在 1 个硬件级错误：左半区第 4、5 列绑错了引脚。**

| 项目 | 结果 |
| --- | --- |
| 编译 / CI | ✅ 通过（HEAD 的 GitHub Actions `success`） |
| 矩阵几何（transform / 物理布局 / 三层 keymap / Studio JSON） | ✅ 全部一致，48 键位 |
| 分体映射（右半区 `col-offset = <6>`） | ✅ 正确 |
| 左半区 kscan 列引脚 | ❌ **第 4、5 列错误**（详见第二节） |
| 右半区 kscan 全部引脚 | ✅ 与 BOM 手册 / 接线图完全一致 |
| 组合键（Studio 解锁） | ✅ 与文档图片一致 |

> ⚠️ 关键影响：**仓库里已发布的 `Premade Firmware/firmware .zip` 是好的**（构建于错误发生之前），但**从当前 HEAD 重新构建的固件会带这个错误**，左半区会有 8 个键失灵。

---

## 二、P0：左半区第 4、5 列引脚错误

### 2.1 现象

`boards/shields/ortho20_20/ortho20_20_left.overlay` 当前内容：

```dts
col-gpios
    = <&pro_micro 9 GPIO_ACTIVE_HIGH>   // col0 → P1.06  ✅
    , <&pro_micro 8 GPIO_ACTIVE_HIGH>   // col1 → P1.04  ✅
    , <&pro_micro 7 GPIO_ACTIVE_HIGH>   // col2 → P0.11  ✅
    , <&pro_micro 6 GPIO_ACTIVE_HIGH>   // col3 → P1.00  ✅
    , <&pro_micro 5 GPIO_ACTIVE_HIGH>   // col4 → P0.24  ❌ 应为 P0.02
    , <&pro_micro 4 GPIO_ACTIVE_HIGH>   // col5 → P0.22  ❌ 应为 P1.15
    // , <&gpio0 2 GPIO_ACTIVE_HIGH>     // ← 被注释掉的正确值（P0.02）
    // , <&pro_micro 18 GPIO_ACTIVE_HIGH> // ← 被注释掉的正确值（P1.15）
```

引脚换算依据：ZMK v0.3 `app/boards/arm/nice_nano/arduino_pro_micro_pins.dtsi`
（`pro_micro 4`=P0.22、`5`=P0.24、`18`=P1.15、`19`=P0.02）

### 2.2 证据链（本仓库自己的三处权威来源全部指向 002/115）

| 来源 | 左半区 col4 / col5 | 右半区 col4 / col5 |
| --- | --- | --- |
| `Media/20_20 split keyboard BOM and manual.md` 接线表 | **002 / 115** | 024 / 022 |
| `Media/pinout.png` 实物接线图（左边 T 列 / 右边 P 列） | **002 / 115** | 024 / 022 |
| `README.md:137` | **002 / 115** | 024 / 022 |
| `boards/shields/ortho20_20/ortho20_20_left.overlay`（HEAD） | 024 / 022 ❌ | 024 / 022 ✅ |

也就是说：**当前固件把左半区和右半区的第 4、5 列接到了同一组引脚上**，与项目自身的接线文档矛盾。

### 2.3 成因（git 历史）

```
19b4ee4  修正Pro Micro 编号            ← 把 24/22 改成 5/4（仍是 P0.24/P0.22），CI 转绿
9a13604  left中将002、115改成024、022    ← 把正确的 P0.02/P1.15 误改成右半区的引脚，CI 失败
76fad1f  Readme remap                  ← 发布版固件用的就是正确的 <&gpio0 2> + <&pro_micro 18>
```

`9a13604` 用了 `pro_micro 24` / `pro_micro 22`，这两个编号在 gpio-map 里不存在 → 编译失败；
`19b4ee4` 改成合法编号 `5` / `4` → 编译通过，但引用的物理引脚（P0.24 / P0.22）依旧是右半区的那两根。
**这两次提交修的是"编译错误"，不是"接线错误"，所以把一个物理引脚问题掩盖成了绿灯。**

### 2.4 影响面

- 左半区 4 行 × 2 列 = **8 个键位失效**：`R` `T` / `F` `G` / `V` `B` / `Lower` `SPACE`。
- 实际接在 P0.02、P1.15 上的两根列线变为悬空；而 col-gpios 没有配上下拉（只有行配了 `GPIO_PULL_DOWN`），
  → 这两列可能出现**幽灵键 / 随机误触**。
- `Lower` 键失效连带影响：Left 的 `Lower`（位置 40）与 Right 的 `Raise`（位置 43）组成的
  **Studio 解锁组合键将无法触发**（组合键跨半区，需要两边同时按下）。
- 右半区不受影响。
- **连带效应（2026-10-26 补充）**：右半区 `PgUp`（位置 43）虽然引脚正确，但它是上述组合键的
  成员之一。按 ZMK v0.3 `app/src/combo.c`，组合键成员在被按下后会先被 *captured*，
  只有 `timeout-ms = 50` 超时后才会通过 `cleanup() → release_pressed_keys() → ZMK_EVENT_RELEASE`
  交还给 keymap；因此位置 43 的按下会被吞掉最多 50 ms（右半区是 peripheral，还会先在
  peripheral 上被捕获一次）。在位置 40 已死、组合键永远凑不齐的情况下：
  - 轻点 `PgUp`（按下后很快松开）→ 按下与松开几乎同时到达 `&mo RAISE`，层切换瞬间生效又失效，
    **看起来就是“完全没反应”**；
  - 长按 `PgUp` → 要等组合键超时后才会切到 Raise 层，有明显延迟。
  这就是用户观察到 “V / PgOn / PgUp 三个位置没反应” 的完整成因：V、PgOn 是引脚问题直接导致，
  PgUp 是组合键 + 位置 40 已死导致的连带问题。

### 2.5 修复补丁（✅ 已于 2026-10-26 应用到工作区，未提交）

```diff
--- a/boards/shields/ortho20_20/ortho20_20_left.overlay
+++ b/boards/shields/ortho20_20/ortho20_20_left.overlay
@@ -10,10 +10,8 @@
             = <&pro_micro 9 GPIO_ACTIVE_HIGH>
             , <&pro_micro 8 GPIO_ACTIVE_HIGH>
             , <&pro_micro 7 GPIO_ACTIVE_HIGH>
             , <&pro_micro 6 GPIO_ACTIVE_HIGH>
-            , <&pro_micro 5 GPIO_ACTIVE_HIGH>
-            , <&pro_micro 4 GPIO_ACTIVE_HIGH>
-            // , <&gpio0 2 GPIO_ACTIVE_HIGH>
-            // , <&pro_micro 18 GPIO_ACTIVE_HIGH>
+            , <&pro_micro 19 GPIO_ACTIVE_HIGH>
+            , <&pro_micro 18 GPIO_ACTIVE_HIGH>
             ;
```

- `pro_micro 19` = P0.02 = A1，`pro_micro 18` = P1.15 = A0，与其余条目统一用 `pro_micro` 别名书写。
- 若**实物已经改线**（左半区确实接到了 024/022），则固件是对的，应反过来把 BOM 手册、`pinout.png`、README 三处文档更新为一致。
- 应用后 `python tools/check_consistency.py` 由 1 项 FAIL 变为 **ALL CHECKS PASSED**。

### 2.6 引脚冲突复核（已确认无冲突）

nice!nano v2 板级占用：LED=P0.15、电源开关=P0.13、uart0=P0.08/P0.06、i2c0=P0.17/P0.20、spi1=P1.13/P0.10/P1.11。

- **P0.02 / P1.15 未被板级占用** ✅
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
| 8 | 右半区列线 P1.06 / P1.04 / P0.11 / P1.00 / P0.24 / P0.22，与手册一致 | ✅ |
| 9 | 组合键 `key-positions = <40 43>` = 左半区 `Lower` + 右半区 `Raise`，与 `Media/Studio unlock combo.png` 一致 | ✅ |
| 10 | `config/ortho20_20.conf` / `.keymap` 能被 ZMK 找到（shield 名 `ortho20_20_left/right` 会派生出候选名 `ortho20_20`） | ✅ |
| 11 | `board: nice_nano_v2` 在 ZMK v0.3 中有效（`app/boards/arm/nice_nano/nice_nano_v2.dts`） | ✅ |
| 12 | `revision: v0.3` 是 ZMK 真实存在的 tag；`self: path: config` 使 `ZMK_CONFIG=<repo>/config` | ✅ |
| 13 | `settings_reset` shield 自带 keymap，单独构建不会因找不到 keymap 而失败 | ✅ |
| 14 | Kconfig：`ZMK_SPLIT` 两半区开启、左半区 central、名称只给 central —— 与 ZMK 官方 new-shield 规范一致 | ✅ |
| 15 | Studio 用法：仅 central（左半区）加 `studio-rpc-usb-uart` snippet —— 符合 ZMK 官方文档 | ✅ |
| 16 | `Media/Full layout.png` 与 keymap 实际绑定完全对应 | ✅ |

---

## 四、次要问题与改进建议

1. **README 的构建产物名不准确**
   README「Build Artifacts」表写的是 `ortho20_20_left_with_studio` / `ortho20_20_right` / `settings_reset`，
   但 ZMK 的 `build-user-config.yml` 实际产物是 `artifact-<name>.uf2`（`settings_reset` 未指定 `artifact-name`，
   实际为 `artifact-settings_reset-nice_nano_v2-zmk.uf2`），最终合并包名为 `firmware`。建议按实际产物名修正。

2. **缺少 shield 元数据文件**
   ZMK 官方 new-shield 规范建议为每个 part 提供 `ortho20_20_left.zmk.yml` / `ortho20_20_right.zmk.yml`
   （含 `features: [keys, studio]`、`siblings` 等）。缺失不影响编译，但会让键盘无法出现在 ZMK 官方硬件列表 /
   Studio 的键盘目录里。

3. **右半区也被打上了 Studio 开关**
   `config/ortho20_20.conf` 对两个半区同时生效，`CONFIG_ZMK_STUDIO=y` 会连带编译进右半区固件。
   右半区本不需要 Studio（ZMK 文档明确只给 central 加），会白白占用 flash/RAM。
   建议拆成 `ortho20_20.conf`（共享）+ `ortho20_20_left.conf`（Studio 相关）两个文件。

4. **Studio 可用层数受限**
   keymap 只定义了 3 层。若希望在 Studio 里新增层，需在 keymap 中追加 `status = "reserved";` 的空层，
   否则 Studio 无法增加/启用新层。

5. **keymap 注释与实际绑定不符（小）**
   base 层底排注释写的是 `| CTL | WIN| ALT| WIN| ...`，实际第 4 位绑定为 `&kp RGUI`（与 `Full layout.png` 一致，
   注释里的 "WIN" 应改成 "RGUI"），第 9 位也是 `&kp RGUI`。功能无误，仅注释误导。

6. **列线建议加上 `GPIO_PULL_DOWN`**
   行线已配 `GPIO_PULL_DOWN`，列线未配。若某根列线接触不良/悬空，容易产生幽灵键；两半区对齐配置更稳妥。

7. **CI 触发时机**
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

刷机后自测建议（对应第 2.4 节）：

1. 左半区依次按 `R T F G V B`，确认 6 个键都有响应；
2. 左半区 `SPACE` 应可用（且不产生多余键）；
3. 同时按住左半区 `Lower` + 右半区 `Raise`，应弹出 ZMK Studio 解锁提示；
4. 右半区按 `P` `BSPC`，确认不受影响。

> `tools/check_consistency.py` 已内置本报告的全部断言（矩阵几何、keymap 绑定数、Studio JSON 对齐、
> 左右半区引脚与 BOM 手册比对、transform 偏移、build.yaml / west.yml 有效性），修复后可一键回归。
