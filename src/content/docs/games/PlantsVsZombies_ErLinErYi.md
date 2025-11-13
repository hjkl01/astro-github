---
title: PlantsVsZombies
---

# Plants vs Zombies – ErLinErYi  
**项目地址**: https://github.com/ErLinErYi/PlantsVsZombies  

## 主要特性  
- **完整的 Plants vs Zombies 核心玩法**：玩家在 5×9 的网格上种植植物，利用收集到的阳光（Sun）来抵御不断进攻的僵尸。  
- **多种植物与僵尸**：包括向日葵、豌豆射手、坚果墙、冰冻射手等植物，以及普通僵尸、快步僵尸、重装僵尸、爆炸僵尸等。  
- **关卡系统**：预设多波僵尸进攻，支持自定义关卡配置。  
- **计分与排行榜**：游戏结束后显示分数，并可记录最高分。  
- **音效与动画**：包含植物种植、阳光掉落、僵尸移动、攻击等动画与音效。  
- **UI 与交互**：简洁的 UI，支持鼠标点击与拖拽操作。  

## 功能模块  
| 模块 | 说明 | 主要脚本 |
|------|------|----------|
| **Grid** | 网格管理（生成格子、占用检测） | `GridManager.cs` |
| **Plant** | 植物基类与具体实现 | `BasePlant.cs`, `Sunflower.cs`, `Peashooter.cs`, `Wallnut.cs`, `IcePeashooter.cs` |
| **Zombie** | 僵尸基类与具体实现 | `BaseZombie.cs`, `NormalZombie.cs`, `FastZombie.cs`, `CannonZombie.cs`, `CactusZombie.cs` |
| **Sun** | 阳光掉落与收集 | `Sun.cs` |
| **GameManager** | 游戏状态、计分、波次管理 | `GameManager.cs` |
| **UI** | 主界面、分数、按钮 | `UIManager.cs`, `ScoreText.cs` |
| **Audio** | 音效播放 | `AudioManager.cs` |

## 用法  

1. **克隆仓库**  
   ```bash
   git clone https://github.com/ErLinErYi/PlantsVsZombies.git
   cd PlantsVsZombies
   ```

2. **打开 Unity**  
   - 需要 Unity 2021.3 或更高版本。  
   - 直接双击 `PlantsVsZombies/PlantsVsZombies.unity` 打开项目。  

3. **运行游戏**  
   - 在 Unity 编辑器中点击 **Play**。  
   - 或者构建后生成可执行文件（File → Build Settings → Build）。  

4. **自定义**  
   - 关卡配置文件位于 `Assets/Resources/Levels/`，可自行添加 JSON 关卡。  
   - 植物与僵尸可在 `Assets/Scripts/Plants/` 与 `Assets/Scripts/Zombies/` 中扩展。  

5. **调试**  
   - Unity 控制台会输出游戏状态日志，方便调试。  

> 该项目为学习与演示用途，已在 Windows 平台下完成测试。若需移植到其他平台，请根据 Unity 文档进行相应设置。