---
title: rime-ice
---


# rime-ice (iDvel)

**GitHub 地址**: [https://github.com/iDvel/rime-ice](https://github.com/iDvel/rime-ice)

## 项目概述
rime-ice 为 RIME 输入法提供的开源配置方案，聚焦简洁、美观与高效。它整合了多种常用词库、智能排版规则与自定义皮肤，以提升中文与多语言输入体验。

## 主要特性
- **多语言支持**：内置中英混合、日语、韩语、俄语等预设词库，兼容多语言文字。
- **自定义词典**：支持用户自建词库，灵活添加专有名词、行业术语。
- **智能学习**：按使用频率自动调整词条顺序，提升输入精度。
- **主题皮肤**：提供多套可切换皮肤，支持自定义字体与色调。
- **词库一键更新**：内置脚本可同步官方词库或第三方词典。
- **高效排版**：字形排版优化，减少视觉卡顿。

## 核心功能
| 功能 | 说明 |
|------|------|
| 词库管理 | `schema.json` 与 `custom_dict.yaml` 管理语法，支持增删改查 |
| 皮肤定制 | 通过 `style.css` 或 `theme.json` 统一修改 UI |
| 快捷键映射 | `key_bindings.yaml` 可自定义功能键 |
| 驱动层面 | 通过 `build.sh` 一键编译与部署配置 |

## 用法

### 1. 环境准备
```bash
# 需要 RIME Engine（常见于 Rime 1.0 及以上）
# clone 项目
git clone https://github.com/iDvel/rime-ice.git
```

### 2. 安装与部署
```bash
# 复制到 RIME 配置目录
cp -r rime-ice/* ~/.config/fcitx/rime/
# 重新加载配置
fcitx5 rime
```

### 3. 添加自定义词典
```bash
# 创建 custom_dict.yaml
vi ~/.config/fcitx/rime/custom_dict.yaml
# 以如下格式添加
custom:
  - "神经网络 : shen2 jing1 wang3 luo4"
```

### 4. 更新词库
```bash
# 进入项目目录
cd rime-ice
# 运行更新脚本
./update.sh
```

### 5. 切换皮肤
```bash
# 在 ~/.config/fcitx/rime/ 目录中创建 theme 文件夹
mkdir -p ~/.config/fcitx/rime/theme
# 拷贝皮肤
cp rime-ice/theme/default.css ~/.config/fcitx/rime/theme/
# 打开配置文件修改 theme 名称
vi ~/.config/fcitx/rime/schemas/example.schema.yaml
# 找到 theme 字段并改为相应文件名
```

## 贡献方式
- Fork 本仓库 → 创建新分支 → 新功能或 bug 修复 → 提交 Pull Request
- 任何好的词典、主题或文档改进都欢迎提交

## 常见问答

**Q: 如何在 IBus 或 Fcitx 里使用？**  
A: 按上述安装方式即可，无需额外配置。

**Q: 词库不更新怎么办？**  
A: 检查网络连通，或手动执行 `./update.sh --force`。

**Q: 如何兼容 macOS？**  
A: 使用 Mac 下的 RIME（如 HarmonyOS 输入法），同样拷贝到 `~/Library/Rime/` 即可。

---
> 本文件为项目 README 的简化中文版本，所有说明均基于官方文档的默认配置。  
```
