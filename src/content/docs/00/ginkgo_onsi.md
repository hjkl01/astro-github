---
title: ginkgo
---

# Ginkgo

## 项目简介

Ginkgo 是一个现代化的 Go 语言测试框架，旨在帮助开发者编写表达性强的测试规范（specs）。它建立在 Go 的 `testing` 包基础上，并与 [Gomega](https://github.com/onsi/gomega) 匹配器库互补使用。Ginkgo 采用行为驱动开发（BDD）风格，支持编写单元测试、集成测试甚至性能测试。

## 主要功能

- **表达性 DSL**：提供嵌套的容器节点（如 `Describe`、`Context`、`When`）来组织测试规范。
- **设置和清理**：支持 `BeforeEach`、`AfterEach`、`BeforeSuite`、`AfterSuite` 等节点进行测试前后的准备和清理工作。
- **断言支持**：与 Gomega 结合，提供丰富的同步和异步断言匹配器。
- **并行执行**：支持测试规范的并行运行，提高测试效率。
- **随机化**：可以以可重现的随机顺序运行测试，确保测试的独立性。
- **标签和过滤**：使用标签对测试进行分类，并支持按标签过滤运行特定测试。
- **报告生成**：提供多种格式的机器可读报告，并支持自定义报告器。
- **命令行工具**：`ginkgo` CLI 工具支持生成、运行、过滤和分析测试套件，还支持 `watch` 模式自动检测文件变化并重新运行测试。

## 用法示例

### 基本结构

```go
import (
    . "github.com/onsi/ginkgo/v2"
    . "github.com/onsi/gomega"
)

var _ = Describe("Checking books out of the library", Label("library"), func() {
    var library *libraries.Library
    var book *books.Book
    var valjean *users.User

    BeforeEach(func() {
        library = libraries.NewClient()
        book = &books.Book{
            Title: "Les Miserables",
            Author: "Victor Hugo",
        }
        valjean = users.NewUser("Jean Valjean")
    })

    When("the library has the book in question", func() {
        BeforeEach(func(ctx SpecContext) {
            Expect(library.Store(ctx, book)).To(Succeed())
        })

        Context("and the book is available", func() {
            It("lends it to the reader", func(ctx SpecContext) {
                Expect(valjean.Checkout(ctx, library, "Les Miserables")).To(Succeed())
                Expect(valjean.Books()).To(ContainElement(book))
                Expect(library.UserWithBook(ctx, book)).To(Equal(valjean))
            }, SpecTimeout(time.Second*5))
        })

        // 更多测试用例...
    })
})
```

### 运行测试

- 运行所有测试：`ginkgo`
- 并行运行：`ginkgo -p`
- 监听文件变化并自动运行：`ginkgo watch`
- 按标签过滤：`ginkgo --label-filter="library"`

### 安装和设置

1. 安装 Ginkgo：`go install github.com/onsi/ginkgo/v2/ginkgo`
2. 初始化测试套件：`ginkgo bootstrap`
3. 生成测试文件：`ginkgo generate [测试名]`

更多详细信息请参考 [官方文档](https://onsi.github.io/ginkgo/)。
