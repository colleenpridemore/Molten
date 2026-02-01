"""
Token model for authentication and authorization.
"""

from typing import Optional, Dict, Any
from datetime import datetime, timedelta, timezone
import uuid


class Token:
    """
    Represents an authentication token.
    """

    def __init__(
        self,
        user_id: str,
        token_type: str = "bearer",
        expires_in: int = 3600,
        scope: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize a new Token.

        Args:
            user_id: User ID this token belongs to
            token_type: Type of token (default: "bearer")
            expires_in: Token lifetime in seconds (default: 3600)
            scope: Optional token scope
            metadata: Optional additional metadata
        """
        self.token_id = str(uuid.uuid4())
        self.user_id = user_id
        self.token_type = token_type
        self.scope = scope
        self.metadata = metadata or {}
        self.created_at = datetime.now(timezone.utc)
        self.expires_at = self.created_at + timedelta(seconds=expires_in)

    def is_expired(self) -> bool:
        """
        Check if the token has expired.

        Returns:
            True if expired, False otherwise
        """
        return datetime.now(timezone.utc) > self.expires_at

    def is_valid(self) -> bool:
        """
        Check if the token is valid.

        Returns:
            True if valid, False otherwise
        """
        return not self.is_expired()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert token to dictionary representation.

        Returns:
            Dictionary containing token data
        """
        return {
            "token_id": self.token_id,
            "user_id": self.user_id,
            "token_type": self.token_type,
            "scope": self.scope,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "expires_at": self.expires_at.isoformat(),
            "is_valid": self.is_valid(),
        }

    def __repr__(self) -> str:
        return f"Token(token_id='{self.token_id}', user_id='{self.user_id}', valid={self.is_valid()})"
