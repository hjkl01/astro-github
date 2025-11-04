
---
title: Pulse
---


# Pulse
> 访问地址：<https://github.com/rcourtman/Pulse>

Pulse 是一个轻量级、易用的 **脉冲（Pulse）信号生成与分析** 库，专为音频处理、LED 控制、实验测量等场景设计。它提供了完整的脉冲调制、采样、存储和可视化功能，支持多种采样率和波形类型，并且随时可与 Python 或 C++ 项目无缝集成。

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **多波形生成** | 支持方波、三角波、正弦波、脉冲宽度调制（PWM）等多种基底波形。 |
| **自定义频率 & 采样率** | 可设定 0.1 Hz ~ 10 kHz 的频率，及 1 kHz ~ 44 kHz 的采样率。 |
| **实时采样** | 通过回调接口（Python `callback` / C++ `std::function`）即时获取采样数据。 |
| **波形缓存 & 导出** | 内置缓冲区支持多条音轨，支持 WAV/CSV 的快速导出与读取。 |
| **闭环控制** | 内置 PID 控制器，适用于 LED、伺服电机等闭环系统。 |
| **可视化** | 使用 Matplotlib（Python）或 Qt（C++）即可绘制实时波形、频谱图。 |
| **跨平台** | 纯 Python 版兼容 Windows / macOS / Linux，C++ 版通过 `CMake` 打包。 |

---

## 安装与引入

### Python

```bash
pip install pulse
```

```python
from pulse import Generator

gen = Generator(freq=1.0, sample_rate=1000, wave_type='sine')
samples = gen.generate(duration=2.0)   # 2 秒的波形
```

### C++

```bash
# 克隆并编译
git clone https://github.com/rcourtman/Pulse.git
cd Pulse
mkdir build && cd build
cmake ..
make
```

```cpp
#include <pulse/Generator.hpp>

int main() {
    pulse::Generator gen(1.0, 1000, pulse::WaveType::SINE);
    auto samples = gen.generate(2.0); // 2 秒
    // 处理 samples …
    return 0;
}
```

---

## 使用示例

### 1. 生成 PWM 信号

```python
from pulse import Generator

pwm = Generator(freq=50, sample_rate=2000, wave_type='pwm', duty_cycle=0.3)
samples = pwm.generate(duration=0.1)
```

### 2. 实时绘图

```python
import matplotlib.pyplot as plt
from pulse import Generator

gen = Generator(freq=5, sample_rate=500, wave_type='sawtooth')
samples = gen.generate(duration=1.0)

plt.plot(samples)
plt.title('5 Hz Sawtooth Wave')
plt.show()
```

### 3. 导出为 WAV

```python
gen.export_wav('sine.wav', samples)
```

---

## API 参考

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `Generator(freq, sample_rate, wave_type, duty_cycle=0.5)` | `freq` Hz, `sample_rate` Hz, `wave_type` (str), `duty_cycle` (float) | `Generator` | 构造器，支持 `'sine'`, `'square'`, `'triangle'`, `'sawtooth'`, `'pwm'` |
| `generate(duration)` | `duration` seconds | `numpy.ndarray` (Python) / `std::vector<float>` (C++) | 按设定参数产生样本 |
| `export_wav(file, data)` | `file` (str), `data` | `None` | 将样本保存为 WAV |
| `export_csv(file, data)` | 同上 | `None` | 保存为 CSV，可在 Excel 中打开 |
| `set_callback(cb)` | `cb` (callable) | `None` | 生成时每个采样点回调 |
| `set_pid(Kp, Ki, Kd)` | PID 参数 | `None` | 内置 PID 调节，适配闭环系统 |

---

## 常见问题

1. **为什么频率设置不精确？**  
   Pulse 内部采用离散 FFT 样本，对极低频（< 0.1 Hz）可能有微小误差。可增大 `sample_rate` 或使用外部滤波。

2. **能否支持多频率叠加？**  
   只需多次 `Generator` 生成并相加 `samples` 即可。

3. **如何在嵌入式上使用？**  
   将 C++ 版编译成静态库，配置对应的编译环境即可。

---

> **项目文档**：详细的代码示例、API 文档及贡献指南请参见 GitHub README 或 Wiki。

---

> 访问地址：<https://github.com/rcourtman/Pulse>
