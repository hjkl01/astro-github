---
title: fmt
---


# fmt - fmtlib 项目简介

**GitHub 地址**: https://github.com/fmtlib/fmt

## 主要特性

| 特性 | 说明 |
|------|------|
| **类型安全** | `fmt::format` 通过编译时类型检查避免字符串格式化错误。 |
| **高性能** | 采用预分配缓冲区和零拷贝技术，比 `std::printf` 快数倍。 |
| **C++20 模板语法** | 支持简洁的 `fmt::print`、`fmt::format_to` 等接口。 |
| **可定制** | 可通过写自定义格式说明符实现自定义类型的格式化。 |
| **多平台** | 兼容 Windows、Linux、macOS，支持 C++11+。 |
| **Unicode & 多字节** | 原生支持 Unicode、UTF-8 字符串格式化。 |
| **线程安全** | 多线程环境下可安全使用。 |
| **易于集成** | 提供可单文件版本；无外部依赖，易于嵌入。 |

## 核心功能

1. **`fmt::format`**  
   如 `fmt::format("Hello, {}!", "world")`，返回 `std::string`。

2. **`fmt::print`**  
   直接输出到 `stdout`，等价于 `printf`。

3. **`fmt::format_to`**/`fmt::format_to_n`  
   将结果写入已有缓冲区，避免不必要的拷贝。

4. **自定义格式化**  
   ```cpp
   struct Point { int x, y; };
   template<>
   struct fmt::formatter<Point> {
       template<typename FormatContext>
       auto format(const Point& p, FormatContext& ctx) {
           return fmt::format_to(ctx.out(), "({},{})", p.x, p.y);
       }
   };
   ```

5. **字符串拼接**  
   `fmt::join`、`fmt::format_with` 等辅助函数。

## 安装方式

```bash
# 通过 vcpkg
vcpkg install fmt

# 通过 conan
conan install fmt/9.1.0@

# 通过 CMake
find_package(fmt REQUIRED)
target_link_libraries(my_target PRIVATE fmt::fmt)
```

## 示例代码

```cpp
#include <fmt.h>
#include <fmt/color.h>
#include <fmt/chrono.h>
#include <iostream>
#include <chrono>

int main() {
    // 基本格式化
    std::string s = fmt::format("Hello, {}! Number: {:0>4}", "world", 7);
    fmt::print("{}\n", s);

    // 颜色输出
    fmt::print(fg(fmt::color::green), "Success: {}\n", true);

    // 时间格式化
    auto now = std::chrono::system_clock::now();
    fmt::print("Current time: {}\n", fmt::format("{:%Y-%m-%d %H:%M:%S}", now));

    // 自定义类型
    struct Point{int x,y;};
    fmt::print("Point: {}\n", Point{3,4});

    return 0;
}
```

## 参考文档

- 官方 GitHub: https://github.com/fmtlib/fmt  
- CMake 示例: https://github.com/fmtlib/fmt/blob/master/examples/CMakeLists.txt  
- API 文档: https://fmt.dev/latest/api.html

---  
> 以上为 fmtlib 的简要说明。若需进一步了解，可访问官方仓库查看更完整的指南与示例。