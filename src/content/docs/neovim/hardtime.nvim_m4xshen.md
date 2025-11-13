---
title: hardtime.nvim
---

# hardtime.nvim

**GitHub 地址**： https://github.com/m4xshen/hardtime.nvim

## 一、项目简介

> Description from GitHub: Break bad habits, master Vim motions

## 二、主要特性

| 特性           | 描述                                                                               |
| -------------- | ---------------------------------------------------------------------------------- |
| **卡片式练习** | 将代码拆分为可练习的“硬化卡片”，每张卡片对应一个小功能或 Bug 修复。                |
| **难度递增**   | 每完成一张卡片，插件自动提升下一张卡片的难度，例如增加复杂度、约束数量或时间限制。 |
| **进度跟踪**   | 通过 Neovim 内置 UI 展示练习进度、完成时间、错误率等统计信息。                     |
| **自动测试**   | 在提交前自动运行单元测试，确保改动不破坏现功能。                                   |
| **多语言支持** | 目前支持 Ruby、Python、JavaScript、TypeScript 等主流语言，易于集成到多语言项目中。 |
| **项目导入**   | 通过配置文件导入已有项目，插件会自动识别文件结构并生成对应练习卡片。               |
| **可视化操作** | 通过 `Telescope`、`nvim-tree` 等插件集成，实现卡片筛选、跳转、编辑一键化。         |

## 三、核心功能

1. **卡片生成**
   - `:HardtimeGenerate`：根据项目文件结构生成练习卡片。
   - `:HardtimeRefresh`：重新扫描代码并更新卡片。

2. **练习流程**
   - `:HardtimeStart <card_id>`：启动指定卡片的练习。
   - `:HardtimeSubmit`：提交练习，并自动跑测试。

3. **查看进度**
   - `:HardtimeStats`：显示当前练习统计信息，如成功率、平均完成时间等。
   - `:HardtimeTimeline`：可视化查看卡片完成时间线。

4. **投降与重做**
   - `:HardtimeFail`：标记当前卡片为失败，自动记录错误。
   - `:HardtimeRedo <card_id>`：重新打开卡片进行练习。

## 四、使用示例

1. **安装插件**  
   使用插件管理器（如 `packer.nvim`）添加：

   ```lua
   use {
     'm4xshen/hardtime.nvim',
     config = function() require('hardtime').setup() end
   }
   ```

2. **项目初始化**

   ```bash
   nvim
   :HardtimeGenerate
   ```

3. **开始练习**

   ```vim
   :HardtimeStart 42
   # 进行代码修改
   :HardtimeSubmit
   ```

4. **查看统计**

   ```vim
   :HardtimeStats
   ```

5. **重做卡片**
   ```vim
   :HardtimeRedo 42
   ```

## 五、配置示例

```lua
require('hardtime').setup({
  difficulty_levels = { 5, 7, 10 }, -- 难度阈值
  languages = { 'lua', 'python', 'javascript' },
  test_command = { 'pytest', '-q' }, -- 自动测试命令
  ui = {
    progress_bar = true,
    show_stats = true,
  },
})
```

## 六、常见问题

| 问题             | 解决方案                                                  |
| ---------------- | --------------------------------------------------------- |
| 练习卡片没有生成 | 确认项目根目录存在 `.git` 或 `package.json` 等标识文件    |
| 测试失败         | 检查 `test_command` 配置是否正确，或手动运行              |
| 统计不显示       | 需要安装并配置 `telescope.nvim` / `nvim-tree.lua`（可选） |

## 七、贡献方式

- 反馈 bug：在 GitHub Issues 处提交。
- 新功能：Fork 项目，提交 PR 并添加相应测试。
- 文档：完善 README、示例或翻译。

## 八、授权

本项目使用 MIT 许可证。

---

**GitHub 地址**： https://github.com/m4xshen/hardtime.nvim

```

```
