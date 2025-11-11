---
title: free-font
---

# free-font

## 项目简介

free-font 是由 jaywcjlove 创建的一个开源项目，旨在收集可商用的免费英文和汉字字体。该项目基于已不再维护的字集项目，新增了自动生成字体预览封面的脚本，并重新添加了许多中文字体以及开源英文字体。

## 主要功能

- **字体收集**：收录大量免费商用字体，包括英文和中文字体。
- **字体分类**：支持多种分类，如黑体、宋体、楷体、艺术体、手绘体、英文字体、开源字体等。
- **字体预览**：提供字体预览功能，帮助用户快速查看字体效果。
- **下载支持**：用户可以直接下载字体文件用于个人或商业用途。
- **本地开发**：支持本地开发环境，允许用户添加新字体并生成预览。

## 使用方法

### 在线使用

1. 访问项目主页：[https://wangchujiang.com/free-font/](https://wangchujiang.com/free-font/)
2. 浏览字体分类，选择需要的字体。
3. 点击下载按钮获取字体文件。
4. 将字体安装到系统中，即可在设计软件中使用。

### 本地开发

如果您想贡献新字体或本地预览：

1. 克隆项目仓库：

   ```
   git clone https://github.com/jaywcjlove/free-font.git
   cd free-font
   ```

2. 安装依赖：

   ```
   npm install
   ```

3. 添加字体：
   - 将字体文件放入 `docs/fonts` 目录。
   - 在 `scripts/data.json` 中添加字体信息，包括分类、许可证和来源。

4. 生成预览：

   ```
   npm run one -- ./docs/fonts/english/Prima/Prima-Regular.otf  # 生成单个字体预览
   npm run all  # 生成所有字体预览
   ```

5. 生成网站：

   ```
   npm run dev   # 监听模式
   npm run start # 生成静态网站
   ```

6. 预览网站：打开 `docs/index.html` 在浏览器中查看。

### Docker 部署

使用 Docker 镜像快速部署本地预览服务：

```
docker pull wcjiang/free-font:latest
docker run --name reference --rm -d -p 9677:3000 wcjiang/free-font:latest
```

然后访问 `http://localhost:9677` 查看字体网站。

## 注意事项

- 所有字体的版权归原作者所有，使用时请遵守相应许可证。
- 项目不承担任何法律风险，用户需自行确认字体是否适合商业使用。
- 字体文件较大，下载时请注意网络条件。
- 目前不支持超过 50MB 的字体文件提交。

## 许可证

本项目采用 MIT 许可证。
