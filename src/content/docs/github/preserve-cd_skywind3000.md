
---
title: preserve-cd
---


# preserve-cd
项目地址: https://github.com/skywind3000/preserve-cd

## 主要特性
- **完整复制**：将光盘中的所有文件、目录结构以及文件属性（时间戳、权限等）完整保留到目标位置。  
- **多平台支持**：兼容 Linux、macOS 与 Windows（通过 Cygwin 或 WSL）。  
- **ISO 读取与写入**：支持从 ISO 镜像读取数据，也可将读取结果写回 ISO 或直接写入磁盘。  
- **命令行工具**：提供简单直观的命令行接口，适合脚本化使用。  

## 功能
| 功能 | 说明 |
|------|------|
| `preserve-cd copy <device|iso> <target>` | 复制光盘或 ISO 镜像到本地目录，保持原始文件属性。 |
| `preserve-cd mount <iso> <mountpoint>` | 挂载 ISO 镜像到指定挂载点。 |
| `preserve-cd unmount <mountpoint>` | 卸载已挂载的 ISO。 |
| `preserve-cd backup <device> <output.iso>` | 将光盘内容打包成 ISO 镜像。 |
| `preserve-cd -h` | 显示帮助信息。 |

## 用法示例
```bash
# 复制光盘内容到本地目录
preserve-cd copy /dev/cdrom ./my_cd

# 从 ISO 镜像复制内容
preserve-cd copy my_image.iso ./my_cd

# 挂载 ISO 镜像
preserve-cd mount my_image.iso /mnt/cdrom

# 卸载 ISO 镜像
preserve-cd unmount /mnt/cdrom

# 将光盘内容备份为 ISO
preserve-cd backup /dev/cdrom my_backup.iso
```

> 运行前请确保已安装必要的依赖（如 `dd`, `mkfs.iso9660` 等），并且拥有读写光盘的权限。