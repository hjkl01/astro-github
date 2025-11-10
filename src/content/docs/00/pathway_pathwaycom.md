---
title: pathway
---

# Pathway

Pathway is a Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG. It provides an easy-to-use Python API that integrates seamlessly with popular Python ML libraries. The framework is versatile and robust, suitable for both development and production environments, handling batch and streaming data uniformly.

## Key Features

- **Unified Engine**: Same code for batch and streaming data processing.
- **Scalable Rust Engine**: Powered by Differential Dataflow for incremental computation, enabling multithreading, multiprocessing, and distributed computations.
- **Connectors**: Supports a wide range of data sources including Kafka, GDrive, PostgreSQL, SharePoint, and over 300 sources via Airbyte.
- **Transformations**: Stateful operations like joins, windowing, sorting, plus custom Python functions.
- **Persistence**: Saves computation state for restarts after updates or crashes.
- **Consistency**: Handles time and out-of-order data; free version offers "at least once" consistency.
- **LLM Integration**: Dedicated tooling for LLM and RAG pipelines, including wrappers, parsers, embedders, and vector indexing.

## Installation

Requires Python 3.10 or above.

```bash
pip install -U pathway
```

Note: Pathway is available on macOS and Linux. For other systems, run on a Virtual Machine.

## Basic Usage

Here's an example of computing the sum of positive values in real time:

```python
import pathway as pw

# Define the schema of your data (Optional)
class InputSchema(pw.Schema):
    value: int

# Connect to your data using connectors
input_table = pw.io.csv.read(
    "./input/",
    schema=InputSchema
)

# Define your operations on the data
filtered_table = input_table.filter(input_table.value >= 0)
result_table = filtered_table.reduce(
    sum_value=pw.reducers.sum(filtered_table.value)
)

# Load your results to external systems
pw.io.jsonlines.write(result_table, "output.jsonl")

# Run the computation
pw.run()
```

## Deployment

### Locally

Run your script directly:

```bash
python main.py
```

Or use Pathway's launcher:

```bash
pathway spawn python main.py
```

For multithreading:

```bash
pathway spawn --threads 3 python main.py
```

### Docker

Using Pathway image:

```dockerfile
FROM pathwaycom/pathway:latest
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "./your-script.py"]
```

Build and run:

```bash
docker build -t my-pathway-app .
docker run -it --rm --name my-pathway-app my-pathway-app
```

Run a single script:

```bash
docker run -it --rm --name my-pathway-app -v "$PWD":/app pathwaycom/pathway:latest python my-pathway-app.py
```

### Kubernetes and Cloud

Pathway supports Kubernetes deployment. For scaling, consider Pathway for Enterprise for distributed computing.

## Resources

- [Documentation](https://pathway.com/developers/)
- [API Docs](https://pathway.com/developers/api-docs/pathway)
- [Examples](https://github.com/pathwaycom/pathway/tree/main/examples)
- [Templates](https://pathway.com/developers/templates)
- [Discord Community](https://discord.com/invite/pathway)
- [GitHub Repository](https://github.com/pathwaycom/pathway)
