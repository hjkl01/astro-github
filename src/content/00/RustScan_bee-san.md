# RustScan

## 项目简介

RustScan 是一个现代化的端口扫描器，由 bee-san 开发。它旨在提供快速、智能且有效的端口扫描功能。RustScan 使用 Rust 语言编写，强调速度和可扩展性。

## 主要功能

- **高速扫描**：能够在 3 秒内扫描所有 65,535 个端口。
- **脚本引擎支持**：支持 Python、Lua 和 Shell 脚本，允许用户自定义扫描后的操作，如自动将结果管道到 Nmap。
- **自适应学习**：通过使用模式学习和优化扫描参数，提高扫描效率。
- **网络支持**：支持 IPv6、CIDR 范围、文件输入等。
- **自动集成**：可以自动将开放端口管道到 Nmap 进行进一步分析。
- **可访问性**：致力于提供无障碍的用户体验。

## 安装方法

RustScan 支持多种安装方式，推荐使用包管理器以确保兼容性：

- **macOS**：`brew install rustscan`
- **Arch Linux**：`yay rustscan`
- **Cargo**：如果已安装 Rust，运行 `cargo install rustscan`
- **其他系统**：从 [GitHub Releases](https://github.com/RustScan/RustScan/releases) 下载二进制文件，或使用 Docker。

更多安装详情请参考 [Installation Guide](https://github.com/RustScan/RustScan/wiki/Installation-Guide)。

## 基本用法

RustScan 的基本命令格式为：

```
rustscan [OPTIONS] <TARGET>
```

### 示例

- 扫描单个 IP：`rustscan -a 192.168.1.1`
- 扫描 CIDR 范围：`rustscan -a 192.168.1.0/24`
- 指定端口范围：`rustscan -a 192.168.1.1 -p 1-1000`
- 管道到 Nmap：`rustscan -a 192.168.1.1 | nmap -A -p -`

### 常用选项

- `-a, --addresses <ADDRESSES>`：指定目标地址
- `-p, --ports <PORTS>`：指定端口范围（默认 1-65535）
- `-t, --timeout <TIMEOUT>`：设置超时时间（毫秒）
- `-b, --batch-size <BATCH_SIZE>`：设置批处理大小
- `--scripts <SCRIPTS>`：运行自定义脚本
- `-o, --output <OUTPUT>`：指定输出文件

更多用法请参考 [Usage Guide](https://github.com/RustScan/RustScan/wiki/Usage) 和 [Things you may want to do](https://github.com/RustScan/RustScan/wiki/Things-you-may-want-to-do-with-RustScan-but-don't-understand-how)。

## 配置

RustScan 支持配置文件 `config.toml`，用于自定义默认设置。配置文件通常位于 `~/.rustscan/config.toml`。

示例配置：

```toml
[default]
timeout = 1000
batch_size = 4500
```

更多配置详情请参考 [Config File Documentation](https://github.com/RustScan/RustScan/wiki/Config-File)。

## 社区与贡献

RustScan 是一个开源项目，欢迎社区贡献。项目托管在 GitHub 上，有活跃的 Discord 社区。

- **GitHub**：https://github.com/bee-san/RustScan
- **Discord**：http://discord.skerritt.blog
- **贡献指南**：https://github.com/RustScan/RustScan/wiki/Contributing

## 许可证

RustScan 使用 GPL-3.0 许可证。
