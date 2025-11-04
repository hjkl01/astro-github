
---
title: Drawflow
---

# Drawflow by jerosoler

> **GitHub 地址**: <https://github.com/jerosoler/Drawflow>

## 主要特性

- **可视化节点编辑**：支持拖拽、缩放、连线、节点编辑等操作，类似于流程图或编程节点编辑器。  
- **轻量级、纯前端实现**：使用 HTML5、CSS3、JavaScript（ES6）实现，无需后端支持。  
- **节点自定义**：用户可通过插件方式添加自定义节点类型，定义输入/输出端口、样式与行为。  
- **实时执行**：节点之间的连接可以在浏览器中即时执行，支持回调、事件广播与异步处理。  
- **导入/导出**：支持将图形结构序列化为 JSON，便于存储与加载。  
- **响应式布局**：自动适配不同尺寸屏幕，支持缩放与全屏切换。  
- **事件系统**：节点、连线、画布等对象均可绑定事件（`drag`, `drop`, `connect`, `disconnect`, `execute` 等）。  
- **跨域数据交互**：可与后端 REST API 或 WebSocket 进行交互，实时获取/推送数据。  

## 功能概览

| 功能 | 说明 |
|------|------|
| **创建节点** | 在画布上右键或使用工具栏按钮添加节点。 |
| **编辑节点** | 双击节点可打开属性面板，修改标签、颜色、脚本等。 |
| **连线** | 拖拽端口与端口之间形成连线，支持单向/双向连接。 |
| **删除** | 选中节点或连线后按 `Delete` 或右键删除。 |
| **执行** | 调用 `drawflow.execute()` 可按节点依赖关系执行所有节点。 |
| **导入/导出** | `drawflow.save()` 返回 JSON；`drawflow.load(JSON)` 加载图形。 |
| **自定义节点** | 通过 `drawflow.addNodeType(type, config)` 注册自己的节点类型。 |
| **事件监听** | `drawflow.on('nodeClick', callback)` 等事件可用于交互。 |

## 快速上手

1. **安装**

   ```bash
   # 通过 CDN 直接引用
   <script src="https://cdn.jsdelivr.net/npm/drawflow/dist/drawflow.min.js"></script>

   # 或使用 npm 安装
   npm install drawflow
   ```

2. **初始化画布**

   ```html
   <div id="drawflow" style="width:100%;height:100vh;"></div>
   <script>
     const drawflow = new Drawflow(document.getElementById('drawflow'));
     drawflow.start();   // 开始监听事件
   </script>
   ```

3. **添加节点**

   ```javascript
   const node = drawflow.addNode(
     {
       name: 'Hello World',
       html: '<div>节点内容</div>',
       inputs: 1,  // 输入端口数量
       outputs: 1  // 输出端口数量
     },
     1,  // 行号
     1   // 列号
   );
   ```

4. **连接节点**

   ```javascript
   drawflow.connect(
     node.id, 0,          // 源节点ID + 端口索引
     anotherNode.id, 0    // 目标节点ID + 端口索引
   );
   ```

5. **执行流程**

   ```javascript
   drawflow.execute();   // 按依赖关系执行所有节点
   ```

6. **导入/导出 JSON**

   ```javascript
   // 导出
   const data = drawflow.save();   // 返回 JSON 对象

   // 导入
   drawflow.load(data);
   ```

7. **自定义节点示例**

   ```javascript
   const MyNode = {
     template: `<div class="my-node">自定义节点</div>`,
     inputs: 1,
     outputs: 1,
     init: function(el, node) {
       // 事件绑定或初始化逻辑
     }
   };

   drawflow.registerNode('myNode', MyNode);
   ```

> 详细 API 与高级使用方法请参阅项目官方文档与示例代码。

---