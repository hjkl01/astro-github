---
title: obsidian.nvim
---

# obsidian.nvim

## 功能

obsidian.nvim 是一个 Neovim 插件，用于在 Neovim 中编写和导航 Obsidian vaults。它是用 Lua 编写的，旨在为喜欢 Obsidian 概念（简单的基于 markdown 的笔记应用）但更喜欢在 Neovim 中输入字符的用户提供支持。

该插件不是为了替换 Obsidian 应用，而是为了补充它。Obsidian 应用具有移动应用和许多在 Neovim 中不切实际的功能，如图表浏览器视图。但该插件也可以独立使用。

### 主要功能

- **自动补全**：通过 nvim-cmp 或 blink.cmp 提供笔记引用和标签的超快速异步自动补全（触发于 `[[` 用于 wiki 链接、`[` 用于 markdown 链接，或 `#` 用于标签）。
- **导航**：通过链接、反向链接、标签等在 vault 中导航。
- **图像**：将图像粘贴到笔记中。
- **状态**：在页脚显示笔记状态，如 Obsidian 应用。

### Keymaps

- `smart_action`：绑定到 `<CR>` 将：
  - 如果光标在链接上，跟随链接。
  - 如果光标在标签上，在选择器中显示所有带有该标签的笔记。
  - 如果光标在复选框上，切换复选框。
  - 如果光标在标题上，循环该标题的折叠。
- `nav_link`：绑定到 `[o` 和 `]o` 将光标导航到缓冲区中的下一个有效链接。

### 命令

主要命令是 `:Obsidian`，用于选择子命令。

#### 顶级命令

- `:Obsidian dailies [OFFSET ...]`：打开每日笔记的选择器列表。
- `:Obsidian new [TITLE]`：创建新笔记。
- `:Obsidian open [QUERY]`：在 Obsidian 应用中打开笔记。
- `:Obsidian today [OFFSET]`：打开/创建新的每日笔记。
- `:Obsidian tomorrow`：打开/创建下一个工作日的每日笔记。
- `:Obsidian yesterday`：打开/创建上一个工作日的每日笔记。
- `:Obsidian new_from_template [TITLE] [TEMPLATE]`：从模板创建新笔记。
- `:Obsidian quick_switch`：切换到 vault 中的另一个笔记。
- `:Obsidian search [QUERY]`：使用 ripgrep 和首选选择器搜索 vault 中的笔记。
- `:Obsidian tags [TAG ...]`：获取给定标签的所有出现的选择器列表。
- `:Obsidian workspace [NAME]`：切换到另一个工作区。

#### 笔记命令

- `:Obsidian backlinks`：获取当前笔记的引用选择器列表。
- `:Obsidian follow_link [STRATEGY]`：跟随光标下的笔记引用。
- `:Obsidian toc`：获取当前笔记的目录选择器列表。
- `:Obsidian template [NAME]`：从模板文件夹插入模板。
- `:Obsidian links`：获取当前笔记中所有链接的选择器列表。
- `:Obsidian paste_img [IMGNAME]`：将剪贴板中的图像粘贴到光标位置。
- `:Obsidian rename [NEWNAME]`：重命名当前缓冲区的笔记或光标下的引用。
- `:Obsidian toggle_checkbox`：循环复选框选项。

#### 视觉模式命令

- `:Obsidian extract_note [TITLE]`：将视觉选择的文本提取到新笔记并链接到它。
- `:Obsidian link [QUERY]`：将内联视觉选择的文本链接到笔记。
- `:Obsidian link_new [TITLE]`：创建新笔记并将其链接到内联视觉选择的文本。

## 用法

### 要求

- Neovim >= 0.10.0
- 对于补全和搜索功能：ripgrep 和选择器（如 telescope.nvim、fzf-lua 等）
- 附加系统依赖：根据平台需要 wsl-open、pngpaste、xclip 或 wl-clipboard 用于图像粘贴。

### 安装

使用 lazy.nvim：

```lua
return {
  "obsidian-nvim/obsidian.nvim",
  version = "*", -- 推荐使用最新发布版
  ft = "markdown",
  opts = {
    workspaces = {
      {
        name = "personal",
        path = "~/vaults/personal",
      },
      {
        name = "work",
        path = "~/vaults/work",
      },
    },
  },
}
```

### 配置

通过传递自定义选项到 `require"obsidian".setup()` 来配置插件。默认选项见仓库的配置文件。

更多详细信息请参考 [obsidian.nvim wiki](https://github.com/obsidian-nvim/obsidian.nvim/wiki)。
