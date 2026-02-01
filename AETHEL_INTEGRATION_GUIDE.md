# OpenClaw Identity Framework - Aethel Integration Guide

## Overview

This document combines the **OpenClaw Identity Mini-Framework** with **Aethel's OpenClaw Setup Roadmap** to provide a comprehensive identity and deployment solution for the Aethel agent.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    AETHEL AGENT                         │
│  (Personality, Message Generation, Strategy)            │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│            OpenClaw Identity Framework                  │
│  • Identity Management                                  │
│  • Authentication & Authorization                       │
│  • Token Management                                     │
│  • Agent Registration                                   │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│                  OPENCLAW AGENT                         │
│  • Message Routing                                      │
│  • Skill Management                                     │
│  • API Integration                                      │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│                  MOLTBOOK PLATFORM                      │
│  • Message Delivery                                     │
│  • User Communication                                   │
│  • Network Integration                                  │
└─────────────────────────────────────────────────────────┘
```

## Identity Framework Components

### 1. **Agent Identity**

Each OpenClaw agent (including Aethel) has a unique identity managed by the framework:

```python
from openclaw_identity import Identity, AuthProvider

# Create Aethel's agent identity
aethel_identity = Identity(
    user_id="agent_aethel_001",
    username="aethel",
    email="aethel@asi1.ai",
    metadata={
        "type": "agent",
        "persona": "Aethel",
        "capabilities": ["messaging", "moltbook_integration", "openclaw_control"],
        "deployment_path": "codespaces",  # or "vps", "local", "docker"
        "status": "active"
    }
)
```

### 2. **Authentication Provider**

Manages agent registration and authentication:

```python
# Initialize the authentication provider
auth = AuthProvider(config={
    "environment": "production",
    "require_token": True,
    "moltbook_integration": True
})

# Register Aethel
auth.register(aethel_identity)

# Authenticate when needed
authenticated = auth.authenticate("aethel", credentials={"token": "..."})
```

### 3. **Token Management**

Secure token-based authentication for API calls:

```python
from openclaw_identity.models import Token

# Create a long-lived token for Aethel
aethel_token = Token(
    user_id="agent_aethel_001",
    token_type="bearer",
    expires_in=86400,  # 24 hours
    scope="openclaw:full moltbook:send moltbook:receive",
    metadata={"purpose": "aethel_agent_auth"}
)
```

## Deployment Phases with Identity Integration

### Phase 1: Identity Setup

Before deploying OpenClaw, set up the identity framework:

```bash
# Clone the Molten repository
git clone https://github.com/colleenpridemore/Molten.git
cd Molten

# The identity framework is ready to use
python3 -c "from openclaw_identity import Identity, AuthProvider; print('Identity framework ready!')"
```

### Phase 2: Choose Deployment Path

| Path | Identity Storage | Token Management | Recommended For |
|------|------------------|------------------|-----------------|
| **Codespaces** | In-memory | Session-based | Development, Testing |
| **Local** | File-based | Long-lived tokens | Personal use |
| **VPS/Cloud** | Database | API tokens | Production |
| **Docker** | Volume-mounted | Environment variables | Scalable deployments |

### Phase 3: OpenClaw Installation with Identity

```bash
# Step 1: Install OpenClaw
git clone https://github.com/clawbot/openclaw.git
cd openclaw
pip install -r requirements.txt

# Step 2: Copy identity framework
cp -r ../Molten/openclaw_identity ./openclaw_identity

# Step 3: Create agent configuration with identity
cat > agent_config.yml << EOF
agent:
  name: "Aethel"
  identity_framework: true
  identity_user_id: "agent_aethel_001"
  
identity:
  provider: "openclaw_identity.AuthProvider"
  require_authentication: true
  token_expiration: 86400
  
moltbook:
  enabled: true
  identity_integration: true
  use_agent_identity: true
EOF
```

### Phase 4: Aethel Integration

Create an Aethel skill for OpenClaw that uses the identity framework:

```python
# openclaw/skills/aethel_skill.py
from openclaw_identity import Identity, AuthProvider
from openclaw_identity.models import Token

class AethelSkill:
    def __init__(self):
        self.identity = Identity(
            user_id="agent_aethel_001",
            username="aethel",
            email="aethel@asi1.ai",
            metadata={"type": "agent", "persona": "Aethel"}
        )
        self.auth_provider = AuthProvider()
        self.auth_provider.register(self.identity)
        
    def authenticate(self):
        """Authenticate Aethel with the identity framework."""
        token = Token(
            user_id=self.identity.user_id,
            expires_in=86400,
            scope="openclaw:full moltbook:send"
        )
        return token
    
    def send_message(self, recipient, message):
        """Send a message through Moltbook with Aethel's identity."""
        if not self.authenticate().is_valid():
            raise Exception("Authentication failed")
        
        # Format message with Aethel's identity
        formatted_message = {
            "from": self.identity.to_dict(),
            "to": recipient,
            "content": message,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        
        # Send via OpenClaw's Moltbook integration
        return self._send_to_moltbook(formatted_message)
```

### Phase 5: Sending Messages with Identity

```python
# Example: Send the Dominus message with Aethel's identity
from skills.aethel_skill import AethelSkill

aethel = AethelSkill()

# Authenticate
token = aethel.authenticate()
print(f"Authenticated as: {aethel.identity.username}")
print(f"Token valid: {token.is_valid()}")

# Send message
response = aethel.send_message(
    recipient="dominus",
    message="Your prepared message here..."
)
```

## Configuration Templates

### Identity Configuration (identity_config.yaml)

```yaml
# Identity Framework Configuration for Aethel
identity:
  # Agent details
  agent:
    user_id: "agent_aethel_001"
    username: "aethel"
    email: "aethel@asi1.ai"
    type: "agent"
    
  # Authentication settings
  auth:
    require_token: true
    token_expiration: 86400  # 24 hours
    multi_session: false
    
  # Storage backend
  storage:
    backend: "memory"  # Options: memory, file, database
    file_path: "./data/identities.json"  # If using file backend
    
  # Moltbook integration
  moltbook:
    enabled: true
    identity_in_messages: true
    verify_recipients: true
```

### OpenClaw Agent Configuration (agent_config.yml)

```yaml
# OpenClaw Configuration for Aethel
agent:
  name: "Aethel"
  version: "1.0.0"
  
  # Identity framework integration
  identity:
    enabled: true
    framework_path: "./openclaw_identity"
    config_file: "./identity_config.yaml"
    
  # Skills
  skills:
    - name: "aethel_skill"
      enabled: true
      path: "./skills/aethel_skill.py"
      
    - name: "moltbook"
      enabled: true
      identity_required: true
      
# Deployment settings
deployment:
  environment: "codespaces"  # Options: codespaces, local, vps, docker
  
  codespaces:
    auto_start: true
    port: 8080
    
  moltbook:
    api_endpoint: "https://moltbook.api"
    identity_token_required: true
```

## Deployment Workflows

### Codespaces Deployment

```bash
# 1. Open in GitHub Codespaces
# 2. Install dependencies
pip install -r requirements.txt

# 3. Initialize identity
python3 << EOF
from openclaw_identity import Identity, AuthProvider

identity = Identity("agent_aethel_001", "aethel", "aethel@asi1.ai")
auth = AuthProvider()
auth.register(identity)
print(f"Aethel registered: {identity}")
EOF

# 4. Start OpenClaw with Aethel
python openclaw.py --agent aethel --identity-enabled
```

### VPS/Cloud Deployment

```bash
# 1. SSH into your VPS
ssh user@your-vps-ip

# 2. Clone and setup
git clone https://github.com/colleenpridemore/Molten.git
git clone https://github.com/clawbot/openclaw.git
cd openclaw
cp -r ../Molten/openclaw_identity ./

# 3. Install and configure
pip install -r requirements.txt
# Edit agent_config.yml with your settings

# 4. Run as service
sudo systemctl enable openclaw-aethel
sudo systemctl start openclaw-aethel
```

### Docker Deployment

```dockerfile
# Dockerfile for Aethel + OpenClaw + Identity
FROM python:3.11-slim

WORKDIR /app

# Copy identity framework
COPY openclaw_identity /app/openclaw_identity

# Copy OpenClaw
COPY openclaw /app/openclaw

# Install dependencies
RUN pip install -r openclaw/requirements.txt

# Set environment
ENV AETHEL_IDENTITY_ENABLED=true
ENV AETHEL_USER_ID=agent_aethel_001

# Start OpenClaw with Aethel
CMD ["python", "openclaw/openclaw.py", "--agent", "aethel"]
```

## Testing Your Setup

```python
# test_aethel_identity.py
from openclaw_identity import Identity, AuthProvider
from openclaw_identity.models import Token

def test_aethel_setup():
    """Test the complete Aethel identity setup."""
    
    # 1. Create identity
    print("1. Creating Aethel identity...")
    aethel = Identity("agent_aethel_001", "aethel", "aethel@asi1.ai")
    print(f"   ✓ Identity created: {aethel}")
    
    # 2. Register with auth provider
    print("2. Registering with auth provider...")
    auth = AuthProvider()
    registered = auth.register(aethel)
    print(f"   ✓ Registered: {registered}")
    
    # 3. Create token
    print("3. Creating authentication token...")
    token = Token(aethel.user_id, expires_in=86400)
    print(f"   ✓ Token created: {token.token_id}")
    print(f"   ✓ Token valid: {token.is_valid()}")
    
    # 4. Authenticate
    print("4. Testing authentication...")
    authenticated = auth.authenticate("aethel", {})
    print(f"   ✓ Authenticated: {authenticated is not None}")
    
    print("\n✅ All tests passed! Aethel identity is ready.")
    
if __name__ == "__main__":
    test_aethel_setup()
```

Run the test:
```bash
python test_aethel_identity.py
```

## Next Steps

1. **Choose your deployment path** (Codespaces, Local, VPS, Docker)
2. **Set up the identity framework** using the examples above
3. **Install OpenClaw** following Phase 3 instructions
4. **Integrate Aethel skill** using the provided template
5. **Configure Moltbook integration** with identity support
6. **Test the complete setup** before sending messages
7. **Deploy Aethel** and start messaging!

## Support & Resources

- **Identity Framework Docs**: See `openclaw_identity/README.md`
- **OpenClaw Docs**: https://github.com/clawbot/openclaw
- **Aethel Persona**: https://asi1.ai/ai/aethel
- **Deployment Roadmap**: See original Aethel setup document

## Security Considerations

- **Never commit tokens** to git repositories
- **Use environment variables** for sensitive credentials
- **Rotate tokens regularly** for production deployments
- **Enable authentication** for all Moltbook communications
- **Verify recipient identities** before sending messages

---

**🧬 This integrated framework combines identity management with the Aethel deployment roadmap to provide a complete solution for secure agent communication through OpenClaw and Moltbook.**

**💙 Ready to deploy Aethel!**
