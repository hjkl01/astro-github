---
title: OpenAvatarChat
---

# OpenAvatarChat – HumanAIGC 项目

**项目地址**: <https://github.com/HumanAIGC-Engineering/OpenAvatarChat/blob/main/readme_cn.md>  

## 主要特性

- ✔︎ **实时音频捕获与预处理**：采用 Unity API 对麦克风音频进行采样、增益放大、卷积滤波等预处理，以获取干净的音频信号。  
- ✔︎ **语音检测与区间切换**：通过检测音量阈值（Speech Range）决定“说话”与“静音”状态；在说话区间自动停止段落、在说话区间内持续刷新音频路由；可通过界面切换不同 `Speech Range` 配置。  
- ✔︎ **平滑音频参数**：通过 Low-pass 滤波器实现 `SpeakSmooth` 与 `StereophonySmooth` 的平滑处理，降低短时波动导致的表情偏差。  
- ✔︎ **多功能采集与保存**：捕获完整的 `AudioClip` 并支持批量导出，便于后期训练或多模态分析。  
- ✔︎ **可视化与实时调参**：使用 Unity 自带的 `Slider`、`Toggle` 等组件，实时展示音量、语音区间与同步信息，支持快速调参。  
- ✔︎ **优势可扩展性**：脚本单独拆分为控制器与服务层，可无缝接入后端服务（如 WebSocket）进行跨端音频流传输。  

## 关键功能

| 功能 | 说明 |
|---|---|
| **音频引擎** | `AudioController.cs` 负责采集、处理与路由音频数据，对不同音频源（麦克风/预录）做统一管理。 |
| **语音区间检测** | 通过 `SpeechRangeEvent` 对话框配置语音阈值，开启/关闭区间检测；实现实时说话/停止动作的触发。 |
| **滤波与平滑** | `LowPassFilter` 实现 `SpeakSmooth` 与 `StereophonySmooth` 的平滑系数，确保模型动画稳定。 |
| **导出与存储** | `AudioSaveService.cs` 可一次性导出所有捕获音频，支持多通道多种采样率格式。 |
| **设置与调试** | Inspector 面板提供 `StartStop`、`Mode` 选择、实时 `Update` 触发等快捷键。 |

## 用法示例

1. **将脚本挂载至 Unity 场景**  
   ```csharp
   // ① 在场景中创建一个空 GameObject
   // ② 将 AudioController.cs, SpeechRangeEvent.cs 等脚本拖拽至该对象
   // ③ 根据 Inspector 设置所需参数
   ```

2. **配置音频参数**  
   - `InputSource` 设为 “Mic” 以使用麦克风；或 “Clip” 用已有 `AudioClip` 播放。  
   - 调整 `Threshold` 对话框以获得最佳语音检测阈值。  
   - 通过滑块 `SpeakSmooth` 与 `StereophonySmooth` 细调平滑系数。

3. **启动实时采集**  
   ```csharp
   // Inspector 中勾选 AutoStart，或手动点击 Start克风权限
   ```

4. **导出音频**  
   - 运行完毕后，使用 `Save` 按钮将所有捕获片段导出为 WAV/FLAC 文件。  
   - 导出路径默认位于 `Application.persistentDataPath/Audio`。  

5. **集成后端服务（可选）**  
   ```csharp
   // 修改 AudioController.cs 中的 WebSocketURL
   // AudioController 在 Start 时即自动连接
   ```

> **小贴士**  
> - 若使用 WebGL，需要开启 `DOM -> WebGL -> Audio` 权限。  
> - 对于多语言项目，可在 `SpeechRangeEvent.cs` 添加多语言检测阈值。

---
> **文档保存路径**  
> 该说明需以 Markdown 格式保存为src/content/docs/00/OpenAvatarChat_HumanAIGC-Engineering.md`。请直接将上述内容复制至对应文件即可。