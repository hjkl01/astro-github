---
title: call-center-ai
---

# Call Center AI

AI-powered call center solution with Azure and OpenAI GPT.

## Features

- **Enhanced communication and user experience**: Integrates inbound and outbound calls with a dedicated phone number, supports multiple languages and voice tones, and allows users to provide or receive information via SMS. Conversations are streamed in real-time to avoid delays, can be resumed after disconnections, and are stored for future reference.
- **Advanced intelligence and data management**: Leverages gpt-4.1 and gpt-4.1-nano for nuanced comprehension. It can discuss private and sensitive data, follows retrieval-augmented generation (RAG) best practices, understands domain-specific terms, generates automated to-do lists, filters inappropriate content, and detects jailbreak attempts.
- **Customization, oversight, and scalability**: Offers customizable prompts, feature flags, human agent fallback, call recording, and brand-specific custom voice. Deployed on Azure with containerized, serverless architecture for low maintenance and elastic scaling.
- **Cloud-native deployment**: Uses Azure Communication Services, Cognitive Services, and OpenAI resources for secure, rapid iteration.

## Usage

### API Call to Initiate a Call

Send a POST request to initiate a call:

```bash
curl --header 'Content-Type: application/json' \
  --request POST \
  --url https://xxx/call \
  --data '{
    "bot_company": "Contoso",
    "bot_name": "Amélie",
    "phone_number": "+11234567890",
    "task": "Help the customer with their digital workplace.",
    "agent_phone_number": "+33612345678",
    "claim": [
      {
        "name": "hardware_info",
        "type": "text"
      }
    ]
  }'
```

### Deployment

#### Prerequisites

- Azure CLI, Twilio CLI (optional), yq, Bash, Make
- Azure resources: Resource group, Communication Services, Phone number

#### Remote Deployment on Azure

1. Create `config.yaml` from `config-remote-example.yaml`
2. Run `az login`
3. Execute `make deploy name=my-rg-name`

#### Local Deployment

1. Install Rust, uv, run `make install`
2. Create `config.yaml` from `config-local-example.yaml`
3. Run `make deploy-bicep deploy-post name=my-rg-name`
4. Start tunnel: `make tunnel`
5. Run `make dev` for development

### Advanced Configuration

- Enable call recording by setting `recording_enabled` to `true` in App Configuration
- Customize languages, moderation levels, claim schema, prompts, etc.
- Integrate with AI Search for custom training data
- Use Twilio for SMS

### Monitoring

Application sends traces and metrics to Azure Application Insights for monitoring application behavior, LLM metrics, and custom metrics like call latency.

## Demo

A French demo is available on YouTube showcasing inbound calls, conversation storage, and data extraction.
