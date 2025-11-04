
---
title: screenshot-to-code
---


# screenshot-to-code

> **项目地址**  
> https://github.com/abi/screenshot-to-code

## 简介
`screenshot-to-code` 是一个将 PNG/JPEG/WEBP 等截图文件转换为可复现 UI 代码（React、Vue、HTML/CSS）的命令行工具。它通过图像识别、布局分析、组件抽象等技术，自动生成结构化的代码文件，从而大幅降低 UI 原型到代码实现的手工工作量。

## 主要特性

| 特性 | 说明 |
|------|------|
| **多语言支持** | 生成 React、Vue、纯 HTML/CSS 三种代码模板，用户可根据需求选择。 |
| **自动布局解析** | 通过图像分割识别元素边界、对齐方式、层级关系，生成对应的 Flexbox/Grid 布局。 |
| **组件抽象** | 支持将重复出现的 UI 片段抽象为可复用组件，减少代码冗余。 |
| **自定义模板** | 允许用户通过插件或配置文件自定义生成的代码结构、命名规则、样式写法。 |
| **命令行交互** | 通过 `screenshot-to-code` CLI 进行文件输入、输出路径、目标框架选择等操作。 |
| **配置文件** | 支持 `.stc.json` 或 `.stc.yaml` 配置文件，集中管理项目设置。 |
| **高效性能** | 内置多线程处理，支持批量转换，转换速度快。 |
| **可视化调试** | 在转换过程中生成中间结果图，帮助排查识别错误。 |

## 安装方式

```bash
# 全局安装（推荐）
npm install -g screenshot-to-code

# 或者使用 npx 直接运行
npx screenshot-to-code --help
```

### 依赖

- Node.js ≥ 14.x
- Python 3.x（部分图像识别模块使用 Python 绑定）

## 基本用法

```bash
# 单张截图转换为 React 代码
screenshot-to-code input.png --framework react --output ./out/react

# 批量转换多张截图
screenshot-to-code ./screenshots/*.png --framework vue --output ./out/vue

# 使用自定义配置文件
screenshot-to-code --config .stc.yaml
```

### 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-i, --input` | 输入文件或文件夹路径 | 必填 |
| `-o, --output` | 输出目录 | `./out` |
| `-f, --framework` | 目标框架（react, vue, html） | `react` |
| `-c, --config` | 自定义配置文件路径 | `None` |
| `-v, --verbose` | 详细日志 | `false` |
| `-h, --help` | 显示帮助信息 | `false` |

## 配置文件示例 (`.stc.yaml`)

```yaml
framework: vue
output: ./generated
components:
  - name: Button
    selector: button
    style: scoped
globalStyles:
  color: "#333"
  fontFamily: "Arial, sans-serif"
```

## 典型工作流程

1. **准备截图**  
   - 以 PNG、JPEG 或 WebP 格式保存 UI 原型或设计稿截图。  
   - 若为多页面，可将每个页面保存为单独文件。

2. **运行转换命令**  
   ```bash
   screenshot-to-code ./screenshots/*.png --framework react --output ./src/components
   ```

3. **检查生成代码**  
   - 生成的文件夹中会包含 `.tsx/.jsx/.vue` 文件以及对应的 `.css` 或 `.scss`。  
   - 可根据需要手动调整组件命名或样式细节。

4. **集成到项目**  
   - 将生成的组件复制到项目结构中。  
   - 通过 `import` 或 `require` 引入并使用。

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| **识别错误导致布局错位** | 调整截图分辨率或使用 `--verbose` 查看调试图。 |
| **生成的组件命名不符合规范** | 在配置文件中修改 `components` 名称或添加 `namePattern`。 |
| **缺少依赖导致报错** | 先执行 `npm install` 或 `pip install -r requirements.txt`。 |

## 贡献

欢迎提交 Issue 或 Pull Request，具体贡献指南请查看项目根目录的 `CONTRIBUTING.md`。

---

> *此文档摘自 [screenshot-to-code](https://github.com/abi/screenshot-to-code) 项目仓库，供快速了解项目特性与使用方法。*
