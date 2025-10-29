
---
title: LinkSwift
---

# LinkSwift (hmjz100)

**GitHub 地址**: <https://github.com/hmjz100/LinkSwift>

---

## 简介

LinkSwift 是一款专为 Swift 开发者设计的轻量级 URL 链接构建与解析库。它采用链式调用（Builder）模式，让 URL 的拼接、参数编码、路径拼接、查询字符串处理等变得异常直观、易读。无论你是在构造 RESTful API 请求、生成深度链接，还是在实现自定义 URL Scheme，LinkSwift 都能帮你减少样板代码，提升开发效率。

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **链式 URL 构建** | 通过链式语法一步步拼接 scheme、host、path、query 等元素。 |
| **安全编码** | 自动对路径和查询参数进行 URL 编码，避免手动编码导致的错误。 |
| **可组合性** | 支持通过 `merge` 合并已有的 `Link`，实现复用。 |
| **易于解析** | 通过 `Link.parse(_:)` 能快速将字符串解析回 `Link` 对象，方便反向操作。 |
| **自定义 Scheme** | 轻松处理自定义 URL Scheme（如 `myapp://`）以及 universal links。 |
| **友好的错误处理** | 通过 `Result` 或 `throws` 方式返回构建失败信息。 |
| **Swift Package Manager** | 完全兼容 SPM，直接在 `Package.swift` 中添加依赖即可。 |

---

## 安装

### Swift Package Manager

```swift
// Package.swift
.package(url: "https://github.com/hmjz100/LinkSwift.git", from: "1.0.0")
```

### CocoaPods

> LinkSwift 尚未发布到 CocoaPods，请使用 SPM 或直接克隆仓库。

---

## 使用示例

### 1. 构建一个 RESTful 请求 URL

```swift
import LinkSwift

let url = Link()
    .scheme("https")
    .host("api.example.com")
    .path("v1", "users")
    .query(["page": "2", "limit": "20"])
    .build()

print(url) // https://api.example.com/v1/users?page=2&limit=20
```

### 2. 生成自定义 Scheme 链接

```swift
let customURL = Link()
    .scheme("myapp")
    .host("open")
    .path("profile")
    .query(["userId": "12345"])
    .build()

// 打开链接
UIApplication.shared.open(customURL, options: [:], completionHandler: nil)
```

### 3. 合并已有链接

```swift
let base = Link()
    .scheme("https")
    .host("cdn.example.com")
    .path("assets")

let imageLink = base
    .path("images", "logo.png")
    .build()
// https://cdn.example.com/assets/images/logo.png
```

### 4. 解析字符串为 Link 对象

```swift
if let parsedLink = Link.parse("https://github.com/hmjz100/LinkSwift") {
    print(parsedLink.scheme)   // "https"
    print(parsedLink.host)     // "github.com"
    print(parsedLink.path)     // "/hmjz100/LinkSwift"
}
```

---

## API 参考

| 结构体 / 类 | 方法 / 属性 | 描述 |
|------------|------------|------|
| `Link` | `init()` | 创建空链式链接 |
| `Link` | `scheme(_:)` | 设置 URL scheme |
| `Link` | `host(_:)` | 设置 host |
| `Link` | `path(_:)` | 添加路径段（可多次调用） |
| `Link` | `query(_:)` | 设置查询参数（字典） |
| `Link` | `build() -> URL?` | 生成最终 `URL` 对象 |
| `Link` | `merge(with:)` | 合并另一个 `Link` 的部分 |
| `Link` | `static func parse(_:) -> Link?` | 将字符串解析为 `Link` 对象 |
| `Link` | `var scheme: String?` | 读取 scheme |
| `Link` | `var host: String?` | 读取 host |
| `Link` | `var path: String` | 读取完整路径（含 `/`） |
| `Link` | `var query: [String: String]` | 读取查询参数 |

---

## 贡献 & 反馈

如果你发现任何问题、想提出改进建议，欢迎提交 Issue 或 Pull Request。你也可以在 README 中查看 [Contribution Guidelines](CONTRIBUTING.md)。

---