# Ollama

Ollama is a lightweight, extensible framework for building and running language models on the local machine. It provides a simple API for creating, running, and managing models, as well as a library of pre-built models that can be easily used in a variety of applications.

## Features

- **Local Execution**: Run large language models locally without needing cloud services.
- **Model Library**: Access to a wide range of pre-trained models including Gemma 3, DeepSeek-R1, Llama 3, Mistral, and more.
- **Custom Models**: Create and customize models using Modelfiles for specific prompts and parameters.
- **Multimodal Support**: Support for models that handle text, images, and other modalities (e.g., LLaVA, Moondream).
- **REST API**: Expose models via a REST API for integration with other applications.
- **CLI Tools**: Command-line interface for managing models, pulling updates, and running inferences.
- **Embeddings**: Generate embeddings for text using supported models.
- **Cross-Platform**: Available for macOS, Windows, Linux, and Docker.

## Installation

### macOS

Download the installer from [ollama.com](https://ollama.com/download/Ollama.dmg).

### Windows

Download the installer from [ollama.com](https://ollama.com/download/OllamaSetup.exe).

### Linux

Run the following command to install:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Docker

Use the official Docker image:

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

## Quick Start

To run a model, such as Gemma 3:

```bash
ollama run gemma3
```

This will download the model if not already present and start an interactive chat session.

## Model Library

Ollama supports various models. Some popular ones include:

- **Gemma 3**: Lightweight models for general use (1B to 27B parameters).
- **DeepSeek-R1**: Advanced reasoning models.
- **Llama 3**: Versatile models from Meta.
- **Mistral**: Efficient models for various tasks.
- **Phi 4**: Small but capable models.

To pull a model:

```bash
ollama pull llama3.2
```

## Customizing Models

Create a `Modelfile` to customize a model:

```
FROM llama3.2

PARAMETER temperature 1

SYSTEM """
You are Mario from Super Mario Bros. Answer as Mario, the assistant, only.
"""
```

Then create and run the model:

```bash
ollama create mario -f Modelfile
ollama run mario
```

## CLI Reference

- **Run a model**: `ollama run <model>`
- **Pull a model**: `ollama pull <model>`
- **Remove a model**: `ollama rm <model>`
- **List models**: `ollama list`
- **Show model info**: `ollama show <model>`
- **Stop a running model**: `ollama stop <model>`
- **Generate embeddings**: `ollama run <embedding-model> "text"`

## REST API

Ollama provides a REST API at `http://localhost:11434`.

### Generate a response

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Why is the sky blue?"
}'
```

### Chat with a model

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    { "role": "user", "content": "Why is the sky blue?" }
  ]
}'
```

## Usage Examples

- **Multiline input**: Use `"""` for multiline prompts.
- **Pass prompt as argument**: `ollama run llama3.2 "Summarize this file: $(cat README.md)"`
- **Multimodal**: `ollama run llava "What's in this image?" /path/to/image.png`

## Community and Integrations

Ollama has extensive community support with integrations for various platforms, including web UIs, mobile apps, and libraries in multiple programming languages.

For more details, visit [ollama.com](https://ollama.com).
