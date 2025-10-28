
---
title: MoneyPrinterTurbo
---

# MoneyPrinterTurbo (harry0703)

**项目地址**  
<https://github.com/harry0703/MoneyPrinterTurbo>

## 主要特性

- **快速打印货币**：一次调用即可生成任意数量的游戏内货币。  
- **支持多种货币类型**：默认提供美元、欧元、比特币等多种货币，可自定义扩展。  
- **可配置的分配策略**：支持随机分配、固定金额、分批分配等多种策略，满足不同游戏需求。  
- **事件回调机制**：在货币生成、分配完成后触发事件，方便与游戏逻辑进行联动。  
- **轻量封装**：仅 20KB 代码，易于集成到任何 Unity/C# 项目。  
- **安全隐蔽**：内部使用随机化与加密，防止被外部工具直接识别与干扰。  

## 功能概览

| 功能 | 简述 |
|------|------|
| `MoneyPrinter.Print(amount)` | 直接打印指定金额的货币。 |
| `MoneyPrinter.PrintBatch(count, amount)` | 分批打印多笔货币，支持自定义批次数量。 |
| `MoneyPrinter.RegisterCallback(Action callback)` | 注册货币生成完成后的回调。 |
| `MoneyPrinter.SetCurrencyType(CurrencyType type)` | 切换当前使用的货币类型。 |
| `MoneyPrinter.GetTotal()` | 获取当前已打印的总金额。 |
| `MoneyPrinter.Clear()` | 清空已打印的所有货币（仅用于调试）。 |

## 用法

1. **引入库**  
   将 `MoneyPrinterTurbo.dll` 拖入 Unity 项目 Assets 目录，或在 .NET 项目中使用 NuGet 包管理器安装。

2. **初始化**  
   ```csharp
   using MoneyPrinterTurbo;

   // 可选：设置货币类型
   MoneyPrinter.SetCurrencyType(CurrencyType.Dollar);
   ```

3. **打印货币**  
   ```csharp
   // 打印 1000 元
   MoneyPrinter.Print(1000);

   // 分批打印 5 份，每份 200 元
   MoneyPrinter.PrintBatch(5, 200);
   ```

4. **监听事件**  
   ```csharp
   MoneyPrinter.RegisterCallback(() =>
   {
       Debug.Log("货币已成功打印");
   });
   ```

5. **查询与清理**  
   ```csharp
   int total = MoneyPrinter.GetTotal();
   Debug.Log($"当前总金额: {total}");

   // 如需重置
   MoneyPrinter.Clear();
   ```

> **提示**：在正式发布前建议在调试环境下多次测试，确保货币生成逻辑与游戏经济系统兼容。

## 结语

MoneyPrinterTurbo 为游戏开发者提供了一套简洁、高效、可扩展的货币打印解决方案。无论是快速原型验证还是正式上线，都能帮助你专注于游戏玩法而非底层实现。