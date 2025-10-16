
---
title: Blasting_dictionary
---

# Blasting_dictionary 项目

## 项目地址
[GitHub 项目地址](https://github.com/rootphantomer/Blasting_dictionary)

## 主要特性
- **字典生成与优化**：项目专注于生成高质量的爆破字典（blasting dictionary），用于渗透测试和安全评估，支持自定义规则和模式匹配，提高字典的针对性和效率。
- **多语言支持**：内置多种语言的词汇库，包括英文、中文等，便于适应不同场景的爆破需求。
- **性能优化**：采用高效算法生成字典，避免冗余，支持并行处理，大幅缩短生成时间。
- **开源与可扩展**：基于Python开发，代码开源，用户可轻松扩展或修改规则以适应特定需求。

## 主要功能
- **字典生成**：根据用户输入的种子词、规则和参数，自动生成爆破字典，支持弱密码、用户名、路径等类型。
- **规则自定义**：允许用户定义替换规则、组合模式和过滤器，确保生成的字典更贴合目标系统。
- **输出格式多样**：支持TXT、CSV等多种输出格式，便于集成到其他工具如Hydra、Burp Suite等。
- **集成工具**：可与常见安全工具结合使用，提供脚本接口简化工作流。

## 用法
1. **安装依赖**：
   - 克隆仓库：`git clone https://github.com/rootphantomer/Blasting_dictionary.git`
   - 进入目录：`cd Blasting_dictionary`
   - 安装Python依赖：`pip install -r requirements.txt`（如果有requirements.txt文件）

2. **基本命令**：
   - 生成简单字典：`python main.py --seed "password" --rules basic --output dict.txt`
     - `--seed`：种子词或基础词汇。
     - `--rules`：指定规则集（如basic、advanced）。
     - `--output`：输出文件路径。

3. **高级用法**：
   - 自定义规则：编辑`rules/`目录下的配置文件，添加替换模式（如将"pass"替换为"pass123"）。
   - 批量生成：使用`--input seeds.txt`从文件中读取多个种子词。
   - 示例：`python main.py --input targets.txt --rules custom_rules.json --min-length 6 --max-length 12 --output advanced_dict.txt`

4. **注意事项**：
   - 项目仅供合法安全测试使用，请遵守相关法律法规。
   - 运行前确保Python 3.x环境，并根据README.md文件查看详细配置。