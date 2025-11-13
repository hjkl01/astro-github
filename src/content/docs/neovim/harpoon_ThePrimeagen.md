---
title: harpoon
---

下面是对 GitHub 仓库 [ThePrimeagen/harpoon](https://github.com/ThePrimeagen/harpoon) 的中文说明，仅包含项目地址、主要特性、功能以及使用方法，按要求以 Markdown 格式保存为 `src/content/docs/00/harpoon_ThePrimeagen.md`。  

```markdown
# Harpoon

**GitHub 项目地址**: https://github.com/ThePrimeagen/harpoon

## 主要特性

- **快速文件跳转**：将常用文件标记为“harpoon”，在任何位置通过快捷键或命令迅速切换。
- **多窗口／标签页支持**：一次标记可以在同一会话中多次跳转，不受窗口或标签页限制。
- **持久化状态**：harpoon 列表会在退出时保持，重新打开时自动恢复。
- **简易配置**：默认配有一组可自定义的快捷键，便于快速上手。
- **与 NeoVim `split` / `tab` 兼容**：支持在水平、垂直分屏以及新标签页中跳转。
- **可视化列表**：`:HarpoonList` 显示已标记文件，支持跳转和删除。

## 功能说明

| 功能 | 说明 |
|------|------|
| `:HarpoonAdd` | 将当前窗口所在文件添加到 harpoon 列表 |
| `:HarpoonRemove` | 从 harpoon 列表中删除当前文件 |
| `:HarpoonToggleNumberedMode` | 打开**<br>(`:Hurl`等) | 在新窗口/标签页中打开对应文件 |
| `:HarpoonList` | 打印所有已标记文件，并列出跳转快捷键| `:harpoon ui` (插件 API) | 通过 API 读取/写入列表，可在自定义脚本中使用 |
| 显示/隐藏列表 | `:lua require('harpoon.ui'):toggle_quick_menu()` |
| 持久化文件 | 默认会写入到 `~/.config/nvim/data/harpoon.json`，或自定义位置 |
| 预置序号 | `:HarpoonAdd 1` 直达第 1 个标记；最高支持 5 级 |

## 使用方法

1. **安装**  
   ```bash
   # 推荐使用 packer.nvim
   use { 'ThePrimeagen/harpoon', requires = { 'nvim-lua/plenary.nvim' } }
   ```

2. **基本配置（可放在 `init.lua` 或 `plugins/harpoon.lua`）**  
   ```lua
   local harpoon = require("harpoon")

   -- 快捷键（示例）
   vim.api.nvim_set_keymap('n', '<leader>ha', '<cmd>lua require("harpoon.mark").add_file()<CR>', { noremap = true, silent = true })
   vim.api.nvim_set_keymap('n', '<leader>hg', '<cmd>lua require("harpoon.ui").toggle_quick_menu()<CR>', { noremap = true, silent = true })
   vim.api.nvim_set_keymap('n', '<leader>1',  '<cmd>lua require("harpoon.ui").nav_file(1)<CR>', { noremap = true, silent = true })
   vim.api.nvim_set_keymap('n', '<leader>2',  '<cmd>lua require("harpoon.ui").nav_file(2)<CR>', { noremap = true, silent = true })
   vim.api.nvim_set_keymap('n', '<leader>3',  '<cmd>lua require("harpoon.ui").nav_file(3)<CR>', { noremap = true, silent = true })
   vim.api.nvim_set_keymap('n', '<leader>4',  '<cmd>lua require("harpoon.ui").nav_file(4)<CR>', { noremap = true, silent = true })
   vim.api.nvim_set_keymap('n', '<leader>5',  '<cmd>lua require("harpoon.ui").nav_file(5)<CR>', { noremap = true, silent = true })
   ```

3. **使用流程**  
   - **标记文件**： `:Ha` (`<leader>ha`)，或在当前 buffer 按 `<leader>ha`。  
   - **查看/切换**： `:Hurl` (`<leader>hg`) 打开可视化列表，或直接按 `<leader>1` ~ `<leader>5`。  
   - **删除标记**：在列表中使用 `x` 或 `:HarpoonRemove`。  
   - **切到已有文件**：`nnoremap <leader>1 :lua require('harpoon.ui').nav_file(1)<CR>`。  

4. **自定义持久化路径**（可选）  
   ```lua
   harpoon.settings:set("save_path", vim.fn.stdpath("config") .. "/harpoon.json")
   ```

5. **常用命令总结**  
   - `:HarpoonAdd` / `<leader>ha` – 添加当前文件。  
   - `:HarpoonRemove` – 删除标记。  
   - `:HarpoonList` – 列出所有标记。  
   - `:HarpoonToggleNumberedMode` – 开/关编号模式。  
   - `:lua require('harpoon.ui').toggle_quick_menu()` – 触发侧边栏列表。

> 通过上述配置，你可以在 Neovim 中像使用书签一样快速跳转到任何重要文件，极大提升大项目的开发效率。
