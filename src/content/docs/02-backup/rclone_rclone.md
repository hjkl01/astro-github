---
title: rclone
---

# Rclone 项目

## 项目地址

[https://github.com/rclone/rclone](https://github.com/rclone/rclone)

## 主要特性

Rclone（“rsync for cloud storage”）是一个命令行程序，用于在不同云存储提供商之间同步文件和目录。

- MD5/SHA-1 哈希始终检查文件完整性
- 文件上的时间戳保留
- 支持整个文件基础上的部分同步
- [Copy](https://rclone.org/commands/rclone_copy/) 模式仅复制新/更改的文件
- [Sync](https://rclone.org/commands/rclone_sync/)（单向）模式使目录相同
- [Bisync](https://rclone.org/bisync/)（双向）保持两个目录双向同步
- [Check](https://rclone.org/commands/rclone_check/) 模式检查文件哈希相等
- 可以同步到和从网络，例如两个不同的云账户
- 可选大文件分块（[Chunker](https://rclone.org/chunker/)）
- 可选透明压缩（[Compress](https://rclone.org/compress/)）
- 可选加密（[Crypt](https://rclone.org/crypt/)）
- 可选 FUSE 挂载（[rclone mount](https://rclone.org/commands/rclone_mount/)）
- 多线程下载到本地磁盘
- 可以 [serve](https://rclone.org/commands/rclone_serve/) 本地或远程文件通过 HTTP/WebDAV/FTP/SFTP/DLNA

## 主要功能

Rclone 支持超过 70 种云存储服务，包括 Google Drive、S3、Dropbox、Backblaze B2、One Drive、Swift、Hubic、Wasabi、Google Cloud Storage、Azure Blob、Azure Files、Yandex Files 等。请查看完整存储提供商及其功能列表。

## 用法

请访问 [rclone 网站](https://rclone.org/) 获取安装、文档和配置信息。
