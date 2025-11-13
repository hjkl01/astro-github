---
title: kopia
---

# Kopia 项目

**GitHub 项目地址:** [https://github.com/kopia/kopia](https://github.com/kopia/kopia)

## 主要特性

Kopia 是一个快速和安全的开源备份/恢复工具，允许您创建加密快照并将快照保存到您选择的远程或云存储、本地网络附加存储或服务器，或本地机器上。Kopia 不“镜像”您的整个机器。而是允许您备份/恢复您认为重要或关键的任何和所有文件/目录。

Kopia 具有 CLI（命令行界面）和 GUI（图形用户界面）版本，使其成为高级和普通用户的完美工具。您可以阅读 Kopia 的独特功能——包括压缩、重复数据删除、用户控制的端到端加密和错误纠正——以更好地了解 Kopia 的工作原理。

当准备好时，请访问安装页面下载并安装 Kopia，并确保阅读入门指南以获取 Kopia 使用的一步一步演练。

## 主要功能

Kopia 支持将加密和压缩的快照保存到以下存储位置：

- Amazon S3 和任何与 S3 兼容的云存储
- Azure Blob Storage
- Backblaze B2
- Google Cloud Storage
- 任何支持 WebDAV 的远程服务器或云存储
- 任何支持 SFTP 的远程服务器或云存储
- 一些 Rclone 支持的云存储选项（需要另外下载并设置 Rclone，然后 Kopia 管理/运行 Rclone；Rclone 支持是实验性的：并非所有 Rclone 支持的云存储产品都经过测试与 Kopia 兼容，一些可能不与 Kopia 兼容；Kopia 已测试与 Dropbox、OneDrive 和 Google Drive 通过 Rclone 兼容）
- 您的本地机器和任何网络附加存储或服务器
- 通过设置 Kopia Repository Server 的您自己的服务器

Kopia 使用数据重复数据删除来为您节省资金！阅读存储库帮助页面以获取有关支持存储位置的更多信息。

使用 Kopia，您完全控制存储快照的位置，即您选择要使用的存储提供商。您必须为任何存储位置的存储提供商提供和付费，然后告诉 Kopia 这些存储位置是什么。您甚至可以为不同的备份存储库使用多个存储位置。您也可以支持在同一存储位置备份多个机器。

## 用法

请访问 [Kopia 文档](https://kopia.io/docs/) 获取更多信息。
