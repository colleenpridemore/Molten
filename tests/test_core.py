"""
Unit tests for OpenClaw Identity core functionality
"""
import pytest
from openclaw_identity import Identity, AuthProvider
from openclaw_identity.models import Token
from openclaw_identity.utils import validate_email, validate_username


class TestIdentity:
    """Test Identity class"""
    
    def test_identity_creation(self):
        """Test creating a new identity"""
        identity = Identity(
            user_id="test-123",
            username="aethel",
            email="aethel@openclaw.ai"
        )
        assert identity.username == "aethel"
        assert identity.email == "aethel@openclaw.ai"
        assert identity.user_id == "test-123"
    
    def test_identity_to_dict(self):
        """Test identity dictionary conversion"""
        identity = Identity(
            user_id="test-123",
            username="aethel",
            email="aethel@openclaw.ai"
        )
        data = identity.to_dict()
        assert data["username"] == "aethel"
        assert data["email"] == "aethel@openclaw.ai"
        assert "created_at" in data
    
    def test_identity_update(self):
        """Test identity update"""
        identity = Identity(
            user_id="test-123",
            username="aethel",
            email="old@example.com"
        )
        identity.update(email="new@example.com")
        assert identity.email == "new@example.com"


class TestAuthProvider:
    """Test AuthProvider class"""
    
    def test_auth_provider_creation(self):
        """Test creating auth provider"""
        auth = AuthProvider()
        assert auth is not None
        assert auth.config == {}
    
    def test_register_identity(self):
        """Test registering an identity"""
        auth = AuthProvider()
        identity = Identity(
            user_id="test-123",
            username="aethel",
            email="aethel@openclaw.ai"
        )
        result = auth.register(identity)
        assert result is True
        
        # Try to register again - should fail
        result2 = auth.register(identity)
        assert result2 is False
    
    def test_get_identity(self):
        """Test retrieving an identity"""
        auth = AuthProvider()
        identity = Identity(
            user_id="test-123",
            username="aethel",
            email="aethel@openclaw.ai"
        )
        auth.register(identity)
        
        retrieved = auth.get_identity("test-123")
        assert retrieved is not None
        assert retrieved.user_id == "test-123"


class TestToken:
    """Test Token class"""
    
    def test_token_creation(self):
        """Test creating a token"""
        token = Token(user_id="test-user-123")
        assert token.user_id == "test-user-123"
        assert token.token_id is not None
        assert token.is_valid() is True
    
    def test_token_expiration(self):
        """Test token expiration"""
        # Token that expires immediately
        token = Token(user_id="test-user-123", expires_in=0)
        # It should be expired
        assert token.is_valid() is False
    
    def test_token_to_dict(self):
        """Test token dictionary conversion"""
        token = Token(user_id="test-user-123")
        data = token.to_dict()
        assert data["user_id"] == "test-user-123"
        assert "token_id" in data
        assert "expires_at" in data


class TestValidators:
    """Test validation utilities"""
    
    def test_valid_email(self):
        """Test valid email validation"""
        is_valid, _ = validate_email("test@example.com")
        assert is_valid is True
    
    def test_invalid_email(self):
        """Test invalid email validation"""
        is_valid, error = validate_email("invalid-email")
        assert is_valid is False
        assert error is not None
    
    def test_valid_username(self):
        """Test valid username validation"""
        is_valid, _ = validate_username("aethel")
        assert is_valid is True
    
    def test_invalid_username_short(self):
        """Test username too short"""
        is_valid, error = validate_username("ab")
        assert is_valid is False
        assert error is not None
    
    def test_invalid_username_special_chars(self):
        """Test username with invalid characters"""
        is_valid, error = validate_username("user@name!")
        assert is_valid is False
        assert error is not None
