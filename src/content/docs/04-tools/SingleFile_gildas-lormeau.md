
---
title: SingleFile
---


# SingleFile

**项目地址**: https://github.com/gildas-lormeau/SingleFile

## 概述
SingleFile 是一款浏览器扩展，能够将完整的网页（包括 HTML、CSS、JavaScript、图片、字体等资源）保存为单一的 HTML 文件。用户可以离线查看、分享或归档网页内容。

## 主要特性
- **完整保存**：自动抓取页面所有资源，生成可离线浏览的单文件 HTML。
- **资源内联**：将外部 CSS、JS、图片等内容直接嵌入文件，确保页面无依赖。
- **容错处理**：对跨域请求、损坏资源等情况做降级处理，保证文件可用。
- **可自定义**：支持自定义保存选项（如去除广告、保留/删除脚本、压缩图像等）。
- **批量保存**：可一次性处理多个页面，生成批量文件。
- **插件兼容**：支持与常见浏览器插件（如 AdBlock、NoScript）配合使用。

## 功能
| 功能 | 说明 |
|------|------|
| **单文件导出** | 将当前页面导出为单一 `.html` 文件。 |
| **高级导出** | 选择是否保留 JavaScript、CSS、图片等，或进行压缩。 |
| **批量导出** | 通过书签文件或 URL 列表批量生成保存文件。 |
| **命令行工具** | 提供 Node.js CLI，支持服务器端批量处理。 |
| **API 接口** | 可嵌入到自定义脚本或服务中，调用保存功能。 |
| **日志与报告** | 生成导出报告，记录资源抓取情况。 |

## 用法

### 1. 浏览器插件使用
1. 在 Chrome/Edge/Firefox 里安装 SingleFile 扩展。  
2. 打开想保存的网页，点击浏览器工具栏的 SingleFile 图标。  
3. 在弹出的对话框中选择导出选项后，点击 **Save**，即可下载单文件。

### 2. Node.js CLI
```bash
# 安装
npm install -g singlefile

# 单页导出
singlefile https://example.com --output example.html

# 批量导出
cat urls.txt | singlefile -i - -o output_dir/
```

### 3. API 调用
```javascript
const { SingleFile } = require('singlefile');
const sf = new SingleFile();

sf.save('https://example.com', { output: 'example.html' })
  .then(() => console.log('保存完成'))
  .catch(err => console.error(err));
```

### 4. 自定义配置
在浏览器扩展的设置页可以配置：
- 是否保留脚本
- 是否压缩图片
- 是否去除广告元素
- 自定义黑名单/白名单

## 参考链接
- 官方文档: https://github.com/gildas-lormeau/SingleFile  
- 示例项目: https://github.com/gildas-lormeau/SingleFile/tree/main/examples

--- 

保存路径: `src/content/docs/00/SingleFile_gildas-lormeau.md`
