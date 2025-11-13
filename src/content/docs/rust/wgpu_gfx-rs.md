---
title: wgpu
---



---
title: wgpu
---

**项目地址**  
https://github.com/gfx-rs/wgpu

**主要特性与功能**  
| 领域 | 说明 |
|------|------|
| **跨平台 GPU 抽象** | `wgpu` 提供统一接口，支持 Windows (DX12/11, Vulkan), macOS/iOS (Metal), Linux (Vulkan, OpenGL), 以及 Web（WebGPU via `wasm32`）|
| **安全性** | 用 Rust 编写，全程借用检查，内存安全与并发无数据竞争，避免裸指针与显存泄漏|
| **WebGPU 规范实现** | `wgpu` 作为 W3C WebGPU 规范的参考实现，直接支持浏览器内嵌。|
| **现代渲染管线** | 支持顶点/几何/片段/光栅化、计算着色器、可变形光栅率、多样本抗锯齿、深度/模板缓冲|
| **资源管理** | 对纹理、缓冲、采样器、绑定组（BindGroups）等资源进行统一管理，支持异步加载与生命周期跟踪|
| **性能监控** | 能生成 GPU 调试、性能概况 (profiling) 报告，支持 `GPUStatistics` 接口|
| **异步渲染** | 采用异步 GPU 访问模型，配合 Rust `Future`，降低同步等待，提升多线程渲染效率|
| **集成工具** | 官方提供 `wgpu-app` 示例、`wgpu-async`、`wgpu-util` 等工具，促进快速原型开发|
| **FFI 与绑定** | 提供 C++、Python、其他语言绑定接口，便于不同生态融合|

**核心 API 典型使用流程**  
```rust
// 1. 创建实例并查询适配器
let instance = wgpu::Instance::new(wgpu::Backends::all());
let adapter = instance
    .request_adapter(&wgpu::RequestAdapterOptions {
        power_preference: wgpu::PowerPreference::HighPerformance,
        compatible_surface: Some(&surface),
        ..Default::default()
    })
    .await
    .expect("Failed to find an appropriate adapter");

// 2. 请求设备 + 渲染通道
let (device, queue) = adapter
    .request_device(
        &wgpu::DeviceDescriptor {
            label: Some("device"),
            features: wgpu::Features::empty(),
            limits: wgpu::Limits::default(),
        },
        None,
    )
    .await
    .expect("Failed to create device");

// 3. 创建缓冲区、纹理、采样器等
let vertex_buffer = device.create_buffer_init(&wgpu::util::BufferInitDescriptor {
    label: Some("Vertex Buffer"),
    contents: bytemuck::cast_slice(VERTICES),
    usage: wgpu::BufferUsages::VERTEX,
});

// 4. 组建渲染管线
let shader = device.create_shader_module(&wgpu::ShaderModuleDescriptor {
    label: Some("Shader"),
    source: wgpu::ShaderSource::Wgsl(include_str!("shader.wgsl").into()),
});

let pipeline_layout = device.create_pipeline_layout(&wgpu::PipelineLayoutDescriptor {
    label: Some("Pipeline Layout"),
    bind_group_layouts: &[],
    push_constant_ranges: &[],
});

let render_pipeline = device.create_render_pipeline(&wgpu::RenderPipelineDescriptor {
    label: Some("Render Pipeline"),
    layout: Some(&pipeline_layout),
    vertex: wgpu::VertexState {
        module: &shader,
        entry_point: "vs_main",
        buffers: &[wgpu::VertexBufferLayout {
            array_stride: std::mem::size_of::<Vertex>() as wgpu::BufferAddress,
            step_mode: wgpu::VertexStepMode::Vertex,
            attributes: &VERTEX_ATTR,
        }],
    },
    fragment: Some(wgpu::FragmentState {
        module: &shader,
        entry_point: "fs_main",
        targets: &[wgpu::ColorTargetState {
            format: surface_format,
            blend: Some(wgpu::BlendState::REPLACE),
            write_mask: wgpu::ColorWrites::ALL,
        }],
    }),
    primitive: wgpu::PrimitiveState::default(),
    depth_stencil: None,
    multisample: wgpu::MultisampleState::default(),
    multiview: None,
});

// 5. 描绘帧
let mut encoder = device.create_command_encoder(&wgpu::CommandEncoderDescriptor { label: Some("Render Encoder") });
{
    let mut rpass = encoder.begin_render_pass(&wgpu::RenderPassDescriptor {
        label: Some("Render Pass"),
        color_attachments: &[wgpu::RenderPassColorAttachment {
            view: &frame.texture_view,
            resolve_target: None,
            ops: wgpu::Operations {
                load: wgpu::LoadOp::Clear(wgpu::Color::BLACK),
                store: true,
            },
        }],
        depth_stencil_attachment: None,
    });
    rpass.set_pipeline(&render_pipeline);
    rpass.set_vertex_buffer(0, vertex_buffer.slice(..));
    rpass.draw(0..VERTICES.len() as u32, 0..1);
}
// 提交到队列
queue.submit(std::iter::once(encoder.finish()));
surface.present(&frame);
```

**使用场景**  
- 游戏引擎底层渲染；  
- 高性能可视化、科学计算；  
- 跨平台应用（桌面 + Web）里统一 GPU 接口；  
- 学术与原型快速实验。

**社区与贡献**  
wGPU 是一项开源项目，GitHub 上有大量 issue、PR。社区活跃，文档持续完善。想要参与请关注 `CONTRIBUTING.md`。