
---
title: ComfyUI-WanVideoWrapper
---


# ComfyUI-WanVideoWrapper

[GitHub 项目地址](https://github.com/kijai/ComfyUI-WanVideoWrapper)

## 主要特性

- **视频包装功能**  
  将视频文件（`.mp4`、`.mov`、`.webm` 等）拆分为帧，作为多维张量输入到 ComfyUI 图形化工作流中；同样支持将输出帧重新合成为视频。

- **高效批处理**  
  内置多线程读取与写入，支持大尺寸视频的快速预处理与后期渲染，显著降低内存占用。

- **多种视频处理节点**  
  - `VideoLoader`：加载视频，返回帧序列张量。  
  - `VideoSaver`：将帧序列张量保存为视频文件。  
  - `VideoResizer`：按比例或固定尺寸重塑视频帧。  
  - `VideoCropper`：裁剪视频帧到指定区域。  
  - `VideoFrameSplitter`：将视频拆分为单帧图像。  
  - `VideoFrameMerger`：将单帧图像合并为视频。  

- **与 ComfyUI 原生节点无缝集成**  
  可与 Diffusion 模型、图像编辑节点、调色节点等直接拼接，实现一键视频到图像再到视频的完整流水线。

## 功能实现

- 使用 `ffmpeg-python` 进行视频 I/O，保证兼容大多数视频格式。  
- 通过 `torchvision.transforms` 进行视频尺度、裁剪操作。  
- 节点框架遵循 ComfyUI 的 `BaseNode` 规范，支持自定义图形化界面。  
- 采用 `torch.tensor` 存储帧序列，便于后续 GPU 加速处理。  

## 用法说明

1. **安装插件**  
   将插件文件夹 `ComfyUI-WanVideoWrapper` 拖放到 `ComfyUI/custom_nodes/` 目录下，重启 ComfyUI 即可加载。

2. **加载视频**  
   ```json
   {
     "id": 1,
     "type": "VideoLoader",
     "inputs": {
       "filepath": "./input/sample.mp4",
       "fps": 30,
       "normalize": true
     }
   }
   ```

3. **在工作流中插入图像处理节点**  
   (例如 Stable Diffusion)  
   ```json
   {
     "id": 2,
     "type": "StableDiffusionVAE",
     "inputs": {
       "latents": 1,
       "prompt": "a futuristic cityscape"
     }
   }
   ```

4. **保存视频**  
   ```json
   {
     "id": 3,
     "type": "VideoSaver",
     "inputs": {
       "frames": 2,
       "filepath": "./output/edited.mp4",
       "fps": 30,
       "codec": "libx264",
       "crf": 18
     }
   }
   ```

5. **完整工作流示例（JSON）**  
   ```json
   {
     "1": {
       "type": "VideoLoader",
       "inputs": {"filepath": "./input/sample.mp4", "fps": 30, "normalize": true}
     },
     "2": {
       "type": "VideoResizer",
       "inputs": {"input_frames": 1, "size": [512, 512]}
     },
     "3": {
       "type":StableDiffusionVAE",
       "inputs": {"latents": 2, "prompt": "abstract art"}
     },
     "4": {
       "type": "VideoSaver",
       "inputs": {"frames": 3, "filepath": "./output/awesome.mp4", "fps": 30}
     },
     "connections": [
       {"src": 1, "dst": 2},
       {"src": 2, "dst": 3},
       {"src": 3, "dst": 4}
     ]
   }
   ```

6. **命令行示例**  
   ```bash
   python main.py --prompt "cat surfing a wave" --model_path ./models/StableDiffusion/
   ```

> **提示**：由于视频帧数可能非常大，请根据显存情况选择是否使用 `normalize` 或者先做 `VideoResizer`。

## 文档与支持

- 访问项目 GitHub 页面查看完整说明与使用案例。  
- 如遇到兼容性问题，可在 `issues` 上提交，作者会在下一次发布中进行修复。  

--- 

**文件路径**: `src/content/docs/00/ComfyUI-WanVideoWrapper_kijai.md`   
**内容已以 markdown 格式提供。```
