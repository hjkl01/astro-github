
---
title: cookie-editor
---


# cookie-editor

**项目地址**  
<https://github.com/Moustachauve/cookie-editor>

## 简介
`cookie-editor` 是一个基于浏览器的轻量级工具，用于查看、编辑、删除和导入/导出网页 Cookie。它支持跨域 Cookie 管理，并提供直观的图形化界面，方便开发者、测试人员和普通用户快速定位和修改 Cookie。

## 主要特性
- **Cookie 列表**：按域名、路径、名称等字段展示所有 Cookie，支持分页与搜索。
- **编辑和删除**：单击 Cookie 直接编辑字段（名称、值、域、路径、过期时间、HttpOnly、Secure、SameSite），也可以一次性删除选中的 Cookie。
- **导入/导出**：支持 JSON 或浏览器默认格式的 Cookie 导入与导出，便于备份或迁移。
- **批量操作**：可一次性清除当前页面或所有域名下的 Cookie。
- **过滤器**：按域名、路径、类型（Session/Persistent）过滤显示。
- **实时同步**：操作后立即反映到浏览器 Cookie 存储，刷新页面后保持一致。
- **跨浏览器**：兼容 Chrome、Edge、Safari 以及 Firefox（通过相应插件或脚本）。

## 功能说明
| 功能 | 操作步骤 |
|------|----------|
| **查看 Cookie** | 打开工具，浏览列表即可看到所有 Cookie。 |
| **编辑 Cookie** | 双击字段或点击“编辑”按钮，修改后保存即可。 |
| **删除 Cookie** | 选中后点击“删除”按钮，或右键单独删除。 |
| **导出 Cookie** | 选择“导出” → 选择格式 → 下载。 |
| **导入 Cookie** | 选择“导入” → 选择文件 → 解析后插入。 |
| **清除所有 Cookie** | 选择“清除全部” → 确认。 |
| **搜索/过滤** | 在搜索框输入关键词或使用过滤器条件。 |

## 快速使用
1. **安装**  
   - 在 Chrome/Edge/Firefox 浏览器中打开扩展商店，搜索 `cookie-editor` 并安装。  
   - 或者直接下载源码，打开 `manifest.json` 并在浏览器中加载已解压的插件。

2. **打开工具**  
   - 浏览器工具栏点击 `cookie-editor` 图标，弹出管理窗口。

3. **编辑 Cookie**  
   - 选中对应 Cookie，点击“编辑”或双击字段即可修改。  
   - 修改后点击“保存”，浏览器会立即更新。

4. **导入/导出**  
   - 通过菜单进入对应功能，按提示操作即可完成导入/导出。

5. **批量清除**  
   - 选择“清除全部”或使用过滤器后批量删除。

## 代码结构
```
src/
├─ components/      # Vue/React 组件
├─ utils/           # 工具函数（解析 JSON、日期等）
├─ assets/          # 静态资源
└─ manifest.json    # 扩展配置
```

## 贡献
欢迎提交 Issues 或 Pull Requests。请先阅读 `CONTRIBUTING.md`，遵循项目编码规范。

## 许可证
MIT © 2024 Moustachauve

