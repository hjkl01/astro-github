
---
title: rerun
---

# Rerun  –  实时可视化与调试框架

**项目地址**  
https://github.com/rerun-io/rerun

---

## 📌 项目简介
Rerun 是一个跨语言、跨平台的实时可视化与调试框架，旨在帮助开发者快速可视化任何时间序列数据、三维对象、变换、日志等。通过轻量级的 `rerun` 日志协议，可将数据实时投送到可视化客户端，极大提升调试与数据分析效率。

---

## ✨ 主要特性

| # | 特性 | 说明 |
|---|------|------|
| 1 | **多语言支持** | Rust、Python、C++、Java 等均可使用官方 SDK |
| 2 | **实时可视化** | 支持摄像机、轨迹、图像、点云、网格、坐标变换、Bounding Box 等多种数据类型 |
| 3 | **高性能** | 零拷贝数据传输、低延迟、可扩展的多线程日志写入 |
| 4 | **可扩展插件** | 与 `rerun-sdk` 合作开发自定义组件，支持自定义 UI、渲染器 |
| 5 | **跨设备同步** | 通过 TCP/UDP 或日志文件实现多机器同步可视化 |
| 6 | **版本化日志** | 数据打包为 `.rerun` 文件，可多版本回溯、版本控制 |
| 7 | **易用 CLI** | `rerun` 命令行启动 UI，支持热更新、调试信息输出 |

---

## 📦 安装与依赖

### Rust
```bash
cargo add rerun  # 记录接口
cargo add rerun-cli  # CLI 入口
```

### Python
```bash
pip install rerun-sdk
```

> 查看完整安装指南请参阅官方[安装文档](https://github.com/rerun-io/rerun/blob/main/docs/install.md)。

---

## 🚀 用法示例

### Rust 示例

```rust
use rerun::{RecordingStream, Point3d, ColorRGBA};

fn main() -> anyhow::Result<()> {
    // 连接到 本地 Rerun 服务器
    let mut stream = RecordingStream::new("127.0.0.1:8888")?;

    // 发送点云
    let points: Vec<Point3d> = (0..1000)
        .map(|i| Point3d::new(i as f32, (i/10) as f32, (i%5) as f32))
        .collect();
    stream.log_points("points", &points)?;

    // 发送颜色信息
    stream.log_colors("colors", &vec![ColorRGBA::random(); 1000])?;

    stream.finish()
}
```

### Python 示例

```python
import rerun as rr
import numpy as np

rr.init("demo", spawn=True)  # 启动 Rerun 服务器

points = np.random.rand(1000, 3).astype(np.float32)
rr.log("points", rr.Points3D(points))

# 可持续更新
for _ in range(10):
    points += np.random.randn(1000, 3) * 0.01
    rr.log("points", rr.Points3D(points))
```

### 查看可视化

```bash
$ rerun
```

打开浏览器访问 `http://localhost:8080` 即可实时查看。

---

## 📚 文档与教程

- 官方文档: https://github.com/rerun-io/rerun/blob/main/docs/intro.md  
- API 参考: https://github.com/rerun-io/rerun/blob/main/docs/api_reference.md  
- 如何做可扩展插件: https://github.com/rerun-io/rerun/blob/main/docs/extensions.md  
- 贡献指南: https://github.com/rerun-io/rerun/blob/main/CONTRIBUTING.md

---

## 🤝 参与贡献

- Fork → Issue / PR  
- 欢迎提交 bug 报告、功能建议  
- 文档完善、示例代码、插件开发

---