---
title: ore
---

# ORE

ORE is a crypto mining protocol built on Solana, enabling decentralized mining and staking of ORE tokens.

## Features

- **Mining**: Includes instructions for automating mining, claiming rewards (ORE and SOL), deploying SOL, initializing, resetting rounds, and more.
- **Staking**: Supports depositing and withdrawing ORE, claiming Seeker tokens, and claiming staking yield.
- **Admin Functions**: Allows burying transactions, wrapping SOL, setting admin authority, fee collector, and fee rates.
- **State Management**: Tracks automation configs, board state, global configs, miner states, rounds, Seeker claims, stakes, and treasury operations.

## Usage

### Building and Testing

To run the test suite using the Solana toolchain:

```bash
cargo test-sbf
```

For line coverage:

```bash
cargo llvm-cov
```

### API Overview

- **Consts**: Program constants.
- **Error**: Custom program errors.
- **Event**: Custom program events.
- **Instruction**: Declared instructions and arguments.

### Key Instructions

- Mining: Automate, Checkpoint, ClaimORE, ClaimSOL, Deploy, Initialize, Log, Reset.
- Staking: Deposit, Withdraw, ClaimSeeker, ClaimYield.
- Admin: Bury, Wrap, SetAdmin, SetFeeCollector, SetFeeRate.

For detailed implementation, refer to the [GitHub repository](https://github.com/regolith-labs/ore).
