
---
title: bevy
---

# Bevy - 一个现代化的 Rust 游戏引擎

> 项目地址: <https://github.com/bevyengine/bevy>

---

## 概述  
Bevy 是一款用 Rust 编写的高性能、数据驱动的游戏引擎。它通过**实体-组件-系统（ECS）**架构、模块化插件体系以及可热重载等特性，帮助开发者快速构建 2D/3D 游戏、实时可视化或任何交互式应用。

---

## 主要特性  

| 类别 | 说明 |
|------|------|
| **ECS** | 高效的数据驱动，支持并行更新、查询优化。 |
| **模块化插件** | 内置 2D/3D 渲染、输入、音频、物理、UI 等插件，用户可自行编写插件扩展。 |
| **实时渲染** | 使用 wgpu（WebGPU）实现跨平台 GPU 渲染，支持光照、阴影、材质、后处理。 |
| **热重载** | 在开发时自动重新加载代码、资源、着色器，缩短迭代周期。 |
| **跨平台** | 支持 Windows / macOS / Linux / iOS / Android / WebAssembly。 |
| **可组合** | 通过资源、系统、事件等构建可复用的功能块。 |
| **性能** | 零拷贝、分层缓存、无 GC，适合高帧率游戏。 |
| **社区生态** | 丰富的第三方插件、资产、教程。 |

---

## 主要功能  

1. **渲染**  
   - 2D Sprite、Tilemap、Canvas、Canvas 2D API。  
   - 3D Mesh、Material、PBR、阴影、光源、后处理。  
   - 着色器编写：wgsl、glsl。

2. **输入**  
   - 鼠标、键盘、手柄、触摸。  
   - 可自定义绑定、状态查询。

3. **物理**  
   - 与 rapier 3D/2D 集成（可选）。  
   - 刚体、碰撞体、约束、力场。

4. **音频**  
   - 2D/3D 音频播放、音量、循环、淡入淡出。  
   - 支持 Ogg、WAV、MP3、FLAC。

5. **UI**  
   - 布局、文本、交互组件。  
   - 支持 SVG、TTF、字体加载。

6. **资源管理**  
   - 资产热加载、引用计数、压缩。  
   - 自定义资源类型。

7. **事件系统**  
   - 发布/订阅模式，跨系统通信。  

8. **调试工具**  
   - ECS 视图、帧率统计、GPU 调试。  

---

## 快速上手  

### 1. 创建项目

```bash
cargo new my_bevy_app --lib
cd my_bevy_app
cargo add bevy
```

### 2. 编写 `src/main.rs`

```rust
use bevy::prelude::*;

fn main() {
    App::new()
        .add_plugins(DefaultPlugins)           // 加载默认插件
        .add_startup_system(setup)             // 启动系统
        .add_system(move_camera)               // 运行系统
        .run();
}

// 启动系统：添加相机
fn setup(mut commands: Commands) {
    commands.spawn(Camera3dBundle::default());
}

// 运行系统：每帧移动相机
fn move_camera(time: Res<Time>, mut query: Query<&mut Transform, With<Camera3d>>) {
    for mut transform in query.iter_mut() {
        transform.translation.x += 0.5 * time.delta_seconds();
    }
}
```

### 3. 运行

```bash
cargo run
```

> 你将看到一个空白窗口，摄像机沿 X 轴不断移动。

---

## 常用插件示例

```rust
use bevy::prelude::*;
use bevy::pbr::PbrPlugin;     // 物理基础渲染插件
use bevy_rapier3d::prelude::*; // Rapier 物理插件

fn main() {
    App::new()
        .add_plugins(DefaultPlugins)
        .add_plugin(PbrPlugin)                 // 开启 PBR 渲染
        .add_plugin(RapierPhysicsPlugin::<NoUserData>::default()) // 3D 物理
        .add_startup_system(setup)
        .run();
}
```

---

## 开发者资源  

- 文档: <https://docs.rs/bevy/latest/bevy/>  
- GitHub 示例: <https://github.com/bevyengine/bevy/tree/main/examples>  
- 社区: Discord、Reddit、Discord 频道 `#bevy`  

---

> 以上内容已保存为 `src/content/docs/00/bevy_bevyengine.md`，请根据项目需要使用。