---
title: vello
---


# Vello – 高性能 2D GPU 渲染引擎（linebender/vello）

**项目地址**: <https://github.com/linebender/vello>

## 主要特性
| Feature | 说明 |
|---------|------|
| **GPU 加速** | 基于 WebGPU、Vulkan、Metal、DX12 等后端，利用 GPU 进行路径、渐变、文本等多种渲染任务。 |
| **向量图形支持** | 完整的 Path、Stroke、Fill、渐变、纹理填充、图形变换与层叠。 |
| **无锁并行** | 不使用任何冲突锁，提供高并发、低延迟的渲染流水线。 |
| **平台无关** | 纯 Rust，支持 Windows、macOS、Linux、WebAssembly 等多平台。 |
| **可扩展性** | 提供 `RenderContext`、`SceneBuilder` 等 API，可与现有 UI / 游戏框架 (eg. winit, egui) 无缝集成。 |
| **生态友好** | 与 `wgpu` 集成，能够直接复用已有 GPU 资源与命令缓冲区。 |

## 核心 API
- `Renderer` – GPU 资源管理、命令提交。  
- `Scene`、`SceneBuilder` – 用于构造可重用的渲染图。  
- `RenderContext` – 抽象渲染上下文，负责绘制与同步。  
- `path::Path`、`style::Fill/Stroke` – 定义路径与样式。  

## 快速上手

### Cargo.toml
```toml
[dependencies]
vello = "0.41"          # 根据官方推荐的最新版本更新
wgpu = { version = "0.15", features = ["webgl"] }   # 视需要加入的后端
```

### 示例代码
```rust
use wgpu::util::DeviceExt;
use vello::{
    BasicRenderContext, Renderer, Scene, SceneBuilder, Style, Stroke, Fill,
    RenderTarget, RenderSource, Transform,
};

fn main() {
    // 1. 初始化 wgpu
    let instance = wgpu::Instance::default();
    let surface = /* 创建窗口表面 */;
    let adapter = futures::executor::block_on(
        instance.request_adapter(&wgpu::RequestAdapterOptions::default()),
    ).unwrap();
    let (device, queue) = futures::executor::block_on(
        adapter.request_device(&wgpu::DeviceDescriptor::default(), None),
    ).unwrap();

    // 2. 创建渲染器
    let mut renderer = Renderer::new(device, queue, surface).unwrap();

    // 3. 构造场景
    let mut builder = SceneBuilder::new();
    let path = vello::drawing::Path::new()
        .move_to((50.0, 50.0))
        .line_to((150.0, 50.0))
        .line_to((150.0, 150.0))
        .close();
    builder.stroke(
        path.clone(),
        Stroke::new().color(vello::penumbra::Pixel::rgba(0.5, 0.2, 0.8, 1.0)),
    );
    builder.fill(
        path,
        Fill::new().color(vello::penumbra::Pixel::rgba(0.2, 0.7, 0.3, 1.0)),
    );
    let scene = builder.build();

    // 4. 渲染循环
    let mut target = RenderTarget {
        width: 800,
        height: 600,
    };
    renderer
        .update_target(&mut target)
        .expect("更新目标失败");
    renderer
        .render(
            RenderSource::new(scene),
            target,
            &wgpu::ColorTargetState {
                format: wgpu::TextureFormat::Bgra8UnormSrgb,
                ops: wgpu::Operations {
                    load: wgpu::LoadOp::Clear(wgpu::Color::WHITE),
                    store: true,
                },
                ..Default::default()
            },
            &wgpu::PrimitiveState::default(),
        )
        .expect("渲染失败");
}
```

> ⚠️ 上述代码省略了窗口创建、事件循环等细节，主要展示 Vello 的核心编程流程。

## 文档与资源
- 官方 README 与 API 文档: <https://github.com/linebender/vello/blob/main/README.md>
- 示例代码与集成案例: <https://github.com/linebender/vello/tree/main/examples>
- 官方 Discord/讨论组 (用于绑定问答与技术交流)

--- 
如需更详细的使用示例或高级功能（如渐变、纹理、层混合、动画等），请参考上述官方资源与 API 文档。祝使用愉快！

💝 Support this free API: https://www.paypal.com/donate/?hosted_button_id=XS3CAYT8LE2BL