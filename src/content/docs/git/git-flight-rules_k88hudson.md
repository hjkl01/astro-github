---
title: git-flight-rules
---

# Git Flight Rules (中文版)

**项目地址:** [https://github.com/k88hudson/git-flight-rules](https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md)

## 项目概述
Git Flight Rules 是一个开源指南项目，旨在帮助开发者在 Git 操作中避免常见错误和混乱情况。通过类比飞行规则（Flight Rules），它提供针对特定 Git 场景的实用建议和最佳实践。该项目由 k88hudson 维护，README_zh-CN.md 是其中文翻译版本，基于英文原版内容。

## 主要特性
- **场景导向的指导**：项目按不同 Git 使用场景分类，如“修复已推送的提交”、“处理合并冲突”、“恢复丢失的更改”等，每个场景提供清晰的规则和步骤。
- **实用性和简洁性**：规则基于实际开发经验，强调安全、快速的解决方案，避免 Git 的复杂性导致的“飞行事故”。
- **多语言支持**：原版为英文，并有中文翻译（README_zh-CN.md），便于全球开发者使用。
- **开源协作**：托管在 GitHub 上，鼓励社区贡献和更新规则，以适应 Git 的演进。
- **易读格式**：采用 Markdown 格式，便于阅读和搜索，支持快速定位问题。

## 主要功能
- **问题诊断与解决**：覆盖 Git 常见痛点，如分支管理、回滚操作、远程仓库同步等，提供一步步的命令示例。
- **最佳实践推荐**：不仅仅是修复，还包括预防措施，例如使用 `git stash` 避免意外覆盖、正确处理 rebase 等。
- **跨平台适用**：规则适用于各种 Git 客户端和环境，包括命令行、GUI 工具。
- **扩展性**：用户可以 fork 项目，添加自定义规则，适用于团队或特定项目需求。

## 用法
1. **访问项目**：克隆仓库或直接浏览 [README_zh-CN.md](https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md)，搜索感兴趣的场景标题（如“飞行规则 #1: 我想回滚最近的提交”）。
2. **应用规则**：在遇到 Git 问题时，匹配对应场景，复制提供的 Git 命令执行。例如：
   - 要恢复已删除的分支：使用 `git reflog` 查看历史，然后 `git checkout -b new-branch <commit-hash>`。
3. **日常参考**：将其作为 Git 速查手册，集成到 IDE 或书签中。建议初学者从基础规则开始，高级用户关注 rebase 和 cherry-pick 等高级主题。
4. **贡献**：如果发现规则过时或有新场景，提交 Pull Request 到 GitHub 仓库。

此项目特别适合 Git 新手和中级开发者，帮助他们在“飞行”中平稳导航。