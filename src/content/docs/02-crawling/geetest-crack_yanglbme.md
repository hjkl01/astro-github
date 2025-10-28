
---
title: geetest-crack
---

# Geetest Crack 项目

## 项目地址
[https://github.com/yanglbme/geetest-crack](https://github.com/yanglbme/geetest-crack)

## 主要特性
- **破解Geetest验证码**：该项目专注于破解极验（Geetest）验证码系统，支持多种版本的Geetest验证码，包括滑块验证和行为验证。
- **自动化识别**：使用计算机视觉和机器学习技术自动识别和模拟用户行为，实现验证码的绕过。
- **开源免费**：基于Python开发，完全开源，用户可以自由修改和扩展。
- **高兼容性**：支持集成到各种自动化脚本中，如Selenium WebDriver，用于网页自动化测试和爬虫。

## 主要功能
- **滑块验证码破解**：自动检测滑块位置、计算偏移量，并模拟拖拽操作完成验证。
- **行为验证模拟**：模拟人类鼠标轨迹和点击行为，避免检测为机器人。
- **API接口**：提供简单的API接口，便于与其他工具集成，支持批量处理验证码。
- **错误处理**：内置重试机制和日志记录，帮助用户调试和优化破解过程。
- **多版本支持**：兼容Geetest 3.0和4.0版本的验证码系统。

## 用法
1. **环境准备**：
   - 确保安装Python 3.x环境。
   - 安装依赖：运行 `pip install -r requirements.txt`（假设项目有requirements.txt文件）。

2. **基本使用**：
   - 克隆项目：`git clone https://github.com/yanglbme/geetest-crack.git`。
   - 进入目录：`cd geetest-crack`。
   - 运行示例脚本：`python main.py --url <目标网页URL>`，其中`<目标网页URL>`是包含Geetest验证码的页面。

3. **集成到脚本**：
   - 在Selenium脚本中导入模块：
     ```python
     from geetest_crack import GeetestCracker
     cracker = GeetestCracker()
     result = cracker.solve(gt_challenge, gtlib)  # gt_challenge和gtlib从页面获取
     ```
   - 使用破解结果提交表单。

4. **注意事项**：
   - 项目仅供学习和研究使用，请遵守法律法规，避免用于非法目的。
   - 验证码系统可能更新，需定期检查项目以保持兼容性。