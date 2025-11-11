---
title: nginx-admins-handbook
---

# nginx-admins-handbook 项目描述

**项目地址:** [https://github.com/trimstray/nginx-admins-handbook](https://github.com/trimstray/nginx-admins-handbook)

## 主要特性

- Comprehensive guide for improving NGINX performance, security, and other important things.
- Structured content with chapters on HTTP Basics, SSL/TLS Basics, NGINX Basics, Helpers, Base Rules, Debugging, Performance, Hardening, Reverse Proxy, Load Balancing, Others, Configuration Examples.
- Practical examples, cheatsheets, printable hardening posters, fully automatic installation scripts, static error pages generator, server names parser.
- Open source and free, community-driven.

## 主要功能

- **HTTP Basics**: Introduction to HTTP, features, HTTP/2, HTTP/3, URI vs URL, connection vs request, HTTP headers, HTTP methods, request/response structures, HTTP client, back-end architecture, useful video resources.
- **SSL/TLS Basics**: Introduction, TLS versions, TLS handshake, RSA and ECC keys/certificates, cipher suites, Diffie-Hellman, certificates, TLS SNI, verify SSL/TLS implementation, useful video resources.
- **NGINX Basics**: Directories and files, commands, processes (CPU pinning, shutdown), configuration syntax (comments, variables, directives, external files, measurement units, regex, highlighting), connection processing (event-driven, multiple processes, simultaneous connections, keep-alive, sendfile/tcp_nodelay/tcp_nopush), request processing stages, server blocks logic (handling connections, matching location, rewrite vs return, URL redirections, try_files, if/break/set, root vs alias, internal, external/internal redirects, allow/deny, uri vs request_uri), compression/decompression, hash tables (server names), log files (conditional, rotation, error levels, start time, body logging, upstream variables), reverse proxy (passing requests, trailing slashes, headers, response headers), load balancing algorithms (backend params, SSL upstreams, round robin, weighted, least connections, IP hash, generic hash, other methods), rate limiting (variables, directives/keys/zones, burst/nodelay), NAXSI WAF, OWASP ModSecurity CRS, core modules (geo), 3rd party modules (set_misc, geoip).
- **Helpers**: Installing from prebuilt packages (RHEL/CentOS, Debian/Ubuntu, FreeBSD), from source (automatic on RHEL/Debian/BSD, nginx package, dependencies, patches, 3rd party modules, configure options, compiler/linker, debugging symbols, SystemTap, installation examples), analyse configuration, monitoring (GoAccess, ngxtop), testing (build OpenSSL, send requests, multiple requests, SSL testing, OCSP, load testing with ab/wrk2/locust, TCP SYN flood, HTTP DoS), debugging (processes, memory, open files, segfault, dump config, configure args, module check, top IPs, top URLs, 4xx/5xx, 502 errors, requests per second, gzip check, worker processing, capture packets, dump memory, gdb, socket leaks), shell aliases, configuration snippets (server header removal, custom log formats, log only 4xx/5xx, basic auth, client cert, geo location, dynamic error pages, blocking/allowing IPs, referrer spam, user-agent, rate limiting, trailing slashes, HTTPS redirect, www prefix, proxy/rewrite, CORS, X-Forwarded-Proto), other snippets (recreate dir, temp backend, temp SSL backend, htpasswd, generate keys/CSR/certs, DH params, extract certs, verify certs, check matches).
- **Base Rules**: Organising config, format/prettify/indent, reload, separate listen 80/443, define listen address:port, prevent undefined server names, never hostname in listen/upstream, set headers properly, one SSL config per listen, use geo/map instead allow/deny, map all things, set global root, use return for redirects, configure log rotation, custom error pages, no duplicate index.
- **Debugging**: Custom log formats, debug mode, disable daemon/master/workers, core dumps, mirror module.
- **Performance**: Adjust workers, HTTP/2, SSL sessions, OCSP, exact server_name, avoid if with server_name, use $request_uri, try_files, return instead rewrite, PCRE JIT, cache connections, exact location match, limit_conn for speed.
- **Hardening**: Keep updated, unprivileged user, disable modules, protect resources, ACL rules, hide version/server, hide proxy headers, remove legacy headers, latest OpenSSL, TLS only, 2048 RSA/256 ECC, TLS 1.3/1.2, strong ciphers, secure ECDH, PFS, prevent 0-RTT replay, BEAST defense, CRIME/BREACH, HSTS, CSP, Referrer-Policy, X-Frame-Options, X-XSS-Protection, X-Content-Type-Options, Feature-Policy, reject unsafe methods, prevent caching sensitive, limit connections, buffer overflow control, slow HTTP DoS, set permissions.
- **Reverse Proxy**: Compatible pass directive, trailing slashes, $host for Host/X-Real-IP/X-Forwarded, X-Forwarded-For, no $scheme with X-Forwarded-Proto, pass Host/X-Real-IP/X-Forwarded, custom headers without X-, $request_uri in proxy_pass.
- **Load Balancing**: Tweak passive checks, no down by comments.
- **Others**: Correct cert chain, DNS CAA, security.txt, tcpdump for HTTP issues.
- **Configuration Examples**: Reverse proxy, HTTPS proxy, load balancing, multiple webapps, static sites, file server, CORS.

## 用法

1. **Clone the repository**: `git clone https://github.com/trimstray/nginx-admins-handbook.git`
2. **Read the handbook**: Open README.md or docs in the repository. It's structured with chapters like HTTP Basics, SSL/TLS Basics, NGINX Basics, etc.
3. **Apply configurations**: Copy examples to your nginx.conf, test with `nginx -t`, reload with `nginx -s reload`.
4. **Contribute**: Fork, edit, PR. Use with official NGINX docs.
5. **适用场景**: 适合初学者快速入门，或资深管理员参考高级优化。手册不包含实际代码运行环境，仅为参考文档。
