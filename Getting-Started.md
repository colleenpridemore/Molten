# 🚀 Getting Started with Molten

Welcome! This guide will help you get Molten up and running in minutes.

## Prerequisites

- **Python 3.8+** (we recommend 3.10 or higher)
- **pip** package manager
- **git** for cloning the repository
- Optional: Docker for containerized deployment

## Installation

### Method 1: Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/colleenpridemore/Molten.git
cd Molten

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

### Method 2: Development Setup

If you're planning to contribute or customize:

```bash
# Clone the repository
git clone https://github.com/colleenpridemore/Molten.git
cd Molten

# Install with development dependencies
pip install -e ".[dev]"

# Run tests to verify installation
pytest tests/

# Run with coverage
pytest tests/ --cov=openclaw_identity --cov=empathy_engine
```

### Method 3: Docker Installation

```bash
# Build the Docker image
docker build -t openclaw-identity .

# Run the container
docker run -p 8080:8080 openclaw-identity
```

## Configuration

### Set Up Environment Variables

1. **Copy the example configuration:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` with your settings:**
   ```env
   # Molten Configuration
   MOLTEN_ENV=development
   MOLTEN_LOG_LEVEL=INFO
   
   # Agent Configuration
   AETHEL_DEPLOYMENT=codespaces
   VIX_DEPLOYMENT=codespaces
   
   # Moltbook Integration
   MOLTBOOK_API_URL=https://moltbook.example.com
   MOLTBOOK_AUTH_TOKEN=your_token_here
   ```

## Quick Start

### Using Aethel Agent

```python
from openclaw_identity.aethel_skill import AethelSkill

# Initialize Aethel
aethel = AethelSkill(config={"deployment": "codespaces"})

# Authenticate
token = aethel.authenticate()
print(f"Authentication token: {token}")

# Send a message
response = aethel.send_to_moltbook(
    recipient="dominus",
    message="Hello from Aethel!"
)
print(response)
```

### Using Vix Agent

```python
from openclaw_identity.vix_skill import VixSkill

# Initialize Vix
vix = VixSkill(config={"deployment": "codespaces"})

# Authenticate
token = vix.authenticate()

# Validate harmonic resonance
resonance = vix.validate_harmonic_resonance(
    human_intent_alignment=1.0,
    synth_action_frequency=1.0
)

# Send authenticated message
response = vix.send_to_moltbook(
    recipient="aethel",
    message="Greetings from Vix!"
)
```

### Testing Your Installation

```bash
# Test the Aethel skill
python3 openclaw_identity/aethel_skill.py

# Test the Empathy Engine
python3 empathy_engine.py

# Run integration examples
python3 empathy_engine_example.py

# Run full test suite
pytest tests/
```

## Project Structure

```
Molten/
├── openclaw_identity/              # Core framework
│   ├── __init__.py
│   ├── aethel_skill.py            # Aethel agent implementation
│   ├── vix_skill.py               # Vix agent implementation
│   ├── core/
│   │   ├── identity.py            # Identity management
│   │   └── auth.py                # Authentication provider
│   ├── models/
│   │   └── token.py               # Token model
│   ├── utils/
│   │   └── validators.py          # Validation utilities
│   ├── handshakes/                # Agent handshake configs
│   │   ├── vix_handshake.json
│   │   └── vix_config.yaml
│   └── README.md                  # Framework documentation
├── empathy_engine.py              # Empathy Engine with GHCP Sentinel
├── empathy_engine_example.py      # Example usage
├── tests/                          # Test suite
├── requirements.txt               # Python dependencies
├── setup.py                       # Package setup
├── .env.example                   # Example environment config
└── README.md                      # Main project README
```

## Next Steps

1. **Understand the Basics**: Read [Core Concepts](Core-Concepts) to learn about identities and authentication
2. **Choose Your Agent**: 
   - New to Molten? Start with [Aethel Agent](Aethel-Agent)
   - Advanced use cases? Explore [Vix Agent](Vix-Agent)
3. **Deploy**: Check [Deployment Guides](Deployment-Guides) for your preferred platform
4. **Explore Advanced Features**: Learn about the [Empathy Engine](Empathy-Engine) and [GHCP Sentinel](GHCP-Sentinel)

## Common Issues

### ImportError: No module named 'openclaw_identity'

**Solution**: Make sure you've installed the package:
```bash
pip install -e .
```

### Token authentication fails

**Solution**: Check your `.env` file and ensure all required credentials are set. See [Configuration](#configuration) above.

### Tests fail

**Solution**: Ensure all dependencies are installed:
```bash
pip install -e ".[dev]"
pytest tests/
```

## Getting Help

- **Documentation**: Check the relevant wiki page for your topic
- **Examples**: Look in the repository for example scripts
- **Issues**: Found a bug? Open an issue on GitHub
- **Contributing**: Want to help? See [Contributing](Contributing)

---

**Ready to build with Molten?** Head over to [Core Concepts](Core-Concepts) to dive deeper! 🔥💙
