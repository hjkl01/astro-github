---
title: drawio-desktop
---


# drawio-desktop（jgraph/drawio-desktop）

- **项目地址**  
  <https://github.com/jgraph/drawio-desktop>

## 主要特性

| 特色 | 说明 |
|------|------|
| **离线桌面应用** | 无需浏览器即能使用 Draw.io，支持 Windows、macOS 与 Linux。 |
| **原生桌面集成** | 支持系统托盘、快捷键、文件拖拽打开/保存、事务日志等。 |
| **完整的 Draw.io 核心** | 图表、流程图、UML、网络拓扑等多种图形模板与自定义形状。 |
| **多种导出格式** | PNG、SVG、JPG、PDF、PNG+HTML、XMI、XML、.drawio等。 |
| **高级文本与样式** | 支持 Markdown、HTML、公式、样式表与自定义主题。 |
| **插件与脚本** | 通过 JavaScript 插件扩展功能，支持结构化或自动化绘图。 |
| **本地云与同步** | 与 Google Drive、OneDrive、Dropbox、GitHub 等进行文件同步。 |
| **资源管理** | 嵌入图片、图层管理、文件夹结构与快捷搜索。 |

## 核心功能

1. **图形绘制**  
   - 支持拖拽、复制粘贴、组合/对齐、连接线智能拐角等。  
   - 形状库可在线更新，支持任意自定义图标。  

2. **协同与版本控制**  
   - 与云端服务集成，实现多人协同编辑与自动保存。  
   - 内置版本历史，支持恢复与比较。  

3. **高级配置**  
   - 打印与导出时可设置页面尺寸、边距、分辨率。  
   - 支持 PDF 书签、书签锚点与批量导出。  

4. **脚本与自动化**  
   - 内置 JavaScript 控制台，编写脚本自动生成或修改图形。  
   - 支持 .JSON、.CSV 等格式的批量导入与导出。  

## 使用方法

### 1. 安装

- **Windows/macOS**  
  下载对应平台的 .exe / .dmg 并按提示安装。  
- **Linux**  
  下载安装包后执行 `sudo dpkg -i <package>.deb` (Debian/Ubuntu) 或相应命令。  

（或使用 npm/yarn 直接安装 `draw.io-desktop`：`npm i -g @drawio/desktop`）

### 2. 打开与创建

```bash
# 直接启动
draw.io-desktop
```

- 选择 **文件 → 新建** 创建空白图。  
- 或 **文件 → 打开** 载入本地或云端 `*.drawio` / `*.xml`。

### 3. 绘制与编辑

1. 选中左侧形状库 → 拖拽至画布。  
2. 使用连接线工具建立边。  
3. 双击形状文本即可编辑。  

### 4. 保存与导出

- **文件 → 保存**：本地`*.drawio`或云端。  
- **导出 → PNG / SVG / PDF**：设置分辨率、压缩率、隐藏网格等。  
- **高级导出**：`文件 → 另存为 -> 访问控制` 或 `导出为 → XMI`。

### 5. 协同与云端

- **文件 → 共享** → 选择 Google Drive / OneDrive / Dropbox。  
- 在对应服务中复制链接，其他人即可在线编辑。  

### 6. 自定义与插件

- 打开 **文件 → 模板 → 开发者模式**，激活 **脚本编辑器**。  
- 在 `scripts.js` 中编写 JavaScript：自动生成流程图或批量修改属性。  

---
> 以上内容可直接保存为 `src/content/docs/00/drawio-desktop_jgraph.md`，便于在项目内文档体系中引用。