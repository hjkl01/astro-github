---
title: typescript-tools.nvim
---

## 功能介绍

typescript-tools.nvim 是一个为 Neovim 提供 TypeScript 集成的插件，它使用原生的 Tsserver 通信协议，类似于 Visual Studio Code 的 TypeScript 支持。该插件旨在为大型 TypeScript/JavaScript 项目提供快速、准确的代码补全和诊断，避免了 `typescript-language-server` 在大型项目中的性能问题和崩溃。

### 主要功能

- **⚡ 极快性能**：利用原生 Tsserver 协议，提供快速的代码补全和诊断。
- **🪭 广泛兼容**：支持 TypeScript 4.0 及以上版本。
- **🌍 LSP 生态支持**：与 Neovim LSP 插件生态系统完全兼容。
- **🔀 多实例支持**：支持运行多个 Tsserver 实例。
- **💻 灵活安装**：支持本地和全局 TypeScript 安装，以及通过 Mason 安装的 tsserver。
- **💅 styled-components 支持**：开箱即用支持 styled-components（需要额外配置）。
- **✨ 增强重构**：提供改进的代码重构功能，如提取变量或函数。

## 用法

### 安装要求

- Neovim >= 0.11.0
- plenary.nvim
- TypeScript >= 4.0
- 兼容的 Node.js 版本

### 安装方法

#### 使用 lazy.nvim

```lua
{
  "pmizio/typescript-tools.nvim",
  dependencies = { "nvim-lua/plenary.nvim", "neovim/nvim-lspconfig" },
  opts = {},
}
```

#### 使用 packer.nvim

```lua
use {
  "pmizio/typescript-tools.nvim",
  requires = { "nvim-lua/plenary.nvim" },
  config = function()
    require("typescript-tools").setup {}
  end,
}
```

### 配置

基本配置示例：

```lua
require("typescript-tools").setup {
  on_attach = function() ... end,
  handlers = { ... },
  settings = {
    -- 在单独的诊断服务器上计算诊断
    separate_diagnostic_server = true,
    -- 确定客户端何时询问服务器诊断："change"|"insert_leave"
    publish_diagnostic_on = "insert_leave",
    -- 指定暴露为代码操作的命令
    expose_as_code_action = {},
    -- 自定义 tsserver.js 路径
    tsserver_path = nil,
    -- 加载的 tsserver 插件列表
    tsserver_plugins = {},
    -- 内存限制
    tsserver_max_memory = "auto",
    -- 格式化选项
    tsserver_format_options = {},
    tsserver_file_preferences = {},
    -- 消息语言
    tsserver_locale = "en",
    -- 完成函数调用
    complete_function_calls = false,
    include_completions_with_insert_text = true,
    -- CodeLens
    code_lens = "off",
    disable_member_code_lens = true,
    -- JSX 关闭标签
    jsx_close_tag = {
        enable = false,
        filetypes = { "javascriptreact", "typescriptreact" },
    }
  },
}
```

### styled-components 支持

安装插件：

```bash
npm i -g @styled/typescript-styled-plugin typescript-styled-plugin
```

在配置中启用：

```lua
require("typescript-tools").setup {
  settings = {
    tsserver_plugins = {
      -- 对于 TypeScript v4.9+
      "@styled/typescript-styled-plugin",
      -- 或对于旧版 TypeScript
      -- "typescript-styled-plugin",
    },
  },
}
```

### 自定义用户命令

插件提供以下命令（仅适用于当前缓冲区）：

- `TSToolsOrganizeImports` - 排序并移除未使用的导入
- `TSToolsSortImports` - 排序导入
- `TSToolsRemoveUnusedImports` - 移除未使用的导入
- `TSToolsRemoveUnused` - 移除所有未使用的语句
- `TSToolsAddMissingImports` - 为缺少导入的语句添加导入
- `TSToolsFixAll` - 修复所有可修复的错误
- `TSToolsGoToSourceDefinition` - 跳转到源定义（TS v4.7+）
- `TSToolsRenameFile` - 重命名当前文件并应用更改
- `TSToolsFileReferences` - 查找引用当前文件的所有文件（TS v4.2+）

### 支持的 LSP 方法

插件支持多种 LSP 方法，包括代码补全、悬停、重命名、诊断、签名帮助、引用、定义、类型定义、实现、文档符号、高亮、代码操作、格式化、折叠范围、语义标记、内联提示、调用层次结构、代码镜头、工作区符号等。
