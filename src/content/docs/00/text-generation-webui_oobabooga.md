
---
title: text-generation-webui
---


# text-generation-webui（oobabooga）

> 项目地址: <https://github.com/oobabooga/text-generation-webui>

## 项目简介  
`text-generation-webui` 是一个开源的、基于 Web 的前端界面，用于加载、管理和推理各类大语言模型（LLM）。它支持多种模型框架（如 Hugging Face Transformers、Llama.cpp、Exllama 等），并提供 GPU、CPU 以及多种显存优化方案。用户只需通过浏览器即可交互式地完成文本生成、对话、自动补全等任务。

## 主要特性  

| 功能 | 描述 |
|------|------|
| **多模型支持** | 兼容 Hugging Face、Llama.cpp、Exllama、MPT、Phi 等多种模型格式。 |
| **高效推理** | 支持 `transformers`、`exllama`、`llama.cpp` 等后端，可在 GPU 或 CPU 上高效推理。 |
| **Web UI** | 简洁的前端页面，支持多会话、提示管理、模型加载、参数调节。 |
| **多语言** | 默认支持中文、英文、日语等多语言输入与输出。 |
| **可视化参数** | 通过滑块调节 `temperature`、`top_k`、`top_p`、`repeat_penalty` 等生成参数。 |
| **自定义提示** | 支持 Prompt Templates、Prompt Templates Editor。 |
| **插件系统** | 通过 `plugins` 目录可扩展功能，如自定义推理器、数据集加载等。 |
| **多会话** | 同时打开多条对话，独立保存每条会话。 |
| **API 接口** | 同时提供 REST API，可在外部程序中调用。 |
| **轻量化** | 仅需 `requirements.txt` 安装依赖，启动即用。 |

## 功能概览  

1. **模型管理**  
   - 加载本地模型文件夹或 Hugging Face Hub。  
   - 自动识别模型架构并切换后端。  

2. **文本生成**  
   - 单句、段落生成。  
   - 基于会话的连续对话。  
   - 支持 `max_new_tokens`、`stop_sequences` 等高级控制。  

3. **参数调节**  
   - `temperature`、`top_k`、`top_p`、`repetition_penalty`。  
   - `stream`（流式输出），`batch_size`，`torch_dtype` 等。  

4. **插件与扩展**  
   - `plugins` 文件夹下可放置自定义脚本。  
   - 例如 `text-generation-webui/plugins/your_plugin.py`，实现自定义推理后处理。  

5. **多种后端**  
   - 对 `transformers` 支持 `torch`、`bitsandbytes`。  
   - 对 `llama.cpp` 支持 `cpp`、`ggml`、`gptq`。  
   - 对 `exllama` 支持 `exllama`、`exllamav2`。  

6. **API**  
   - POST `/api/v1/generate`：接受 JSON 请求，返回生成文本。  

## 快速开始  

### 1. 克隆仓库  
```bash
git clone https://github.com/oobabooga/text-generation-webui.git
cd text-generation-webui
```

### 2. 安装依赖  
```bash
pip install -r requirements.txt
```

> **提示**：若使用 `llama.cpp` 或 `exllama`，请根据 `docs/INSTALL.md` 额外编译对应后端。

### 3. 运行 Web UI  
```bash
python webui.py
```

- 访问 `http://localhost:5000`（默认端口 5000）。  
- 在 UI 中选择 **Load Model** → **Local**，浏览到模型目录即可加载。  

### 4. 使用 API  
```bash
curl -X POST http://localhost:5000/api/v1/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt":"你好，世界！","max_new_tokens":50}'
```

## 常见操作  

| 操作 | 步骤 |
|------|------|
| **更换模型** | 在 **Load Model** 下选择 **Local** 或 **HF**，输入路径或 Hugging Face 名称后点击 **Load**。 |
| **调整参数** | 在 **Settings** 面板中滑动对应滑块或手动输入数值。 |
| **保存会话** | 点击 **Save** → **Download**，将会话 JSON 下载到本地。 |
| **加载会话** | 点击 **Load** → **Upload**，上传之前下载的 JSON。 |
| **关闭后端** | 在 UI 右上角的 **Shutdown** 按钮，或直接终止 `python webui.py`。 |

## 贡献与交流  

- **Issues**：提交 bug、功能请求。  
- **Pull Requests**：欢迎对后端插件、UI 优化等做贡献。  
- **社区**：Telegram、Discord 频道中有活跃讨论。  

---

> 以上内容已保存为 `src/content/docs/00/text-generation-webui_oobabooga.md`。如需进一步定制，请根据实际需求调整参数或插件。

