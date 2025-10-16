
---
title: kopia
---

# Kopia 项目

**GitHub 项目地址:** [https://github.com/kopia/kopia](https://github.com/kopia/kopia)

## 主要特性

Kopia 是一个开源的备份工具，专注于高效、安全的数据备份和恢复。它支持多种存储后端（如本地文件系统、云存储），并采用内容定义的块存储模型来优化空间和性能。主要特性包括：

- **高效去重和压缩**：自动检测和去除重复数据块，仅存储唯一内容，显著减少存储需求。同时支持多种压缩算法（如 LZ4、Zstandard）来进一步节省空间。
- **端到端加密**：使用 AES-256 加密保护备份数据，支持主密码和密钥管理，确保数据隐私和安全性。
- **增量备份**：仅备份自上次备份以来的更改，支持快照式备份，适用于文件、目录或整个系统。
- **多存储后端支持**：兼容本地磁盘、S3 兼容存储（如 AWS S3、MinIO）、Google Cloud Storage、Azure Blob 等云服务，以及 SFTP 和 Rclone 后端。
- **跨平台兼容**：支持 Windows、macOS 和 Linux 系统，提供命令行界面（CLI）和图形用户界面（GUI）。
- **版本管理和恢复**：保留备份历史，支持点对点恢复、文件级恢复或完整系统恢复。内置搜索功能可快速定位文件。
- **性能优化**：多线程上传/下载、并行处理，支持大文件分块传输，适合企业级备份场景。

## 主要功能

- **备份功能**：创建文件/目录备份，支持计划任务（如 cron 式调度）和手动触发。备份策略包括过滤器（排除特定文件类型）和优先级设置。
- **恢复功能**：从备份中恢复单个文件、目录或整个卷，支持到原位置或新位置恢复。
- **仓库管理**：初始化和管理备份仓库，配置加密密钥和存储连接。支持仓库迁移和验证完整性。
- **快照和政策**：定义备份政策，包括保留期、频率和保持策略（如智能保留旧版本）。
- **监控和报告**：生成备份报告、错误日志和统计信息，支持集成到监控系统中。
- **高级功能**：如合成备份（合并增量以生成完整备份）、错误恢复和插件扩展。

## 用法

Kopia 通过命令行工具 `kopia` 操作，安装后可直接使用。以下是基本用法示例（假设已安装）：

### 1. 安装
- 从 GitHub Releases 下载二进制文件，或使用包管理器（如 `brew install kopia/kopia/kopia` on macOS）。
- Windows/Linux：解压并添加到 PATH。

### 2. 初始化仓库
```bash
# 创建新仓库（本地存储示例）
kopia repository create filesystem --path=/path/to/repo --password=your-master-password

# 云存储示例（S3）
kopia repository create s3 --bucket=my-bucket --endpoint=s3.amazonaws.com --password=your-master-password
```

### 3. 配置备份
```bash
# 设置备份源（例如，备份 /home/user 目录）
kopia snapshot create /home/user --policy-file=backup-policy.json

# 定义政策文件（backup-policy.json 示例）
{
  "files": {
    "compression": "zstd",
    "exclude": ["*.tmp", "**/node_modules/"]
  },
  "retention": {
    "keepLatest": 7,
    "keepHourly": 24
  }
}
```

### 4. 执行备份
```bash
# 手动备份
kopia snapshot create /path/to/source

# 计划备份（使用外部调度器如 cron）
# 示例 cron: 0 2 * * * /usr/bin/kopia snapshot create /home/user
```

### 5. 恢复数据
```bash
# 列出快照
kopia snapshot list

# 恢复到指定位置
kopia mount //snapshot-id /mount/point  # 挂载为文件系统浏览
# 或直接恢复
kopia snapshot restore snapshot-id --target=/restore/path
```

### 6. 其他命令
- `kopia repository status`：检查仓库状态。
- `kopia snapshot verify`：验证备份完整性。
- GUI 模式：`kopia server` 启动 Web 界面访问（http://localhost:16443）。

详细文档请参考项目 README 或官方 wiki。Kopia 适合个人和企业用于数据保护，强调简单性和可靠性。