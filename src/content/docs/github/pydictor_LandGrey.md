
---
title: pydictor
---

# PyDictor 项目

## 项目地址
[GitHub 项目地址](https://github.com/LandGrey/pydictor/blob/master/README_CN.md)

## 主要特性
PyDictor 是一个纯 Python 实现的密码字典生成与爆破工具，具有以下主要特性：
- **高效生成字典**：支持多种算法和规则生成自定义密码字典，适用于渗透测试和安全研究。
- **多样化规则**：内置多种密码生成模式，包括数字、字母、符号组合，以及常见模式如键盘序列、年份等。
- **多线程支持**：可配置多线程进行字典生成或爆破，提高效率。
- **轻量级**：纯 Python 编写，无需额外依赖，易于部署和使用。
- **自定义性强**：用户可定义生成规则、长度范围和字符集，灵活适应不同场景。

## 主要功能
- **字典生成**：基于规则生成海量密码字典，支持组合、变异和过滤。
- **密码爆破**：集成 Hydra 等工具接口，用于在线/离线密码破解。
- **规则引擎**：内置规则文件，支持加载自定义规则文件进行扩展。
- **输出管理**：生成字典可直接输出到文件，支持进度显示和内存优化。
- **安全研究工具**：用于弱密码检测、字典攻击模拟，不鼓励非法使用。

## 用法
### 安装
1. 克隆仓库：`git clone https://github.com/LandGrey/pydictor.git`
2. 进入目录：`cd pydictor`
3. 无需安装依赖，直接运行 Python 脚本（推荐 Python 3.x）。

### 基本用法
- **生成字典**：  
  `python pydictor.py -l 8 -t 4 -o dict.txt`  
  （生成长度为 8 的字典，使用 4 个线程，输出到 dict.txt）

- **自定义规则**：  
  编辑 `rules/` 目录下的规则文件，然后运行：  
  `python pydictor.py -r custom.rule -s "abc123" -o output.txt`  
  （使用自定义规则，种子 "abc123" 生成字典）

- **爆破模式**：  
  `python pydictor.py -b ssh -t 192.168.1.1 -u admin -d dict.txt`  
  （对 SSH 服务进行爆破，目标 IP 192.168.1.1，用户 admin，使用 dict.txt）

### 高级选项
- `-l`：密码长度（默认 8）。
- `-c`：字符集（数字、字母等）。
- `-n`：生成数量限制。
- `-p`：代理支持（SOCKS 等）。
- 更多选项详见 `python pydictor.py -h` 或 README 文件。

**注意**：本工具仅供合法安全研究使用，请遵守法律法规。