---
title: aliyundrive-fuse
---

# AliyunDrive FUSE 项目

## 项目地址
[GitHub 项目地址](https://github.com/messense/aliyundrive-fuse)

## 主要特性
- **FUSE 文件系统挂载**：将阿里云盘作为本地文件系统挂载，支持 Linux 和 macOS 系统，无需浏览器直接访问云盘文件。
- **支持多种协议**：基于阿里云盘 WebDAV API 和官方 API 实现，提供高效的文件访问和同步。
- **加密支持**：可选的端到端加密功能，确保数据隐私。
- **跨平台兼容**：主要支持 Linux 和 macOS，也可通过 Docker 在其他平台运行。
- **轻量级**：无依赖复杂图形界面，命令行操作简单高效。

## 主要功能
- **文件浏览与访问**：挂载后像本地目录一样浏览、读取、写入阿里云盘文件。
- **上传与下载**：支持直接上传本地文件到云盘，或下载云盘文件到本地，无需手动操作 Web 界面。
- **目录管理**：创建、删除、重命名文件夹和文件，支持权限控制。
- **缓存机制**：可选的本地缓存，提高访问速度，减少网络请求。
- **分享与协作**：集成阿里云盘的分享功能，便于文件协作。

## 用法
1. **安装依赖**：
   - 在 Linux/macOS 上安装 FUSE 库（例如，`sudo apt install fuse` 或 `brew install macfuse`）。
   - 通过 pip 安装 Python 包：`pip install aliyundrive-fuse`。

2. **配置阿里云盘账号**：
   - 运行 `aliyundrive-fuse config` 命令，输入阿里云盘账号和密码进行授权（会生成 refresh token）。

3. **挂载文件系统**：
   - 基本命令：`aliyundrive-fuse /path/to/mount/point`。
   - 示例：`aliyundrive-fuse ~/aliyun`（将阿里云盘挂载到 `~/aliyun` 目录）。
   - 选项：使用 `--refresh-token=your_token` 指定 token，或添加 `--cache-size=1024` 设置缓存大小。

4. **卸载**：
   - 使用 `fusermount -u /path/to/mount/point`（Linux）或 `umount /path/to/mount/point`（macOS）卸载。

5. **高级用法**：
   - Docker 运行：`docker run -it --device /dev/fuse -v /path/to/mount:/mnt messense/aliyundrive-fuse /mnt`。
   - 查看帮助：`aliyundrive-fuse --help` 获取更多参数。

更多细节请参考 GitHub 仓库的 README 文件。