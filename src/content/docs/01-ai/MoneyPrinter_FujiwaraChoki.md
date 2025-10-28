
---
title: MoneyPrinter
---

# MoneyPrinter

GitHub地址: <https://github.com/FujiwaraChoki/MoneyPrinter>

## 项目简介
**MoneyPrinter** 是一个轻量级、跨平台的 C#/.NET 库，专为在程序中动态生成各种货币（主要是日元、美元、欧元等）模拟纸张印刷效果而设计。它提供了直观的 API 与命令行工具，支持自定义金额、纸张尺寸、模板、字体与水印等多种高级特性，可用于电子票据生成、动画演示、游戏资产制作等场景。

## 主要特性
| 功能 | 说明 |
|------|------|
| **多货币支持** | 支持日元、美元、欧元、人民币等主流货币，金额自动补齿与小数位控制。 |
| **多格式输出** | 以 PDF、PNG、SVG 或位图流形式输出，满足不同平台需求。 |
| **自定义模板** | 以 XML/JSON/手绘图形等方式定义纸张排版、文字位置、印章位置。 |
| **水印与签名** | 可插入企业水印、用户签名图片，保持版式完整。 |
| **CLI 与 API 并存** | 命令行工具适合批处理脚本；API 方便手写代码直接调用。 |
| **高性能渲染** | 使用 SkiaSharp / PdfSharp 等现代渲染库，对大批量生成支持压缩与并发。 |
| **跨平台** | 兼容 .NET Core / .NET 5/6/7，支持 Windows、Linux、macOS。 |

## 核心 API
```csharp
using MoneyPrinter;

// 创建打印器实例
var printer = new MoneyPrinterCore();

// 配置图像参数
var config = new PrintConfig
{
    Currency = Currency.JPY,          // 货币类型
    Amount = 12345.67M,               // 金额
    PaperSize = PaperSize.A5,         // 纸张尺寸
    Template = "default.xml",         // 模板文件
    FontPath = "Arial.ttf",           // 字体文件
    WatermarkPath = "logo.png"        // 水印图片
};

// 输出PDF并保存
var pdfBytes = printer.RenderToPdf(config);
File.WriteAllBytes("output.pdf", pdfBytes);

// 输出PNG
var pngBytes = printer.RenderToPng(config);
File.WriteAllBytes("output.png", pngBytes);
```

## 命令行使用
```bash
# 安装工具（全局或项目中）
dotnet tool install -g MoneyPrinter.Tool

# 生成 PDF
moneyprinter --amount 9876.54 --currency USD --output revenue.pdf

# 生成 PNG（自定义模板）
moneyprinter --template custom.xml --output receipt.png
```

## 快速上手
1. **安装依赖**  
   ```bash
   dotnet add package MoneyPrinter
   ```

2. **创建配置文件**（example.xml）  
   ```xml
   <Template>
       <Paper width="210" height="297" unit="mm" />
       <Text field="amount" fontSize="48" position="(100,150)" />
       <Image name="watermark" source="logo.png" position="(180,260)" />
   </Template>
   ```

3. **代码示例**  
   ```csharp
   var printer = new MoneyPrinterCore();
   var result = printer.Render("example.xml", new { amount = "¥12,345" });
   File.WriteAllText("receipt.svg", result);
   ```

4. **运行**  
   ```bash
   dotnet run --project MoneyPrinter.Samples
   ```

## 开发与贡献
- 代码仓库采用 MIT 许可，欢迎提交 Issue 与 Pull Request。
- 文档与 API 示例已集成至 **docs/** 目录，生成网站请运行  
  ```bash
  dotnet swagger to-file <dll> api.json
  ```

> **提示**：若想自定义模板语法，请参阅 `docs/template-spec.md`。

---

**链接**: <https://github.com/FujiwaraChoki/MoneyPrinter>