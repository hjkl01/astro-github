
---
title: ip2region
---

# ip2region 项目描述

## 项目地址
[https://github.com/lionsoul2014/ip2region](https://github.com/lionsoul2014/ip2region)

## 主要特性
- **高效的IP地址查询库**：ip2region 是一个开源的IP地址库，支持快速查询IP对应的地理位置信息，包括国家、省份、城市、ISP等。
- **多语言支持**：提供Java、C、PHP、C#、Python、Go、JavaScript等多种语言的绑定，实现跨平台使用。
- **高性能**：采用二进制索引文件（.db），查询速度极快，支持内存映射模式，平均查询时间在微秒级别。
- **轻量级**：核心库体积小，易于集成到各种应用中。
- **数据更新**：定期提供IP数据更新，支持自定义数据导入。
- **无外部依赖**：纯本地查询，不需要网络连接，隐私安全。

## 主要功能
- **IP地理位置查询**：根据IPv4或IPv6地址，返回详细的地域信息（如中国/北京市/北京市/中国电信）。
- **批量查询支持**：可处理大量IP查询，适用于日志分析、风控系统等场景。
- **数据解析与构建**：提供工具用于解析和构建自定义IP数据文件。
- **API封装**：各语言绑定提供简单易用的API接口，支持同步和异步查询。

## 用法
### 1. 下载与安装
- 从GitHub仓库克隆或下载项目。
- 下载最新的IP数据文件（ip2region.db），放置在项目目录下。

### 2. Java 示例
```java
import org.lionsoul.ip2region.DataBlock;
import org.lionsoul.ip2region.DbConfig;
import org.lionsoul.ip2region.DbSearcher;

// 初始化搜索器
DbSearcher searcher = new DbSearcher(new DbConfig(), "ip2region.db");

// 查询IP
DataBlock dataBlock = searcher.memorySearch("8.8.8.8");
System.out.println(dataBlock.getRegion()); // 输出: 美国|0|0|0|谷歌
```

### 3. Python 示例
```python
from ip2region import Ip2Region

# 初始化
r = Ip2Region("ip2region.db")

# 查询
data = r.memory_search("8.8.8.8")
print(data.region)  # 输出: 美国|0|0|0|谷歌
```

### 4. 其他语言
类似地，其他语言（如PHP、Go）通过相应绑定库调用`memorySearch`或`binarySearch`方法进行查询。详细用法参考仓库中的README和示例代码。建议根据具体语言查看对应目录的文档。