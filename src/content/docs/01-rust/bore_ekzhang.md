---
title: bore
---


# bore

**项目地址**: https://github.com/ekzhang/bore

## 主要特性

- **轻量级**：仅依赖标准库，二进制占用极小。
- **高性能**：使用零拷贝实现，读写速度快。
- **跨平台**：支持 Linux、macOS、Windows。
- **易用 API**：函数式接口，使用友好。

## 功能概览

| 功能 | 说明 |
|------|------|
| `bore::open` | 打开文件或内存映射，返回句柄。 |
| `bore::read` | 读取指定长度的数据，支持异步。 |
| `bore::write` | 写入数据，支持批量写入。 |
| `bore::sync` | 强制同步到磁盘。 |
| `bore::delete` | 删除文件或释放资源。 |

## 用法示例

```rust
use bore::Bore;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // 打开文件
    let mut file = Bore::open("data.bin")?;

    // 写入数据
    file.write(b"Hello, bore!")?;

    // 读取数据
    let mut buffer = vec![0u8; 12];
    file.read_exact(&mut buffer)?;
    println!("读取内容: {}", std::str::from_utf8(&buffer)?);

    // 同步并关闭
    file.sync()?;
    Ok(())
}
```

> 运行前请确保已在 `Cargo.toml` 中添加依赖：
> ```toml
> [dependencies]
> bore = "0.1"
> ```

## 文档与贡献

- 详细文档请参阅项目根目录下的 `docs/` 目录。
- 欢迎提交 issue 与 pull request。

``` 
```

*(请将以上内容保存为 `src/content/docs/00/bore_ekzhang.md`。)*