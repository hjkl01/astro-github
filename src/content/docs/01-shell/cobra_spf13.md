---
title: cobra
---


# Cobra (spf13/cobra)

> 项目地址: <https://github.com/spf13/cobra>

## 主要特性

- **层级化命令结构**  
  支持多级子命令，命令树结构易于维护。

- **自动生成帮助文档**  
  每个命令、子命令、标志（flags）都有自动生成的 `--help` 文档。

- **多种标志类型**  
  `String`, `Int`, `Bool`, `StringSlice` 等，支持持久化标志（`PersistentFlags`）和本地标志（`Flags`）。

- **自动补全**  
  支持 Bash、Zsh、Fish、PowerShell 等多种 shell 的命令补全脚本。

- **可配置的使用模板**  
  通过 `cmd.SetUsageTemplate()` 自定义用法展示。

- **简易的执行逻辑**  
  `Run`, `RunE`, `PreRun`, `PostRun` 等回调函数，支持错误返回。

- **集成测试友好**  
  通过 `cobra.Command` 的 `ExecuteContextC` 等方法，可在单元测试中执行命令。

## 基本用法

```go
package main

import (
    "fmt"
    "github.com/spf13/cobra"
    "os"
)

func main() {
    rootCmd := &cobra.Command{
        Use:   "app",
        Short: "示例应用",
        Run: func(cmd *cobra.Command, args []string) {
            fmt.Println("Hello, Cobra!")
        },
    }

    // 添加子命令
    var versionCmd = &cobra.Command{
        Use:   "version",
        Short: "显示版本信息",
        Run: func(cmd *cobra.Command, args []string) {
            fmt.Println("v1.0.0")
        },
    }
    rootCmd.AddCommand(versionCmd)

    // 标志
    rootCmd.Flags().StringP("config", "c", "", "配置文件路径")

    // 执行
    if err := rootCmd.Execute(); err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
}
```

## 生成命令补全脚本

```bash
# Bash
app completion bash > /etc/bash_completion.d/app

# Zsh
app completion zsh > "${fpath[1]}/_app"
```

## 参考链接

- 官方文档: <https://github.com/spf13/cobra>
- 示例项目: <https://github.com/spf13/cobra/tree/master/examples>
- 生成帮助: `app --help`
