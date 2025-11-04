
---
title: Fyrox
---


# Fyrox Engine

**项目地址**  
[https://github.com/FyroxEngine/Fyrox](https://github.com/FyroxEngine/Fyrox)

## 主要特性

- **Rust 原生**：完全用 Rust 编写，零 C/C++ 依赖，内存安全、并发友好。  
- **跨平台**：支持 Windows、Linux、macOS；目标可构建 WebAssembly。  
- **现代渲染**：Vulkan 与 OpenGL 后端，支持 PBR、HDR、实时光照与阴影。  
- **物理**：集成 Rapier（2D/3D）、Bullet，提供刚体、碰撞、力场等常用功能。  
- **场景与节点系统**：树形节点、Transform、Camera、Light、Mesh、Particle、UI 等。  
- **资源管理**：异步加载，支持各种纹理、模型、材质、音频、动画等。  
- **内置编辑器**：拖拽式场景编辑、实时预览、资源浏览器、脚本 IDE。  
- **脚本与插件**：通过 `fyrox-script` 提供易用脚本接口（Rust、WASM、Lua）。  
- **多线程与任务调度**：高效利用 CPU，多线程渲染、物理、IO。  
- **可扩展**：插件系统、模块化设计，方便添加自定义组件、后期特效等。

## 典型用法

```bash
# 在 Cargo 项目中添加 Fyrox
cargo add fyrox
```

```rust
use fyrox::prelude::*;

fn main() -> Result<()> {
    // 创建引擎实例，指定帧率与窗口配置
    let mut engine = Engine::new(EngineConfig::default())?;

    // 加载场景或创建根节点
    let root = Node::new();
    engine.scenes.add(root.clone());

    // 添加相机、灯光、网格等组件
    root.add_child(NodeBuilder::new(Camera::new()));
    root.add_child(NodeBuilder::new(DirectionalLight::default()));
    root.add_child(NodeBuilder::new(Mesh::cube()));

    // 主循环
    loop {
        engine.update(&mut ..)?;
    }
}
```

> 详细 API 文档与示例请参阅：[Fyrox Docs](https://fyrox.rs/docs)

---

*保存路径：`src/content/docs/00/Fyrox_FyroxEngine.md`*
