---
title: VirtualWife
---


# VirtualWife 项目概述

## 项目地址
[https://github.com/yakami129/VirtualWife?tab=readme-ov-file](https://github.com/yakami129/VirtualWife?tab=readme-ov-file)

## 主要特性
- **逼真 3D 女伴模型**：基于 Unity 的高质量人物模型，支持动态表情与动作捕捉。  
- **语音交互**：集成语音识别与文本转语音，可通过麦克风与虚拟伴侣对话。  
- **情绪反馈**：根据用户语音和动作判定情绪，实时更新角色表情与语音语调。  
- **虚拟场景多样化**：提供多个可切换的交互环境（客厅、卧室、户外等），支持动态灯光与天气效果。  
- **自定义化与可扩展性**：支持换装、发型、配饰自定义，团队可通过插件方式扩展新功能。  
- **VR/AR 兼容**：兼容 Oculus Quest/VR、HoloLens 等设备，提供手势与头部跟踪交互。  

## 功能说明
| 功能 | 描述 |
|------|------|
| **语音输入** | 通过麦克风接收用户语音，转为文字后与 AI 交互，生成自然回复。 |
| **实时表情** | 根据识别到的情绪（如开心、伤心、愤怒）改变模型表情与动画。 |
| **交互动作** | 使用手柄或手势识别实现握手、拥抱、点头、摇头等动作。 |
| **场景切换** | UI 按钮或语音命令切换不同交互场景，自动调整光照与音乐。 |
| **自定义穿搭** | 通过菜单选择衣服、配饰、颜色，并即时应用到模型。 |
| **数据记录** | 记录交互日志，可用于后期分析或改进 AI 对话模型。 |

## 用法

1. **克隆项目**  
   ```bash
   git clone https://github.com/yakami129/VirtualWife.git
   cd VirtualWife
   ```

2. **安装 Unity**  
   本项目使用 Unity 2021.3（LTS）并已包含必要的包。  
   - 打开 `VirtualWife/` 目录下的 `VirtualWife.sln`。  
   - Unity 会自动下载缺失的包。

3. **配置设备**  
   - **VR**：连接 Oculus Quest 或其他支持 OpenXR 的设备。  
   - **AR**：如需使用 HoloLens，勾选 `Windows Mixed Reality` 或 `VisionOS` 相关包。  

4. **运行**  
   - 在 Unity 菜单选择 **Build & Run** 或使用 **Play** 模式测试。  
   - 通过 GUI 或语音命令切换场景，体验角色交互。  

5. **自定义**  
   - 打开 `Assets/Character/Custom` 目录，替换模型或贴图。  
   - 修改 `Assets/Scripts/DialogueManager.cs` 以调整对话逻辑。  

6. **打包**  
   - 在 **File → Build Settings** 选择目标平台，点击 **Build**。  
   - 如需发布到 Meta Store 或 Microsoft Store，按官方文档进行签名与调试。  

## 依赖与配置
- **Unity Package Manager**：`com.unity.cinemachine`, `com.unity.visualScripting`, `com.unity.opentargets` 等。  
- **语音识别**：使用 `Microsoft.Azure.CognitiveServices.Speech` 或 `Google Cloud Speech-to-Text`。  
- **文本转语音**：集成 Google Text‑to‑Speech 或 Azure TTS。  

> **提示**：若遇到设备兼容问题，参考 Unity 官方 Support 文档或项目 Wiki。  

---  

> 以上描述基于项目开源代码与官方 README 提供的最新信息。  
