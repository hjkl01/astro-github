---
title: toggleterm.nvim
---
---

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| 终端窗口不按预期大小显示 | 确认 `size` 参数是否为数值或函数，根据屏幕宽高设置。 |
| 打开终端后不进入 Insert 模式 | 拷贝 `start_in_insert = true` 至配置中。 |
| 与其他插件键盘映射冲突 | 调整 `open_mapping` 至不冲突的组合键，例如 `Ctrl + t`。 |

---
## 结语
`toggleterm.nvim` 让 Neovim 拥抱终端，短暂离不开编辑轨道即可执行命令、运行脚本、跑测试，极大提升工作效率，适用于任何需要频繁交互终端的工作流。  
> 完整手册见: <https://github.com/akinsho/toggleterm.nvim>  
