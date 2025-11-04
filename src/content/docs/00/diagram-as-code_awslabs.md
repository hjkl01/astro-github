
---
title: diagram-as-code
---


# Diagram-as-Code (AWS Labs)

> **项目地址**  
> https://github.com/awslabs/diagram-as-code

## 主要特性

1. **代码驱动的架构图生成**  
   - 通过在代码中添加简洁的注解或标记，自动将 AWS CDK / CloudFormation 资源转换为可视化的架构图。  
   - 支持的语言包括 TypeScript、Python、Java、C# 等 CDK 语言。

2. **多种输出格式**  
   - 直接生成 **Mermaid**、**PlantUML**、**Graphviz** 等文本化图表格式。  
   - 可进一步导出为 **SVG、PNG、PDF** 等图像文件，便于嵌入文档或演示。

3. **高度可配置**  
   - 通过 `config.yaml` 或 `dac.config.js` 自定义图表主题、字体、颜色、布局风格。  
   - 支持包括关键信息过滤（如仅保留重要资源）、自定义标签、分组节点等。

4. **无缝集成 CI/CD**  
   - 在持续集成流水线中调用 `dac` CLI，自动更新架构图，保持图文同步。  
   - 支持 GitHub Actions、AWS CodeBuild、GitLab CI 等多种 CI 环境。

5. **增量更新与版本管理**  
   - 通过对比变化，只重新生成变更部分，提高生成效率。  
   - 与 Git 集成，可记录图表版本历史，配合版本标签保持一致性。

## 功能概览

| 功能 | 说明 |
|------|------|
| `dac generate` | 根据当前 CDK / CloudFormation 项目生成图表。 |
| `dac watch` | 监听代码变更，实时更新图表。 |
| `dac export` | 指定输出格式与路径，支持批量导出。 |
| `dac init` | 快速初始化项目的配置文件与示例。 |
| `dac help` | 查看各命令用法与参数。 |

## 用法示例

```bash
# 安装
npm i -g diagram-as-code

# 初始化配置文件（可选）
dac init

# 生成 Mermaid 图表
dac generate --format mermaid --output diagram.mmd

# 直接导出 PNG
dac export --format png --output architecture.png

# 在 CI 中使用
dac generate --format svg --output ./docs/architecture.svg
```

### 示例: 在 TypeScript CDK 项目中使用

```ts
import { Construct } from "constructs";
import { Bucket } from "aws-cdk-lib/aws-s3";
import { App, Stack } from "aws-cdk-lib";

class MyStack extends Stack {
  constructor(scope: Construct, id: string) {
    super(scope, id);

    // Swagger: diagram.asCode = true
    new Bucket(this, "MyBucket", { bucketName: "my-bucket" });
  }
}

const app = new App();
new MyStack(app, "MyStack");
app.synth();
```

> 运行 `dac generate` 后会自动识别注解并填入图表。

## 文档与社区

- 详细使用文档请查看项目的 **docs** 目录。  
- 交流问题、提交 PR 或建议，访问仓库 Issues 或 Pull Requests 区域。

---

> **请保存至** `src/content/docs/00/diagram-as-code_awslabs.md`。