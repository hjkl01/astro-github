
---
title: rustfs
---


# RustFS

**项目地址:** https://github.com/rustfs/rustfs

## 主要特性

- **纯 Rust 实现**：完整使用 Rust 语言书写，利用其内存安全和并发特性。  
- **跨平台**：支持 Linux、macOS、Windows，可在不同操作系统下编译运行。  
- **FUSE 文件系统**：提供 FUSE 接口，可将 RustFS 挂载为用户空间文件系统。  
- **模块化设计**：核心层面提供块存储、元数据管理、缓存等模块，可灵活组合使用。  
- **高性能**：采用异步 I/O、内存映射等技术，IO 并发性能优异。  
- **易用 API**：提供 `rustfs` crate外部程序可通过简单函数调用构建或操作文件系统。  
- **可扩展网络协议**：内置 HTTP/REST 与 gRPC 接口，方便与分布式实现对接。  

## 功能列表

| 功能 | 说明 |
|------|------|
| 文件与目录操作 | 创建、删除、重命名、移动、读取、写入、权限设置 |
| 元数据管理 | 支持 `stat`, `chmod`, `chown`, `utimens` 等系统调用 |
| 快照与版本控制 | 提供 snapshot API，支持文件的版本记录与回滚 |
| 复制与同步 | 通过网络接口实现文件的远程同步，支持增量复制 |
| 存储后端可插拔 | 支持多种后端（本地文件、内存、S3、Ceph 等），可在运行时切换 |

## 用法

### 环境准备

1. 安装 Rust 1.70+  
2. 安 FUSE 依赖  
   - macOS: `brew install osxfuse`  
   - Linux: `sudo apt-get install libfuse3-dev`  

### 编译

```bash
git clone https://github.com/rustfs/rustfs.git
cd rustfs
cargo build --release
```

### 运行示例

```bash
# 挂载到 /mnt/rustfs
sudo ./target/release/rustfs --mount /mnt/rustfs
```

> 运行后，你可以在 `/mnt/rustfs` 目录下执行普通文件系统操作。

#### 示例脚本

```bash
# 创建文件
echo "Hello rustfs" > /mnt/rustfs/hello.txt

# 查看文件内容
cat /mnt/rustfs/hello.txt

# 删除文件
rm /mnt/rustfs/hello.txt
```

### API 使用

先在 Cargo.toml 添加依赖：

```toml
[dependencies]
rustfs = { git = "https://github.com/rustfs/rustfs.git" }
```

然后示例代码：

```rust
use rustfs::{MountOptions, RustFs};

fn main() -> anyhow::Result<()> {
    let options = MountOptions::new("/mnt/myfs");
    let _fs = RustFs::mount(options)?;

    // 你可以在此使用文件系统 API
    Ok(())
}
```

## 建议与最佳实践

- **开启异步模式**：使用 `--enable-async`，可获得更高并发吞吐量。  
- **查看日志**：通过 `--log-level info` 查看运行时日志，方便排查。  
- **定期备份**：已挂载文件系统可进行 snapshot，保留前 N 份副本。  
- **自定义后端**：在配置文件中指定 `storage_backend = "s3"` 并填写凭证。  

## 参考文档

- 官方 README: https://github.com/rustfs/rustfs/blob/main/README.md  
- API 文档: https://docs.rs/rustfs  
- 贡献指南: https://github.com/rustfs/rustfs/blob/main/CONTRIBUTING.md  

---
