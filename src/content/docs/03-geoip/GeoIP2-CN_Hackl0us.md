---
title: GeoIP2-CN
---

# GeoIP2-CN 项目

**GitHub 项目地址：** [https://github.com/Hackl0us/GeoIP2-CN](https://github.com/Hackl0us/GeoIP2-CN)

## 主要特性

- **中国IP地址库**：基于MaxMind GeoLite2数据库，提供专属于中国大陆的IP地理位置信息，支持IPv4和IPv6。
- **高精度数据**：数据源来自 ipip.net 和 纯真 IP，经过合并、去重、整理，确保IP归属地的准确性，包括省份、市区等详细信息。
- **轻量级实现**：数据库大小仅约100KB，使用MMDB格式存储，便于快速查询和集成到各种应用中。
- **开源免费**：GPL-3.0许可，允许自由使用、修改和分发。
- **兼容性强**：支持多种编程语言的GeoIP2库，如Python、Go、Node.js等。
- **自动化更新**：项目每隔3天通过全自动化部署自动更新，时刻保持最佳体验。

## 主要功能

- **IP地理查询**：通过IP地址查询对应的国家、省份、城市、ISP等信息，专注于中国大陆区域。
- **数据更新**：提供脚本自动从上游源拉取并生成最新的MMDB数据库文件。
- **批量处理**：支持高效的批量IP解析，适用于日志分析、网络监控等场景。
- **自定义扩展**：用户可修改脚本添加更多数据字段或优化查询性能。
- **代理工具集成**：专为代理工具设计，支持Surge、Shadowrocket、QuantumultX、Clash等工具的GEOIP规则配置。

## 用法

### 1. 下载数据库

项目提供两种格式的文件下载：

- **GeoIP2 数据库 (Country.mmdb)**：适用于Surge、Shadowrocket、QuantumultX、Clash等较新的代理工具。
  - GitHub RAW: [https://github.com/Hackl0us/GeoIP2-CN/raw/release/Country.mmdb](https://github.com/Hackl0us/GeoIP2-CN/raw/release/Country.mmdb)
  - CDN 加速: [https://cdn.jsdelivr.net/gh/Hackl0us/GeoIP2-CN@release/Country.mmdb](https://cdn.jsdelivr.net/gh/Hackl0us/GeoIP2-CN@release/Country.mmdb)

- **IP-CIDR 列表 (CN-ip-cidr.txt)**：适用于防火墙、较老的代理工具等。
  - GitHub RAW: [https://github.com/Hackl0us/GeoIP2-CN/raw/release/CN-ip-cidr.txt](https://github.com/Hackl0us/GeoIP2-CN/raw/release/CN-ip-cidr.txt)
  - CDN 加速: [https://cdn.jsdelivr.net/gh/Hackl0us/GeoIP2-CN@release/CN-ip-cidr.txt](https://cdn.jsdelivr.net/gh/Hackl0us/GeoIP2-CN@release/CN-ip-cidr.txt)

### 2. 配置到代理工具

- 将下载的 `Country.mmdb` 文件放置在代理工具的配置目录中。
- 在规则中添加 `GEOIP, CN, DIRECT` 来查询中国大陆IP。
- 支持的工具及配置教程：
  - Surge
  - Quantumult X
  - Shadowrocket
  - Clash (ClashX, Clash for Windows, OpenClash等)
- 详细配置请参考项目 [Wiki](https://github.com/Hackl0us/GeoIP2-CN/wiki)。

### 3. 查询IP信息（示例使用Python GeoIP2库）

- 安装GeoIP2：`pip install geoip2`
- 示例代码：

  ```python
  import geoip2.database

  reader = geoip2.database.Reader('Country.mmdb')
  response = reader.city('8.8.8.8')  # 替换为目标IP
  print(response.country.iso_code)   # 输出国家代码
  print(response.city.name)          # 输出城市名
  reader.close()
  ```

### 4. 注意事项

- **禁用或删除** 与中国大陆IP地址段相关的其他规则或规则集，如 `RULE-SET, https://handsome.hackl0us.com/China-IP.list, DIRECT` 或 `GEOIP, CN, DIRECT` 的重复规则。
- GEOIP-CN 查询规则建议紧随最终规则之上，以避免域名规则被忽略导致判断错误。
- 规则中不可存在其他国家或地区的 `GEOIP` 查询规则，因为数据库仅包含中国大陆地区的IP地址段记录。

更多细节请参考仓库的README文件。
