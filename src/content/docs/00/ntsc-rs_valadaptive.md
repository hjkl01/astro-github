
---
title: ntsc-rs
---

**文件路径**  
`src/content/docs/00/ntsc-rs_valadaptive.md`

**文件内容**（Markdown）  
```markdown
# ntsc-rs

> https://github.com/valadaptive/ntsc-rs  

## 简述  
`ntsc-rs` 是一个用 Rust 实现的 NTSC 视频信号生成与解析库，提供 RGB 与 NTSC YIQ 成分的互相转换，并可在 Rust 环境中模拟 480i、NTSC 等模拟信号。  

## 主要特性  
- **RGB ↔ YIQ 转换**：支持标准 RGB 输入到 YIQ 分量的转换，反之亦然。  
- **信号模拟**：可根据 YIQ 生成对应的 I/Q 频率，适配模拟电视调制需求。  
- **高精度计数**：提供多种编码/解码路径，满足精度与速度的平衡。  
- **易用 API**：所有核心功能封装为简单函数，接口直观。  
- **Test 与 Benchmark**：自带完整的单元测试与基准测试，确保数值正确性与性能。  

## 如何使用  

### Cargo 依赖  
```toml
[dependencies]
ntsc-rs = "0.x"   # 具体版本请参考仓库 README
```

### 示例代码  
```rust
use ntsc_rs::Ntsc;

// 创建 NTSC 处理器
let ntsc = Ntsc::new();

// RGB 转 YIQ
let rgb = [0.25, 0.50, 0.75];   // 0.0 ~ 1.0 之间的值
let yiq = ntsc.rgb_to_iyq(rgb);
println!("YIQ: {:?}", yiq);

// YIQ 转回 RGB
let rgb_back = ntsc.iyq_to_rgb(yiq);
println!("RGB: {:?}", rgb_back);
```

### 进一步阅读  
- 详细 API 说明与高级用法请参照仓库 `docs/` 或官方 README。  
- 若需在嵌入式或多媒体项目中使用，查看 `examples/` 目录下的完整示例。  

> 以上是 `ntsc-rs` 项目的核心功能与最常见的使用方式。有关更多细节与贡献指南，请访问项目主页。  
``` 

--- 

> **提示**: 将上述内容粘贴到 `src/content/docs/00/ntsc-rs_valadaptive.md` 并提交即可。