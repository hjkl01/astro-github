
---
title: xiaomusic
---

**文件路径**：`src/content/docs/00/xiaomusic_hanxi.md`

```markdown
# 小音乐播放器（xiaomusic）

## 项目地址
https://github.com/hanxi/xiaomusic

## 主要特性
- **简洁 UI**：采用轻量级 UI 框架（如 Ant Design / Element Plus）实现响应式布局。  
- **多格式音乐播放**：支持 MP3、AAC、OGG 等常见音频格式，使用 HTML5 `<audio>` 或 WebAudio API。  
- **播放控制**：播放、暂停、上一曲/下一曲、循环/随机播放、音量调节、进度条拖拽。  
- **歌单管理**：可自定义歌单、收藏/取消收藏、歌单排序、批量删除。  
- **搜索与推荐**：支持关键字搜索本地或网络音乐，展示搜索结果并可直接播放。  
- **本地缓存**：通过 `IndexedDB / localStorage` 缓存播放列表与收藏记录，离线使用。  
- **主题切换**：支持暗黑/亮色主题，主题设置可持久化。  
- **多语言**：默认中文，支持切换为英文等多语言。

## 功能模块
| 模块 | 说明 |
|------|------|
| `Player` | 播放核心逻辑，封装音频 API，提供事件回调。 |
| `Playlist` | 管理歌单数据，支持增删改查。 |
| `Search` | 关键字查询接口，展示结果列表。 |
| `UI Components` | 统一样式、按钮、进度条、模态框等。 |
| `Storage` | 本地持久化，兼容多浏览器。 |

## 使用方法

1. **克隆仓库**  
   ```bash
   git clone https://github.com/hanxi/xiaomusic.git
   cd xiaomusic
   ```

2. **安装依赖**  
   ```bash
   npm install
   # 或者使用 yarn
   yarn
   ```

3. **运行开发环境**  
   ```bash
   npm run dev
   # 或者
   yarn dev
   ```
   打开浏览器访问 `http://localhost:5173`（默认端口）。

4. **构建生产包**  
   ```bash
   npm run build
   # 或者
   yarn build
   ```

5. **部署**  
   将 `dist/` 目录内容部署到任意静态服务器或 CDN。

## 贡献

欢迎提交 Issue 与 Pull Request，详见 `CONTRIBUTING.md`。

## 许可证

MIT © hanxi
