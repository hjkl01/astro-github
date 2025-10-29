
---
title: label-studio
---


# Label‑Studio by HumanSignal

> **GitHub 地址**: https://github.com/HumanSignal/label‑studio

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **多模态标注** | 支持文本、图片、音频、视频、PDF、表格等多种数据类型。 |
| **自定义 UI** | 通过 JSON 定义任务 UI，支持多种标签类型（文本框、单选/多选、时间轴、边框框选等）。 |
| **模型驱动** | 内置或自定义机器学习模型预标注、智能纠错，提升标注效率。 |
| **协作与权限** | 角色管理（管理员、标注者、查看者），任务分配、进度跟踪。 |
| **导入/导出** | 支持 CSV、JSON、XLSX、Label Studio Format 等多种格式；API 可直接读取/写入结果。 |
| **插件与扩展** | 插件体系可接入外部服务（如 AWS S3、Azure Blob、Google Cloud Storage 等）。 |
| **Docker 与 Cloud** | 官方 Docker 镜像、K8s 部署，亦可在 AWS、GCP、Azure 上快速启动。 |
| **RESTful API** | 完整的 HTTP API，方便与现有工作流、CI/CD、ML Pipelines 集成。 |
| **多语言与多租户** | UI 本地化，支持多租户部署。 |

---

## 核心功能

1. **项目创建** – 定义标注任务、数据源、标签类型、导出格式。  
2. **任务分配** – 自动或手动将任务分发给标注者。  
3. **数据浏览** – 支持分页、搜索、筛选，快速定位目标样本。  
4. **标注编辑** – 可撤销、恢复、批量操作；支持缩放、裁剪、旋转等图像/视频工具。  
5. **质量控制** – 交叉验证、抽样审核、指标监控。  
6. **模型集成** – 通过 `label-studio[ml]` 直接调用 TensorFlow、PyTorch、Hugging Face 等模型。  
7. **导出报告** – 生成 CSV/JSON/Excel/Swagger 等格式，供后续分析或训练。  

---

## 快速上手

### 1. 安装

```bash
# 直接安装
pip install label-studio

# 或使用 Docker
docker run -it -p 8080:8080 -v /path/to/data:/data heartexlabs/label-studio
```

### 2. 启动服务

```bash
label-studio start
```

访问 `http://localhost:8080` 创建第一个项目。

### 3. 创建项目

1. 登录后点击 **Create Project**。  
2. 选择数据源（文件夹、数据库、API）或上传文件。  
3. 通过 **Labeling Interface** JSON 定义 UI。  
4. 配置 **Export Format** 与 **Permissions**。  

### 4. 标注

- 在任务列表中选择样本，使用 UI 进行标注。  
- 可使用 **Hotkeys**（`Ctrl+Z` 撤销，`Ctrl+Shift+Z` 恢复）。  
- 标注完成后，点击 **Save**。

### 5. 导出结果

在项目页面点击 **Export**，选择格式并下载文件。  
或使用 API：

```bash
curl -X GET "http://localhost:8080/api/projects/1/export?format=csv" \
     -H "Authorization: Token YOUR_TOKEN"
```

### 6. 与 ML 集成

```bash
pip install label-studio[ml]
label-studio ml register my-model --api-key=YOUR_KEY
```

然后在项目中启用模型预标注。

---

## 参考文档

- 官方 GitHub 仓库: https://github.com/HumanSignal/label-studio  
- 文档与教程: https://labelstud.io/guide/  
- API 说明: https://labelstud.io/api  
- Docker 镜像: https://hub.docker.com/r/labelstudios/label-studio  

---

> 以上内容即为 **label‑studio** 的核心特性、功能与使用指南。请将本文件保存为 `src/content/docs/00/label-studio_HumanSignal.md`。