---
title: ezbookkeeping
---

# ezBookkeeping

## 功能

ezBookkeeping 是一个轻量级的自托管个人财务应用，具有用户友好的界面和强大的记账功能。它易于部署，只需一个 Docker 命令即可启动。设计为资源高效且高度可扩展，可在 Raspberry Pi 等小型设备上流畅运行，或扩展到 NAS、微服务器甚至大型集群环境。

ezBookkeeping 为移动和桌面设备提供定制界面，支持 PWA（渐进式 Web 应用），您甚至可以将其添加到移动主屏幕，像原生应用一样使用。

### 主要功能

- **开源 & 自托管**
  - 注重隐私和控制
- **轻量 & 快速**
  - 性能优化，即使在低资源环境中也能流畅运行
- **易安装**
  - Docker 就绪
  - 支持 SQLite、MySQL、PostgreSQL
  - 跨平台（Windows、macOS、Linux）
  - 支持 x86、amd64、ARM 架构
- **用户友好界面**
  - UI 针对移动和桌面优化
  - PWA 支持，提供类似原生的移动体验
  - 暗模式
- **AI 功能**
  - 收据图像识别
  - 支持 MCP（模型上下文协议）进行 AI 集成
- **强大记账**
  - 两级账户和类别
  - 交易附加图像
  - 位置跟踪与地图
  - 重复交易
  - 高级过滤、搜索、可视化和分析
- **本地化 & 全球化**
  - 多语言和多货币支持
  - 自动汇率
  - 多时区感知
  - 自定义日期、数字和货币格式
- **安全**
  - 双因素认证 (2FA)
  - 登录速率限制
  - 应用锁（PIN 码 / WebAuthn）
- **数据导入/导出**
  - 支持 CSV、OFX、QFX、QIF、IIF、Camt.053、MT940、GnuCash、Firefly III、Beancount 等

## 用法

### 使用 Docker 运行

访问 [Docker Hub](https://hub.docker.com/r/mayswind/ezbookkeeping) 查看所有镜像和标签。

**最新发布版：**

```bash
docker run -p8080:8080 mayswind/ezbookkeeping
```

**最新每日构建：**

```bash
docker run -p8080:8080 mayswind/ezbookkeeping:latest-snapshot
```

### 从二进制安装

从 [GitHub Releases](https://github.com/mayswind/ezbookkeeping/releases) 下载最新发布版。

**Linux / macOS**

```bash
./ezbookkeeping server run
```

**Windows**

```bash
.\ezbookkeeping.exe server run
```

默认情况下，ezBookkeeping 监听端口 8080。然后您可以访问 `http://{YOUR_HOST_ADDRESS}:8080/`。

### 从源码构建

确保安装了 [Golang](https://golang.org/)、[GCC](https://gcc.gnu.org/)、[Node.js](https://nodejs.org/) 和 [NPM](https://www.npmjs.com/)。然后下载源码，按照以下步骤操作：

**Linux / macOS**

```bash
./build.sh package -o ezbookkeeping.tar.gz
```

所有文件将打包在 `ezbookkeeping.tar.gz` 中。

**Windows**

```bash
.\build.bat package -o ezbookkeeping.zip
```

或

```powershell
.\build.ps1 package -Output ezbookkeeping.zip
```

所有文件将打包在 `ezbookkeeping.zip` 中。

您也可以构建 Docker 镜像。确保安装了 [Docker](https://www.docker.com/)，然后按照以下步骤操作：

**Linux**

```bash
./build.sh docker
```
