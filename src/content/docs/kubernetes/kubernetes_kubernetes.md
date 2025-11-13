---
title: kubernetes
---

# Kubernetes (K8s)

Kubernetes, also known as K8s, is an open-source system for managing containerized applications across multiple hosts. It provides basic mechanisms for the deployment, maintenance, and scaling of applications.

## Features

- **Container Orchestration**: Automates the deployment, scaling, and management of containerized applications.
- **Scalability**: Handles large-scale production workloads, based on Google's Borg system.
- **Portability**: Runs on various platforms and cloud providers.
- **Extensibility**: Supports custom resources and integrations via APIs.
- **Community-Driven**: Hosted by the Cloud Native Computing Foundation (CNCF).

## Usage

### Getting Started

To start using Kubernetes:

1. Visit the official documentation at [kubernetes.io](https://kubernetes.io).
2. Take a free course on [Scalable Microservices with Kubernetes](https://www.udacity.com/course/scalable-microservices-with-kubernetes--ud615).

### Developing Kubernetes

If you want to build Kubernetes from source:

#### With Go Environment

```bash
git clone https://github.com/kubernetes/kubernetes
cd kubernetes
make
```

#### With Docker Environment

```bash
git clone https://github.com/kubernetes/kubernetes
cd kubernetes
make quick-release
```

For more details, see the [developer's documentation](https://git.k8s.io/community/contributors/devel#readme).

### Support and Community

- **Troubleshooting**: Start with the [troubleshooting guide](https://kubernetes.io/docs/tasks/debug/).
- **Community Meetings**: Check the [Kubernetes Calendar](https://www.kubernetes.dev/resources/calendar/).
- **User Case Studies**: Explore real-world use cases at [kubernetes.io/case-studies/](https://kubernetes.io/case-studies/).

Kubernetes is governed by principles and processes outlined in the [Kubernetes Community](https://github.com/kubernetes/community/blob/master/governance.md) and [Steering Committee](https://github.com/kubernetes/steering) repositories.
