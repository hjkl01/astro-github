---
title: cpython
---

## 功能介绍

CPython 是 Python 编程语言的官方实现，由 Python Software Foundation 维护。它提供了完整的 Python 解释器、标准库以及所有必要的组件，用于开发和运行 Python 应用程序。CPython 支持多种平台，包括 Unix、Linux、BSD、macOS、Windows 和 Cygwin。

主要功能包括：

- Python 解释器：执行 Python 代码
- 标准库：内置模块和函数
- 扩展支持：C/C++ 扩展模块
- 跨平台兼容性
- 性能优化：支持 Profile Guided Optimization (PGO) 和 Link Time Optimization (LTO)

## 用法

### 安装 Python

从 [python.org](https://www.python.org) 下载预编译的安装包，或从源码构建。

### 从源码构建

在 Unix、Linux、BSD、macOS 和 Cygwin 上：

```bash
./configure
make
make test
sudo make install
```

这将安装 Python 作为 `python3`。

### 运行 Python

安装后，可以使用 `python3` 命令运行 Python 脚本：

```bash
python3 script.py
```

### 测试

运行测试套件：

```bash
make test
```

### 贡献

如果想为 CPython 贡献代码，请参考 [Developer Guide](https://devguide.python.org/)。

更多信息请访问 [Python 官方网站](https://www.python.org) 和 [文档](https://docs.python.org)。
