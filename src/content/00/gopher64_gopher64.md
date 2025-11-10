# gopher64

## 功能

gopher64 是一个高度兼容的 Nintendo 64 (N64) 模拟器，使用 Rust 编写。它提供了以下主要功能：

- **高度兼容性**：支持广泛的 N64 游戏库，具有良好的兼容性。
- **Netplay 支持**：通过云托管服务器支持在线多人游戏，也可以在局域网中运行自己的服务器。
- **便携模式**：创建 `portable.txt` 文件以将所有游戏数据保存在可执行文件同一目录中。
- **跨平台支持**：提供 Windows 和 Linux 版本，包括 Flatpak 支持。
- **自定义控制**：支持键盘和游戏手柄映射，默认映射参考 Wiki 页面。

## 用法

### 下载和安装

- **Windows**：从 [GitHub Releases](https://github.com/gopher64/gopher64/releases/latest/download/gopher64-windows-x86_64.exe) 下载可执行文件。
- **Linux**：通过 Flatpak 从 [Flathub](https://flathub.org/apps/io.github.gopher64.gopher64) 安装。

### 运行游戏

1. 下载 N64 ROM 文件（.z64 格式）。
2. 运行 gopher64 可执行文件，并将 ROM 文件路径作为参数传入，例如：
   ```
   ./gopher64 /path/to/rom.z64
   ```
3. 对于 Flatpak 版本，需要添加 `--filesystem=host:ro` 选项：
   ```
   flatpak run --filesystem=host:ro io.github.gopher64.gopher64 /path/to/rom.z64
   ```

### 控制设置

- 键盘映射：参考 [默认键盘设置](https://github.com/gopher64/gopher64/wiki/Default-Keyboard-Setup)。
- 游戏手柄映射：参考 [默认游戏手柄设置](https://github.com/gopher64/gopher64/wiki/Default-Gamepad-Setup)。

### Netplay

- 加入在线会话或在局域网中运行服务器（参考 [gopher64-netplay-server](https://github.com/gopher64/gopher64-netplay-server)）。

### 构建

1. 安装 Rust：从 [rust-lang.org](https://www.rust-lang.org/tools/install) 下载。
2. Linux 用户：安装 SDL3 依赖（参考 [SDL3 Linux 构建依赖](https://wiki.libsdl.org/SDL3/README-linux#build-dependencies)）。
3. 克隆仓库：
   ```
   git clone --recursive https://github.com/gopher64/gopher64.git
   cd gopher64
   ```
4. 构建：
   ```
   cargo build --release
   ```
5. 运行：
   ```
   ./target/release/gopher64 /path/to/rom.z64
   ```

### 社区和支持

- **Wiki**：[GitHub Wiki](https://github.com/gopher64/gopher64/wiki)
- **Discord**：[Discord 服务器](https://discord.gg/9RGXq8W8JQ)
- **贡献**：欢迎通过 GitHub Issues 或 Discord 联系开发者（loganmc10）。

### 许可证

gopher64 基于 GPLv3 许可证发布。部分代码改编自 mupen64plus 和 ares。
