---
title: ALVR
---

# ALVR

ALVR (Air Light VR) is an open-source wireless VR headset streaming software that enables streaming VR games from a PC to standalone VR headsets like Oculus Quest, Meta Quest, and Pico over Wi-Fi, providing a wireless PC VR experience.

## Features

- Wireless streaming of VR content from PC to VR headsets
- Support for various VR headsets including Oculus Quest, Meta Quest, and Pico
- Low-latency video and audio streaming
- Compatible with SteamVR
- Cross-platform support (Windows, Linux)
- Customizable video settings (resolution, bitrate, codec)

## Usage

1. **Install ALVR Server on PC**:
   - Download the latest release from the GitHub repository
   - For Windows: Extract `alvr_streamer_windows.zip` and run the executable
   - For Linux: Extract `alvr_streamer_linux.tar.gz` and run `bin/alvr_dashboard`
   - Alternatively, use the ALVR Launcher for easier version management

2. **Install ALVR Client on Headset**:
   - Enable developer mode on your VR headset
   - Install the ALVR APK using SideQuest or directly via ADB
   - For Quest/Pico: Download from SideQuest store

3. **Setup and Connection**:
   - Launch ALVR dashboard on PC
   - Ensure PC and headset are on the same network
   - In ALVR dashboard, add the headset device (it should auto-discover or enter IP manually)
   - Configure audio settings (may require Virtual Audio Cable on Windows)

4. **Streaming**:
   - Launch SteamVR on PC
   - Put on your VR headset and launch ALVR app
   - Start VR games through SteamVR - they will stream wirelessly to your headset

## Requirements

- PC with compatible GPU (NVIDIA, AMD, or Intel with proper drivers)
- VR headset (Quest, Quest 2, Quest 3, Pico, etc.)
- Stable Wi-Fi network (5GHz recommended for better performance)
- SteamVR installed on PC

For detailed installation guides and troubleshooting, refer to the [ALVR Wiki](https://github.com/alvr-org/ALVR/wiki).
