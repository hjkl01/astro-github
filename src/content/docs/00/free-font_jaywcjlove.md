
---
title: free-font
---

**项目地址**  
https://github.com/jaywcjlove/free-font

**主要特性与功能**  

| 序号 | 功能特性 | 说明 |
|------|----------|------|
| 1 | **海量免费字体集合** | 包含上千款字体，涵盖中文、日文、英文、符号等多种语言与风格。 |
| 2 | **分类与标签** | 字体按正文字体、标题字体、手写体、 Display 体、图标字体、语言系列等多维度分类，方便快速定位。 |
| 3 | **授权信息一览** | 每款字体均标注对应授权方式（如 SIL OFL、ISC、APSL 等）以及可使用范围，帮助用户遵循法律要求。 |
| 4 | **预览与下载** | 为每款字体提供在线预览文本，用户可以直接在浏览器中预览并点击下载按钮获得完整字体包。 |
| 5 | **搜索与筛选** | 页面底部提供搜索框及多种筛选条件（许可证、字类、语言、标签），支持快速定位需要的字体。 |
| 6 | **多平台支持** | 所有字体均以标准 TTF/OTF/WOFF/WOFF2 等格式提供，兼容 Windows、macOS、Linux、Web 与移动端。 |
| 7 | **持续维护** | 项目保持定期更新，及时加入新的免费字体资源，并对过期或已失效的资源做标注或移除。 |

**使用方法**  

1. 访问项目主页：<https://github.com/jaywcjlove/free-font>。  
2. 在页面左侧或上方的搜索栏中键入关键词（如“手写体”、“中文”），也可使用筛选条件进一步细化。  
3. 在搜索结果列表中，点击字体名称查看详细信息页面，页面中会展示：  
   * 字体预览（可自行输入自己想看的文字或使用默认样例）。  
   * 许可证说明、授权链接，以及字体作者/来源。  
4. 在字体页面底部有 **Download** / **Download ZIP** 按钮，点击即可下载完整字体文件或压缩包。  
5. 下载完成后将字体文件放入系统字体目录或项目中使用即可。  
   * **Windows**：右键字体文件 → “安装”。  
   * **macOS**：双击字体 → “安装字体”。  
   * **Web**：将 WOFF/WOFF2 文件上传至服务器，在 CSS 中使用 `@font-face` 加载。  

**快速示例（Web）**  

```html
<link rel="preconnect" href="https://fonts.gstatic.com">
<style>
@font-face {
  font-family: 'OpenSans';
  src: url('fonts/OpenSans-Regular.woff2') format('woff2'),
       url('fonts/OpenSans-Regular.woff') format('woff');
  font-weight: 400;
  font-style: normal;
}
body { font-family: 'OpenSans', sans-serif; }
</style>
```

**高阶使用**  

- 若要批量下载某一类别字体，可先在 GitHub 页面右上角点击 “Code” → “Download ZIP” 下载整仓库；  
- 在本地使用 `find` / `grep` 命令快速定位所需字体文件；  
- 若你具备用脚本定期同步新的免费字体，请参考项目文件夹内的 `LICENSE` 与 `NOTICE`，确保遵守相应开源协议。  

> 只需一个浏览器、一次下载，项目即提供给你完整的免费字体库。无需额外安装工具，直接调用即可开始创作。

💝 Support this free API: https://www.paypal.com/donate/?hosted_button_id=XS3CAYT8LE2BL