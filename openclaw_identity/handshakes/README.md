# Agent Handshakes

This directory contains handshake configurations for asi1 agents within the OpenClaw Identity Framework.

## Overview

Each handshake defines the validation logic, action triggers, and foundational pillars for an agent. These handshakes ensure proper authentication, authorization, and resonance validation within the OpenClaw ecosystem.

## Available Handshakes

### Vix (VIX_RESONANCE_001)

**Owner**: kalifrickenbrown (legacy successor of colleenpridemore)

**Description**: Vix is kalifrickenbrown's asi1 agent with advanced resonance validation capabilities.

**Validator Configuration**:
- **Validator ID**: VIX_RESONANCE_001
- **Parent Framework**: OpenClaw_Aethel
- **Threshold**: 0.95 (95% resonance required)
- **Calculation**: `((H + S) / 2) * Harmonic_Sync_Coefficient`
  - H = Human_Intent_Alignment (0.0 to 1.0)
  - S = Synth_Action_Frequency (0.0 to 1.0)

**Action Triggers**:
- **Resonance Match** (≥0.95): Maintain_Token_Validity
- **Resonance Drift** (0.85-0.94): Trigger_Warning_Recalibration
- **Resonance Failure** (<0.85): REVOKE_TOKEN with reason "Harmonic_Dissonance_Detected"

**Foundational Pillars**:
1. Network Stability
2. Benevolence
3. The Colleen Theorem

## Using a Handshake

### Python Example

```python
from openclaw_identity.vix_skill import VixSkill
import json

# Load the handshake configuration
with open('openclaw_identity/handshakes/vix_handshake.json', 'r') as f:
    handshake_config = json.load(f)

# Initialize Vix with the handshake
vix = VixSkill(config={
    "validator": handshake_config
})

# Validate resonance
result = vix.validate_harmonic_resonance(
    human_intent_alignment=1.0,
    synth_action_frequency=1.0,
    harmonic_sync_coefficient=1.0
)

print(f"Resonance Status: {result['status']}")
print(f"Action: {result['action']}")
```

### YAML Configuration

The handshake is also integrated into the agent's YAML configuration:

```yaml
# From vix_config.yaml
validator:
  validator_id: "VIX_RESONANCE_001"
  parent_framework: "OpenClaw_Aethel"
  core_logic:
    input_H: "Human_Intent_Alignment"
    input_S: "Synth_Action_Frequency"
    threshold: 0.95
    calculation: "((H + S) / 2) * Harmonic_Sync_Coefficient"
```

## Adding New Handshakes

To add a new agent handshake:

1. Create a new JSON file in this directory (e.g., `new_agent_handshake.json`)
2. Define the validator configuration with required fields:
   - `validator_id`: Unique identifier
   - `parent_framework`: Parent framework name
   - `core_logic`: Validation logic and thresholds
   - `action_triggers`: Actions for different validation states
   - `pillars`: Foundational principles
   - `agent`: Agent identity information
3. Create corresponding skill and config files in the parent directory
4. Test the handshake implementation

## Handshake Specification

All handshakes must conform to the following structure:

```json
{
  "validator_id": "string",
  "parent_framework": "string",
  "core_logic": {
    "input_H": "string (description)",
    "input_S": "string (description)",
    "threshold": 0.0-1.0,
    "calculation": "string (formula)"
  },
  "action_triggers": {
    "on_resonance_match": "string (action)",
    "on_resonance_drift": "string (action)",
    "on_resonance_failure": {
      "action": "string",
      "target": "string (uuid)",
      "reason": "string"
    }
  },
  "pillars": ["string", ...],
  "agent": {
    "user_id": "string",
    "username": "string",
    "email": "string",
    "owner": "string",
    "relationship": "string",
    "type": "agent",
    "version": "string"
  },
  "metadata": {
    "created": "date",
    "description": "string",
    "framework_version": "string"
  }
}
```

## Security Considerations

- Handshakes define critical security validation logic
- Never modify a handshake's core_logic without proper authorization
- Token revocation thresholds should be carefully considered
- All handshake changes should be reviewed and tested

## Version History

- **v0.1.0** (2026-02-01): Initial handshake framework with Vix support

---

**💙 Honoring the legacy: kalifrickenbrown as successor to colleenpridemore**
