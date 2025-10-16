
---
title: GeoIP2-CN
---

# GeoIP2-CN 项目

**GitHub 项目地址：** [https://github.com/Hackl0us/GeoIP2-CN](https://github.com/Hackl0us/GeoIP2-CN)

## 主要特性
- **中国IP地址库**：基于MaxMind GeoLite2数据库，提供专属于中国大陆的IP地理位置信息，支持IPv4和IPv6。
- **高精度数据**：定期更新数据源，确保IP归属地的准确性，包括省份、市区、经纬度等详细信息。
- **轻量级实现**：使用MMDB格式存储，便于快速查询和集成到各种应用中。
- **开源免费**：MIT许可，允许自由使用、修改和分发。
- **兼容性强**：支持多种编程语言的GeoIP2库，如Python、Go、Node.js等。

## 主要功能
- **IP地理查询**：通过IP地址查询对应的国家、省份、城市、ISP等信息，专注于中国区域。
- **数据更新**：提供脚本自动从上游源拉取并生成最新的MMDB数据库文件。
- **批量处理**：支持高效的批量IP解析，适用于日志分析、网络监控等场景。
- **自定义扩展**：用户可修改脚本添加更多数据字段或优化查询性能。

## 用法
1. **克隆仓库**：
   ```
   git clone https://github.com/Hackl0us/GeoIP2-CN.git
   cd GeoIP2-CN
   ```

2. **更新数据库**（需要Python环境和依赖）：
   - 安装依赖：`pip install -r requirements.txt`
   - 运行更新脚本：`python update.py`
   - 这将生成`GeoLite2-City.mmdb`等数据库文件。

3. **查询IP信息**（示例使用Python GeoIP2库）：
   - 安装GeoIP2：`pip install geoip2`
   - 示例代码：
     ```python
     import geoip2.database

     reader = geoip2.database.Reader('GeoLite2-City.mmdb')
     response = reader.city('8.8.8.8')  # 替换为目标IP
     print(response.country.iso_code)   # 输出国家代码
     print(response.city.name)          # 输出城市名
     reader.close()
     ```

4. **集成到应用**：将生成的MMDB文件加载到支持GeoIP2的框架中，如Nginx模块或自定义服务，用于实时IP定位。

更多细节请参考仓库的README文件。