---
title: VectorChord
---

# VectorChord

VectorChord is a PostgreSQL extension for scalable, high-performance, and disk-efficient vector similarity search. It serves as the successor to pgvecto.rs, offering better stability and performance.

## Features

- **Enhanced Performance**: Up to 5x faster queries, 16x higher insert throughput, and 16x quicker index building compared to pgvector's HNSW implementation.
- **Affordable Vector Search**: Query 100 million 768-dimensional vectors using just 32GB of memory, achieving 35ms P50 latency with top10 recall@95%.
- **Seamless Integration**: Fully compatible with pgvector data types and syntax, providing optimal defaults without manual parameter tuning.
- **Accelerated Index Build**: Uses IVF for external index building (e.g., on GPU) combined with RaBitQ compression for efficient storage and autonomous reranking.
- **Long Vector Support**: Supports vectors up to 60,000 dimensions, enabling use of high-dimensional models like text-embedding-3-large.
- **Scalability**: Based on horizontal expansion, easily scales to 10,000+ QPS for 5M/100M 768-dimensional vectors with top10 recall@90%.
- **Production Proven**: Handles 3 billion+ vectors in production environments.

## Usage

### Quick Start with Docker

Run the Docker container:

```bash
docker run \
  --name vectorchord-demo \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -d ghcr.io/tensorchord/vchord-postgres:pg18-v0.5.3
```

Connect to the database:

```bash
psql -h localhost -p 5432 -U postgres
```

### Basic Operations

1. Create the extension:

```sql
CREATE EXTENSION IF NOT EXISTS vchord CASCADE;
```

2. Create a table with vector column:

```sql
CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));
```

3. Insert sample data:

```sql
INSERT INTO items (embedding) SELECT ARRAY[random(), random(), random()]::real[] FROM generate_series(1, 1000);
```

4. Create an index:

```sql
CREATE INDEX ON items USING vchordrq (embedding vector_l2_ops);
```

5. Perform vector search:

```sql
SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

For more advanced usage, refer to the [official documentation](https://docs.vectorchord.ai/vectorchord/).
