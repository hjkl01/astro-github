
---
title: three.js
---


# Three.js（mrdoob/three.js）

项目地址：<https://github.com/mrdoob/three.js>

## 简介
Three.js 是一个轻量级、跨平台的 JavaScript 库，用于在 WebGL 上创建和渲染 3D 图形。它提供了高级抽象层，简化了 3D 渲染、几何体、材质、光照、动画等复杂工作，支持多种渲染后端（WebGL、Canvas、SVG）和多平台（Web、Node.js、React Native 等）。

## 主要特性
- **跨平台渲染**：支持 WebGL、Canvas、SVG 渲染器。
- **高级几何体**：内置多种预定义几何体（立方体、球体、圆柱体、平面等）和自定义几何体支持。
- **多种材质**：MeshBasicMaterial、MeshLambertMaterial、MeshPhongMaterial、MeshStandardMaterial、MeshPhysicalMaterial、ShaderMaterial 等。
- **光照与阴影**：点光源、聚光灯、平行光、环境光，支持阴影映射。
- **相机与视图**：PerspectiveCamera、OrthographicCamera、CameraControls、OrbitControls、FirstPersonControls、FlyControls 等。
- **动画系统**：KeyframeTrack、AnimationClip、AnimationMixer、骨骼动画（SkinnedMesh）等。
- **物理与碰撞**：集成物理引擎（Ammo.js、Cannon.js 等）或自定义碰撞检测。
- **加载器**：GLTFLoader、OBJLoader、FBXLoader、TextureLoader、FontLoader 等。
- **后期处理**：EffectComposer、RenderPass、ShaderPass、UnrealBloomPass 等。
- **工具与插件**：Stats.js、OrbitControls、TrackballControls、VR/AR 支持、音频分析、GUI（dat.GUI）等。

## 主要模块与功能

| 模块 | 说明 |
|------|------|
| **Scene** | 场景容器，管理所有可渲染对象 |
| **Camera** | 相机系统，定义视点和投影方式 |
| **Renderer** | 渲染器，负责将场景绘制到画布 |
| **Object3D / Mesh** | 3D 对象基类，支持层级结构、变换 |
| **Geometry** | 几何体数据，支持 BufferGeometry、Geometry |
| **Material** | 材质系统，支持多种渲染模型 |
| **Light** | 光源，控制场景照明 |
| **Texture** | 纹理加载与管理 |
| **Loader** | 资源加载器，支持多种格式 |
| **Controls** | 交互控制器，提供视角和对象操作 |
| **Animation** | 动画系统，支持关键帧动画、骨骼动画 |
| **PostProcessing** | 后期处理管线，支持特效和滤镜 |
| **VR / AR** | 虚拟现实、增强现实模块 |
| **Stats** | 性能监控工具 |

## 基础用法

1. **引入 Three.js**

```html
<script src="https://cdn.jsdelivr.net/npm/three@latest/build/three.min.js"></script>
```

2. **创建场景、相机、渲染器**

```js
const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(
  75, window.innerWidth / window.innerHeight, 0.1, 1000
);
camera.position.z = 5;

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
```

3. **添加几何体与材质**

```js
const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshStandardMaterial({ color: 0x44aa88 });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);
```

4. **添加光源**

```js
const ambient = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambient);

const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
dirLight.position.set(3, 5, 2);
scene.add(dirLight);
```

5. **渲染循环**

```js
function animate() {
  requestAnimationFrame(animate);
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;
  renderer.render(scene, camera);
}
animate();
```

6. **窗口尺寸变化处理**

```js
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
```

## 进阶示例

- **加载 GLTF 模型**

```js
const loader = new THREE.GLTFLoader();
loader.load('model.glb', gltf => {
  scene.add(gltf.scene);
});
```

- **使用 OrbitControls**

```js
const controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
```

- **添加后期特效（Bloom）**

```js
const composer = new THREE.EffectComposer(renderer);
composer.addPass(new THREE.RenderPass(scene, camera));
composer.addPass(new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 1.5, 0.4, 0.85));
```

## 文档与社区

- 官方文档: <https://threejs.org/docs/>
- 示例库: <https://threejs.org/examples/>
- 开源社区: GitHub Issues、Discussions、Stack Overflow

## 小结
Three.js 通过封装 WebGL 的低级细节，提供了丰富的工具和模块，帮助开发者快速构建交互式 3D 内容、游戏、可视化项目以及 AR/VR 体验。其活跃的社区和持续更新的功能，使其成为 Web 3D 开发的首选框架。

