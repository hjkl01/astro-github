---
title: Atlas
---

# Atlas

<p align="center">
    <a href="https://github.com/Atlas-OS/Atlas/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/atlas-os/atlas?style=for-the-badge&logo=github&color=1A91FF"/></a>
    <a href="https://github.com/Atlas-OS/Atlas/graphs/contributors"><img alt="Contributors" src="https://img.shields.io/github/contributors/atlas-os/atlas?style=for-the-badge&color=1A91FF" /></a>
    <a href="https://github.com/Atlas-OS/Atlas/releases/latest"><img alt="Release" src="https://img.shields.io/github/release/atlas-os/atlas?style=for-the-badge&color=1A91FF" /></a>
    <a href="https://github.com/Atlas-OS/.github/blob/main/profile/CODE_OF_CONDUCT.md"><img alt="Code of Conduct" src="https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg?style=for-the-badge&color=1A91FF" /></a>
  </p>
<p align="center">一个透明且轻量的 Windows 修改，旨在优化性能、隐私和可用性。</p>

<p align="center">
  <a href="https://atlasos.net" target="_blank">🌐 网站</a>
  •
  <a href="https://docs.atlasos.net" target="_blank">📚 文档</a>
  •
  <a href="https://discord.atlasos.net" target="_blank">☎️ Discord</a>
  •
  <a href="https://github.com/Atlas-OS/Atlas/discussions" target="_blank">💬 讨论</a>
</p>

## 📚 **重要文档**

- [安装](https://docs.atlasos.net/getting-started/installation/)
- [安装 FAQ](https://docs.atlasos.net/install-faq/removed-features/)
- [一般 FAQ](https://docs.atlasos.net/general-faq/atlas-and-security/)
- [贡献指南](https://docs.atlasos.net/contributing/contribution-guidelines/)
- [品牌](https://docs.atlasos.net/branding/)

## 🤔 什么是 Atlas？

AtlasOS，或 Atlas，是一个开源项目，通过方便地应用隐私、可用性和性能优化来增强 Windows，同时保持功能性和 [自定义性](https://docs.atlasos.net/getting-started/post-installation/atlas-folder/general-configuration/)。

## 👀 为什么选择 Atlas？

### 🔒 增强隐私

Atlas 移除 Windows 中嵌入的大多数遥测，并实施众多组策略以最小化数据收集。然而，它无法确保 Windows 范围之外的隐私，例如浏览器和其他第三方应用程序。

### 📈 优化性能

Atlas 在性能和兼容性之间取得平衡。它实施众多有意义的更改以改善 Windows 性能和响应性，而不破坏基本功能。Atlas 不会做安慰剂效果或边际收益的调整，使 Atlas 更稳定和兼容。

### 🛡️ 安全特性

大多数 Windows 修改移除大多数用户需要维护安全系统的关键安全功能。另一方面，Atlas 允许用户在自己的风险下自定义他们的安全，同时告知用户每个选项的 [利弊](https://docs.atlasos.net/getting-started/post-installation/atlas-folder/security/)。

一些可选安全功能包括：

- Windows Defender & SmartScreen
- Windows Update
- 自动更新是可切换的
- CPU 缓解
- 用户账户控制
- 核心隔离功能

### ✅ 增加可用性

Atlas 应用许多修改和默认设置，使 Windows 更容易使用。这包括移除常用不需要的应用（可重新安装）、配置界面许多方面、禁用广告等。

### 🔍 开源和透明

与自定义 Windows ISO 不同，由于使用 [AME Wizard](https://amelabs.net)，Atlas 更容易审计。AME Wizard 由 Playbooks 控制，这是一个可自定义的脚本式系统，可以执行各种任务。

Playbooks 是重命名的 **.zip** 档案，密码为 [`malte`](https://docs.atlasos.net/developers/getting-started/creation.html)。由于它们主要由纯文本组成，Playbooks 启用透明性，与自定义 Windows ISO 不同，后者有许多恶意活动的入口点。

Playbook 中的少数二进制文件在我们 [`utilities` 仓库](https://github.com/Atlas-OS/utilities) 中开源， [哈希列在这里](https://github.com/Atlas-OS/Atlas/blob/main/src/playbook/Executables/AtlasModules/README.md)。

虽然 AME Wizard 的 GUI 不是开源的，但 AME Wizard 的整个后端（称为 [TrustedUninstaller](https://github.com/Ameliorated-LLC/trusted-uninstaller-cli)）在 MIT 下开源，其中包含运行 Atlas 使用的每个动作。Atlas Playbook 在 [GPLv3 许可证](https://github.com/Atlas-OS/Atlas/blob/main/LICENSE) 下开源。

### 🔒 法律合规

由于 Atlas 不重新分发修改的 Windows ISO，它符合 [Microsoft Windows 使用条款](<https://www.microsoft.com/content/dam/microsoft/usetm/documents/windows/11/oem-(pre-installed)/UseTerms_OEM_Windows_11_English.pdf>)。此外，Atlas 不改变 Windows 中的激活。

## 🎨 品牌套件

想要用原创创意设计创建自己的 Atlas 壁纸？访问我们的 [文档上的品牌套件](https://docs.atlasos.net/branding/) 并在我们的 [GitHub 讨论](https://github.com/Atlas-OS/Atlas/discussions/categories/community-artwork) 中分享你的创作！

## 💙 贡献者

<a href="https://github.com/Atlas-OS/Atlas/graphs/contributors" target="_blank"><img src="https://contrib.rocks/image?repo=Atlas-OS/Atlas&columns=18" alt="所有贡献者的头像"></a>
