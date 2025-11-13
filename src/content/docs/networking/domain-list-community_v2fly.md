---
title: Domain List Community
---

# Domain List Community

Domain List Community 是一个社区管理的域名列表项目，用于为 V2Ray 等代理工具生成 geosite.dat 文件。该项目不主张或暗示任何域名应被阻塞或代理，仅提供用于按需生成路由规则的域名列表。

## 功能

- **社区维护**：由社区贡献者维护的域名列表，支持分类和属性标记。
- **生成 geosite.dat**：将域名列表编译成二进制格式，用于 V2Ray 的路由规则。
- **灵活规则**：支持域名、关键词、正则表达式和完整域名匹配。
- **属性支持**：允许为域名添加属性，如 `@ads`，用于子组过滤。

## 用法

### 下载预编译文件

- **dlc.dat**：[最新版本下载](https://github.com/v2fly/domain-list-community/releases/latest/download/dlc.dat)
- **校验文件**：[SHA256 校验](https://github.com/v2fly/domain-list-community/releases/latest/download/dlc.dat.sha256sum)

### 在 V2Ray 配置中使用

在 V2Ray 的路由规则中使用 `geosite:filename` 格式引用列表。

### 手动生成 dlc.dat

1. 安装 Go 和 Git。
2. 克隆项目：`git clone https://github.com/v2fly/domain-list-community.git`
3. 进入目录：`cd domain-list-community`
4. 下载依赖：`go mod download`
5. 生成文件：`go run ./`

### 数据结构

域名列表存储在 `data` 目录下，每个文件代表一个子列表。文件格式包括：

- `domain:example.com`：子域名匹配
- `keyword:google`：关键词匹配
- `regexp:www\.google\.com$`：正则表达式匹配
- `full:www.google.com`：完整域名匹配
- `include:another-file`：包含其他文件
- `@attr`：属性标记

### 贡献

- Fork 项目，提交 PR。
- PR 需通过自动化测试。
- 小型 PR 优先，需经审核。
