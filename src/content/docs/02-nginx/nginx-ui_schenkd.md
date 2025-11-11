---
title: nginx-ui
---

# nginx-ui 项目

## 项目地址

[https://github.com/schenkd/nginx-ui](https://github.com/schenkd/nginx-ui)

## 主要特性

Nginx UI allows you to access and modify the nginx configurations files without cli.

- Web-based interface for editing nginx configs
- Real-time preview and validation
- Supports common nginx modules like reverse proxy, load balancing, SSL/TLS
- Easy deployment with Docker
- Open source and free

## 主要功能

- Config editing via forms for server, location, upstream blocks
- Monitoring and logs integration
- Backup and restore
- Templates for common setups
- Multi-site management

## 用法

1. **Setup**:
   - Clone: `git clone https://github.com/schenkd/nginx-ui.git`
   - Install deps: npm/yarn
   - Run: `npm start` or Docker `docker run -p 8080:8080 schenkd/nginx-ui`

2. **UI**:
   - Access at `http://localhost:8080`
   - Connect to nginx conf dir

3. **Operations**:
   - Add/edit sites
   - Navigate modules (Servers > Locations)
   - Save, auto-reload nginx
   - View logs, test config

See README for details.
