---
title: TrackersListCollection
---

# TrackersListCollection 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/XIU2/TrackersListCollection/blob/master/README-ZH.md)

## 主要特性
- **开源免费**：项目完全开源，提供大量公共 BT  tracker 列表，适用于各种 torrent 客户端。
- **定期更新**：维护者定期更新 tracker 列表，确保列表中的节点活跃且有效。
- **多语言支持**：README 文档提供中英文版本，便于全球用户使用。
- **分类整理**：tracker 列表按来源和类型分类，便于用户选择合适的节点。
- **兼容性强**：支持 qBittorrent、uTorrent、Transmission 等主流 BT 客户端。

## 主要功能
- **提供 tracker 列表**：收集全球范围内的公共 tracker 服务器地址，用于提升 BT 下载速度和稳定性。
- **UDP 和 HTTP 支持**：包含 UDP 和 HTTP 协议的 tracker，支持不同网络环境。
- **列表生成工具**：项目包含脚本工具，可自动生成和更新 tracker 列表文件。
- **性能优化**：通过筛选高质量 tracker，帮助用户减少下载时间和失败率。
- **社区贡献**：鼓励用户提交新的 tracker 节点，保持列表的活跃度。

## 用法
1. **获取列表**：访问项目 README，复制最新的 tracker 列表文本（通常为一行多 tracker 地址的字符串）。
2. **添加到客户端**：
   - 在 qBittorrent 中：打开 torrent 文件属性 > 添加 tracker > 粘贴列表。
   - 在 uTorrent 中：右键 torrent > 属性 > Tracker > 添加 URL（粘贴列表）。
   - 在 Transmission 中：编辑 torrent > 添加 tracker URL。
3. **使用脚本更新**：克隆仓库，运行提供的 Python 脚本（如 `all.txt` 生成脚本）来自动拉取和合并最新 tracker。
4. **自定义**：用户可根据需要编辑列表，只保留特定协议或区域的 tracker。
5. **注意事项**：定期更新列表以保持最佳性能，避免使用过时节点；确保客户端支持批量添加。