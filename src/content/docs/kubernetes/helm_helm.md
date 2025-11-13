---
title: Helm
---

# Helm

Helm is the Kubernetes Package Manager, a tool that streamlines installing and managing Kubernetes applications. It acts like apt/yum/homebrew for Kubernetes, allowing you to define, install, and upgrade even the most complex Kubernetes applications.

## Functionality

Helm manages "Charts," which are packages of pre-configured Kubernetes resources. Key features include:

- **Package Management**: Find and use popular software packaged as Helm Charts from repositories like Artifact Hub.
- **Application Sharing**: Share your own applications as reusable Helm Charts.
- **Reproducible Builds**: Create consistent deployments of Kubernetes applications.
- **Manifest Management**: Intelligently manage Kubernetes manifest files with templating.
- **Release Management**: Manage releases of Helm packages, including upgrades, rollbacks, and uninstalls.

Helm operates by rendering templates (which contain Kubernetes manifests) and communicating with the Kubernetes API. Charts consist of at least a `Chart.yaml` file describing the package and one or more templates.

## Usage

### Installation

1. **Binary Download**: Download the latest Helm client from the [Releases page](https://github.com/helm/helm/releases/latest), unpack the binary, and add it to your PATH.

2. **Package Managers**:
   - Homebrew: `brew install helm`
   - Chocolatey: `choco install kubernetes-helm`
   - Winget: `winget install Helm.Helm`
   - Scoop: `scoop install helm`
   - Snapcraft: `snap install helm --classic`
   - Flox: `flox install kubernetes-helm`

### Getting Started

- Follow the [Quick Start Guide](https://helm.sh/docs/intro/quickstart/) to begin using Helm.
- Refer to the [complete documentation](https://helm.sh/docs) for detailed usage instructions.

### Basic Commands

- `helm install`: Install a chart
- `helm upgrade`: Upgrade a release
- `helm rollback`: Roll back to a previous release
- `helm uninstall`: Uninstall a release
- `helm list`: List releases
- `helm repo add`: Add a chart repository
- `helm search`: Search for charts

### Chart Development

To create your own charts:

1. Use `helm create <chart-name>` to scaffold a new chart.
2. Edit the `Chart.yaml` and templates in the `templates/` directory.
3. Package with `helm package` and share via repositories.

## Community and Support

- **Slack Channels**: #helm-users, #helm-dev, #charts on Kubernetes Slack
- **Mailing List**: [Helm Mailing List](https://lists.cncf.io/g/cncf-helm)
- **Developer Calls**: Thursdays at 9:30-10:00 Pacific
- **Contributing**: See [Contributing Guide](https://github.com/helm/helm/blob/main/CONTRIBUTING.md)

Helm is maintained by the CNCF and follows semantic versioning for stable releases.
