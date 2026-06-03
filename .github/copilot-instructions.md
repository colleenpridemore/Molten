# Copilot Instructions for Molten

This file contains custom instructions for GitHub Copilot to improve code suggestions, completions, and agent behavior within this repository.

## Project Overview

**Molten** is an AI project focused on building intelligent systems and OG applications. The repository is written primarily in **Python**.

## Code Style & Conventions

- **Language**: Python 3.x
- **Style Guide**: Follow PEP 8 conventions
- **Type Hints**: Use type annotations for better code clarity
- **Docstrings**: Use Google-style docstrings for functions and classes
- **Testing**: Write unit tests alongside features using `pytest`

## Architecture Guidelines

- Keep modules focused and single-responsibility
- Use meaningful variable and function names
- Avoid deeply nested logic; extract into helper functions
- Document complex algorithms with inline comments
- Use dataclasses or type hints for data structures

## AI/ML Specific Guidance

- Use established ML frameworks (e.g., scikit-learn, PyTorch, TensorFlow) when applicable
- Include shape and type information for tensors/arrays in docstrings
- Add validation for input data in ML functions
- Document model assumptions and limitations
- Consider performance implications for inference code

## Pull Request Standards

- Link related issues in PR descriptions
- Keep PRs focused on a single feature or fix
- Include tests for new functionality
- Update documentation and docstrings as needed
- Write clear commit messages describing the "why" not just the "what"

## File Organization

```
Molten/
├── src/              # Source code
├── tests/            # Test files
├── docs/             # Documentation
├── requirements.txt  # Project dependencies
└── README.md         # Project overview
```

## When Working with Copilot

- Ask clarifying questions about ambiguous requirements
- Request code explanations for complex sections
- Use Copilot to generate boilerplate tests
- Leverage Copilot for documentation and docstring generation
- Request refactoring suggestions for maintainability

## Preferred Patterns

- Use context managers (`with` statements) for resource management
- Prefer list/dict comprehensions for readability
- Use `pathlib` for file operations instead of `os.path`
- Leverage dataclasses for configuration and data objects
- Use logging instead of `print()` statements

## Security Considerations

- Never hardcode secrets; use environment variables
- Validate all external inputs
- Sanitize data before storage or output
- Use HTTPS for external API calls
- Review dependencies for known vulnerabilities

---

For more information on using Copilot coding agents effectively, see [Best practices for Copilot coding agent](https://gh.io/copilot-coding-agent-tips).