
---
title: trufflehog
---


# trufflehog (trufflesecurity)

> **项目地址**  
> https://github.com/trufflesecurity/trufflehog

## 1. 项目简介  
trufflehog 是一款用来扫描 Git 仓库历史（本地或远程）中泄露的**敏感信息（Secrets）**的安全工具。它可以递归遍历每一次提交，识别出隐藏在历史记录中的 API Key、密码、密钥等敏感内容，并提供可靠的报警和修复建议。

## 2. 核心特性  

| 功能 | 说明 |
|------|------|
| **深度扫描** | 递归遍历整个 Git 历史（从 `HEAD` 到最早提交），每一次提交都被完整检查。 |
| **多种检测方式** | - 基于正则表达式的模式匹配<br>- 基于熵（entropy）的泄露检测（识别长随机字符串）<br>- 可自定义的 Glob/DFA 检测模式 |
| **支持多种存储** | 本地磁盘、S3、GCS、Azure Blob 等，支持从云端下载和解析 Git 仓库。 |
| **Docker & CLI** | 通过 Docker 或 `pip install trufflehog` 安装后即可直接使用命令行；支持标准的 `--help` 文档。 |
| **大规模仓库支持** | 针对非常大的仓库提供 BFG 方式加速 | 
| **可配置输出** | JSON、CSV、Plain text、GitHub Actions 注释等多种格式；还能创建 GitHub Issue / PR 注释。 |
| **可扩展** | 支持自定义插件，用来识别特定组织所使用的密钥格式。 |

## 3. 入门使用

### 3.1 本地安装

```bash
# 安装 Python 依赖（建议使用 venv）
python -m pip install trufflehog
```

### 3.2 本地仓库扫描

```bash
trufflehog --regex --entropy=True /path/to/repo.git
```

- `--regex`：启用正则表达式规则（默认已开启）  
- `--entropy=True`：开启熵检测  
- `--max-depth 10`：只扫描最近 10 级提交（可选）  
- `--json`：以 JSON 格式返回结果

> **示例**  
> ```bash
> trufflehog --json /tmp/test-repo
> ```

### 3.3 远程 Git 仓库扫描

```bash
trufflehog --regex --entropy=True https://github.com/<org>/<repo>.git
```

> **注意**：首次扫描下载完整仓库，耗时大，建议先作浅克隆 (`--max-depth` 调小)。

### 3.4 Docker 版

```bash
docker run --rm -v "$PWD":/repo \
  ghcr.io/trufflesecurity/trufflehog:v1.7.2 \
  --regex --entropy=True /repo
```

- `-v "$PWD":/repo` 挂载本地目录  
- 直接在容器内执行扫描

### 3.5 配置文件

创建 `.trufflehog.yaml`

```yaml
regex: true
entropy: true
max_depth: 200
output: json
```

然后：

```bash
trufflehog -c .trufflehog.yaml /path/to/repo.git
```

## 4. 输出与集成

| 输出格式 | 用途 | 生成命令 |
|----------|------|----------|
| `json` | 自动化 CI、日志存档 | `trufflehog --json /repo` |
| `csv` | Excel、数据分析 | `trufflehog --csv /repo` |
| `github` | 自动在 GitHub PR/Issue 添加注释 | `trufflehog --github`| `stdout` | CLI 直观查看 | `trufflehog /repo` |

> **GitHub Actions 示例**  
> ```yaml
> steps:
> - uses: actions/checkout@v3
> - name: Trufflehog Scan
>   uses: trufflesecurity/trufflehog-action@v1
>   with:
>     target: ./
> ```

## 5. 典型用例

1. **CI Pipeline** – 在每次 PR 合并前自动扫描，阻止泄露的密钥被推送。  
2. **回溯审计** – 对历史仓库进行一次性扫描，找出已被推送但被遗忘的敏感信息。  
3. **灾难恢复** – 在数据泄露后，使用 trufflehog 检查是否还有隐藏密钥。  
4. **安全工具链** – 与 Snyk、GitGuardian 等工具配合使用，形成多层防护。

## 6. 如何贡献

- Fork 项目 → `git clone`
- 创建分支 `feature/*` 或 `bugfix/*`  
- 运行测试：`pytest`
- 提交 PR 并填写描述
- 查看 CI 结果

## 7. 许可证

MIT License – 可商业使用、修改、分发，需保留原作者声明。

---

> 以上内容已全部以中文简洁明了的方式进行描述，方便快速入门和日常使用。  
> **保存路径**：`src/content/docs/00/trufflehog_trufflesecurity.md`
