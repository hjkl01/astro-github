---
title: Colima
---

# Colima

Colima 是一个在 macOS（和 Linux）上提供容器运行时的工具，具有最小设置。它支持 Intel 和 Apple Silicon macOS，以及 Linux 系统。

## 功能

- **简单 CLI 接口**：具有合理的默认设置。
- **自动端口转发**：无需手动配置端口映射。
- **卷挂载**：支持挂载本地目录到容器中。
- **多实例**：可以运行多个 Colima 实例。
- **多种容器运行时支持**：
  - Docker（可选 Kubernetes）
  - Containerd（可选 Kubernetes）
  - Incus（容器和虚拟机）

## 用法

### 安装

Colima 可通过 Homebrew、MacPorts 和 Nix 安装。更多安装选项请查看 [INSTALL.md](https://github.com/abiosoft/colima/blob/main/docs/INSTALL.md)。

```bash
# Homebrew
brew install colima

# MacPorts
sudo port install colima

# Nix
nix-env -iA nixpkgs.colima
```

### 启动

使用默认设置启动 Colima：

```bash
colima start
```

### 自定义配置

可以通过命令行参数或配置文件自定义 VM：

```bash
# 使用编辑器编辑配置文件
colima start --edit

# 指定 CPU、内存和磁盘大小
colima start --cpu 4 --memory 8 --disk 100
```

### 运行时

- **Docker**：默认运行时。启动后可直接使用 `docker` 命令。
- **Containerd**：使用 `colima start --runtime containerd` 启动，然后使用 `colima nerdctl` 与 Containerd 交互。
- **Incus**：使用 `colima start --runtime incus` 启动，支持容器和虚拟机（仅限 Apple Silicon M3 或更新设备）。

### Kubernetes

启用 Kubernetes 支持：

```bash
colima start --kubernetes
```

需要安装 `kubectl`（`brew install kubectl`）。

### 模板

使用模板自定义配置：

```bash
colima template
```

这会在编辑器中打开默认模板文件，保存后会覆盖默认配置。

## 注意事项

- 从 v0.5.6 或更低版本升级时，需要删除现有实例：`colima delete` 然后 `colima start`。
- 磁盘大小在 VM 创建后无法减少，但从 v0.5.3 开始可以增加。
- Rosetta 2 仿真需要 v0.5.3 和 macOS 13（Ventura）或更高版本的 Apple Silicon。
