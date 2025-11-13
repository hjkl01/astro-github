---
title: diagrams
---

# GitHub 项目：diagrams

**项目地址：** [https://github.com/mingrammer/diagrams](https://github.com/mingrammer/diagrams)

## 主要特性
- **纯 Python 实现**：无需安装 Graphviz 等外部依赖，直接使用 Python 代码生成图表，支持多种流行图表库和工具。
- **节点和边定义**：通过简单的类和方法定义图表的节点（Node）和连接边（Edge），支持自定义样式、颜色和布局。
- **内置支持多种图表类型**：包括流程图（Diagram）、类图（ClassDiagram）、实体关系图（ERDiagram）等，适用于系统架构、数据库设计和 UML 图等场景。
- **导出多种格式**：生成的图表可导出为 PNG、SVG、PDF 等图像格式，便于集成到文档或演示中。
- **插件扩展**：支持自定义节点类型和扩展现有功能，兼容 AWS、Azure 等云服务图标库。
- **跨平台兼容**：在 Python 3.7+ 环境下运行，无需图形界面，支持命令行生成图表。

## 主要功能
- **图表生成**：使用 Python 脚本快速创建结构化图表，如网络拓扑、数据流程和软件架构图。
- **样式自定义**：支持节点形状、颜色、标签和方向（从上到下、从左到右等）自定义。
- **集成图标库**：内置数百个预定义图标（如云服务、数据库、容器），可直接导入使用。
- **自动布局**：利用底层引擎自动处理节点位置和边路由，避免手动调整。
- **代码即图表**：将图表逻辑转化为可读的 Python 代码，便于版本控制和协作。

## 用法
1. **安装**：
   ```bash
   pip install diagrams
   ```

2. **基本示例**（创建简单流程图）：
   ```python
   from diagrams import Diagram
   from diagrams.generic.blank import Blank
   from diagrams.onprem.client import Client

   with Diagram("简单流程图", show=False, direction="TB"):  # TB 表示从上到下
       client = Client("客户端")
       server = Blank("服务器")
       client >> server  # 定义边连接
   ```
   - 运行脚本后，会在当前目录生成 `简单流程图.png` 文件。

3. **高级用法**（使用云服务图标）：
   ```python
   from diagrams import Diagram
   from diagrams.aws.compute import EC2
   from diagrams.aws.database import RDS
   from diagrams.aws.network import ELB

   with Diagram("AWS 架构图", show=False):
       elb = ELB("负载均衡")
       ec2s = [EC2("Web服务器1"), EC2("Web服务器2")]
       rds = RDS("数据库")
       
       elb >> ec2s  # 连接到多个节点
       ec2s >> rds
   ```
   - 支持子图（Cluster）和条件边等高级特性。

4. **导出和查看**：
   - 默认导出为 PNG；使用 `outformat="svg"` 参数指定格式。
   - 设置 `show=True` 在运行时打开图像查看器。
   - 更多示例和文档见项目 README。