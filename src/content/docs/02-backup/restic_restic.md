---
title: restic
---

# Restic 项目

## 项目地址

[https://github.com/restic/restic](https://github.com/restic/restic)

## 主要特性

restic 是一个备份程序，它快速、高效且安全。它支持三个主要操作系统（Linux、macOS、Windows）和一些较小的操作系统（FreeBSD、OpenBSD）。

Restic 是一个正确备份的程序，并设计遵循以下原则：

- **易用**：备份应该是一个无摩擦的过程，否则您可能会倾向于跳过它。Restic 应该易于配置和使用，以便在数据丢失事件中，您可以只恢复它。同样，恢复数据不应该复杂。

- **快速**：使用 restic 备份您的数据应该只受限于您的网络或硬盘带宽，以便您每天备份文件。没有人做备份如果它需要太多时间。恢复备份应该只传输恢复文件所需的数据，以便这个过程也快速。

- **可验证**：比备份更重要的是恢复，所以 restic 使您能够轻松验证所有数据都可以恢复。

- **安全**：Restic 使用加密来保证数据的机密性和完整性。存储备份的位置被假定为不受信任的环境（例如，其他人如系统管理员可以访问您的备份的共享空间）。Restic 旨在保护您的数据免受此类攻击者。

- **高效**：随着数据增长，额外快照应该只占用实际增量的存储。更重要的是，重复数据应该在实际写入存储后端之前进行重复数据删除，以节省宝贵的备份空间。

## 主要功能

restic 支持以下后端用于本地存储备份：

- [本地目录](https://restic.readthedocs.io/en/latest/030_preparing_a_new_repo.html#local)
- [sftp 服务器（通过 SSH）](https://restic.readthedocs.io/en/latest/030_preparing_a_new_repo.html#sftp)
- [HTTP REST 服务器](https://restic.readthedocs.io/en/latest/030_preparing_a_new_repo.html#rest-server)（[协议](https://restic.readthedocs.io/en/latest/100_references.html#rest-backend)，[rest-server](https://github.com/restic/rest-server)）
- [Amazon S3](https://restic.readthedocs.io/en/latest/030_preparing_a_new_repo.html#amazon-s3)（来自 Amazon 或使用 [Minio](https://minio.io) 服务器）
- [OpenStack Swift](https://restic.readthedocs.io/en/latest/030_preparing_a_new_repo.html#openstack-swift)
- [BackBlaze B2](https://restic.readthedocs.io/en/latest/030_preparing_a_new_repo.html#backblaze-b2)
- [Microsoft Azure Blob Storage](https://restic.readthedocs.io/en/latest/030_preparing_a_new_repo.html#microsoft-azure-blob-storage)
- [Google Cloud Storage](https://restic.readthedocs.io/en/latest/030_preparing_a_new_repo.html#google-cloud-storage)
- 通过 [rclone](https://rclone.org) [后端](https://restic.readthedocs.io/en/latest/030_preparing_a_new_repo.html#other-services-via-rclone) 的许多其他服务

## 用法

请查看 [restic 文档](https://restic.readthedocs.io/en/latest) 获取详细用法和安装说明。
