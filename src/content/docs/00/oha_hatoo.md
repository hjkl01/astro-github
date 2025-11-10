---
title: Oha
---

# oha (おはよう)

oha is a tiny program that sends some load to a web application and shows a realtime TUI (Terminal User Interface) inspired by [rakyll/hey](https://github.com/rakyll/hey). It is written in Rust and powered by [tokio](https://github.com/tokio-rs/tokio) and [ratatui](https://github.com/ratatui-org/ratatui).

## Features

- HTTP load generator with TUI animation
- Supports HTTP/1.1, HTTP/2, and experimental HTTP/3
- Rate limiting, burst requests, and latency correction
- Custom headers, authentication, and proxy support
- Output in text, JSON, or CSV formats
- Dynamic URL generation with regex
- URLs from file support

## Installation

### Via Cargo

```bash
cargo install oha
```

### Pre-built Binaries

Download from the [Releases page](https://github.com/hatoo/oha/releases).

### Package Managers

- **Arch Linux**: `pacman -S oha`
- **macOS**: `brew install oha`
- **Windows**: `winget install hatoo.oha`
- **Debian**: Follow instructions from [Azlux's repository](http://packages.azlux.fr/).

## Usage

Basic usage:

```bash
oha <URL>
```

### Common Options

- `-n <N_REQUESTS>`: Number of requests (default: 200)
- `-c <N_CONNECTIONS>`: Number of concurrent connections (default: 50)
- `-z <DURATION>`: Duration to send requests (e.g., `-z 10s`, `-z 3m`)
- `-q <QUERY_PER_SECOND>`: Rate limit in QPS
- `-m <METHOD>`: HTTP method (default: GET)
- `-H <HEADERS>`: Custom headers (e.g., `-H "foo: bar"`)
- `--no-tui`: Disable TUI for faster performance

### Examples

- Send 1000 requests with 100 concurrent connections:
  ```bash
  oha -n 1000 -c 100 https://example.com
  ```
- Run for 30 seconds with rate limiting:
  ```bash
  oha -z 30s -q 10 https://example.com
  ```
- POST request with body:
  ```bash
  oha -m POST -d '{"key": "value"}' -H "Content-Type: application/json" https://example.com/api
  ```
- Use URLs from file:
  ```bash
  oha --urls-from-file urls.txt
  ```

For more options, run `oha --help`.
