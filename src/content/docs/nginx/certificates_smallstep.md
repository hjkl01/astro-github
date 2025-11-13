---
title: certificates
---

# step-ca

🛡️ 一个私有证书颁发机构 (X.509 & SSH) & ACME 服务器，用于安全自动证书管理，让您可以在任何地方使用 TLS 和 SSH SSO。

## Features

### 🦾 A fast, stable, flexible private CA

Setting up a _public key infrastructure_ (PKI) is out of reach for many small teams. `step-ca` makes it easier.

- Choose key types (RSA, ECDSA, EdDSA) and lifetimes to suit your needs
- [Short-lived certificates](https://smallstep.com/blog/passive-revocation.html) with automated enrollment, renewal, and passive revocation
- Can operate as [an online intermediate CA for an existing root CA](https://smallstep.com/docs/tutorials/intermediate-ca-new-ca)
- [Badger, BoltDB, Postgres, and MySQL database backends](https://smallstep.com/docs/step-ca/configuration#databases)

### ⚙️ Many ways to automate

There are several ways to authorize a request with the CA and establish a chain of trust that suits your flow.

You can issue certificates in exchange for:

- [ACME challenge responses](#your-own-private-acme-server) from any ACMEv2 client
- [OAuth OIDC single sign-on tokens](https://smallstep.com/blog/easily-curl-services-secured-by-https-tls.html), eg:
  - ID tokens from Okta, GSuite, Azure AD, Auth0.
  - ID tokens from an OAuth OIDC service that you host, like [Keycloak](https://www.keycloak.org/) or [Dex](https://github.com/dexidp/dex)
- [Cloud instance identity documents](https://smallstep.com/blog/embarrassingly-easy-certificates-on-aws-azure-gcp/), for VMs on AWS, GCP, and Azure
- [Single-use, short-lived JWK tokens](https://smallstep.com/docs/step-ca/provisioners#jwk) issued by your CD tool — Puppet, Chef, Ansible, Terraform, etc.
- A trusted X.509 certificate (X5C provisioner)
- A host certificate from your Nebula network
- A SCEP challenge (SCEP provisioner)
- An SSH host certificates needing renewal (the SSHPOP provisioner)

### 🏔 Your own private ACME server

ACME is the protocol used by Let's Encrypt to automate the issuance of HTTPS certificates. It's _super easy_ to issue certificates to any ACMEv2 ([RFC8555](https://tools.ietf.org/html/rfc8555)) client.

- [Use ACME in development & pre-production](https://smallstep.com/blog/private-acme-server/#local-development--pre-production)
- Supports the most popular [ACME challenge types](https://letsencrypt.org/docs/challenge-types/):
  - For `http-01`, place a token at a well-known URL to prove that you control the web server
  - For `dns-01`, add a `TXT` record to prove that you control the DNS record set
  - For `tls-alpn-01`, respond to the challenge at the TLS layer ([as Caddy does](https://caddy.community/t/caddy-supports-the-acme-tls-alpn-challenge/4860)) to prove that you control the web server
- Works with any ACME client. We've written examples for:
  - [certbot](https://smallstep.com/docs/tutorials/acme-protocol-acme-clients#certbot)
  - [acme.sh](https://smallstep.com/docs/tutorials/acme-protocol-acme-clients#acmesh)
  - [win-acme](https://smallstep.com/docs/tutorials/acme-protocol-acme-clients#win-acme)
  - [Caddy](https://smallstep.com/docs/tutorials/acme-protocol-acme-clients#caddy-v2)
  - [Traefik](https://smallstep.com/docs/tutorials/acme-protocol-acme-clients#traefik)
  - [Apache](https://smallstep.com/docs/tutorials/acme-protocol-acme-clients#apache)
  - [nginx](https://smallstep.com/docs/tutorials/acme-protocol-acme-clients#nginx)
- Get certificates programmatically using ACME, using these libraries:
  - [`lego`](https://github.com/go-acme/lego) for Golang ([example usage](https://smallstep.com/docs/tutorials/acme-protocol-acme-clients#golang))
  - certbot's [`acme` module](https://github.com/certbot/certbot/tree/master/acme) for Python ([example usage](https://smallstep.com/docs/tutorials/acme-protocol-acme-clients#python))
  - [`acme-client`](https://github.com/publishlab/node-acme-client) for Node.js ([example usage](https://smallstep.com/docs/tutorials/acme-protocol-acme-clients#node))
- Our own [`step` CLI tool](https://github.com/smallstep/cli) is also an ACME client!

### 👩🏽‍💻 An online SSH Certificate Authority

- Delegate SSH authentication to `step-ca` by using [SSH certificates](https://smallstep.com/blog/use-ssh-certificates/) instead of public keys and `authorized_keys` files
- For user certificates, [connect SSH to your single sign-on provider](https://smallstep.com/blog/diy-single-sign-on-for-ssh/), to improve security with short-lived certificates and MFA (or other security policies) via any OAuth OIDC provider.
- For host certificates, improve security, [eliminate TOFU warnings](https://smallstep.com/blog/use-ssh-certificates/), and set up automated host certificate renewal.

### 🤓 A general purpose PKI tool, via [`step` CLI](https://github.com/smallstep/cli) [integration](https://smallstep.com/docs/step-cli/reference/ca/)

- Generate key pairs where they're needed so private keys are never transmitted across the network
- [Authenticate and obtain a certificate](https://smallstep.com/docs/step-cli/reference/ca/certificate/) using any provisioner supported by `step-ca`
- Securely [distribute root certificates](https://smallstep.com/docs/step-cli/reference/ca/root/) and [bootstrap](https://smallstep.com/docs/step-cli/reference/ca/bootstrap/) PKI relying parties
- [Renew](https://smallstep.com/docs/step-cli/reference/ca/renew/) and [revoke](https://smallstep.com/docs/step-cli/reference/ca/revoke/) certificates issued by `step-ca`
- [Install root certificates](https://smallstep.com/docs/step-cli/reference/ca/root/) on your machine and browsers, so your CA is trusted
- [Inspect](https://smallstep.com/docs/step-cli/reference/certificate/inspect/) and [lint](https://smallstep.com/docs/step-cli/reference/certificate/lint/) certificates

## Installation

See our installation docs [here](https://smallstep.com/docs/step-ca/installation).
