---
title: PlayCanvas Engine
---

# PlayCanvas Engine

PlayCanvas Engine 是一个开源游戏引擎，使用 HTML5 和 WebGL 在任何移动或桌面浏览器中运行游戏和其他交互式 3D 内容。它提供了强大的 Web 图形运行时，基于 WebGL、WebGPU、WebXR 和 glTF。

## 功能特性

PlayCanvas Engine 是一个功能完整的游戏引擎，主要特性包括：

- **图形**：先进的 2D + 3D 图形引擎，基于 WebGL2 和 WebGPU
- **动画**：强大的基于状态的动画系统，用于角色和任意场景属性
- **物理**：与 3D 刚体物理引擎 ammo.js 完全集成
- **输入**：鼠标、键盘、触摸、游戏手柄和 VR 控制器 API
- **声音**：基于 Web Audio API 的 3D 位置声音
- **资产**：基于 glTF 2.0、Draco 和 Basis 压缩的异步流系统
- **脚本**：使用 TypeScript 或 JavaScript 编写游戏行为

## 用法示例

以下是一个简单的 Hello World 示例，展示如何创建一个旋转的立方体：

```javascript
import * as pc from 'playcanvas';

const canvas = document.createElement('canvas');
document.body.appendChild(canvas);

const app = new pc.Application(canvas);

// 填充可用空间，全分辨率
app.setCanvasFillMode(pc.FILLMODE_FILL_WINDOW);
app.setCanvasResolution(pc.RESOLUTION_AUTO);

// 确保窗口大小改变时调整画布
window.addEventListener('resize', () => app.resizeCanvas());

// 创建立方体实体
const box = new pc.Entity('cube');
box.addComponent('model', {
  type: 'box',
});
app.root.addChild(box);

// 创建相机实体
const camera = new pc.Entity('camera');
camera.addComponent('camera', {
  clearColor: new pc.Color(0.1, 0.2, 0.3),
});
app.root.addChild(camera);
camera.setPosition(0, 0, 3);

// 创建方向光实体
const light = new pc.Entity('light');
light.addComponent('light');
app.root.addChild(light);
light.setEulerAngles(45, 0, 0);

// 根据上一帧的时间增量旋转立方体
app.on('update', (dt) => box.rotate(10 * dt, 20 * dt, 30 * dt));

app.start();
```

您可以在 [CodePen](https://codepen.io/playcanvas/pen/NPbxMj) 上编辑此代码。

有关设置基于 PlayCanvas Engine 的本地开发环境的完整指南，请参见[此处](https://developer.playcanvas.com/user-manual/engine/standalone/)。

## 构建方式

确保安装了 Node.js 18+。然后安装所有必需的 Node.js 依赖：

```
npm install
```

现在可以运行各种构建选项：

| 命令            | 描述                       | 输出到  |
| --------------- | -------------------------- | ------- |
| `npm run build` | 构建所有引擎版本和类型声明 | `build` |
| `npm run docs`  | 构建引擎 API 参考文档      | `docs`  |

## PlayCanvas 编辑器

除了引擎，我们还提供了 [PlayCanvas 编辑器](https://playcanvas.com/)，用于创建 HTML5 应用/游戏。

编辑器相关的错误和问题，请参考[编辑器仓库](https://github.com/playcanvas/editor)。
