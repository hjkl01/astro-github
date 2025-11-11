---
title: evals
---

# Evals

Evals is a framework for evaluating large language models (LLMs) and LLM systems, providing an open-source registry of benchmarks. It allows users to test different dimensions of OpenAI models and create custom evals for specific use cases.

## Features

- **Framework for Evaluation**: Provides tools to evaluate LLMs and systems built with LLMs.
- **Registry of Benchmarks**: Includes a collection of existing evals to assess model performance.
- **Custom Evals**: Supports writing private or public evals using your own data without exposing sensitive information.
- **Integration**: Can be run directly in the OpenAI Dashboard or locally.
- **Logging Options**: Supports logging results to Snowflake databases.

## Usage

### Setup

1. Obtain an OpenAI API key from [OpenAI Platform](https://platform.openai.com/account/api-keys).
2. Set the `OPENAI_API_KEY` environment variable.
3. Install the package: `pip install evals` (for running existing evals) or clone the repo and install with `pip install -e .` (for creating evals).

### Downloading Evals

If cloning the repo, use Git-LFS to fetch data:

```bash
cd evals
git lfs fetch --all
git lfs pull
```

### Running Evals

Run existing evals using the framework. Refer to `docs/run-evals.md` for full instructions. Example:

```bash
oaieval <eval_name> <completion_fn>
```

### Writing Evals

Create custom evals by following `docs/build-eval.md`. Use YAML for configuration and JSON for data. Examples are in the `examples` folder.

For more details, visit the [GitHub repository](https://github.com/openai/evals).
