
---
title: restic
---

# Restic 项目

## 项目地址
[https://github.com/restic/restic](https://github.com/restic/restic)

## 主要特性
Restic 是一个快速、安全、备份文件和目录的命令行程序，支持增量备份、加密和去重。它的核心特性包括：
- **加密备份**：所有备份数据使用 AES-256 加密，确保数据隐私和安全性。
- **去重和增量备份**：自动检测重复数据块，只存储变化部分，提高存储效率。
- **支持多种后端**：可以备份到本地文件系统、SFTP、REST 服务器、AWS S3、Backblaze B2、Microsoft Azure Blob 等多种存储服务。
- **快照管理**：创建、检查和恢复文件快照，支持版本控制和历史回溯。
- **无供应商锁定**：数据格式开源，用户可以自由迁移或恢复数据。
- **跨平台支持**：适用于 Linux、macOS 和 Windows，支持 ARM 和 x86 架构。
- **高效性能**：使用并行处理和内容寻址存储，备份和恢复速度快。

## 主要功能
- **备份（Backup）**：备份文件、目录或整个系统，支持排除规则和标签。
- **快照管理（Snapshots）**：列出、删除和检查备份快照。
- **恢复（Restore）**：从指定快照恢复文件或目录，支持部分恢复。
- **检查和验证（Check）**：验证备份完整性，检测损坏或不一致。
- **挂载（Mount）**：将备份快照挂载为文件系统，便于浏览。
- **忘记和清理（Forget/Prune）**：根据策略自动删除旧快照，释放空间。
- **生成报告**：统计备份大小、使用情况和历史数据。

## 用法
Restic 使用命令行接口，首先需要初始化仓库，然后进行备份和恢复。以下是基本用法示例（假设已安装 restic 二进制文件）：

### 1. 初始化仓库
```bash
# 初始化本地仓库
restic -r /path/to/repo init

# 初始化远程仓库（如 S3）
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
restic -r s3:s3.amazonaws.com/bucket init
```

### 2. 备份
```bash
# 备份目录（使用密码环境变量）
export RESTIC_PASSWORD=your_password
restic -r /path/to/repo backup /home/user --exclude=/home/user/tmp
```

### 3. 列出快照
```bash
restic -r /path/to/repo snapshots
```

### 4. 恢复
```bash
restic -r /path/to/repo restore latest --target /restore/path --include /home/user/docs
```

### 5. 检查和清理
```bash
# 检查仓库完整性
restic -r /path/to/repo check

# 忘记旧快照并清理
restic -r /path/to/repo forget --keep-last 5 --prune
```

更多高级用法请参考官方文档：https://restic.readthedocs.io。安装方式包括从 GitHub Releases 下载二进制文件或使用包管理器（如 apt、brew）。