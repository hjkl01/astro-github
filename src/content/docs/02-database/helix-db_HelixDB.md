---
title: Helix Db
---

# HelixDB

HelixDB is an open-source graph-vector database built from scratch in Rust. It provides a unified platform for building AI applications, eliminating the need for separate databases for application data, vectors, graphs, and application layers.

## Key Features

- **Graph-Vector Data Model**: Primarily operates with graph + vector data, but also supports KV, documents, and relational data.
- **Built-in MCP Tools**: Allows agents to discover data and traverse graphs.
- **Built-in Embeddings**: Use the `Embed` function to vectorize text without pre-processing.
- **RAG Tooling**: Includes vector search, keyword search, and graph traversals for RAG applications.
- **Secure by Default**: Private by default, accessible only through compiled HelixQL queries.
- **Ultra-Low Latency**: Built in Rust with LMDB storage engine.
- **Type-Safe Queries**: HelixQL is 100% type-safe.

## Getting Started

### Install Helix CLI

```bash
curl -sSL "https://install.helix-db.com" | bash
```

### Initialize a Project

```bash
mkdir <path-to-project> && cd <path-to-project>
helix init
```

### Write Queries

Edit the generated `.hx` files to define your schema and queries. For example:

```sql
N::User {
   INDEX name: String,
   age: U32
}

QUERY getUser(user_name: String) =>
   user <- N<User>({name: user_name})
   RETURN user
```

### Check and Deploy

```bash
helix check  # Optional: Verify queries compile
helix push dev  # Deploy to API endpoints
```

### Use with SDKs

Install and use the TypeScript or Python SDK to interact with your deployed queries.

**TypeScript Example:**

```typescript
import HelixDB from 'helix-ts';

const client = new HelixDB();

await client.query('addUser', {
  name: 'John',
  age: 20,
});

const user = await client.query('getUser', {
  user_name: 'John',
});

console.log(user);
```

For more details, visit the [official documentation](https://docs.helix-db.com).
