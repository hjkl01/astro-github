---
title: turborepo
---

# Turborepo

Turborepo is a high-performance build system for JavaScript and TypeScript codebases, written in Rust.

## Features

- **Task Caching**: Caches task outputs to avoid redundant work.
- **Dependency Graph**: Understands task dependencies for efficient execution.
- **Parallel Execution**: Runs independent tasks simultaneously.
- **Remote Caching**: Shares cache with team members.
- **Daemon Process**: Background process for performance optimization.
- **Watch Mode**: Automatically re-runs tasks on file changes.
- **Code Generation**: Uses generators for scaffolding code.

## Installation

Install Turborepo as a development dependency:

```bash
pnpm add turbo --save-dev --ignore-workspace-root-check
# or
yarn add turbo --dev --ignore-workspace-root-check
# or
npm install turbo --save-dev
# or
bun install turbo --dev
```

## Usage

### Configuration

Create a `turbo.json` file to define tasks:

```json
{
  "$schema": "https://turborepo.com/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", "!.next/cache/**"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

### Running Tasks

Run tasks with:

```bash
turbo run build
turbo run dev
```

### Watch Mode

Enable watch mode to re-run tasks on changes:

```bash
turbo watch dev lint test
```

### Other Commands

- `turbo query`: Query the dependency graph.
- `turbo telemetry enable/disable`: Manage telemetry.

For more details, visit [turborepo.com](https://turborepo.com).
