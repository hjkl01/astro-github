---
title: ScottPlot
---

# ScottPlot 项目

**项目地址:** [https://github.com/ScottPlot/ScottPlot](https://github.com/ScottPlot/ScottPlot)

## 主要特性
ScottPlot 是一个免费开源的 .NET 图表库，专为科学和工程应用设计。它支持多种图表类型，包括线图、散点图、柱状图、热图、填充图等，提供高性能的绘图功能。库的核心特性包括：
- **跨平台支持**：兼容 Windows、macOS 和 Linux，支持 .NET Framework、.NET Core 和 .NET 5+。
- **简单易用**：API 设计直观，允许快速创建专业级图表。
- **高性能**：使用高效的渲染引擎，支持大规模数据集的实时绘图。
- **交互性**：内置缩放、平移、数据点拾取和工具提示等交互功能。
- **自定义性**：支持主题、颜色、标签和轴设置的全面自定义。
- **无外部依赖**：纯 .NET 实现，不依赖第三方库如 WinForms 或 WPF（但可集成）。

## 主要功能
- **图表类型**：支持 2D 绘图，包括信号图（Signal Plot）、散点图（Scatter Plot）、台阶图（Step Plot）、柱状图（Bar Plot）、蜡烛图（Finance Plot）、热图（Heatmap）等。还包括统计图如箱线图（Box Plot）和直方图（Histogram）。
- **轴和刻度**：自动或手动配置 X/Y 轴，支持日期时间轴、对数轴和自定义刻度。
- **数据处理**：内置数据插值、平滑和统计计算功能。
- **导出与集成**：可导出为 PNG、SVG、PDF 等格式；易于集成到 WinForms、WPF、Avalonia 或 ASP.NET 等 UI 框架中。
- **高级功能**：支持多面板布局（Multi-Plot）、动画和实时更新，适用于数据可视化、科学模拟和仪表盘应用。

## 用法
### 安装
通过 NuGet 包管理器安装：
```
Install-Package ScottPlot
```
或在项目文件中添加：
```xml
<PackageReference Include="ScottPlot" Version="5.0.36" />
```

### 基本用法示例（C#）
1. **创建简单线图**（WinForms 示例）：
   ```csharp
   using ScottPlot;

   public partial class Form1 : Form
   {
       public Form1()
       {
           InitializeComponent();
           var plt = new ScottPlot.Plot(400, 300);
           double[] xs = { 1, 2, 3, 4 };
           double[] ys = { 1, 4, 2, 3 };
           plt.Add.Scatter(xs, ys);
           plt.SavePng("plot.png");
           formsPlot1.Plot = plt;  // 如果使用 FormsPlot 控件
       }
   }
   ```

2. **添加交互控件**（WPF 示例）：
   ```csharp
   using ScottPlot.WPF;

   // 在 XAML 中添加 <scottplot:WpfPlot x:Name="MyPlot" />
   // 在代码中：
   double[] dataX = Generate.Consecutive(1, 1000);
   double[] dataY = Generate.Sin(100);
   MyPlot.Plot.Add.Scatter(dataX, dataY);
   MyPlot.Plot.Title("Sine Wave");
   MyPlot.Plot.XLabel("Sample");
   MyPlot.Plot.YLabel("Amplitude");
   MyPlot.Refresh();
   ```

3. **高级自定义**：
   - 设置轴限制：`plt.Axes.SetLimits(xMin, xMax, yMin, yMax);`
   - 添加图例：`plt.Legend.IsVisible = true;`
   - 实时更新：使用 `plt.Refresh()` 在循环中更新数据。

更多示例和文档请参考项目仓库的 [Examples](https://github.com/ScottPlot/ScottPlot/tree/main/examples) 文件夹和 [官方网站](https://scottplot.net/)。