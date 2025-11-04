
---
title: snapdom
---


# Snapdom

**GitHub 项目地址:** https://github.com/zumerlab/snapdom

## 主要功能

- **DOM 快照**：捕捉页面或指定元素的完整 DOM 结构与样式信息，生成可序列化的快照。
- **快照比较**：对比两个快照，识别新增、删除、属性/样式变更等差异。
- **可视化差异**：将差异展示为高亮层，方便开发者快速定位变更。
- **交互式回放**：对快照链进行时间轴回放，查看页面变迁。
- **导出与复现**：将快照导出为 JSON 或 HTML，支持离线复现与回归测试。

## 核心 API

| 方法 | 参数 | 描述 |
|------|------|------|
| `Snapdom.take(element, options?)` | `HTMLElement` 或 `string` 选择器，`options` 可选 | 捕获元素当前 DOM 与样式快照，返回 Promise 解析到快照对象。 |
| `Snapdom.compare(oldSnapshot, newSnapshot)` | `Snapshot` 对象 | 对比两快照，返回差异对象（added、removed、modified 节点）。 |
| `Snapdom.renderDiff(diff, container)` | `Diff` 对象，容器元素 | 在指定容器渲染差异高亮层。 |
| `Snapdom.export(snapshot, format)` | `Snapshot`，`"json"` | 将快照导出为 JSON 字符串。 |
| `Snapdom.playback(sequence, container)` | 快照数组，容器元素 | 在容器中按时间轴回放快照序列。 |

## 安装与使用

```bash
# npm
npm install snapdom

# yarn
yarn add snapdom
```

```js
import Snapdom from 'snapdom';

// 1. 拍摄快照
const snapshot1 = await Snapdom.take('#app');

// 2. 页面进行更改后再次拍摄
const snapshot2 = await Snapdom.take('#app');

// 3. 比较两次快照
const diff = Snapdom.compare(snapshot1, snapshot2);

// 4. 在页面中渲染差异
Snapdom.renderDiff(diff, document.getElementById('diff-container'));

// 5. 导出快照
const json = Snapdom.export(snapshot2, 'json');
```

## 文档与示例

- 👉 详细 API 文档：[Docs](https://zumerlab.github.io/snapdom/)
- 👉 在线演示：[Demo](https://zumerlab.github.io/snapdom/demo)

> 该项目适用于前端开发中的 UI 测试、变更跟踪与性能调试。``` 

``` 

> **备注：** 如果需要参考项目源码，请访问上述 GitHub 地址。