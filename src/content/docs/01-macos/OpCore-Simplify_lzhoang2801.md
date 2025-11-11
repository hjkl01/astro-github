---
title: OpCore-Simplify
---

## 功能介绍

OpCore-Simplify 是一个专门设计的工具，用于简化 [OpenCore](https://github.com/acidanthera/OpenCorePkg) EFI 的创建过程。它通过自动化基本设置并提供标准化配置来减少手动工作，确保 Hackintosh 旅程的准确性。

### 主要功能

1. **全面的硬件和 macOS 支持**  
   完全支持现代硬件。使用兼容性检查器检查支持/不支持的设备和支持的 macOS 版本。
   - **CPU**: Intel 从 Nehalem 和 Westmere (1nd Gen) 到 Arrow Lake (15th Gen/Core Ultra Series 2)；AMD Ryzen 和 Threadripper 与 AMD Vanilla。
   - **GPU**: Intel iGPU 从 Iron Lake (1nd Gen) 到 Ice Lake (10th Gen)；AMD APU Vega Raven ASIC 系列；AMD dGPU Navi 23, 22, 21 及更早系列；NVIDIA Kepler, Pascal, Maxwell, Fermi, Tesla 系列。
   - **macOS**: 从 macOS High Sierra 到 macOS Tahoe。

2. **ACPI Patches 和 Kexts**  
   根据硬件配置自动检测并添加 ACPI patches 和 kexts。集成 SSDTTime，支持常见 patches，如 FakeEC, FixHPET, PLUG, RTCAWAC。包括自定义 patches，如防止内核 panic、禁用不支持的 PCI 设备、修复睡眠状态等。

3. **自动更新**  
   在每次 EFI 构建前自动检查并更新 OpenCorePkg 和 kexts 从 Dortania Builds 和 GitHub releases。

4. **EFI 配置**  
   基于广泛使用的来源和个人经验应用额外自定义，如欺骗 GPU IDs、禁用 SIP、欺骗 CPU IDs、添加 NVRAM 条目等。

5. **易于自定义**  
   除了默认设置，用户可以轻松进行进一步自定义，如自定义 ACPI patches、kexts 和 SMBIOS 调整。

## 使用方法

1. **下载 OpCore Simplify**  
   点击 Code → Download ZIP，或直接下载 [链接](https://github.com/lzhoang2801/OpCore-Simplify/archive/refs/heads/main.zip)。解压到所需位置。

2. **运行 OpCore Simplify**
   - Windows: 运行 `OpCore-Simplify.bat`。
   - macOS: 运行 `OpCore-Simplify.command`。

3. **选择硬件报告**  
   在 Windows 上，使用 `E. Export hardware report` 选项以获得最佳结果。或者使用 Hardware Sniffer 创建 Report.json 和 ACPI dump。

4. **选择 macOS 版本并自定义 OpenCore EFI**  
   默认选择最新的兼容 macOS 版本。工具将自动应用必要的 ACPI patches 和 kexts。可以手动审查和自定义。

5. **构建 OpenCore EFI**  
   选择 Build OpenCore EFI 生成 EFI。工具将自动下载必要的引导加载程序和 kexts，可能需要几分钟。

6. **USB 映射**  
   构建 EFI 后，按照步骤映射 USB 端口。

7. **创建 USB 并安装 macOS**  
   使用 UnPlugged 在 Windows 上创建 USB macOS 安装程序，或遵循 Dortania 指南。对于故障排除，参考 OpenCore Troubleshooting Guide。

注意：成功安装后，如果需要 OpenCore Legacy Patcher，只需应用 root patches 以激活缺失功能。对于 AMD GPUs，应用 root patches 后移除 `-radvesa`/`-amd_no_dgpu_accel` 以启用图形加速。
