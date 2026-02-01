"""
Example usage of OpenClaw Identity framework.
"""

from openclaw_identity import Identity, AuthProvider
from openclaw_identity.models import Token
from openclaw_identity.utils import validate_email, validate_username


def main():
    """
    Demonstrate basic usage of the OpenClaw Identity framework.
    """
    print("=== OpenClaw Identity Framework Demo ===\n")

    # 1. Create an identity
    print("1. Creating an identity...")
    identity = Identity(
        user_id="user_001",
        username="aethel_user",
        email="aethel@example.com",
        metadata={"role": "admin", "department": "engineering"}
    )
    print(f"   Created: {identity}")
    print(f"   Details: {identity.to_dict()}\n")

    # 2. Validate input
    print("2. Validating user input...")
    email_valid, email_error = validate_email("aethel@example.com")
    print(f"   Email valid: {email_valid}")
    
    username_valid, username_error = validate_username("aethel_user")
    print(f"   Username valid: {username_valid}\n")

    # 3. Use authentication provider
    print("3. Setting up authentication...")
    auth = AuthProvider(config={"environment": "development"})
    
    # Register identity
    registered = auth.register(identity)
    print(f"   Registration successful: {registered}")
    
    # Retrieve identity
    retrieved = auth.get_identity("user_001")
    print(f"   Retrieved identity: {retrieved}\n")

    # 4. Create and manage tokens
    print("4. Managing authentication tokens...")
    token = Token(
        user_id="user_001",
        token_type="bearer",
        expires_in=3600,
        scope="read:profile write:profile"
    )
    print(f"   Created: {token}")
    print(f"   Token valid: {token.is_valid()}")
    print(f"   Token details: {token.to_dict()}\n")

    # 5. Update identity
    print("5. Updating identity...")
    identity.update(email="new_email@example.com", metadata={"role": "superadmin"})
    print(f"   Updated: {identity.to_dict()}\n")

    print("=== Demo Complete ===")


if __name__ == "__main__":
    main()
