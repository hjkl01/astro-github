---
title: servo
---


# Servo — Rust 编写的浏览器引擎

[GitHub 项目地址](https://github.com/servo/servo)

## 主要特性
- **Rust 编写**：内存安全、无数据竞争、易于并行化。  
- **多进程 / 多线程**：渲染、JS 引擎、CSS 解析各自独立。  
- **GPU 加速**：支持 OpenGL、Vulkan、Metal；使用 `wgpu` 进行抽象。  
- **现代 Web 标准**：WebGL、WebGPU、WebAssembly、Canvas 等。  
- **模块化设计**：可按需启用/禁用子系统，适合实验与嵌入。

## 核心功能
1. **渲染引擎**：实现 CSS Flexbox/Grid、SVG、Canvas。  
2. **JavaScript 引擎**：内置 Hermes / Spidermonkey 兼容层。  
3. **DOM / Layout**：事件驱动、异步 DOM 更新、布局树。  
4. **安全沙箱**：利用 Rust 与 OS 安全机制进行资源隔离。  
5. **测试与 CI**：完整测试套件，默认使用 GitHub Actions。

## 用法

```bash
# 1. 克隆仓库
git clone https://github.com/servo/servo.git
cd servo

# 2. 安装 Cargo（Rust 1.70+ 以上）
rustup install stable
rustup default stable

# 3. 编译
cargo build -p servo

# 4. 运行
cargo run -p servo -- -headless           # 无 GUI
cargo run -p servo -- --port 8080          # 指定监听端口
```

### 常用命令示例
```bash
# 仅启动渲染器
cargo run -p servo -- -headless -port 5000

# 开发模式，自动重载
cargo run -p servo -- --watch
```

## 贡献
- Issues: https://github.com/servo/servo/issues  
- Pull requests: https://github.com/servo/servo/pulls  
- 贡献指南: https://github.com/servo/servo/blob/main/CONTRIBUTING.md

## 进一步阅读
- 官方文档: https://servo.org/docs/  
- 示例: https://github.com/servo/servo/tree/main/src/demo
