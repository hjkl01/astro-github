---
title: AdGuardHome
---

## 功能介绍

AdGuard Home 是一个免费开源的网络范围广告和跟踪器拦截DNS服务器。它可以覆盖所有家庭设备，无需安装客户端软件。通过将跟踪域名重定向到“黑洞”，防止设备连接到这些服务器。基于AdGuard DNS服务器的技术，提供强大的隐私保护。

主要功能包括：

- 网络范围广告和跟踪器拦截
- 自定义过滤规则
- 内置DHCP服务器
- 支持加密DNS上游服务器（DNS-over-HTTPS、DNS-over-TLS、DNSCrypt）
- 跨平台支持
- 运行作为DNS-over-HTTPS或DNS-over-TLS服务器
- 拦截钓鱼和恶意软件域名
- 家长控制（拦截成人域名）
- 强制搜索引擎安全搜索
- 按客户端（设备）配置
- 访问设置控制谁可以使用AGH DNS
- 无需root权限运行

## 用法

### 安装

#### 自动化安装（Linux/Unix/MacOS/FreeBSD/OpenBSD）

使用curl：

```bash
curl -s -S -L https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/scripts/install.sh | sh -s -- -v
```

使用wget：

```bash
wget --no-verbose -O - https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/scripts/install.sh | sh -s -- -v
```

使用fetch：

```bash
fetch -o - https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/scripts/install.sh | sh -s -- -v
```

选项：

- `-c <channel>` 指定频道
- `-r` 重新安装
- `-u` 卸载
- `-v` 详细输出

#### Docker

使用官方Docker镜像：[Docker Hub](https://hub.docker.com/r/adguard/adguardhome)

#### Snap Store

在Linux上从[Snap Store](https://snapcraft.io/adguard-home)安装。

### 配置

安装后，访问Web界面进行配置。设置上游DNS服务器、过滤规则等。详细指南请参考[Wiki](https://github.com/AdguardTeam/AdGuardHome/wiki)。

### API

支持REST API，可用于集成。也可使用[Python客户端](https://pypi.org/project/adguardhome/)。
