---
title: sim
---

# Sim

Open-source platform to build and deploy AI agent workflows.

## Features

- Build and deploy AI agent workflows in minutes
- Supports various AI models including OpenAI, Anthropic, Gemini, DeepSeek
- Low-code/no-code visual workflow editor using ReactFlow
- Knowledge bases with vector embeddings for semantic search
- Realtime collaboration with Socket.io
- Background job processing with Trigger.dev
- Remote code execution with E2B
- Supports local models via Ollama integration

## Usage

### Cloud-hosted

Visit [sim.ai](https://sim.ai) for the cloud-hosted version.

### Self-hosted Options

#### NPM Package (Quick Start)

```bash
npx simstudio
```

Access the application at [http://localhost:3000](http://localhost:3000)

**Note:** Requires Docker to be installed and running.

#### Docker Compose

```bash
git clone https://github.com/simstudioai/sim.git
cd sim
docker compose -f docker-compose.prod.yml up -d
```

Access at [http://localhost:3000](http://localhost:3000)

#### Using Local Models with Ollama

For running with local AI models without external APIs:

```bash
# With GPU support (downloads gemma3:4b model)
docker compose -f docker-compose.ollama.yml --profile setup up -d

# For CPU-only systems
docker compose -f docker-compose.ollama.yml --profile cpu --profile setup up -d
```

Add more models:

```bash
docker compose -f docker-compose.ollama.yml exec ollama ollama pull llama3.1:8b
```

#### Dev Containers

1. Open in VS Code with Remote - Containers extension
2. Run `bun run dev:full` to start both main app and realtime server

#### Manual Setup

**Requirements:**

- Bun runtime
- PostgreSQL 12+ with pgvector extension

1. Clone and install:

```bash
git clone https://github.com/simstudioai/sim.git
cd sim
bun install
```

2. Setup PostgreSQL with pgvector (choose one option):

**Docker (Recommended):**

```bash
docker run --name simstudio-db \
  -e POSTGRES_PASSWORD=your_password \
  -e POSTGRES_DB=simstudio \
  -p 5432:5432 -d \
  pgvector/pgvector:pg17
```

**Manual Installation:** Install PostgreSQL and pgvector extension.

3. Configure environment:

```bash
cd apps/sim
cp .env.example .env
# Set DATABASE_URL, BETTER_AUTH_SECRET, BETTER_AUTH_URL
```

4. Setup database:

```bash
cd packages/db
cp .env.example .env
# Set DATABASE_URL
bunx drizzle-kit migrate --config=./drizzle.config.ts
```

5. Start servers:

```bash
# Run both servers (recommended)
bun run dev:full

# Or separately:
bun run dev  # Main app
cd apps/sim && bun run dev:sockets  # Realtime server
```

## Tech Stack

- Framework: Next.js (App Router)
- Runtime: Bun
- Database: PostgreSQL with Drizzle ORM
- Authentication: Better Auth
- UI: Shadcn, Tailwind CSS
- State Management: Zustand
- Flow Editor: ReactFlow
- Realtime: Socket.io
- Background Jobs: Trigger.dev
- Remote Code Execution: E2B

## License

Apache License 2.0
