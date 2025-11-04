
---
title: cube
---


# cube

> 项目地址: https://github.com/cube-js/cube

## 简介
cube 是一个轻量级的 JavaScript 库，专注于在浏览器中创建、渲染和交互 3D 立方体。它基于 WebGL，提供简洁易用的 API，支持自定义材质、纹理、光照以及动画控制。

## 主要特性
- **WebGL 渲染**：直接使用 WebGL，性能优越，兼容性好。  
- **易用 API**：链式调用方式，快速创建、定位、旋转、缩放立方体。  
- **材质与纹理**：支持颜色、纹理贴图、法线贴图等多种材质。  
- **光照模型**：点光源、方向光、环境光等多种光照模式。  
- **动画控制**：时间轴驱动，支持关键帧动画、循环动画。  
- **交互支持**：鼠标拖拽、缩放、键盘事件等交互控制。  
- **模块化**：ES6 模块导出，兼容 Rollup、Webpack 等构建工具。

## 安装
```bash
npm install @cube-js/cube
```

## 快速示例
```js
import { Cube, Scene, Renderer, OrbitControls } from '@cube-js/cube';

const scene = new Scene();
const renderer = new Renderer({ canvas: document.getElementById('canvas') });

const cube = new Cube({
  size: 1,
  material: { color: 0x00ff00 },
});
scene.add(cube);

new OrbitControls(scene.camera, renderer.domElement);

renderer.render(scene, scene.camera);
```

## 使用方法
1. **创建场景**：`const scene = new Scene();`  
2. **添加相机**：`scene.addCamera(camera);`  
3. **创建立方体**：`const cube = new Cube(options);`  
4. **添加光源**：`scene.addLight(new DirectionalLight(...));`  
5. **渲染循环**：`renderer.setAnimationLoop(() => renderer.render(scene, scene.camera));`

## 文档
- [API Reference](https://github.com/cube-js/cube/wiki/API-Reference)  
- [Examples](https://github.com/cube-js/cube/tree/main/examples)

## 贡献
欢迎提交 Issues 与 PR。请遵守 [CONTRIBUTING.md](CONTRIBUTING.md)。