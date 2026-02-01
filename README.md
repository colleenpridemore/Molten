# Molten
AI  OG's

## OpenClaw Identity Framework for Aethel

This repository contains the **OpenClaw Identity Mini-Framework**, a lightweight identity management system designed for use by the Aethel agent with OpenClaw and Moltbook integration.

### 🧬 What's New: Aethel Integration

The framework now includes full support for Aethel agent deployment with:

- **Agent Identity Management**: Complete identity system for Aethel
- **OpenClaw Integration**: Ready-to-use skill for OpenClaw deployment
- **Moltbook Communication**: Authenticated messaging capabilities
- **Deployment Guides**: Codespaces, VPS, Local, and Docker deployment paths

### Quick Start

```python
from openclaw_identity.aethel_skill import AethelSkill

# Initialize Aethel
aethel = AethelSkill(config={"deployment": "codespaces"})

# Authenticate
token = aethel.authenticate()

# Send a message
response = aethel.send_to_moltbook(
    recipient="dominus",
    message="Your message here"
)
```

### Documentation

- **[Aethel Integration Guide](AETHEL_INTEGRATION_GUIDE.md)** - Complete deployment and integration guide
- **[Identity Framework README](openclaw_identity/README.md)** - Core framework documentation
- **[Aethel Skill Documentation](openclaw_identity/aethel_skill.py)** - Agent skill implementation

### Components

1. **Core Identity Framework** - User identity and authentication management
2. **Aethel Skill** - OpenClaw skill for Aethel agent operations  
3. **Token Management** - Secure authentication tokens
4. **Validation Utilities** - Input validation for emails and usernames

### Testing Aethel Integration

```bash
# Test the Aethel skill
python3 openclaw_identity/aethel_skill.py
```

---

**💙 Ready to deploy Aethel with OpenClaw!** 🧬
