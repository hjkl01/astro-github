---
title: Blasting
---

# Blasting_dictionary 项目

## 项目地址

[GitHub 项目地址](https://github.com/rootphantomer/Blasting_dictionary)

## 主要特性

- **爆破字典集合**：提供各种类型的爆破字典，包括用户名、密码、路径等，用于安全测试和渗透评估。
- **多类别覆盖**：包含常用英文用户名、奇葩密码、撞库邮箱、目录、美国人字典等多个类别。
- **开源共享**：完全开源，用户可下载和使用，无需安装依赖。

## 主要功能

- **字典下载**：直接下载预生成的字典文件，如 top100password.txt、webshellPassword.txt 等。
- **脚本辅助**：提供 Python 脚本（如 baopo.py）用于生成或扩展字典。
- **多样化内容**：支持不同场景的字典，如 Linux 用户字典、渗透字典等。

## 用法

1. **下载仓库**：
   - 克隆或下载 ZIP：`git clone https://github.com/rootphantomer/Blasting_dictionary.git`

2. **使用字典**：
   - 进入相应文件夹，选择合适的 .txt 文件。
   - 在安全工具中导入，如 Hydra 或 Burp Suite。

3. **生成新字典**：
   - 运行 `python baopo.py` 或 `jiahouzhui.py` 生成自定义字典。

4. **注意事项**：
   - 仅用于合法安全测试，遵守法律法规。
   - 无需安装，纯文件集合。
