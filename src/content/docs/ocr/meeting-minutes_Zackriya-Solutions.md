---
title: meeting-minutes
---


# meeting-minutes

项目地址: https://github.com/Zackriya-Solutions/meeting-minutes

## 主要特性
- 支持从 PDF、DOCX、PPTX、TXT 等多种办公文件中提取会议纪要
- 自动识别议程、发言人、时间、决议、待办事项等关键信息
- 生成结构化的 JSON 或 Markdown 记录，便于存档与共享
- 提供命令行工具，支持一次性处理文件夹中的多份会议资料

## 功能概述
1. **文档解析**：利用 Apache POI、PDFBox 等库处理各类型文件  
2. **结构化抽取**：基于正则表达式与 NLP 技术识别并归类会议要点  
3. **输出格式**：可自定义模板，生成符合需求的 Markdown 或 JSON 结果  
4. **CLI 接口**：提供简洁的命令行操作，支持批量转换与日志记录  

## 用法示例
```bash
# 全局安装
npm install -g meeting-minutes

# 解析单个文件
meeting-minutes parse meeting.pdf

# 批量处理文件夹
meeting-minutes parse ./meetings --out ./output

# 按模板生成 Markdown 归档
meeting-minutes generate --template custom.tpl -o archive.md

# 查看帮助
meeting-minutes --help
```

## 运行环境
- Node.js ≥ 14.x  
- npm

## 贡献
欢迎提交 PR 或 issue，遵循项目贡献规范。  
