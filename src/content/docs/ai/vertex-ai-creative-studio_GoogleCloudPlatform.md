---
title: vertex-ai-creative-studio
---

# Vertex AI Creative Studio

## 项目简介

Vertex AI Creative Studio（GenMedia Creative Studio）是一个展示Google Cloud Vertex AI生成媒体能力的Web应用程序。它利用Imagen、Veo、Gemini、Gemini TTS、Chirp 3、Lyria等生成媒体API，为创意探索和灵感提供平台。

## 主要功能

### 图像生成

- **Imagen 3 & Imagen 4**：先进的图像生成模型
- **Virtual Try-On**：虚拟试穿功能
- **Gemini 2.5 Flash Image Generation**：快速图像生成

### 视频生成

- **Veo 2 & Veo 3**：高质量视频生成

### 音乐生成

- **Lyria**：AI音乐创作工具

### 语音生成

- **Chirp 3 HD**：高清语音合成
- **Gemini Text to Speech**：文本转语音

### 创意工作流

- **Character Consistency**：角色一致性维护
- **Shop the Look**：购物外观匹配
- **Starter Pack Moodboard**：入门包情绪板
- **Interior Designer**：室内设计助手

### 资产库

- 存储和管理生成的媒体资产

## 实验功能

项目还包含实验文件夹，提供各种独立应用程序和新功能，包括：

- MCP Tools：为Veo、Imagen、Lyria、Chirp和Gemini提供Model Context Protocol服务器
- 组合工作流：倒计时视频、故事板生成等
- 提示优化工具：Promptlandia、Veo遗传提示优化器
- 图像分析：虚拟试穿、产品重新语境化
- 音频视频：创意播客助手、Babel等

## 部署方式

### 前置条件

- Google Cloud项目
- 如果使用自定义域名，需要DNS A记录创建权限

### 环境变量设置

```bash
export REGION=us-central1
export PROJECT_ID=$(gcloud config get project)
export INITIAL_USER=admin@example.com
```

### 部署选项

#### 1. 自定义域名部署

适用于需要外部身份支持或自定义域名的场景。

步骤：

1. 设置域名环境变量：`export DOMAIN_NAME=creativestudio.example.com`
2. 初始化Terraform：`terraform init`
3. 创建terraform.tfvars文件
4. 应用Terraform配置：`terraform apply`
5. 创建DNS A记录指向负载均衡器IP
6. 构建和部署：`./build.sh`
7. 等待证书配置完成

#### 2. Cloud Run域名部署

适用于无法创建DNS记录的场景。

步骤：

1. 创建terraform.tfvars（设置use_lb=false）
2. 初始化和应用Terraform
3. 构建和部署容器
4. 配置IAP策略添加用户访问权限

#### 3. Cloud Shell测试部署

快速测试使用Cloud Shell运行UI。

## 开发环境设置

### Python虚拟环境

使用uv包管理器：

```bash
uv sync
```

### 环境变量

创建.env文件，设置PROJECT_ID等变量。

### 运行应用

```bash
uv run main.py
```

## 注意事项

- 这不是官方支持的Google产品
- 不适用于生产环境
- 推荐使用Google Chrome浏览器
- 代码基于Apache 2.0许可证

## 贡献

欢迎提交问题和拉取请求。详情请见CONTRIBUTING.md。
