
---
title: EIPs
---


# Ethereum Improvement Proposals (EIPs)

**项目地址**: [https://github.com/ethereum/EIPs](https://github.com/ethereum/EIPs)

---

## 概述
- **EIP** 是 Ethereum 社区用来提交、讨论和记录协议改进的正式机制。  
- 该仓库收集所有已发布与待评审的 EIP 文档，提供统一的格式与审核流程。  
- 任何人都可以通过提交 PR 的方式贡献新的 EIP，社区通过讨论与投票决定是否纳入协议。

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **统一格式** | 所有 EIP 采用 Markdown + JSON 结构，包含 `Title`、`Author`、`Status`、`Type`、`Category` 等字段。 |
| **版本控制** | 每个 EIP 通过 GitHub Issue 进行跟踪，状态如 `Draft`、`Last Call`、`Active`、`Final` 等。 |
| **社区治理** | 通过 Issue 讨论、提案标签、社区投票等方式决定 EIP 的接受与实施。 |
| **项目目录** | `eips/` 目录存放正式 EIP 文档；`draft/` 目录存放正在评审的草稿。 |
| **工具链** | 提供 `eip-generator`、`eip-validator` 等脚本，帮助作者快速生成并校验 EIP。 |

---

## 主要功能

- **提交新提案**  
  1. Fork 项目。  
  2. 在 `draft/` 目录下创建以 `EIP-XXX.md` 命名的文件。  
  3. 填写 EIP 结构（标题、作者、类型、状态等）。  
  4. 提交 PR，附上 Issue 关联。  

- **评审与讨论**  
  - 通过 Issue 讨论技术细节。  
  - 采用 GitHub Discussions 或者 Discord 进行实时交流。  
  - 通过 `Last Call` 标记进入最终投票阶段。  

- **合并与发布**  
  - 通过 `Active` → `Final` 状态标记完成。  
  - 文档同步到 `eips/` 目录，旧版本保留在 `draft/`。  

- **工具支持**  
  - `make lint`：检查 Markdown 语法与字段完整性。  
  - `make generate`：根据模板生成新的 EIP 文件。  

---

## 使用方法

1. **克隆仓库**  
   ```bash
   git clone https://github.com/ethereum/EIPs.git
   cd EIPs
   ```

2. **查看已发布的 EIP**  
   - 浏览 `eips/` 目录。  
   - 使用 `search` 或 `grep` 快速定位特定编号。  

3. **阅读 EIP 标准**  
   - `EIP-1.md`（EIP 规范）  
   - `EIP-2.md`（EIP 版本控制）  
   - `EIP-3.md`（EIP 状态定义）  

4. **提交新提案**  
   ```bash
   # 在 draft 目录中创建文件
   cp eip-template.md draft/EIP-9999.md
   # 编辑文件
   # 提交 PR 并关联 Issue
   ```

5. **参与评审**  
   - 在对应 Issue 下评论。  
   - 使用 `:thumbsup:` 或 `:thumbsdown:` 表达投票。  

6. **保持同步**  
   ```bash
   git pull upstream main
   ```  

---

## 参考链接

- [EIP 规范](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1.md)  
- [EIP 2：版本控制](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2.md)  
- [EIP 3：状态定义](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-3.md)  

--- 
