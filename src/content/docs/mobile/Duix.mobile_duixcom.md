---
title: Duix.mobile
---

# Duix Mobile 项目

**GitHub 项目地址：** [https://github.com/duixcom/Duix.mobile](https://github.com/duixcom/Duix.mobile)

## 主要特性

Duix Mobile 是一个开源 SDK，由 [www.duix.com](http://www.duix.com) 开发，用于在移动设备或嵌入式屏幕上创建实时交互式 AI 数字人。它支持跨平台部署（iOS / Android / 平板 / 车载系统 / VR / IoT / 大屏交互等），开发者可以轻松集成自有或第三方的大语言模型（LLM）、语音识别（ASR）和语音合成（TTS）服务。主要特性包括：

- **仿真数字人体验**：自然呈现面部表情、语调和情绪共鸣，打造「像人一样」的 AI 对话。
- **支持流式音频**：边合成、边说话，支持中途打断、抢话，让数字人不仅会说话，而且更像「人」。
- **极致响应速度**：数字人响应延迟低于 120ms（测试设备为骁龙® 8 Gen 2 SoC），带来毫秒级流畅互动体验。
- **成本友好，随处部署**：轻量化运行，资源占用极低，轻松适配手机、平板、智能屏等终端。
- **无惧弱网环境**：核心处理本地完成，对网络依赖极低，尤其适合金融、政务、法律等高稳定性场景。
- **全行业适配**：模块化设计，支持快速定制，轻松打造各行业专属数字人解决方案。

## 应用场景

- 智能客服
- 虚拟医生
- 虚拟律师
- 虚拟陪伴
- 虚拟教学
- 其他需要实时对话数字人的场景

## 主要功能

- **实时对话数字人**：支持自然语言对话，集成 LLM、ASR、TTS。
- **唇动同步**：数字人说话时唇部同步。
- **多语种字幕**：支持多种语言字幕显示。
- **自定义数字人**：提供公有数字人下载，支持私有定制。
- **跨平台支持**：Android 和 iOS 一键部署。

## 用法

1. **克隆项目**：
   - 使用 Git 命令克隆仓库：`git clone https://github.com/duixcom/Duix.mobile.git`。

2. **开发集成**：
   - 对于 Android 开发者：参考 [Duix Mobile SDK for Android](./duix-android/dh_aigc_android/README_zh.md)。
   - 对于 iOS 开发者：参考 [Duix Mobile SDK for iOS](./duix-ios/GJLocalDigitalDemo/README_zh.md)。

3. **集成 LLM、ASR、TTS**：
   - 支持集成自有或第三方服务，实现自定义对话逻辑。

4. **下载公有数字人**：
   - 从项目 Releases 下载预训练的数字人模型，如 Leo、Oliver、Sofia、Lily。

5. **定制私有数字人**：
   - 联系 support@duix.com 或企业微信进行定制，通常需要 15 秒至 2 分钟的视频样本。

该项目适合开发者构建交互式 AI 数字人应用，鼓励开源贡献和反馈。
