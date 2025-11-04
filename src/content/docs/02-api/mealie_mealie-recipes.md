
---
title: mealie
---

**项目地址**  
[https://github.com/mealie-recipes/mealie](https://github.com/mealie-recipes/mealie)

**核心特性与功能**  

| 类别 | 主要功能 |
|------|----------|
| **食谱管理** | • CRUD（新建、读取、更新、删除）食谱<br>• 归类（分类、标签）<br>• 支持图片、视频、步骤视频分段<br>• 自动抓取（Web Scraper）与手动导入（JSON, Markdown, CSV） |
| **营养信息** | • 自动计算每份营养成分（热量、蛋白质、脂肪、碳水化合物）<br>• 支持自定义营养字段 |
| **膳食规划** | • 预设“Meal Plan”日历视图，选择菜品安排日常菜单<br>• 计划视图支持冲突检测与提醒 |
| **购物清单** | • 根据膳食规划自动生成购物清单<br>• 支持合并相同物品、分组（杂货、冷冻、饮料） |
| **多用户 & 权限** | • 用户管理（注册、登录）<br>• 角色：管理员（可管理所有用户）/普通用户（只能管理自己的数据） |
| **API & SDK** | • RESTful API，便于第三方集成（如 Home Assistant、IFTTT）<br>• OpenAPI 文档可在 `/docs` 访问 |
| **部署方式** | • Docker / Docker‑Compose 一键部署<br>• CI/CD 自动构建镜像 |
| **界面** | • 响应式 Web UI（React/Vue/TS）<br>• dark/light 主題，支持自定義 CSS 主题 |
| **备份 & 恢复** | • 支持自动备份数据库（SQLite / PostgreSQL）<br>• GUI 与 CLI 备份工具 |
| **扩展插件** | • 内置插件架构，社区可自行开发插件 |
| **多语言** | • 18+ 语言包（中文、英文、法文、德文…） |
| **安全** | • OAuth2 / JWT 认证、HTTPS 强制、CSRF 保护 |

**快速使用方式**

1. **克隆代码**  
   ```bash
   git clone https://github.com/mealie-recipes/mealie.git
   cd mealie
   ```

2. **本地运行（Docker）**  
   - 安装 Docker 与 Docker‑Compose  
   - 复制 `dev.docker-compose.yml` 并根据需要改动环境变量  
   ```bash
   docker compose -f dev.docker-compose.yml up -d
   ```
   - 访问 `http://localhost:3000`（默认 UI）  
   - 第一次登录使用 `admin` / `123456` 并立即修改密码

3. **手动安装（Python）**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   export FLASK_APP=app.py
   flask run
   ```
   访问 `http://127.0.0.1:5000`。

4. **使用 API**  
   - 生成访问 token（在 UI 的“Profile→API Keys”生成）  
   - 示例请求  
     ```bash
     curl -H "Authorization: Bearer <token>" https://localhost:3000/api/v1/recipes
     ```

5. **定制与扩展**  
   - 将 `config.json` 放在 `resources/` 目录并修改  
   - 使用插件文件夹 `plugins/`，存放自定义插件代码

**常见任务**

| 任务 | 操作 | 说明 |
|------|------|------|
| **添加食谱** | UI → Recipes → Add | 填写标题、材料、步骤、图片等 |
| **批量导入** | CLI → `python import.py <source>` | 支持 `url`, `markdown`, `csv` |
| **生成购物清单** | UI → Meal Planner → Export Shopping List | 甚至可以直接打印或导出 CSV |
| **多用户部署** | 在环境变量 `USERS_FILE` 指定 `users.yaml` | 文件示例：<br>`- username: alice<br>  password: $2b$12$…` |
| **备份数据库** | CLI → `python backup.py` | 输出 `backup.db`，移动至安全位置 |

**维护与贡献**

- 通过 issues & PR 参与社区。  
- 代码遵循 PEP8（Python）与 ESLint（前端）。  
- 自动化脚本位于 `/scripts`，持续集成使用 GitHub Actions。  

这样你即可在本地或服务器上快速搭建 Mealie，享受完整的食谱管理与膳食规划体验。