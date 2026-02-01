"""
Identity class for managing user identities within OpenClaw.
"""

from typing import Optional, Dict, Any
from datetime import datetime


class Identity:
    """
    Represents a user identity in the OpenClaw framework.
    """

    def __init__(
        self,
        user_id: str,
        username: str,
        email: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize a new Identity.

        Args:
            user_id: Unique identifier for the user
            username: Username for the identity
            email: Optional email address
            metadata: Optional additional metadata
        """
        self.user_id = user_id
        self.username = username
        self.email = email
        self.metadata = metadata or {}
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def update(self, **kwargs) -> None:
        """
        Update identity attributes.

        Args:
            **kwargs: Attributes to update
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert identity to dictionary representation.

        Returns:
            Dictionary containing identity data
        """
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def __repr__(self) -> str:
        return f"Identity(user_id='{self.user_id}', username='{self.username}')"
