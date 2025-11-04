
---
title: ossnav
---

# OSSNav

**Project URL:**  
<https://github.com/maxiaobang7/ossnav>

---

## 📦 主要特性

| 特色 | 说明 |
|------|------|
| **简洁命令行界面** | 采用类似 `s3cmd` 的语法，操作直观、易学 |
| **支持阿里云 OSS** | 可一键访问、管理 OSS Bucket 及对象 |
| **多功能管理** | 包括列举、上传、下载、删除、同步、权限设置等 |
| **进度显示** | 上传/下载时实时显示进度条 |
| **配置文件 & 环境变量** | 统一管理 AccessKey、SecretKey、Endpoint 等 |
| **批量处理** | `--recursive` 递归操作，`sync` 同步目录 |
| **多线程上传** | 大文件支持分块上传（多线程） |
| **命令帮助** | `ossnav help` 或 `ossnav <command> --help` |

---

## ⚙️ 功能与用法

### 1️⃣ 安装

```bash
# 直接下载安装包
wget https://github.com/maxiaobang7/ossnav/releases/download/v1.0.0/ossnav_linux_amd64.tar.gz
tar xzf ossnav_linux_amd64.tar.gz
sudo mv ossnav /usr/local/bin/
```

或使用 `go` 安装：

```bash
go install github.com/maxiaobang7/ossnav@latest
```

### 2️⃣ 配置

默认配置文件位于 `~/.ossnav/config.yaml`（如不存在则会自动创建）：

```yaml
access_key_id:     "YourAccessKeyID"
access_key_secret: "YourAccessKeySecret"
endpoint:          "oss-cn-hangzhou.aliyuncs.com"
```

也可以使用环境变量：

```bash
export OSSNAV_ACCESS_KEY_ID="YourAccessKeyID"
export OSSNAV_ACCESS_KEY_SECRET="YourAccessKeySecret"
export OSSNAV_ENDPOINT="oss-cn-hangzhou.aliyuncs.com"
```

### 3️⃣ 常用命令

| 命令 | 说明 | 示例 |
|------|------|------|
| `ls` | 列举 Bucket 内容 | `ossnav ls oss://my-bucket/` |
| `cp` | 上传/下载文件 | `ossnav cp localfile.txt oss://my-bucket/`<br>`ossnav cp oss://my-bucket/remote.txt ./` |
| `rm` | 删除对象 | `ossnav rm oss://my-bucket/file.txt` |
| `sync` | 同步目录 | `ossnav sync local_dir/ oss://my-bucket/` |
| `acl` | 设置或查看 ACL | `ossnav acl set oss://my-bucket/file.txt --acl public-read`<br>`ossnav acl get oss://my-bucket/file.txt` |
| `mb` | 创建 Bucket | `ossnav mb oss://my-new-bucket/` |
| `rb` | 删除 Bucket | `ossnav rb oss://my-new-bucket/` |

> 以上命令支持 `--recursive`、`--exclude`、`--include` 等可选参数。

### 4️⃣ 示例

```bash
# 1. 列出 bucket
ossnav ls oss://example-bucket/

# 2. 上传本地文件
ossnav cp ./photo.jpg oss://example-bucket/photos/

# 3. 下载文件到本地
ossnav cp oss://example-bucket/photos/photo.jpg ./photo_downloaded.jpg

# 4. 删除远程文件
ossnav rm oss://example-bucket/photos/old_photo.jpg

# 5. 同步目录（上传本地 -> OSS）
ossnav sync ./local_folder/ oss://example-bucket/

# 6. 同步目录（下载 OSS -> 本地）
ossnav sync oss://example-bucket/ ./remote_folder/
```

### 5️⃣ 进阶用法

- **多线程上传**：默认使用 4 条线程，使用 `--threads` 可调整：

  ```bash
  ossnav cp --threads 8 large_file.zip oss://example-bucket/
  ```

- **分块上传**：通过 `--chunk-size` 调整分块大小（单位 MB）：

  ```bash
  ossnav cp --chunk-size 20 large_file.iso oss://example-bucket/
  ```

- **分配自定义 header**：

  ```bash
  ossnav cp local.txt oss://example-bucket/ --header "x-oss-meta-author=Maxiaobang7"
  ```

- **显示帮助**：

  ```bash
  ossnav help
  # 或者针对单个命令
  ossnav cp --help
  ```

---

## 📚 结语

OSSNav 让你通过命令行就能高效地管理阿里云 OSS，适用于快速备份、同步以及日常文件操作。欢迎尝试并提出任何建议或 issue！