
---
title: uBlock
---

# uBlock - Gorhill

项目地址: https://github.com/gorhill/uBlock  

## 主要特性  
- **强大广告拦截**：利用多种过滤列表阻止广告、追踪器、恶意内容。  
- **自定义规则面板**：直观界面可添加、编辑、禁用过滤规则。  
- **跨平台**：兼容 Chrome、Firefox、Edge 等主流浏览器。  
- **隐私保护**：阻止第三方追踪器，降低隐私泄露风险。  
- **模块化扩展**：支持插件化功能，例如 JSON/MySQL 库、下载器、媒体信息检索等。  
- **高性能**：低内存占用、快速执行，减少页面加载延迟。  
- **可视化统计**：实时查看拦截数量、来源和网络请求。  

## 功能概览

| 功能 | 说明 |
|------|------|
| 过滤列表 | 预置 `easylist`, `easyprivacy` 等官方列表 |
| 规则面板 | 可自定义或通过浏览器扩展管理规则 |
| 声明式 API | `uDom`/`uMsg` 与扩展交互 |
| 代理层 | 通过 proxy/redirect 处理请求 |
| 统计页 | 页面级拦截率及来源统计 |
| 主题化 | 支持多种 UI 主题 |
| 操作日志 | 记录拦截日志，排查问题 |
| 开发者工具 | 调试面板，编写自定义模块 |

## 如何使用

1. **安装**  
   - Chrome/Edge: 在 Chrome 网上应用店搜索 “uBlock Origin” 并安装。  
   - Firefox: 在附加组件商店搜索 “uBlock Origin”，或使用 `about:addons` 导入。  
   - 其它浏览器: 下载 `uBlock Origin.zip` 并手动导入。  

2. **基础配置**  
   - 打开扩展图标 → 选项 → 过滤器  
   - 默认加载 `easylist`, `easyprivacy` 等公用列表  
   - 如需更强过滤，可启用 `uBlock filter lists`  

3. **自定义拦截**  
   - 网页中右键识别广告 → “拦截广告”  
   - 或在“自定义过滤器”添加规则（如 `||example.com^`）  
   - 保存后立即生效  

4. **高级功能**  
   - 使用 `uDom` API 处理页面脚本  
   - 通过右键创建 “Local block rules”  
   - 利用 “下载” 面板导出/导入规则  
   - `uBlock list manager` 协同管理多种列表  

5. **调试与日志**  
   - 在 `storage` 面板查看已启用的过滤器  
   - 在控制台执行 `uBlock.console.getToken('uBlock.log')` 查看日志  
   - 在扩展“站点特定规则”添加临时规则  

6. **移除/禁用**  
   - 在“过滤器”列表禁用规则，或在浏览器扩展管理中关闭。  

## 快速开始（本地构建）

```bash
# 克隆仓库
git clone https://github.com/gorhill/uBlock.git
cd uBlock
# 运行构建脚本
./do.sh all
# 在开发者模式下加载 unpacked 扩展
```

> **提示**：所有过滤器为开源，可 fork、定制并共享。  

> **官方文档**  
> - 主页: https://github.com/gorhill/uBlock  
> - 文档: https://github.com/gorhill/uBlock/wiki  
> - 过滤列表: https://easylist.to/filters/easylist.txt