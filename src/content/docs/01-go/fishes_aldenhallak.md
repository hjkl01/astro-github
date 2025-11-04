
---
title: fishes
---

# fishes（GitHub：aldenhallak/fishes）

**项目地址**  
https://github.com/aldenhallak/fishes  

## 主要特性

| 特性 | 说明 |
|------|------|
| **核心库** | 纯 Go 实现，可直接 `import` 使用。 |
| **海鱼种类** | 提供多种鱼类模型（鲣鱼、鲑鱼、金枪鱼等）。 |
| **尺寸自定义** | 可通过 `Size` 参数指定鱼的宽高比例。 |
| **颜色支持** | 支持 ANSI 颜色码，能在终端输出彩色鱼。 |
| **随机化生成** | `Generate()` 产生随机属性的鱼，适合生成趣味 ASCII 艺术。 |
| **多平台兼容** | 兼容 Linux、macOS、Windows 下的终端输出。 |
| **内置绘制函数** | `Draw()` 返回鱼的字符串表现，可直接 `fmt.Print`。 |
| **轻量化** | 仅 6KB 代码，只依赖 Go 标准库。 |

## 主要功能

1. **新建鱼模型**  
   ```go
   fish := fishes.NewFish()        // 创建默认鱼
   fish.Size = 20                  // 设定鱼的宽度
   fish.Color = fishes.Yellow      // 设定颜色（常量提供   ```

2. **随机化生成鱼**  
   ```go
   randomFish := fishes.Generate()   // 返回随机属性的鱼
   ```

3. **绘制鱼**  
   ```go
   output := randomFish.Draw()       // 返回鱼的 ASCII 表示
   fmt.Print(output)                 // 直接打印到终端
   ```

4. **批量处理**  
   ```go
   for i := 0; i < 5; i++ {
       f := fishes.Generate()
       fmt.Print(f.Draw())
   }
   ```

5. **自定义图案**  
   本项目预定义多种鱼形模板，也可通过实现 `Template()` 方法自定义新形态。

## 用法示例

```go
package main

import (
    "fmt"
    "github.com/aldenhallak/fishes"
)

func main() {
    // 创建一条自定义鱼
    myFish := fishes.NewFish()
    myFish.Size = 25
    myFish.Color = fishes.Cyan

    // 打印鱼
    fmt.Print(myFish.Draw())

    // 随机生成并打印多条鱼
    for i := 0; i < 3; i++ {
        f := fishes.Generate()
        fmt.Print(f.Draw())
    }
}
```

> **提示**：  
> - 若终端不支持 ANSI 颜色，可以设置 `fish.Color = fishes.Default`。  
> - `Size` 的取值范围是 10~50，超出范围将会自动限制。

> **文档**：  
> 详细 API 说明请参见仓库 `docs` 目录下的 `README.md`。