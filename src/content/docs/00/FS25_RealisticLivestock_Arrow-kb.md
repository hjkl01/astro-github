
---
title: FS25_RealisticLivestock
---

**src/content/docs/00/FS25_RealisticLivestock_Arrow-kb.md**

```markdown
# FS25_RealisticLivestock (Arrow-kb)

**项目地址**  
[https://github.com/Arrow-kb/FS25_RealisticLivestock](https://github.com/Arrow-kb/FS25_RealisticLivestock)

---

## 主要特性
- **真实动物行为**：改进羊、牛、猪等动物的移动、吃草、休息等行为模式，提升沉浸感。  
- **动态健康系统**：动物会因饥饿、受伤、疾病而产生不同表现并影响繁殖与产量。  
- **自然繁殖**：支持交配、怀孕、出生等生命周期过程，模拟真实畜牧业。  
- **逼真声音与纹理**：替换默认音效、贴图，使动物更加生动。  
- **与游戏事件集成**：兼容天气、日夜循环等事件，对动物行为产生连锁反应。  

---

## 功能概览
1. **动物 AI**  
   - 路径寻路、逃跑、跟随主人、群体协作。  
   - 根据饲料类型和稀缺度自动决定觅食路径。  

2. **健康管理**  
   - `Health`, `Stamina`, `Hunger` 三大状态自动调节。  
   - 受伤后可通过“喂药”或“隔离”恢复。  

3. **繁殖逻辑**  
   - 成体交配周期、怀孕天数、产仔数、性别比例随机。  
   - 孵化期间可观看可视化提示。  

4. **事件触发**  
   - 霜冻、雷电等天气会导致动物不适。  
   - 夜间活动强度下降；日间活跃度提升。  

5. **扩展与自定义**  
   - 支持加入自定义动物模型（*e.g.* 外来物种）。  
   - 可通过配置文件调节行为阈值与数值。  

---

## 用法

1. **安装**  
   - 下载并解压 `FS25_RealisticLivestock.zip`。  
   - 放置至 `FS25/Mods` 目录下。  

2. **启动**  
   - 启动 Farming Simulator 25，选择该 Mod，按 F8 开关自定义配置。  

3. **配置**  
   - 在 `mod/version.xml` 中查看 Mod 版本。  
   - 若需自定义动物参数，修改 `mod/config/config.ini`（具体键值请参见官方文档）。  

4. **调试**  
   - 日志文件位于 `FS25/Logs/mods_log.txt`，可查看 AI 行为、错误信息。  

5. **更新**  
   - 访问 GitHub Releases 页面获取最新版本。  

---

> 本说明仅包含核心信息，详细技术实现请参考项目 README 与源码。

