---
title: task
---

# Task

Task 是一个用 Go 编写的任务运行器/构建工具，旨在比 GNU Make 等工具更简单易用。它允许用户使用 YAML 格式定义任务，支持变量、依赖关系、循环、文件监视等功能。

## 功能特性

- **简单易用**：使用 YAML 语法定义任务，比 Makefile 更直观
- **跨平台**：单二进制文件，无依赖，支持 Windows、macOS、Linux
- **变量支持**：支持环境变量、任务变量和全局变量
- **依赖管理**：任务可以依赖其他任务，按顺序执行
- **文件监视**：支持监视文件变化，自动重新运行任务
- **循环执行**：支持对列表或范围进行循环操作
- **任务包含**：可以包含其他 Taskfile，实现模块化
- **输出控制**：支持分组输出、前缀输出等
- **Shell 补全**：支持 bash、zsh、fish、PowerShell 的自动补全

## 安装方法

### 使用安装脚本（推荐）

```bash
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d
```

### 使用包管理器

- **Homebrew** (macOS/Linux): `brew install go-task`
- **Snap** (Linux): `sudo snap install task --classic`
- **Scoop** (Windows): `scoop install task`
- **Chocolatey** (Windows): `choco install go-task`
- **Arch Linux**: `pacman -S go-task`
- **Fedora**: `dnf install go-task`
- **npm**: `npm install -g @go-task/cli`

### 从源码构建

```bash
go install github.com/go-task/task/v3/cmd/task@latest
```

## 基本用法

### 1. 初始化 Taskfile

```bash
task --init
```

这会在当前目录创建 `Taskfile.yml`。

### 2. 基本 Taskfile 示例

```yaml
version: '3'

vars:
  GREETING: Hello, World!

tasks:
  default:
    cmds:
      - echo "{{.GREETING}}"
    silent: true

  build:
    cmds:
      - go build ./cmd/main.go

  test:
    desc: 运行所有 Go 测试
    cmds:
      - go test -race ./...
```

### 3. 运行任务

```bash
# 运行默认任务
task

# 运行指定任务
task build
task test

# 在子目录中运行
task --dir ./subdirectory build

# 使用自定义 Taskfile
task --taskfile Custom.yml build
```

### 4. 任务依赖

```yaml
version: '3'

tasks:
  build:
    cmds:
      - go build ./cmd/main.go

  test:
    deps: [build]
    cmds:
      - go test ./...

  release:
    deps: [test]
    summary: |
      发布项目到 GitHub

      会在开始发布前构建项目。
      请确保在开始前设置了 GITHUB_TOKEN。
    cmds:
      - your-release-tool
```

### 5. 文件监视

```yaml
version: '3'

interval: 500ms

tasks:
  build:
    desc: 构建 Go 应用
    watch: true
    sources:
      - '**/*.go'
    cmds:
      - go build
```

### 6. 循环执行

```yaml
version: '3'

tasks:
  process-files:
    cmds:
      - for: ['foo.txt', 'bar.txt', 'baz.txt']
        cmd: cat {{.ITEM}}
```

### 7. 任务包含

```yaml
version: '3'

includes:
  docs: ./documentation # 会查找 ./documentation/Taskfile.yml
  docker: ./DockerTasks.yml

tasks:
  all:
    deps: [docs:build, docker:build]
```

## 高级用法

### 状态检查（避免重复执行）

```yaml
version: '3'

tasks:
  generate-files:
    cmds:
      - mkdir directory
      - touch directory/file1.txt
    status:
      - test -d directory
      - test -f directory/file1.txt
```

### 任务别名

```yaml
version: '3.17'

tasks:
  hello:
    aliases: [hi, hey]
    cmds:
      - echo "Hello, world!"
```

### 输出控制

```yaml
version: '3'

output: prefixed # 或 'group', 'interleaved'

tasks:
  default:
    cmds:
      - echo "foo"
      - echo "bar"
```

## 常用命令

- `task --list`: 列出所有可用任务
- `task --summary`: 显示任务摘要
- `task --completion <shell>`: 生成 shell 补全脚本
- `task --version`: 显示版本信息
- `task --help`: 显示帮助信息

Task 是一个强大的任务自动化工具，特别适合现代开发工作流中的构建、测试、部署等任务管理。
