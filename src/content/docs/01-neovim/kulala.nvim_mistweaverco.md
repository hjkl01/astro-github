---
title: kulala.nvim
---

# Kulala.nvim

**项目地址**  
<https://github.com/mistweaverco/kulala.nvim>

## 概述

> Description from GitHub: A fully-featured 🤏 HTTP-client 🐼 interface 🖥️ for Neovim ❤️.

## 安装

```lua
-- packer.nvim
use {
  'mistweaverco/kulala.nvim',
  requires = {
    'MunifTanjim/nui.nvim',
    'nvim-lua/plenary.nvim',
    'nvim-telescope/telescope.nvim'  -- optional, for fuzzy finder
  },
  config = function()
    require('kulala').setup()
  end
}
```

## 主要特性

| 功能           | 说明                                                                                     |
| -------------- | ---------------------------------------------------------------------------------------- |
| **请求 UI**    | 侧边栏展示请求列表，支持分组、搜索、创建/编辑请求文件（`.http` 或 `.json`）。            |
| **环境变量**   | 支持全局、请求级别、动态变量；变量可通过 `{{var}}` 语法引用。                            |
| **请求链**     | 通过 `kulala.set_env` 或 `kulala.add_env` 在请求中更新变量，方便依赖前一次响应值。       |
| **响应查看**   | 自动格式化 JSON、XML、文本；支持原始文本、树形视图、图片预览等。                         |
| **历史记录**   | 按时间排序保存请求/响应，支持搜索与重用。                                                |
| **导入导出**   | 支持 Postman Collection、Insomnia Collection、CSV 等格式。                               |
| **身份验证**   | 内置 Basic Auth、Bearer Token、API Key、OAuth2 等多种认证方式。                          |
| **插件化**     | 可通过 Lua 脚本扩展功能，定义自定义请求头、请求体模板、后置脚本。                        |
| **键盘导航**   | 默认快捷键：`<C-k>` 打开 UI，`<C-s>` 发送请求，`<C-h>` 切换历史/环境，`<C-e>` 编辑请求。 |
| **多终端支持** | 在多终端/窗口中保持同步状态，方便团队协作。                                              |

## 用法

1. **打开 Kulala UI**

   ```vim
   :Kulala
   ```

   或使用快捷键 `Ctrl-k`（可自定义）。

2. **创建/编辑请求**
   - 在 UI 侧边栏中选中或新建请求文件（`.http` 或 `.json`）。
   - 使用 `nvim` 编辑器直接编写请求，支持 `httpie` 或 `curl` 语法。
   - 示例（`.http` 文件）：

     ```http
     GET https://api.example.com/users/{{user_id}}
     Authorization: Bearer {{token}}

     # Request body (optional)
     ```

3. **发送请求**
   - 在请求文件的聚焦状态下，按 `Ctrl-s` 或输入 `:KulalaSend`。
   - Kulala 会使用 `curl`（或系统默认的 HTTP CLI）异步发送请求，并在 UI 下方显示响应。

4. **查看响应**
   - 通过键盘切换响应面板：`Ctrl-h` 切换历史/环境，`Ctrl-Enter` 打开原始响应。
   - 支持 `:KulalaTogglePretty` 切换 JSON/文本预览。

5. **使用环境变量**
   - 在 UI 右侧的 Environment 面板中添加或编辑变量。
   - 变量可在请求体中使用 `{{var_name}}` 语法。
   - 运行前，Kulala 会自动替换所有变量。

6. **请求链**
   - 在请求脚本中使用 `kulala.set_env('key', response.body.field)` 更新变量。
   - 例如：
     ```lua
     local token = json.decode(response.body).access_token
     kulala.set_env('token', token)
     ```

7. **导入导出**
   - 命令：`:KulalaImport <path>` / `:KulalaExport <path>`。
   - 支持 Postman Collection (`.json`)、Insomnia Collection (`.json`) 等。

## 配置示例

```lua
require('kulala').setup({
  ui = {
    theme = 'dark',
    width = 40,
  },
  request = {
    timeout = 30,          -- 秒
    cli = 'curl',          -- 可选 'httpie'
  },
  env = {
    file = '~/.config/nvim/kulala.env.json',
  },
})
```

## 贡献

欢迎提交 Issue 与 PR，或在 Discord/Slack 讨论插件功能。  
请先阅读官方文档与代码规范。

---

**项目地址**：<https://github.com/mistweaverco/kulala.nvim>
