
---
title: rime_wanxiang
---

# rime_wanxiang

**项目地址**  
https://github.com/amzxyz/rime_wanxiang

## 主要特性
- **自定义方案**：提供 `wanxiang.schema.yaml`，支持自由配置拼音/注音/字根等输入方式。  
- **高效字典**：内置多份高频字词库（如 `wanxiang.dict.yaml`、`wanxiang.custom.dict.yaml`），可根据实际使用需求增删。  
- **自动补全与预测**：结合 RIME 的词频模型，实现快速连词补全与智能预测。  
- **多平台支持**：兼容 Windows、Linux、macOS 的 RIME 输入框架。  

## 功能概述
- **拼音/注音输入**：支持标准拼音、双拼、注音方案。  
- **字根/笔画输入**：可按字根、笔画快速查字。  
- **自定义短语**：用户可通过 `wanxiang.custom.dict.yaml` 添加个人常用词组。  
- **词频管理**：RIME 自动记录使用频率，按需调优。  

## 使用方法

1. **下载并复制**  
   ```bash
   git clone https://github.com/amzxyz/rime_wanxiang
   cp -r rime_wanxiang/* ~/.config/rime/
   ```

2. **编辑方案**（可选）  
   - 打开 `~/.config/rime/wanxiang.schema.yaml`  
   - 根据需求修改 `engine`, `translator`, `filter` 等配置。  

3. **重建数据库**  
   - 打开 RIME 输入法，右键点击托盘图标 → `重建数据库`（或在终端执行 `rime -r`）。  

4. **加载方案**  
   - 在 `default.custom.yaml` 或 `default.yaml` 中添加  
     ```yaml
     schema_list:
       - schema: wanxiang
     ```  
   - 重新启动 RIME。  

5. **使用**  
   - 开启输入法，开始输入拼音或注音即可。  
   - 可通过快捷键查看词库或切换输入模式。  

> **提示**：如果出现乱码或加载失败，请确认文件编码为 UTF‑8，且路径无空格。  

---  
**上述步骤可在任何支持 RIME 的环境下完成，适用于日常中文输入。**