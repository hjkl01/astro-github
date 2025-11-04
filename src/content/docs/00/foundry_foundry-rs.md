
---
title: foundry
---


# Foundry（foundry-rs/foundry）

- 项目地址: <https://github.com/foundry-rs/foundry>

## 1. 主要特性

| 领域 | 功能 |
|------|------|
| **编译** | `forge build` 基于 solc 的多版本编译器，支持 `pragma` 自动切换；增量编译、缓存、优化等 |
| **单元测试** | `forge test` 支持 Solidity 单元测试、合约间相互调用、随机 fuzzing（`bdffakes`），报告渔人报告（gas, coverage） |
| **网络交互** | `cast` CLI：调用合约方法、发送交易、查询链信息、监控事件；支持多链、JSON-RPC、WebSocket |
| **REPL** | `dapp`（又名 `forge script`）在 REPL 或脚本中直接调用合约、执行事务、交互式调试 |
| **CI/CD** | 与 GitHub Actions、Gitlab CI 等集成，支持 `forge` 任务自动化、缓存、步骤化构建 |
| **Rust 库** | 对 Solidity 对象的低级交互，使用 Rust 生成 ABIs、签名签名 |
| **插件系统** | 可通过 `forge plugin` 安装插件（比如 `forge-bsc`，`forge-optimism` 等） |

## 2. 核心工具

| 工具 | 用途 |
|------|------|
| `forge` | 主要命令行工具，编译、测试、部署 |
| `cast` | 轻量级命令行，交互式调用合约、RPC |
| `dapp` | REPL / Script 入口，支持 Rust 语法交互 |
| `foundryup` | 自动安装与更新 Foundry 工具链 |

## 3. 使用方法

### 3.1 安装

```bash
curl -L https://foundry.paradigm.xyz | bash
foundryup
```

> 安装后，系统 PATH 自动包含 `forge`、`cast`、`dapp`。

### 3.2 初始化项目

```bash
forge init myproject
cd myproject
```

生成目录结构：

```
contracts/
script/
lib/
test/
```

### 3.3 编译 & 生成 ABI

```bash
forge build
```

编译结束后，ABI、字节码保存在 `out/` 目录。

### 3.4 单元测试

```bash
forge test
```

- Fuzzing: 自动调用函数多次，参数随机生成。
- 覆盖率: `forge coverage`.
- Gas Reporter: `forge test --gas-report`.

示例 `test/MyToken.t.sol`：

```solidity
pragma solidity ^0.8.0;
import "forge-std/Test.sol";
import "../contracts/MyToken.sol";

contract MyTokenTest is Test {
    MyToken token;

    function setUp() public {
        token = new MyToken();
    }

    function testBalanceAfterMint() public {
        token.mint(address(this), 1000);
        assertEq(token.balanceOf(address(this)), 1000);
    }
}
```

### 3.5 交互式调用（cast）

查询链 ID：

```bash
cast chain-id
```

调用合约函数（只读）：

```bash
cast call <address> "totalSupply()"
```

发送交易：

```bash
cast send <address> "transfer(address,uint256)" 0x1234... 1000 \
  --private-key $PRIVATE_KEY
```

### 3.6 脚本与 REPL

```bash
dapp script script/Deploy.s.sol
```

或在 REPL 里执行：

```bash
dapp
> let token := Address(0x...);
> token.totalSupply();
```

### 3.7 与 CI 集成

在 `.github/workflows/ci.yml` 示例：

```yaml
name: CI
on: [push, pull_request]
jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: foundry-rs/foundry-toolchain@v1
      - run: forge test --no-match-path "test/mocks/**"
```

## 4. 进阶功能

- **多链配置**：在 `foundry.toml` 或 `.env.local` 配置 RPC URL、链 ID、代币信息。
- **代理合约**：使用 `forge deploy` 的 `upgradeable` 选项。
- **网络监视**：`cast watch --block --event` 实时查看事件。
- **自定义插件**：`forge plugin install <name>`，例如 `forge-optimism`。

## 5. 文档与社区

- 官方文档: <https://book.getfoundry.sh/>
- 示例项目: <https://github.com/foundry-rs/forge-template>
- Discord: <https://discord.gg/7x7u4w8dFj>
- Slack： Foundry 官方社区 <https://join.slack.com/t/foundry-community/shared_invite/...>

> 以上即为 Foundry 的主要特性、功能及典型使用方式。祝开发顺利！