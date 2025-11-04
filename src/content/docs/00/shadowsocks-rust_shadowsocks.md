
---
title: shadowsocks-rust
---


# Shadowsocks Rust

> GitHub 项目地址: [https://github.com/shadowsocks/shadowsocks-rust](https://github.com/shadowsocks/shadowsocks-rust)

## 项目概述
Shadowsocks Rust 是 Shadowsocks 项目的 Rust 语言实现，旨在提供高效、可靠且易于部署的代理服务器和客户端。由于 Rust 的安全性与性能优势，该实现不但在速度和资源占用方面有显著提升，还符合现代网络安全需求。

## 主要特性
- **高性能**：使用 Rust 编译为高效二进制文件，低 CPU 占用。
- **多协议支持**：支持 SNI、TCP、UDP 代理。
- **加密算法丰富**：包括 AEAD (AES-GCM, ChaCha20-Poly1305 等) 和 legacy 加密方式。
- **EOL 兼容**：与 Shadowsocks Core 的配置格式保持兼容。
- **可扩展插件体系**：支持插件化的企业版与软件包上传。
- **配置文件兼容**：原始 JSON 配置文件和服务器自定义脚本均可使用。
- **多平台**：支持 Linux、macOS、Windows、Android、iOS 等。

## 主要功能
- **服务器端**：创建可将流量转发到真实目标主机的代理服务器。
- **客户端**：透明代理系统，支持 SOCKS5、HTTP(S) 请求。
- **UDP 代理**：UDP封包通过 Socks5 的 UDP Map 转发。
- **加密实现**：实现多种 AES-256-GCM、ChaCha20-Poly1305 等安全加密算法。
- **动态 DNS 解析**：支持在配置中指定 DNS 选项，让 hostname 动态解析。
- **日志记录**：支持多级日志，输出到系统日志或自定义文件。
- **监控接口**：可通过 HTTP 接口输出当前连接数等基本统计信息。

## 使用方法

### 1. 安装依赖
```bash
# Rust 官方工具链
curl https://sh.rustup.rs -sSf | sh
```

### 2. 克隆代码
```bash
git clone https://github.com/shadowsocks/shadowsocks-rust.git
cd shadowsocks-rust
```

### 3. 编译
```bash
cargo build --release
```
编译后可在 `target/release/ss-server` 与 `target/release/ss-client`。

### 4. 配置文件
示例 `config.json`：
```json
{
  "server":"0.0.0.0",
  "server_port":8388,
  "password":"your_password",
  "timeout":300,
  "method":"aes-256-gcm"
}
```

### 5. 启动服务器
```bash
./target/release/ss-server -c config.json
```

### 6. 启动客户端（Socks5）
```json
{
  "server":"服务器IP",
  "server_port":8388,
  "password":"your_password",
  "timeout":300,
  "method":"aes-256-gcm",
  "local_address":"127.0.0.1",
  "local_port":1080,
  "plugin":""
}
```
```bash
./target/release/ss-local -c local-config.json
```
随后将系统或浏览器代理指向 `127.0.0.1:1080`。

### 7. 进阶：插件支持
复制 `shadowsocks-plugins` 到 `plugins/` 目录，按需添加插件。

---

*上述为快速上手指南，更多高级设置请参考项目仓库中的 README 与 `docs` 目录。*
