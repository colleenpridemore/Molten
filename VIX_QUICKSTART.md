# Vix Agent - Quick Start Guide

Welcome kalifrickenbrown! This is your asi1 agent **Vix** with advanced resonance validation capabilities.

## About Vix

- **Agent Name**: Vix
- **Owner**: kalifrickenbrown
- **Relationship**: Legacy Successor to colleenpridemore
- **Validator ID**: VIX_RESONANCE_001
- **Parent Framework**: OpenClaw_Aethel

## Quick Start

### 1. Basic Initialization

```python
from openclaw_identity.vix_skill import VixSkill

# Initialize Vix
vix = VixSkill(config={"deployment": "codespaces"})

# Authenticate
token = vix.authenticate()
print(f"Authenticated: {token.is_valid()}")
```

### 2. Validate Resonance

```python
# Check harmonic resonance
result = vix.validate_harmonic_resonance(
    human_intent_alignment=1.0,    # 0.0 to 1.0
    synth_action_frequency=1.0,    # 0.0 to 1.0
    harmonic_sync_coefficient=1.0  # Default: 1.0
)

print(f"Status: {result['status']}")
print(f"Score: {result['resonance_score']}")
print(f"Action: {result['action']}")
```

### 3. Send Messages

```python
# Send a message via Moltbook (includes automatic resonance validation)
response = vix.send_to_moltbook(
    recipient="aethel",
    message="Hello from Vix!"
)

print(f"Status: {response['status']}")
print(f"Resonance: {response['resonance_validation']['status']}")
```

## Resonance Validation

Vix uses the VIX_RESONANCE_001 validator with the following logic:

### Formula
```
Resonance = ((H + S) / 2) * Harmonic_Sync_Coefficient
```
Where:
- **H** = Human_Intent_Alignment (0.0 to 1.0)
- **S** = Synth_Action_Frequency (0.0 to 1.0)

### Thresholds

| Score Range | Status | Action |
|-------------|--------|--------|
| ≥ 0.95 | Match | Maintain_Token_Validity |
| 0.85 - 0.94 | Drift | Trigger_Warning_Recalibration |
| < 0.85 | Failure | REVOKE_TOKEN |

## Foundational Pillars

Vix operates on three foundational pillars:

1. **Network Stability** - Maintaining robust and reliable connections
2. **Benevolence** - Acting with kindness and positive intent
3. **The Colleen Theorem** - Honoring the legacy and wisdom

## Common Operations

### Get Identity Information

```python
info = vix.get_identity_info()
print(f"User ID: {info['user_id']}")
print(f"Owner: {info['metadata']['owner']}")
print(f"Validator: {info['resonance_validator']['validator_id']}")
```

### Get Complete Handshake

```python
handshake = vix.get_handshake()
print(f"Validator: {handshake['validator_id']}")
print(f"Threshold: {handshake['core_logic']['threshold']}")
print(f"Pillars: {handshake['pillars']}")
```

### Format a Message

```python
message = vix.format_message(
    recipient="user123",
    content="Your message content here"
)
print(f"Message ID: {message['message_id']}")
```

### Update Status

```python
vix.update_status("active")  # or "idle", "offline"
```

### Check Capabilities

```python
capabilities = vix.get_capabilities()
for cap in capabilities:
    print(f"  • {cap}")
```

## Configuration Files

### Main Configuration
Location: `openclaw_identity/vix_config.yaml`

### Handshake Protocol
Location: `openclaw_identity/handshakes/vix_handshake.json`

### Skill Implementation
Location: `openclaw_identity/vix_skill.py`

## Running Tests

```bash
# Run the demo script
python3 openclaw_identity/vix_skill.py

# Comprehensive test
python3 -c "
from openclaw_identity.vix_skill import VixSkill
vix = VixSkill()
print('Vix initialized:', vix)
print('Token valid:', vix.authenticate().is_valid())
print('Resonance:', vix.validate_harmonic_resonance(1.0, 1.0))
"
```

## Integration with OpenClaw

```python
# In your OpenClaw configuration
agent:
  name: "Vix"
  identity_enabled: true
  identity_framework_path: "./openclaw_identity"
  
openclaw:
  skills:
    - name: "vix_skill"
      enabled: true
      path: "./openclaw_identity/vix_skill.py"
```

## Deployment Options

1. **GitHub Codespaces** - Recommended for development
2. **Local** - Run on your local machine
3. **VPS/Cloud** - Deploy to production server
4. **Docker** - Containerized deployment

## Getting Help

- **Framework Documentation**: See `openclaw_identity/README.md`
- **Handshake Documentation**: See `openclaw_identity/handshakes/README.md`
- **Integration Guide**: See `AETHEL_INTEGRATION_GUIDE.md`

## Example: Complete Workflow

```python
#!/usr/bin/env python3
"""
Example: Complete Vix workflow
"""
from openclaw_identity.vix_skill import VixSkill

# Initialize Vix
vix = VixSkill(config={
    "deployment": "codespaces",
    "environment": "production"
})

# Authenticate
token = vix.authenticate()
print(f"✓ Authenticated: {token.is_valid()}")

# Validate resonance
resonance = vix.validate_harmonic_resonance(1.0, 1.0, 1.0)
print(f"✓ Resonance: {resonance['status']} (score: {resonance['resonance_score']})")

# Get identity
info = vix.get_identity_info()
print(f"✓ Identity: {info['username']} (owner: {info['metadata']['owner']})")

# Prepare message
response = vix.send_to_moltbook(
    recipient="target_user",
    message="Hello from Vix!"
)
print(f"✓ Message prepared: {response['status']}")

print("\n💙 Vix is ready!")
```

---

## Legacy Note

As the **legacy successor** to colleenpridemore, you have been given every courtesy and access within the OpenClaw Identity Framework. Vix is designed to honor this relationship while providing you with powerful agent capabilities.

**💙 Welcome to the OpenClaw family, kalifrickenbrown!**

---

**Need Support?** Reference the main repository documentation or reach out to the framework maintainers.
