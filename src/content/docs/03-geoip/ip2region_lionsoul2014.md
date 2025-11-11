---
title: ip2region
---

# ip2region 项目描述

## 项目地址

[https://github.com/lionsoul2014/ip2region](https://github.com/lionsoul2014/ip2region)

## 主要特性

- **离线IP定位库**：ip2region 是一个离线IP地址定位库和IP定位数据管理框架，同时支持IPv4和IPv6，10微秒级别的查询效率。
- **多语言支持**：提供众多主流编程语言的xdb数据生成和查询客户端实现，包括Golang、PHP、Java、C、Lua、Rust、Python、JavaScript、C#、Erlang、Nginx、C++等。
- **高性能**：采用xdb二进制索引文件，查询速度极快，支持内存映射模式，平均查询时间在微秒级别。可通过vIndex索引缓存或整个xdb文件缓存实现内存加速查询。
- **轻量级**：核心库体积小，易于集成到各种应用中，支持亿级别IP数据段。
- **数据管理框架**：xdb支持完全自定义region信息，自带数据格式为：国家|省份|城市|ISP，可追加GPS信息、邮编等业务数据。
- **数据去重和压缩**：xdb格式生成程序自动处理输入数据，合并相连IP段，去重和压缩相同地域信息。
- **数据更新**：项目自带原始数据不提供更新，建议购买商用离线数据以获取更高精度和更新频率的数据。
- **无外部依赖**：纯本地查询，不需要网络连接，隐私安全。

## 主要功能

- **IP地理位置查询**：根据IPv4或IPv6地址，返回详细的地域信息（如中国|北京市|北京市|中国电信），支持精确到城市的查询定位。
- **批量查询支持**：可处理大量IP查询，适用于日志分析、风控系统、网络监控等场景。
- **数据解析与构建**：提供工具用于解析和构建自定义IP数据文件，支持数据编辑和更新。
- **API封装**：各语言绑定提供简单易用的API接口，支持同步和异步查询，统一的查询接口同时支持IPv4和IPv6。
- **内存加速查询**：支持vIndex索引缓存（512KiB内存）和整个xdb文件缓存，实现10微秒级别的查询效率。
- **自定义数据管理**：支持完全自定义region信息，可用于管理自己的IP定位数据，追加业务相关信息。

## 用法

### 1. 下载与安装

- 从GitHub仓库下载项目：[https://github.com/lionsoul2014/ip2region](https://github.com/lionsoul2014/ip2region)
- 下载最新的 xdb 数据文件（ip2region_v4.xdb 用于IPv4，ip2region_v6.xdb 用于IPv6），放置在项目目录下。
- 项目自带示例数据文件：`data/ip2region_v4.xdb` 和 `data/ip2region_v6.xdb`

### 2. 查询方式

支持三种查询方式：

- **memorySearch**：整个xdb文件加载到内存，10微秒级别查询效率
- **binarySearch**：基于文件的二分查找查询
- **btreeSearch**：基于文件的B树查询

### 3. Java 示例

```java
import org.lionsoul.ip2region.DataBlock;
import org.lionsoul.ip2region.DbConfig;
import org.lionsoul.ip2region.DbSearcher;

DbSearcher searcher = new DbSearcher(new DbConfig(), "ip2region_v4.xdb");

DataBlock dataBlock = searcher.memorySearch("8.8.8.8");
System.out.println(dataBlock.getRegion()); // 输出: 美国|0|0|0|谷歌
```

### 4. Python 示例

```python
from ip2region import Ip2Region

r = Ip2Region("ip2region_v4.xdb")

data = r.memory_search("8.8.8.8")
print(data.region)  # 输出: 美国|0|0|0|谷歌
```

### 5. Golang 示例

```go
package main

import (
    "fmt"
    "github.com/lionsoul2014/ip2region/binding/golang"
)

func main() {
    searcher, err := xdb.New("ip2region_v4.xdb")
    if err != nil {
        fmt.Printf("failed to create searcher: %s\n", err)
        return
    }
    defer searcher.Close()

    region, err := searcher.Search("8.8.8.8")
    if err != nil {
        fmt.Printf("failed to search: %s\n", err)
        return
    }
    fmt.Printf("region: %s\n", region) // 输出: 美国|0|0|0|谷歌
}
```

### 6. 其他语言支持

xdb 查询客户端支持多种编程语言，包括：

- Golang, PHP, Java, C, Lua (C扩展), Rust, Python, JavaScript (Node.js), C#, Erlang, Nginx, C++
- 第三方实现：php composer客户端、node.js addon、ruby客户端等

详细用法和API文档请参考各语言绑定目录下的README文件。
