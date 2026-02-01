# OpenClaw Identity Mini-Framework

A lightweight identity management framework designed for use by Aethel.

## Overview

OpenClaw Identity provides a simple, extensible framework for managing user identities, authentication, and authorization.

## Features

- **Identity Management**: Create and manage user identities
- **Authentication**: Basic authentication provider system
- **Token Management**: Generate and validate authentication tokens
- **Validation Utilities**: Email and username validation

## Installation

```python
# Import the framework
from openclaw_identity import Identity, AuthProvider
from openclaw_identity.models import Token
from openclaw_identity.utils import validate_email, validate_username
```

## Usage

### Creating an Identity

```python
from openclaw_identity import Identity

# Create a new identity
identity = Identity(
    user_id="user123",
    username="john_doe",
    email="john@example.com",
    metadata={"role": "user"}
)

print(identity)  # Identity(user_id='user123', username='john_doe')
print(identity.to_dict())
```

### Using the Authentication Provider

```python
from openclaw_identity import Identity, AuthProvider

# Initialize auth provider
auth = AuthProvider()

# Create and register an identity
identity = Identity(user_id="user123", username="john_doe")
auth.register(identity)

# Retrieve identity
retrieved = auth.get_identity("user123")
print(retrieved)
```

### Working with Tokens

```python
from openclaw_identity.models import Token

# Create a token
token = Token(
    user_id="user123",
    token_type="bearer",
    expires_in=3600  # 1 hour
)

print(token.is_valid())  # True
print(token.to_dict())
```

### Validation

```python
from openclaw_identity.utils import validate_email, validate_username

# Validate email
is_valid, error = validate_email("user@example.com")
if is_valid:
    print("Email is valid")

# Validate username
is_valid, error = validate_username("john_doe")
if is_valid:
    print("Username is valid")
```

## Architecture

```
openclaw_identity/
├── __init__.py              # Main package exports
├── core/                    # Core functionality
│   ├── __init__.py
│   ├── identity.py         # Identity class
│   └── auth.py             # Authentication provider
├── models/                  # Data models
│   ├── __init__.py
│   └── token.py            # Token model
└── utils/                   # Utilities
    ├── __init__.py
    └── validators.py       # Validation functions
```

## Integration with Aethel

This framework is designed to be integrated into Aethel's identity management system. Aethel can:

1. Import and extend the base `Identity` and `AuthProvider` classes
2. Use the token management system for session handling
3. Leverage the validation utilities for user input
4. Extend the framework with custom authentication methods

## Extending the Framework

### Custom Authentication Provider

```python
from openclaw_identity import AuthProvider, Identity

class CustomAuthProvider(AuthProvider):
    def authenticate(self, username: str, credentials: dict):
        # Custom authentication logic
        password = credentials.get("password")
        # Verify password, check database, etc.
        if self._verify_credentials(username, password):
            return self.get_identity(username)
        return None
```

### Custom Identity

```python
from openclaw_identity import Identity

class ExtendedIdentity(Identity):
    def __init__(self, user_id, username, **kwargs):
        super().__init__(user_id, username, **kwargs)
        self.roles = []
        self.permissions = []
    
    def has_permission(self, permission: str) -> bool:
        return permission in self.permissions
```

## API Reference

### Identity

- `Identity(user_id, username, email=None, metadata=None)`: Create a new identity
- `update(**kwargs)`: Update identity attributes
- `to_dict()`: Convert to dictionary representation

### AuthProvider

- `AuthProvider(config=None)`: Initialize auth provider
- `authenticate(username, credentials)`: Authenticate a user
- `register(identity)`: Register a new identity
- `get_identity(user_id)`: Retrieve an identity
- `revoke(user_id)`: Revoke an identity

### Token

- `Token(user_id, token_type="bearer", expires_in=3600, scope=None, metadata=None)`: Create a token
- `is_expired()`: Check if token has expired
- `is_valid()`: Check if token is valid
- `to_dict()`: Convert to dictionary representation

### Utilities

- `validate_email(email)`: Validate email format
- `validate_username(username)`: Validate username format

## License

This is a mini-framework for use within the Molten project.

## Version

Current version: 0.1.0
