---
title: captcha
---

# Captcha Break 项目

## 项目地址
[GitHub 项目地址](https://github.com/ypwhs/captcha_break)

## 主要特性
- **验证码识别支持**：项目专注于破解多种类型的验证码，包括滑动验证码、图片验证码等，支持AI模型辅助识别。
- **自动化工具**：集成Python脚本和深度学习框架（如TensorFlow或PaddlePaddle），实现高效的验证码绕过或识别。
- **模块化设计**：代码结构清晰，易于扩展，支持自定义验证码类型和识别算法。
- **开源免费**：基于MIT许可，允许用户自由修改和使用。

## 主要功能
- **验证码检测与破解**：自动检测网页上的验证码类型，并使用预训练模型进行识别或模拟破解。
- **集成浏览器自动化**：结合Selenium等工具，实现无头浏览器环境下的验证码处理，支持批量操作。
- **模型训练接口**：提供数据集处理和模型微调功能，用户可根据特定验证码训练自定义模型。
- **API支持**：内置简单API接口，便于与其他自动化脚本或应用集成。

## 用法
1. **环境准备**：
   - 克隆仓库：`git clone https://github.com/ypwhs/captcha_break.git`
   - 安装依赖：`pip install -r requirements.txt`（确保安装Python 3.7+、Selenium、OpenCV等）。

2. **基本使用**：
   - 运行主脚本：`python main.py --url <目标网页URL> --type <验证码类型>`，例如滑动验证码使用`--type slide`。
   - 配置模型：编辑`config.py`文件，设置模型路径和参数。

3. **高级用法**：
   - 训练模型：使用`train.py`脚本加载数据集，进行模型训练：`python train.py --dataset <路径>`。
   - 集成到项目：导入模块，如`from captcha_break import Breaker; breaker = Breaker(); result = breaker.solve(image_path)`。
   - 注意：需遵守法律法规，仅用于合法测试目的，避免用于恶意自动化。