
---
title: dotfiles
---


# dotfiles (typecraft-dev)

项目地址: https://github.com/typecraft-dev/dotfiles

## 主要特性

- **完整的配置管理**：集合了开发环境中常用工具（zsh、tmux、vim、git 等）的配置文件，方便快速搭建工作站。
- **统一配置**：通过统一的 dotfiles 管理，实现多台机器之间的一致性，减少配置冲突。
- **可复用脚本**：包含安装脚本与符号链接脚本，支持一键部署。
- **模块化设计**：不同工具的配置文件通过子目录分离，易于维护与扩展。
- **文档化**：项目中齐全的说明文件（README、INSTALL 等）指导用户完成安装和使用。

## 安装与使用

```bash
# 克隆仓库
git clone https://github.com/typecraft-dev/dotfiles.git
cd dotfiles

# 运行安装脚本
./install.sh
```

> `install.sh` 会自动创建符号链接，并根据需要执行依赖安装。

## 结构示例

```
dotfiles/
├── bin/        # 工具脚本
├── etc/        # 通用配置
├── etc/vim/    # Vim 配置
├── etc/zsh/    # Zsh 配置
├── etc/tmux/   # Tmux 配置
├── etc/git/    # Git 配置
├── install.sh  # 一键安装脚本
├── README.md
└── ...
```

## 贡献

可直接提交 PR 或 issue，提交前请参考项目的贡献指南。

--- 

> 以上内容已保存为文件 `src/content/docs/00/dotfiles_typecraft-dev.md`。