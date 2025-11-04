
---
title: blink.cmp
---


# blink.cmp

> 项目地址: https://github.com/saghen/blink.cmp

---

## 1. 项目简介

blink.cmp 是一个极简、可移植的 C 语言实现，用来驱动嵌入式 PWM 或 GPIO 产生 LED 闪烁效果。它不依赖任何复杂的 RTOS 或硬件抽象层，适合用在裸机或轻量级微控制器项目中。

---

## 2. 核心特性

- **极简 API**：仅有 3-4 个函数，易于集成。
- **可配置闪烁周期**：支持自定义闪烁间隔（毫秒级）。
- **低功耗**：在无闪烁时保持 GPIO 低电平，避免不必要的能耗。
- **多平台兼容**：仅使用标准 C，兼容 ARM GCC、IAR、Keil 等编译器。
- **轻量级**：源码文件约 200 行，二进制体积 ≤ 1KB。

---

## 3. 快速开始

```bash
# 克隆仓库
git clone https://github.com/saghen/blink.cmp.git
cd blink.cmp

# 编译示例（假设使用 ARM GCC）
make

# 运行测试（若有硬件连线）
make test
```

### 代码示例

```c
#include "blink.h"

int main(void) {
    // 初始化时钟和 GPIO（视 MCU 而定）
    SystemClock_Config();
    GPIO_Init();

    // 启动闪烁，周期为 500 毫秒
    blink_start(500);

    while (1) {
        // 主循环可执行其他任务
    }
}
```

> **提示**：将 `blink.c` 与项目编译链接即可，无需额外库。

---

## 4. API 文档

| 函数 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `void blink_init(void)` | – | – | 初始化内部计时器及 GPIO。 |
| `void blink_start(uint32_t period_ms)` | 闪烁周期（毫秒） | – | 开始定时闪烁。 |
| `void blink_stop(void)` | – | – | 停止闪烁并将 GPIO 关闭。 |
| `bool blink_is_running(void)` | – | true/false | 查询闪烁是否正在进行。 |
| `void blink_callback(void)` | – | – | 在每个周期内被调用，可用于自定义动作。 |

> 具体实现可在 `blink.h / blink.c` 中查看。

---

## 5. 集成到项目

1. **配置硬件**  
   - 在 `blink.c` 中修改 `BLINK_PIN`、`BLINK_PORT` 以及对应的时钟开启代码。  
   - 确保 MCU 的 GPIO 时钟已启动。

2. **添加到项目构建**  
   - 在 CMake 或 Makefile 中加入 `blink.c` 与 `blink.h`。  
   - `blink` 模块无外部依赖，直接编译即可。

3. **使用示例**  
   - 调用 `blink_init()` 初始化。  
   - 根据需要调用 `blink_start()` 或 `blink_stop()`。

---

## 6. 贡献

- Fork 本仓库 → 新建分支 → 提交代码 → 发起 Pull Request。  
- 所有提交请严格遵守代码风格：简洁、可读、无宏味。  
- 任何新增功能请先提交 Issue 讨论。

---

## 7. 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

---