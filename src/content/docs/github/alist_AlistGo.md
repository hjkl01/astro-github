
---
title: alist
---


# AlistGo/alist

> **项目地址**: <https://github.com/AlistGo/alist>

---

## 一、项目简介
Alist 是一款基于 Go 语言开发的轻量级文件管理系统，支持多种云存储驱动（本地文件、S3、Aliyun OSS、Google Cloud Storage、Cloudflare R2 等）以及 WebDAV、Git、SFTP 等协议的同步与加密。它提供了直观的 WebUI 与命令行工具，适用于个人与团队的文件共享、备份与协作。

---

## 二、核心功能

| 功能 | 说明 |
|------|------|
| **多存储后端** | 支持 20+ 云存储服务（S3、OSS、MinIO、FTP、SFTP、WebDAV、WebDAV、Google Drive、Microsoft Azure、阿里云 OSS、腾讯云 COS 等）。 |
| **文件操作** | 上传、下载、删除、重命名、移动、复制、压缩解压、快照、时间戳切片。 |
| **分享 & 公开链接** | 为单个文件/目录生成公开链接、token 链接、临时分享链接，支持密码访问、有效期设定。 |
| **WebDAV 同步** | 通过 WebDAV 协议与多端同步，支持双向冲突解决。 |
| **CLI 与 API** | 提供官方命令行工具 alistctl 与 RESTful API，支持批量操作与自动化脚本。 |
| **权限管理** | 通过账号组、Token、Web Auth 实现细粒度访问控制。 |
| **插件/扩展** | 支持基于插件系统的功能扩展（如 OneDrive、Nextcloud、使命扩展）。 |
| **安全** | 全量 HTTPS(支持自签/CA证书)、JWT 验证、CSRF 保护、日志审计、账户双重验证码。 |

---

## 三、特色亮点

- **极简部署**：单二进制文件，无需数据库；Docker 镜像一次部署即可上线。
- **快速性能**：内置 HTTP/3, TCP Nagle、连接池，支持高并发读写。
- **支持多端**：自带官方手机 App 与桌面 App（基于 Electron 的桌面版本）。
- **模块化架构**：统一的存储抽象层，新增驱动仅需实现接口，代码量低。
- **自动更新**：内置版本检测与自动更新（CLI 方式），配合 Docker Compose 可一键升级。

---

## 四、安装与运行

### 1. Docker Compose 一键部署

```yaml
version: "3.9"
services:
  alist:
    image: alistgo/alist:latest
    container_name: alist
    ports:
      - "5244:5244"
    volumes:
      - ./data:/app/data
      - ./config.yml:/app/config.yml
    restart: unless-stopped
```

```bash
# 创建配置目录
mkdir -p data
# 复制默认配置到 host（可自行编辑）
docker run --rm -v ${PWD}:/backup alistgo/alist:latest cp /app/config.yml /backup/config.yml
# 启动
docker compose up -d
```

> 访问地址: `http://<宿主机IP>:5244`

### 2. 直接下载二进制

```bash
# 下载
wget https://github.com/AlistGo/alist/releases/latest/download/alist_linux_amd64.tar.gz
tar -xzvf alist_linux_amd64.tar.gz
sudo mv alist /usr/local/bin/
# 启动
alist
```

> 运行后会在 `./data` 目录下生成 `config.yml`，按需修改。

---

## 五、基本用法

### 1. 配置文件示例（config.yml）

```yaml
# 基本信息
app:
  baseUrl: http://localhost:5244
  listenHttp: 5244
  enableHttps: false

# 存储驱动
storage:
  drive: local
  local:
    root: /data

# 用户
accounts:
  - name: admin
    password: <hashed_password>
    role: admin

# 分享链接
share:
  openLink:
    enable: true
    expire: 24h
```

> 上述仅为最小配置示例，详细参数请参考官方文档。

### 2. 命令行工具 (alistctl)

```bash
# 列出存储路径
alistctl list --path /

# 上传文件
alistctl upload --path /docs/report.pdf ./report.pdf

# 删除
alistctl delete --path /docs/report.pdf

# 生成公开链接
alistctl share --path /docs/report.pdf --expire 12h
```

---

## 六、常见问题

- **文件上传大文件卡住**  
  解决方案：开启 HTTP3 或调整 `chunkSize` 参数；或使用官方桌面/移动 App 直接上传。

- **HTTPS 证书报错**  
  在自签证书的情况下请在浏览器中信任证书，或者使用 Let's Encrypt。

- **权限报 403**  
  检查 `config.yml` 中的用户名/密码 Hash 是否正确，或确认 `drive` 区域权限。

---

## 七、贡献 & 开发

```bash
# 克隆仓库
git clone https://github.com/AlistGo/alist.git
cd alist
# 编译
go build

# 开发分支
git checkout -b feature/your-feature
```

> 提交前请先运行 `go test ./...` 与 `golangci-lint run`，并保持代码风格一致。

---

## 八、参考链接

- 官方网站: <https://alist.miyoushe.com/>
- 讨论组: <https://github.com/AlistGo/alist/discussions>
- 文档仓库: 本文件包含基础使用信息，更多高级用法请参阅项目 Wiki。

--- 
```

*文件已生成在 `src/content/docs/00/alist_AlistGo.md`*