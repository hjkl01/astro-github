
---
title: system_prompts_leaks
---


# system_prompts_leaks

**项目地址**: https://github.com/asgeirtj/system_prompts_leaks

## 项目简介
`system_prompts_leaks` 是一个用于检测、分析和管理大型语言模型（LLM）系统提示（system prompts）泄露风险的工具库。它通过预定义的规则集和可扩展的检测引擎，帮助开发者快速定位系统提示中可能泄露敏感信息的模式，并提供相应的修复建议。

## 主要特性
- **自动化检测**：扫描系统提示文本，识别常见泄露模式（如包含个人身份信息、敏感指令或内部逻辑泄露）。
- **可扩展规则引擎**：支持自定义正则表达式、关键词列表或深度学习模型，满足不同场景需求。
- **报告生成**：输出可视化报告（Markdown / JSON / HTML），便于后期审计与合规检查。
- **CLI 与 API**：提供命令行工具和 Python API，适配 CI/CD 流程与自动化脚本。
- **示例与模板**：附带一套常见系统提示示例和安全最佳实践模板，帮助快速上手。

## 功能模块
| 模块 | 说明 |
|------|------|
| `scanner` | 负责读取系统提示文件，执行检测规则，返回匹配结果。 |
| `rules` | 规则集合，支持正则、关键词、深度学习三种检测方式。 |
| `reporter` | 负责格式化检测结果，生成 Markdown / JSON / HTML 报告。 |
| `cli` | 命令行接口，支持批量扫描、规则管理、报告导出等操作。 |
| `api` | Python API，方便在项目中嵌入检测逻辑。 |

## 用法

### 1. 安装
```bash
pip install system-prompts-leaks
```

### 2. 命令行使用
```bash
# 扫描单个文件
system-prompts-leaks scan path/to/system_prompt.txt

# 扫描目录
system-prompts-leaks scan path/to/prompts_dir/ --report markdown --output report.md

# 添加自定义规则
system-prompts-leaks rule add custom_rule.yaml
```

### 3. Python API
```python
from system_prompts_leaks import Scanner, Reporter

scanner = Scanner(rules_path="rules.yaml")
results = scanner.scan("system_prompt.txt")

report = Reporter(format="markdown")
report.generate(results, output_path="report.md")
```

### 4. 集成到 CI
```yaml
# .github/workflows/lint-prompts.yml
name: Prompt Lint
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install SDK
        run: pip install system-prompts-leaks
      - name: Run prompt scan
        run: system-prompts-leaks scan prompts/ --report json --output prompt_report.json
      - name: Upload report
        uses: actions/upload-artifact@v4
        with:
          name: prompt-report
          path: prompt_report.json
```

## 贡献

欢迎提供新的检测规则、改进报告格式或修复已知问题。请提交 Pull Request 并遵循项目的贡献指南。

---

> **提示**：在使用过程中如遇到敏感信息泄露，建议立即排查并更新相应提示内容或规则。
