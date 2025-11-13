---
title: n8n-workflows
---

# n8n-workflows

n8n-workflows 是 n8n 自动化工作流的终极集合，包含 4,343 个生产就绪的工作流和 365 个独特集成。

## 功能特性

- **大规模工作流集合**：超过 4,000 个预构建的工作流，涵盖各种自动化场景
- **智能搜索**：支持按名称、描述和节点进行全文搜索
- **分类浏览**：按 15+ 个类别组织，包括营销、销售、DevOps 等
- **在线访问**：无需安装即可在 [zie619.github.io/n8n-workflows](https://zie619.github.io/n8n-workflows) 上浏览和下载
- **本地部署**：支持 Python 和 Docker 部署
- **高性能**：SQLite FTS5 提供 <100ms 的搜索响应
- **移动友好**：响应式设计，支持任何设备

## 使用方法

### 在线使用（推荐）

1. 访问 [zie619.github.io/n8n-workflows](https://zie619.github.io/n8n-workflows)
2. 使用搜索框查找所需工作流
3. 按类别或复杂度筛选
4. 直接下载 JSON 文件导入到 n8n 中

### 本地安装

#### 前置要求

- Python 3.9+
- pip
- 100MB 磁盘空间

#### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/Zie619/n8n-workflows.git
cd n8n-workflows

# 安装依赖
pip install -r requirements.txt

# 启动服务器
python run.py

# 在浏览器中打开 http://localhost:8000
```

### Docker 部署

```bash
# 使用 Docker Hub 镜像
docker run -p 8000:8000 zie619/n8n-workflows:latest

# 或本地构建
docker build -t n8n-workflows .
docker run -p 8000:8000 n8n-workflows
```

## API 接口

- `GET /` - Web 界面
- `GET /api/search` - 搜索工作流
- `GET /api/stats` - 仓库统计
- `GET /api/workflow/{id}` - 获取工作流 JSON
- `GET /api/categories` - 列出所有类别
- `GET /api/export` - 导出工作流

## 技术栈

- 后端：Python, FastAPI, SQLite with FTS5
- 前端：Vanilla JS, Tailwind CSS
- 部署：Docker, GitHub Actions, GitHub Pages
- 安全：Trivy 扫描, CORS 保护, 输入验证

## 许可证

MIT License
