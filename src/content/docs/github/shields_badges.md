---
title: shields
---


# shields.io

项目地址: https://github.com/badges/shields

## 项目简介
shields.io 是一个生成自定义徽章（Badges）的在线服务，广泛用于 GitHub README、文档等地方展示项目状态、构建进度、许可证、版本等信息。

## 主要特性
- **高度可定制**：支持多种主题、颜色、标签、徽章尺寸等。
- **多种数据源**：可直接映射 GitHub 统计（如 stars、forks、issues、pull requests 等），也支持自定义 JSON、HTTP、Travis CI、CircleCI、AppVeyor、GitLab CI 等。
- **静态生成**：所有徽章均为静态图像，缓存友好，加载速度快。
- **Markdown 友好**：通过简单的 Markdown 语法即可嵌入徽章。
- **可公开访问**：默认公开可用，无需账号即可使用。

## 功能概览
| 功能 | 说明 |
|------|------|
| **GitHub 数据徽章** | 显示 stars、forks、issues、pull requests、watchers 等。 |
| **CI/CD 状态** | 集成 Travis CI、CircleCI、AppVeyor、GitLab CI 等 CI 状态。 |
| **版本 & 许可证** | 显示最新 release 版本、许可证类型。 |
| **自定义徽章** | 通过 `?label=...&message=...&color=...` 参数自定义文本与颜色。 |
| **统计图形** | 支持显示 build 通过率、测试覆盖率、贡献者数量等。 |
| **多语言支持** | 通过 `?style=flat-square`、`?style=social` 等参数调整样式。 |

## 用法示例
```markdown
![GitHub stars](https://img.shields.io/github/stars/badges/shields.svg)
![GitHub forks](https://img.shields.io/github/forks/badges/shields.svg)
![GitHub issues](https://img.shields.io/github/issues/badges/shields.svg)
![GitHub license](https://img.shields.io/github/license/badges/shields.svg)
```

### 自定义徽章
```markdown
![自定义徽章](https://img.shields.io/badge/自定义-示例-blue)
```

### CI 状态徽章
```markdown
![Travis CI](https://img.shields.io/travis/badges/shields.svg)
![CircleCI](https://img.shields.io/circleci/project/github/badges/shields.svg)
```

## 使用说明
1. **直接使用**：复制上述 Markdown 代码，在 README 或 Docs 中粘贴即可。
2. **自定义参数**：根据需要修改 URL 中的 `label`、`message`、`color`、`style` 等参数。
3. **缓存 & CDN**：shields.io 使用 CDN 缓存，访问速度快，无需额外配置。

---
> 以上内容已保存为 `src/content/docs/00/shields_badges.md`。