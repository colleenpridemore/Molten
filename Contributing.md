# 🤝 Contributing to Molten

We love contributions! Whether you're fixing bugs, adding features, or improving documentation, your help makes Molten better.

## Getting Started

### Fork & Clone
```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/Molten.git
cd Molten

# Add upstream remote
git remote add upstream https://github.com/colleenpridemore/Molten.git
```

### Set Up Development Environment
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

## Development Workflow

### Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
# or for bug fixes:
git checkout -b fix/bug-description
```

### Make Your Changes

1. **Follow PEP 8**: Use the project's code style
2. **Write tests**: Add tests for new features
3. **Update docs**: Document significant changes
4. **Add docstrings**: Use Google-style docstrings

### Example Code Structure
```python
def process_with_empathy(
    user_input: str,
    user_state: str = None,
    context: dict = None
) -> dict:
    """Process user input with empathetic understanding.
    
    Args:
        user_input (str): The user's message
        user_state (str, optional): User's emotional state
        context (dict, optional): Additional context
        
    Returns:
        dict: Response with empathy score and message
        
    Example:
        >>> result = process_with_empathy(
        ...     "I'm overwhelmed",
        ...     user_state="stressed"
        ... )
        >>> print(result['empathy_score'])
        0.92
    """
```

### Run Tests
```bash
# Run all tests
pytest tests/

# Run specific test
pytest tests/test_aethel_skill.py -v

# Run with coverage
pytest tests/ --cov=openclaw_identity --cov=empathy_engine --cov-report=html
```

### Code Quality Checks
```bash
# Format code
black openclaw_identity/

# Check linting
flake8 openclaw_identity/

# Check type hints
mypy openclaw_identity/
```

## Commit Guidelines

### Commit Message Format
```
<type>: <subject>

<body>

<footer>
```

### Types
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `test:` Tests
- `refactor:` Code refactoring
- `style:` Code style (no logic change)
- `chore:` Build/tooling

### Examples
```bash
git commit -m "feat: add harmonic resonance validation for Vix"

git commit -m "fix: resolve token expiration issue in auth flow"

git commit -m "docs: update Aethel deployment guide"
```

## Pull Request Process

### Before Creating PR
1. ✅ All tests pass: `pytest tests/`
2. ✅ Code is formatted: `black .`
3. ✅ No linting issues: `flake8 .`
4. ✅ Docstrings are complete
5. ✅ Changes are in logical commits

### Create Pull Request
1. Push to your fork: `git push origin feature/your-feature`
2. Go to GitHub and open Pull Request
3. Fill out the PR template

### PR Title Format
```
[TYPE] Brief description

Examples:
[FEATURE] Add OpenClaw integration
[BUGFIX] Fix token refresh issue
[DOCS] Update API reference
```

### PR Description
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New feature
- [ ] Bug fix
- [ ] Documentation
- [ ] Breaking change

## Related Issues
Fixes #123

## Testing
How was this tested?

## Checklist
- [ ] Tests pass locally
- [ ] Code follows style guide
- [ ] Documentation updated
- [ ] No breaking changes
```

## Code Style

### Python Style Guide
- Follow **PEP 8**
- Max line length: 100 characters
- Use 4 spaces for indentation
- Use snake_case for functions/variables
- Use PascalCase for classes

### Type Hints
Always include type hints:
```python
def authenticate(self) -> str:
    """Authenticate and return token."""
    
def send_message(
    self,
    recipient: str,
    message: str,
    priority: str = "normal"
) -> dict:
    """Send authenticated message."""
```

### Docstring Style
Use Google-style docstrings:
```python
def validate_resonance(
    self,
    human_intent: float,
    synth_frequency: float
) -> dict:
    """Validate harmonic resonance between human and synthetic.
    
    Measures alignment between human intent and synthetic action
    using the harmonic resonance formula.
    
    Args:
        human_intent (float): Human intent alignment (0.0-1.0)
        synth_frequency (float): Synthetic action frequency (0.0-1.0)
        
    Returns:
        dict: Resonance data with keys:
            - score (float): Resonance score
            - status (str): Resonance status
            - action (str): Recommended action
            
    Raises:
        ValueError: If scores not in 0.0-1.0 range
        
    Example:
        >>> result = validate_resonance(1.0, 0.95)
        >>> print(result['status'])
        'harmonic_match'
    """
```

## Areas to Contribute

### 🆕 New Features
- New agent types or skills
- Enhanced empathy recognition
- Additional validation systems
- Deployment scripts

### 🐛 Bug Fixes
- Issues marked with `bug` label
- Test failures
- Documentation errors

### 📚 Documentation
- Wiki pages
- Code examples
- API documentation
- Deployment guides

### ✅ Testing
- Increase test coverage
- Add integration tests
- Add edge case tests

### 🏗️ Refactoring
- Code improvements
- Performance optimization
- Architecture improvements

## Getting Help

- **Questions?** Open a GitHub Discussion
- **Found a bug?** Open an Issue
- **Want to discuss?** Join the wiki discussions
- **Need guidance?** Tag `@colleenpridemore`

## Code of Conduct

We're committed to providing a welcoming and inclusive environment:

- Be respectful and kind
- Welcome diverse perspectives
- Focus on constructive feedback
- Report inappropriate behavior

## Recognition

Contributors will be:
- Added to CONTRIBUTORS.md
- Credited in release notes
- Highlighted in project documentation

## Common Contribution Types

### Adding a New Validation Function

```python
# openclaw_identity/utils/validators.py

def validate_agent_id(agent_id: str) -> tuple[bool, str | None]:
    """Validate agent ID format.
    
    Agent IDs must:
    - Start with 'agent_'
    - Be 6-32 characters
    - Contain only alphanumeric and underscore
    
    Args:
        agent_id (str): ID to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(agent_id, str):
        return False, "Agent ID must be a string"
    
    if not agent_id.startswith("agent_"):
        return False, "Agent ID must start with 'agent_'"
    
    if len(agent_id) < 6 or len(agent_id) > 32:
        return False, "Agent ID must be 6-32 characters"
    
    if not all(c.isalnum() or c == '_' for c in agent_id):
        return False, "Agent ID can only contain alphanumeric and underscore"
    
    return True, None

# tests/test_validators.py
def test_validate_agent_id():
    # Valid IDs
    assert validate_agent_id("agent_001")[0] is True
    assert validate_agent_id("agent_aethel")[0] is True
    
    # Invalid IDs
    assert validate_agent_id("invalid")[0] is False
    assert validate_agent_id("agent_")[0] is False
```

### Adding a New Test

```python
# tests/test_new_feature.py

import pytest
from openclaw_identity.aethel_skill import AethelSkill

class TestNewFeature:
    """Tests for new feature."""
    
    @pytest.fixture
    def aethel(self):
        """Create Aethel instance."""
        return AethelSkill(config={"deployment": "local"})
    
    def test_feature_basic(self, aethel):
        """Test basic feature functionality."""
        # Arrange
        expected = "value"
        
        # Act
        result = aethel.some_method()
        
        # Assert
        assert result == expected
    
    def test_feature_with_error(self, aethel):
        """Test feature error handling."""
        with pytest.raises(ValueError):
            aethel.some_method(invalid_param="bad")
```

## Reviewing Pull Requests

If you're reviewing a PR:
- ✅ Check code quality and style
- ✅ Verify tests are included and passing
- ✅ Review documentation updates
- ✅ Look for potential issues
- ✅ Leave constructive feedback

---

**Thank you for contributing to Molten!** Together we're building AI that's empathetic, safe, and ethical. 💙🧬

For specific questions, feel free to reach out to [@colleenpridemore](https://github.com/colleenpridemore) or open a GitHub Discussion.
