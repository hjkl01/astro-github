
---
title: VoiceInk
---

# VoiceInk（Beingpax）  
> GitHub 地址：<https://github.com/Beingpax/VoiceInk>

---

## 主要特性
- **语音驱动绘画**：使用麦克风实时捕获语音，将其转化为文字 Prompt 并输入 AI 绘图模型，完成“一语成图”体验。  
- **高质量 AI 生成**：默认调用 OpenAI/Claude / Stable Diffusion 等模型，支持自定义模型与参数。  
- **画布交互**：生成图像后可在浏览器中查看、保存、下载。  
- **历史记录**：支持本地或云端保存生成记录，便于回溯与分享。  
- **多语言支持**：内置中文、英文等语音识别与翻译。  

## 功能说明
| 功能 | 说明 |
|------|------|
| 语音识别 | 通过 Web Speech API 或后台 Whisper，将语音实时转为文字。 |
| Prompt 生成 | 自动完成 Prompt 结构（风格、材质、光照等），可在文本框手动编辑。 |
| AI 绘图 | 通过 API 请求生成图像，支持即时预览与大图下载。 |
| 参数调节 | 可调节 CFG Scale、图片尺寸、风格强度等参数。 |
| 结果管理 | 本地缓存、收藏夹、分享链接、复制图片链接等。 |
| 多终端适配 | 兼容桌面浏览器与移动端。 |

## 快速使用
1. **安装依赖**  
   ```bash
   git clone https://github.com/Beingpax/VoiceInk.git
   cd VoiceInk
   npm i   # 或者用 yarn install
   ```

2. **配置 API Key**  
   在根目录创建 `.env` 文件并填入  
   ```
   OPENAI_API_KEY=你的OpenAI或Claude API Key
   FACEVAL_API_KEY=（可选）其他AI模型Key
   ```

3. **启动项目**  
   ```bash
   npm run dev
   ```
   浏览器访问 <http://localhost:5173>（默认端口 5173）。

4. **使用流程**  
   - 打开页面后点击 *语音* 按钮，授权麦克风。  
   - 说出你想生成的图像描述，系统会实时转为文本并点击 *生成* 按钮。  
   - 查看右侧画布中的生成结果，点击 *保存* 或 *下载* 按钮获取本地图像。  
   - 利用左侧面板调节参数或编辑 Prompt，重新生成。

5. **部署**  
   ```bash
   npm run build   # 构建生产版本
   # 你可以将 dist 文件夹部署到任何静态托管服务（GitHub Pages, Netlify, Vercel 等）
   ```

## 常见问题
- **语音识别不准确**：可尝试更换浏览器或调整麦克风质量。  
- **图像生成失败**：检查 API Key 是否正确或网络通畅。  
- **想更换 AI 模型**：在 `src/config.js` 里修改 `modelName` 和相关参数。

## 贡献
欢迎 Issue 与 PR，详细流程请参考 `CONTRIBUTING.md`。

--- 

> 以上即为 VoiceInk 项目的核心特性、功能与使用方法概要，已完全按需求保留在 Markdown 文件 `src/content/docs/00/VoiceInk_Beingpax.md` 内。