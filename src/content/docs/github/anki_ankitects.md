
---
title: anki
---


# anki（ankitects/anki）

**项目地址**  
[https://github.com/ankitects/anki](https://github.com/ankitects/anki)

---

## 主要特性

- **基于间隔重复**  
  使用AnkiDE (Deep Expert) 算法根据记忆曲线自动管理复习间隔，提升学习效率。

- **多媒体支持**  
  卡片内容可包含文本、图片、音频、视频、 LaTeX 等，满足多样化学习需求。

- **跨平台**  
  提供桌面版（Windows、macOS、Linux）、Web 版、Android 与 iOS 版（通过官方同步服务器或第三方同步服务）。

- **插件生态**  
  通过 `anki-extensions` 或 `Anki Add-ons` 目录集成丰富插件，扩展功能（如统计分析、自动化导入、导出、云同步等）。

- **同步服务器**  
  官方 Cloud 服务（AnkiWeb）或自托管 Syncthing、OwnCloud 等实现多设备同步。

- **数据导入/导出**  
  支持 CSV、TSV、Apkg（Anki 懒人包）等多格式导入导出，方便与其他工具交互。

---

## 主要功能

| 功能 | 描述 |
|------|------|
| **卡片创建** | 通过“Add”界面手动输入正反面内容，或使用模板批量生成。 |
| **学习模式** | “Study Now” 紧急卡片；“Review” 自动按复习间隔呈现。 |
| | “Browse” 浏览、编辑、搜索卡片。 |
| **自定义间隔** | 设置学习策略（记忆分级、难度倍增等）。 |
| **批量操作** | 批量编辑标签、删除、移动、复制等。 |
| **AnkiWeb 同步** | 登录 AnkiWeb 账号，实现多设备同步。 |
| **插件管理** | `Tools → Add-ons` 安装/更新/禁用插件。 |
| **数据备份** | 自动生成本地备份文件；支持通过 Git 进行版本管理。 |
| **多格式导入** | CSV、tsv、Apkg、Apkgbd 等。 |
| **高级搜索** | 支持正则、比较、标签、字段搜索。 |

---

## 使用步骤（快速上手）

1. **下载与安装**  
   - 从 GitHub releases 或官方下载安装包。  
   - 对于 Linux，可以使用 `snap install anki` 或直接解压 Zip。

2. **创建新账户**  
   - 访问 <https://ankiweb.net>, 账号注册后获取同步密钥。  
   - 在桌面客户端 `File → Sync` 中输入该密钥完成同步。

3. **创建牌组 & 添加卡片**  
   ```text
   1. File → Deck → Add new <牌组名称>
   2. Select 牌组 → Add
   3. 输入正面、反面内容 → Add
   ```
   - 可选择“Basic (and reverse)”模板快速生成正反两面。

4. **开始学习**  
   - 选中牌组 → Study Now / Review。  
   - 按提示复习，系统会自动记录记忆评分。

5. **同步**  
   - 日常学习后点击 `Sync 或设置自动同步。  
   - 安卓/ iOS 端同样登录 AnkiWeb 账号即可同步。

6. **安装插件**  
   - `Tools → Add-ons → Browse & Install`，搜索插件名或粘贴 .ankiaddon 文件路径。  
   - 重启 Anki 后生效。

7. **备份与导出**  
   - 手动导出：`File → Export…`，选择 `Apkg` 格式。  
   - 自动备份：在 `File → Options → Backup` 开启定时备份。

---

## 常用命令与快捷键

| 快捷键 | 功能 |
|--------|------|
| `A` | Add card |
| `E` | Edit card |
| `F` | Find (Browse) |
| `S` | Study Now |
| `R` | Review |
| `Ctrl+Shift+S` | Sync |
| `Ctrl+P` | Global browser |

---

**小贴士**  
- 常用的第三方插件如 **AnkiConnect**（API 交互）、**Image Occlusion**（遮蔽图像）、**Cadet**（自定义复习策略）等，可大幅提升学习体验。  
- 若需更高级的统计分析，可安装 **AnkiStats** 或 **Anki4Pandas**。

---

> **致谢**  
> 本项目由 AnkiTeam 主导开发，社区贡献者广泛参与。文档、示例卡组与插件可在 GitHub 或 AnkiWeb 上获取。

---