
---
title: opencode.nvim
---


# opencode.nvim (NickvanDyke)

**项目地址**  
<https://github.com/NickvanDyke/opencode.nvim>

---

## 一、主要特性

| 特性 | 简述 |
|------|------|
| 生成远程仓库链接 | 自动识别当前 Git 远程地址（GitHub / GitLab / Bitbucket 等），生成文件 URL 并支持行号、选择区、提交哈希等指令 |
| 多平台支持 | 兼容常见的托管平台，还可通过配置自定义更多仓库类型 |
| 快速打开 | 直接在浏览器中打开链接，支持 `gh` cli、VSCode 等辅助工具 |
| 代码片段分享 | 在选择区域后生成对应行号区间的 URL，适合在电子邮件、Slack、Markdown 等中分享 |
| 强化键位映射 | 提供默认快捷键，可按需自定义，便捷一键打开 |
| 耐用的 URL 缓存 | 通过配置自定义模板（如 `https://github.com/{owner}/{repo}/blob/{branch}/{file}`），支持多种 URL 样式 |
| 易于集成 | 通过适配器模式可与 `packer.nvim`、`lazy.nvim` 等包管理器无缝配合 |

---

## 二、功能列表

1. **打开当前文件**  
   - `:Opencode`：打开当前缓冲区对应文件的 URL（默认当前所在行）。

2. **打开指定行**  
   - `:Opencode {lnum}`：打开指定行号的 URL（若省略则使用当前行号）。

3. **打开选择区**  
   - `:Opencode --range`：将所选文本范围对应的行号区间生成 URL 并打开。

4. **打开特定提交**  
   - `:Opencode {commit}`：根据提交哈希生成对应文件的URL（可提供 `--branch` 指定分支）。

5. **在 VSCode 中打开**  
   - `:Opencode --vscode`：使用 VSCode 打开远程文件，内部会在 URL 前加 `vscode://vscode.git/+/...`。

6. **自定义 URL 模板**  
   - `:Opencode --template '<template>'`：使用自定义 URL 模板（支持占位符 `{owner}`、`{repo}`、`{branch}`、`{file}`、`{lnum}`）。

7. **添加标签页**  
   - `:Opencode --tab`：在新标签页中打开链接（默认使用浏览器）。

---

## 三、基本用法

1. **安装**（使用 packer.nvim 为例）

```lua
use {
  'NickvanDyke/opencode.nvim',
  config = function()
    require('opencode').setup()
  end
}
```

2. **基本命令**

| 命令 | 描述 |
|------|------|
| `:Opencode` | 生成并打开当前文件当前行 |
| `:Opencode {lnum}` | 打开指定行号 |
| `:Opencode {commit}` | 打开指定提交对应的文件 |
| `:Opencode --range` | 在可视模式下使用选择区域 |
| `:Opencode --vscode` | 用 VSCode 打开 |
| `:Opencode --tab` | 在新标签页打开（浏览器） |
| `:Opencode --template '<tpl>'` | 使用自定义模板 |

3. **快捷键**

默认映射（可自行修改）：

```lua
vim.api.nvim_set_keymap('n', '<leader>ol', '<cmd>Opencode<CR>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('v', '<leader>oc', '<cmd>Opencode --range<CR>', { noremap = true, silent = true })
```

---

## 四、配置示例

```lua
require('opencode').setup({
  -- 储存自定义模板
  templates = {
    github = 'https://github.com/{owner}/{repo}/blob/{branch}/{file}#L{lnum}',
    gitlab = 'https://gitlab.com/{owner}/{repo}/-/blob/{branch}/{file}#L{lnum}',
  },

  -- 预设的默认垂直分割浏览器打开方式
  open_browser_in_new_tab = true,

  -- 支持 VSCode
  open_with_vscode = true,
  vscode_command = 'code',
})
```

---

## 五、常见问题

| 场景 | 解决方案 |
|------|----------|
| Git 远程地址无法识别 | 确认 `git remote -v` 显示远程地址，并且已在对应项目根目录 |
| URL 无法正常跳转 | 检查 `templates` 配置，尤其是占位符是否正确 |
| 跳转到错误行号 | 确认当前行号或选区行号已在文件中真实存在 |

---

## 六、贡献

若想贡献代码或改进功能，请查看仓库中的 `CONTRIBUTING.md` 与 `ISSUES`。

---

**项目地址**  
<https://github.com/NickvanDyke/opencode.nvim>
