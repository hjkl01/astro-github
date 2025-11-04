
---
title: AFFiNE
---


# AFFiNE by toeverything

项目地址: [https://github.com/toeverything/AFFiNE](https://github.com/toeverything/AFFiNE)

## 主要特性

- **多文档协作**：支持多人同时编辑同一项目，实时保存与同步。
- **知识图谱**：将文档、笔记、网页等多种内容统一到可视化关系图中，方便快速定位。
- **内嵌式数据库**：把笔记、表格、日历等结构化内容转成可查询、可关联的数据表。
- **模组化编辑器**：支持块级编辑，直接插入表格、代码块、引用、链接等标准模式。
- **本地与云端存储**：可选同步到多种云端（GitHub, Notion, Prisma、MongoDB 等）或仅使用本地存储。
- **可拓展插件**：基于 Web组件、TypeScript 的插件生态，支持自定义工具与样式。
- **跨平台**：桌面客户端（Electron）、Web、移动端（iOS/Android）一套代码覆盖。

## 关键功能

1. **文档与笔记**  
   - 支持 Markdown 语法，实时预览。  
   - 内部链接、引用和双向链接，实现知识网络。

2. **表格与数据库**  
   - 高度可配置的二维表格。  
   - 可以链接到其他块，形成一体化的关系数据库。

3. **日历与任务**  
   - 附带日历视图与任务列表，支持提醒与事件关联。

4. **插件与 API**  
   - 通过 AFFiNE 插件 SDK 可开发自定义功能。  
   - 提供 REST/GraphQL API 供外部系统集成。

5. **导入与导出**  
   - 支持直接导出为 Markdown、PDF、Word、HTML 等格式。  
   - 可以导入本地 Markdown、Notion、Evernote 等数据。

6. **版本与回滚**  
   - 每次保存会生成快照，支持回滚到历史版本。

7. **多语言与国际化**  
   - 支持多语言 UI，方便全球使用。

## 用法指南

1. **安装**  
   ```bash
   npm i @affine/protocol   # 选用包管理
   ```
   或者通过 `electron` 客户端下载官方发行版。

2. **启动**  
   ```bash
   affiNE start
   ```
   或启动 Web 预览：`affiNE preview`.

3. **创建工作区**  
   - 在主界面点击**New Workspace**  
   - 选择存储方式（本地目录或云端）  
   - 输入名称，选择模板（空白、笔记本、知识库等）

4. **编辑与导航**  
   - 左侧树形导航管理页面。  
   - 右侧边栏可开启**知识图谱**视图。  
   - 可使用快捷键：`Ctrl + /` 调出命令面板；`Ctrl + G` 跳转至页面。

5. **同步与协作**  
   - 打开页面右上角的 **Sync** 按钮，选择同步方式（GitHub, GitLab, Gitea 或者自主服务器）。  
   - 在 **Team Settings** 添加成员，设置权限。

6. **插件管理**  
   - 在 **Extensions** 页面搜索并安装插件。  
   - 进入 **Developer** → **New Plugin** 开发自定义功能。

7. **导入内容**  
   - 打开**Import**，选择文件类型（Markdown, Notion 导出等）  
   - 系统会分析并拆拆块，导入为 AFFiNE 页面结构。

8. **导出内容**  
   - 在页面右上角点击 **Export** → 选择格式（Markdown, PDF, HTML 等）  
   - 也可通过命令行批量导出：`affiNE export --format=pdf`.

9. **使用 API**  
   - 在后端启动 AFFiNE API 服务后，使用 GraphQL 查询文档、数据库等。  
   - 示例：  
     ```graphql
     query {
       workspace(id: "w1") {
         pages {
           id
           title
           blocks {
             id
             type
             content
           }
         }
       }
     }
     ```

10. **社区与支持**  
    - 官方文档: https://docs.affine.pro  
    - 讨论区: https://github.com/toeverything/AFFiNE/discussions  
    - Issue: https://github.com/toeverything/AFFiNE/issues

> **提示**：AWIN 采用 [Electron](https://www.electronjs.org/) 构建桌面端，前端使用 TS + Lit + CSF，后端是基于 Warp Rust 框架的 REST/GRPC。若有深度二次开发需求，可关注其 [SDK 文档](https://github.com/toeverything/AFFiNE/tree/dev/sdk)。

---

> 以上信息为快速参考，详细功能与 API 可见官方仓库及文档。祝使用愉快！
