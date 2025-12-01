---
title: crossdesk
---

## 功能介绍

CrossDesk 是一款轻量级的跨平台远程桌面软件，支持通过 Web 客户端进行远程设备控制。它基于 MiniRTC 实时音视频传输库构建，具备网络透传、视频软硬编解码、音频编解码、信令交互、网络拥塞控制和传输加密等核心能力。

主要功能包括：

- **跨平台支持**：兼容 Windows、macOS 和 Linux 系统
- **Web 客户端访问**：通过浏览器即可远程控制设备，无需安装额外软件
- **实时音视频传输**：支持高质量的桌面画面和音频传输
- **硬件编解码**：可选 CUDA 硬件加速，提升性能
- **安全连接**：支持密码保护和加密传输
- **自托管服务器**：支持私有部署，保护数据隐私

## 使用方法

### PC 客户端使用

1. **下载安装**：从 [CrossDesk 官方网站](https://www.crossdesk.cn) 下载对应平台的客户端
2. **启动程序**：运行 CrossDesk 客户端
3. **发起连接**：
   - 在菜单栏"对端ID"处输入远程设备的 ID
   - 如果设置了密码，需要输入正确的连接密码
   - 点击"→"按钮发起远程连接
4. **自定义设置**：
   - 在设置中可配置语言、视频编码格式等选项
   - 支持自托管服务器配置

### Web 客户端使用

1. **浏览器访问**：打开浏览器访问 [CrossDesk Web Client](https://web.crossdesk.cn/)
2. **输入信息**：
   - 输入远程设备 ID
   - 输入连接密码（如果设置了）
3. **开始控制**：点击连接即可远程控制设备

### 自托管服务器部署

如果需要私有部署，可以使用 Docker 进行服务器部署：

```bash
sudo docker run -d \
  --name crossdesk_server \
  --network host \
  -e EXTERNAL_IP=你的公网IP \
  -e INTERNAL_IP=你的内网IP \
  -e CROSSDESK_SERVER_PORT=服务器端口 \
  -e COTURN_PORT=中继服务端口 \
  -e MIN_PORT=端口范围最小值 \
  -e MAX_PORT=端口范围最大值 \
  -v /path/to/certs:/crossdesk-server/certs \
  -v /path/to/db:/crossdesk-server/db \
  -v /path/to/logs:/crossdesk-server/logs \
  crossdesk/crossdesk-server:v1.1.1
```

注意：需要提前准备证书文件，并开放相应端口。

### 证书配置

客户端需要加载根证书，服务端需要服务器私钥和证书。可以从项目提供的脚本生成自签名证书。

## 系统要求

- **Windows**：Windows 10 及以上（64 位）
- **macOS**：Intel 15.0 及以上，Apple Silicon 14.0 及以上
- **Linux**：Ubuntu 22.04 及以上

## 编译说明

项目使用 xmake 构建，需要安装 xmake 和 cmake。

```bash
git clone https://github.com/kunkundi/crossdesk.git
cd crossdesk
git submodule init
git submodule update
xmake b -vy crossdesk
```

可选编译参数：

- `--USE_CUDA=true`：启用 CUDA 硬件编解码
- `--CROSSDESK_VERSION=版本号`：指定版本
