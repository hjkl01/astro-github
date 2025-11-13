---
title: social-app
---

# Bluesky Social App 项目

## 项目地址
[GitHub 项目地址](https://github.com/bluesky-social/social-app)

## 主要特性
Bluesky Social App 是 Bluesky 社交网络的官方移动应用程序项目，基于 AT Protocol（一个去中心化的社交协议）构建。主要特性包括：
- **去中心化社交体验**：用户可以选择不同的服务器（Pods），支持数据迁移和互操作性，避免单一平台的控制。
- **自定义 feeds 和算法**：用户可订阅多种 feeds（如时间线、话题或个性化推荐），并自定义算法以控制内容显示。
- **开源与透明**：整个项目开源，允许开发者贡献代码、修改功能或构建扩展。
- **隐私与控制**：强调用户数据所有权，支持内容过滤、屏蔽和报告机制。
- **跨平台支持**：主要针对 iOS 和 Android 开发，使用 React Native 框架实现。

## 主要功能
- **发帖与互动**：用户可以发布文本、图片、视频等内容，支持点赞、回复、转发和引用。
- **发现与搜索**：内置搜索功能、趋势话题和用户发现，支持 hashtags 和高级过滤。
- **通知系统**：实时推送互动通知，如新关注、回复或提及。
- **账户管理**：创建账户、登录、设置隐私选项，并支持多设备同步。
- **集成 AT Protocol**：兼容 Bluesky 的去中心化生态，包括与其他协议兼容的工具和应用。

## 用法
1. **克隆仓库**：在终端运行 `git clone https://github.com/bluesky-social/social-app.git` 下载项目。
2. **安装依赖**：进入项目目录，运行 `npm install` 或 `yarn install` 安装 Node.js 依赖。
3. **构建与运行**：
   - 对于 iOS：运行 `npm run ios`（需 Xcode 和 CocoaPods）。
   - 对于 Android：运行 `npm run android`（需 Android Studio 和 SDK）。
4. **开发与贡献**：使用 VS Code 等编辑器修改代码，遵循 CONTRIBUTING.md 指南提交 Pull Request。测试时需配置 Bluesky API 密钥。
5. **部署**：项目主要用于本地开发或贡献；生产部署需参考 Bluesky 官方文档集成到 App Store 或 Google Play。

此项目适合开发者探索去中心化社交技术，或贡献 Bluesky 生态。