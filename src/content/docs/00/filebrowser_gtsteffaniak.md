
---
title: filebrowser
---


# Filebrowser (gtsteffaniak)

**仓库地址**: <https://github.com/gtsteffaniak/filebrowser>

---

## 主要特性

| 特色 | 说明 |
|------|------|
| **文件管理** | 浏览、上传、下载、重命名、复制、移动、删除、压缩/解压文件夹 |
| **权限控制** | 基于用户/组的读写/执行权限，支持 ACL  |
| **Web UI** | 响应式图形界面，支持多语言（默认中文/英文） |
| **命令行工具** | 通过 `filebrowser` 命令可在终端管理文件 |
| **身份验证** | 支持本地文件系统凭证、LDAP、OAuth2 等多种登录方式 |
| **插件系统** | 可扩展功能插件（如 FTP、S3、Google Drive） |
| **API** | RESTful API 提供文件操作、用户管理、日志等接口 |
| **日志与审计** | 详细操作日志，支持导出与搜索 |
| **多租户** | 通过配置文件可隔离不同用户的根目录 |

---

## 安装与运行

1. **Docker**（推荐）  
   ```bash
   docker run -d \
     -p 8080:80 \
     -v /path/to/data:/srv \
     -v /path/to/config:/config \
     -e PUID=$(id -u) -e PGID=$(id -g) \
     -e TZ=Asia/Shanghai \
     filebrowser/filebrowser:something
   ```

2. **二进制**  
   ```bash
   wget https://github.com/filebrowser/filebrowser/releases/download/v2.19.0/filebrowser_linux_amd64
   chmod +x filebrowser_linux_amd64
   ./filebrowser_linux_amd64
   ```

3. **源码**  
   ```bash
   go get github.com/filebrowser/filebrowser
   cd $(go env GOPATH)/src/github.com/filebrowser/filebrowser
   go build
   ./filebrowser
   ```

---

## 用法

### 1. 启动并访问

- 默认访问地址：`http://localhost:8080`
- 初始管理员账号：`admin` / `admin`

> **重要**：首次登录后请立即修改管理员密码。

### 2. 配置根目录

- 在 Docker 运行时使用 `-v /data:/srv` 指定根目录。
- 或在 `config.json` 中设置 `root` 字段。

### 3. 用户与权限管理

```json
{
  "users": [
    {
      "name": "alice",
      "password": "hashed_password",
      "groups": ["dev"]
    }
  ],
  "groups": [
    {
      "name": "dev",
      "permissions": {
        "read": true,
        "write": true,
        "execute": false
      }
    }
  ]
}
```

### 4. 使用 API

- **获取文件列表**  
  `GET /api/files?path=/`
- **上传文件**  
  `POST /api/upload?path=/` (multipart/form-data)
- **删除文件**  
  `DELETE /api/files?path=/file.txt`

> 详细 API 文档请参阅 `docs/api.md`。

### 5. 插件使用

```bash
# 安装插件
filebrowser plugin install <plugin_name>

# 例如安装 Google Drive
filebrowser plugin install filebrowser-plugin-gdrive
```

---

## 贡献

- Fork → Clone → `make build` → 提交 PR
- 代码规范：使用 Go 1.22+，遵循 `gofmt` 格式
- 任何问题请创建 Issue，或加入 Discord 社区讨论

---

## 许可证

MIT

---```
