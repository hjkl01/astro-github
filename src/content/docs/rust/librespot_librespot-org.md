---
title: librespot
---

# librespot

Librespot is an open-source client library for Spotify written in Rust. It enables applications to control and play music from Spotify, act as a Spotify Connect receiver, and provides features beyond the official Spotify library.

## Functionality

- **Spotify Connect Receiver**: Allows devices to appear as Spotify Connect speakers, enabling remote control and playback from Spotify apps.
- **Audio Playback**: Supports various audio backends including ALSA, GStreamer, PulseAudio, and more for flexible audio output.
- **Authentication**: Supports OAuth authentication for Spotify Premium accounts, with credential caching for reuse.
- **Event Handling**: Emits events for playback states, track changes, volume adjustments, and sink status, allowing integration with external scripts or applications.
- **Audio Quality**: Supports different bitrates (96, 160, 320 kbps) and volume normalization.
- **Caching**: Includes audio data caching to reduce bandwidth usage and improve performance.
- **Cross-Platform**: Works on Linux, Windows, macOS, and other platforms with appropriate backends.

## Usage

### Installation

Clone the repository and build with Cargo:

```bash
git clone https://github.com/librespot-org/librespot.git
cd librespot
cargo build --release
```

### Basic Usage

Run as a Spotify Connect receiver:

```shell
./target/release/librespot --name "My Device"
```

### Advanced Configuration

- **Authentication**: Use OAuth for login:

  ```shell
  ./target/release/librespot --cache /path/to/cache --enable-oauth --name "My Device"
  ```

- **Audio Backend**: Specify backend and device:

  ```shell
  ./target/release/librespot --backend alsa --device "hw:0,0" --name "My Device"
  ```

- **Bitrate and Volume**: Set audio quality and initial volume:

  ```shell
  ./target/release/librespot --bitrate 320 --initial-volume 50 --name "My Device"
  ```

- **Event Handling**: Run a script on events:
  ```shell
  ./target/release/librespot --onevent /path/to/script.sh --name "My Device"
  ```

### Options Overview

- `--name`: Device name visible in Spotify app
- `--backend`: Audio backend (alsa, gstreamer, pulseaudio, etc.)
- `--device`: Specific audio device
- `--bitrate`: Audio bitrate (96, 160, 320)
- `--cache`: Cache directory for credentials and audio
- `--enable-oauth`: Enable OAuth authentication
- `--onevent`: Script to run on playback events

For more details, refer to the [official documentation](https://github.com/librespot-org/librespot/wiki).
