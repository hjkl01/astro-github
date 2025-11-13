---
title: reinstall
---

# reinstall 项目

**项目地址：** [https://github.com/bin456789/reinstall](https://github.com/bin456789/reinstall)

## 主要特性

reinstall 是一键 VPS 系统重装脚本，支持 Linux 和 Windows 重装，采用分区表 ID 识别硬盘，确保安全。主要特性包括：

- **一键重装 Linux**：支持 19 种发行版，如 Debian、Ubuntu、Alpine 等。
- **一键重装 Windows**：使用官方 ISO，支持自动查找链接和安装驱动。
- **任意方向重装**：Linux 到 Linux/Windows，Windows 到 Linux/Windows。
- **智能 IP 配置**：自动设置静态/动态 IP，支持 IPv4/IPv6。
- **低内存优化**：适配低配机器，内存 256MB 起。
- **开源透明**：所有资源实时从镜像源获取，无自制包。

## 主要功能

- **安装 Linux**：选择发行版和版本，自动下载和安装。
- **安装 Windows**：指定 ISO 或自动查找，支持语言和版本。
- **DD 原始镜像**：支持 raw/vhd 镜像到硬盘。
- **引导到 Alpine Live OS**：内存系统，用于手动操作。
- **引导到 netboot.xyz**：用于手动安装其他系统。
- **高级选项**：SSH 密钥、端口、密码设置，frpc 内网穿透。

## 用法

脚本支持 Linux/Windows 下运行，使用 bash 或 batch 文件。

### 下载

国外：`curl -O https://raw.githubusercontent.com/bin456789/reinstall/main/reinstall.sh`
国内：`curl -O https://cnb.cool/bin456789/reinstall/-/git/raw/main/reinstall.sh`

### 安装 Linux

`bash reinstall.sh debian 12` 或 `ubuntu 24.04 --minimal`

### 安装 Windows

`bash reinstall.sh windows --image-name "Windows 11 Pro" --lang zh-cn`

### DD 镜像

`bash reinstall.sh dd --img "https://example.com/image.xz"`

### 其他功能

`bash reinstall.sh alpine --hold 1` 或 `netboot.xyz`

注意：重装会清除硬盘，使用前备份。更多选项见 README。
