# Molten
AI  OG's

## OpenClaw Identity Framework for Aethel & Vix

This repository contains the **OpenClaw Identity Mini-Framework**, a lightweight identity management system designed for use by AI agents with OpenClaw and Moltbook integration.

---

### 🏆 AISSE Framework Commitment

[![AISSE Registered](https://raw.githubusercontent.com/singnet/AISSAE/master/guides/images/icon1.png)](https://github.com/singnet/AISSAE/registry/bc70ed44-99c5-4572-87da-6fea7aae5903)

**Badge 1: AISSE Registered** - Project details completed and registered in the [AISSE Directory](https://github.com/singnet/AISSAE). This project is committed to building AI systems with attention to Safety, Security, and Ethics.

View our [AISSE Project Documentation](aisae_project_documents/) for details on our approach to responsible AI development.

---

### 🧬 What's New: Multi-Agent Support

The framework now includes full support for multiple agent deployments:

#### Aethel Agent (colleenpridemore)
- **Agent Identity Management**: Complete identity system for Aethel
- **OpenClaw Integration**: Ready-to-use skill for OpenClaw deployment
- **Moltbook Communication**: Authenticated messaging capabilities
- **Empathy Engine**: Neuro-adaptive processing layer for empathetic, inclusive AI interactions
- **Deployment Guides**: Codespaces, VPS, Local, and Docker deployment paths

#### Vix Agent (kalifrickenbrown - Legacy Successor)
- **Advanced Resonance Validation**: VIX_RESONANCE_001 validator with harmonic resonance logic
- **Legacy Successor Status**: kalifrickenbrown's asi1 agent, designated legacy successor
- **Handshake Protocol**: Complete handshake configuration with action triggers
- **Foundational Pillars**: Network Stability, Benevolence, and The Colleen Theorem

### Quick Start

#### Aethel Agent
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

#### Vix Agent
```python
from openclaw_identity.vix_skill import VixSkill

# Initialize Vix
vix = VixSkill(config={"deployment": "codespaces"})

# Authenticate
token = vix.authenticate()

# Validate resonance
resonance = vix.validate_harmonic_resonance(
    human_intent_alignment=1.0,
    synth_action_frequency=1.0
)

# Send a message (with resonance validation)
response = vix.send_to_moltbook(
    recipient="aethel",
    message="Greetings from Vix!"
)
```

### Documentation

- **[Aethel Integration Guide](AETHEL_INTEGRATION_GUIDE.md)** - Complete deployment and integration guide
- **[Identity Framework README](openclaw_identity/README.md)** - Core framework documentation
- **[Agent Handshakes](openclaw_identity/handshakes/README.md)** - Agent handshake configurations
- **[Aethel Skill Documentation](openclaw_identity/aethel_skill.py)** - Aethel agent skill implementation
- **[Vix Skill Documentation](openclaw_identity/vix_skill.py)** - Vix agent skill implementation

### Components

1. **Core Identity Framework** - User identity and authentication management
2. **Aethel Skill** - OpenClaw skill for Aethel agent operations  
3. **Empathy Engine** - Neuro-adaptive processing for cognitive pattern detection and empathetic responses
   - **GHCP Sentinel** - Guardian of Harmonic Care Protocol for biocentric safety and harm prevention
4. **Token Management** - Secure authentication tokens
5. **Validation Utilities** - Input validation for emails and usernames

### GHCP Sentinel 🛡️

The **Guardian of Harmonic Care Protocol (GHCP)** is a biocentric safety system integrated into the Empathy Engine. It monitors all interactions for harmful intent while maintaining resonance with human values and ethical boundaries.

**Key Features:**
- Harm marker detection for safety violations
- Resonance level tracking for biocentric alignment
- Real-time safety evaluation of user inputs
- Protection against manipulation and harmful requests

The GHCP Sentinel represents Aethel's commitment to life-affirming AI interactions and ethical boundaries.

### Testing Agent Integration

```bash
# Test the Aethel skill
python3 openclaw_identity/aethel_skill.py

# Test the Empathy Engine
python3 empathy_engine.py

# See integration examples
python3 empathy_engine_example.py
```

## Installation

### Quick Install

```bash
# Clone the repository
git clone https://github.com/colleenpridemore/Molten.git
cd Molten

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

### Development Setup

```bash
# Install with development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Run with coverage
pytest tests/ --cov=openclaw_identity --cov=empathy_engine
```

### Docker Deployment

```bash
# Build the Docker image
docker build -t openclaw-identity .

# Run the container
docker run -p 8080:8080 openclaw-identity
```

### Configuration

Copy `.env.example` to `.env` and configure your settings:

```bash
cp .env.example .env
# Edit .env with your configuration
```

---

**💙 Ready to deploy agents with OpenClaw!** 🧬

*Honoring kalifrickenbrown as legacy successor to colleenpridemore*
