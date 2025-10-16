
---
title: china-operator-ip
---

# china-operator-ip 项目

## 项目地址
[https://github.com/gaoyifan/china-operator-ip](https://github.com/gaoyifan/china-operator-ip)

## 主要特性
- **中国运营商IP地址数据库**：该项目维护了中国主要电信运营商（如中国电信、中国移动、中国联通等）的IP地址段数据，支持IPv4和IPv6。
- **定期更新**：数据来源于公开来源，并通过脚本定期爬取和更新，确保IP段信息的准确性和时效性。
- **格式支持**：提供多种输出格式，包括JSON、CSV和IP列表，便于集成到各种应用中。
- **开源免费**：采用MIT许可，允许自由使用、修改和分发。

## 主要功能
- **IP查询与匹配**：用户可以通过提供的工具或数据文件查询特定IP地址所属的运营商。
- **自动化生成**：使用Python脚本从官方来源（如APNIC、CNNIC）获取并生成运营商IP列表。
- **过滤与分类**：支持按运营商类型、地区等维度过滤IP段，便于网络安全、路由优化等场景应用。
- **集成友好**：数据文件轻量级，可轻松导入到防火墙、CDN或监控系统中。

## 用法
1. **克隆仓库**：
   ```
   git clone https://github.com/gaoyifan/china-operator-ip.git
   cd china-operator-ip
   ```

2. **安装依赖**（如果需要运行脚本）：
   ```
   pip install -r requirements.txt
   ```

3. **生成数据**：
   - 运行主脚本：`python generate_ip_list.py`，它会自动更新并输出最新的IP列表文件（如`china_telecom_ips.json`）。
   - 输出文件位于`data/`目录下，可直接使用。

4. **查询IP**：
   - 使用提供的查询脚本：`python query_ip.py --ip 8.8.8.8`，返回所属运营商信息。
   - 或者手动解析JSON文件：在代码中加载文件并匹配IP范围（使用IP地址库如`ipaddress`模块）。

5. **集成示例**（Python）：
   ```python
   import json
   with open('data/china_telecom_ips.json', 'r') as f:
       ips = json.load(f)
   # 检查IP是否在列表中
   from ipaddress import ip_address
   ip = ip_address('1.1.1.1')
   for net in ips['networks']:
       if ip in ip_network(net):
           print("属于中国电信")
   ```

项目适合网络工程师、开发者用于IP地理定位、访问控制等用途。建议定期拉取更新以获取最新数据。