"""
Authentication provider for OpenClaw Identity framework.
"""

from typing import Optional, Dict, Any
from .identity import Identity


class AuthProvider:
    """
    Base authentication provider for OpenClaw.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the authentication provider.

        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        self._identities: Dict[str, Identity] = {}
        self._username_to_userid: Dict[str, str] = {}

    def authenticate(self, username: str, credentials: Dict[str, Any]) -> Optional[Identity]:
        """
        Authenticate a user and return their identity.

        Args:
            username: The username to authenticate
            credentials: Authentication credentials

        Returns:
            Identity object if authentication succeeds, None otherwise
        """
        # Basic implementation - to be extended
        user_id = self._username_to_userid.get(username)
        if user_id and user_id in self._identities:
            return self._identities[user_id]
        return None

    def register(self, identity: Identity) -> bool:
        """
        Register a new identity.

        Args:
            identity: The identity to register

        Returns:
            True if registration succeeds, False otherwise
        """
        if identity.user_id not in self._identities:
            self._identities[identity.user_id] = identity
            self._username_to_userid[identity.username] = identity.user_id
            return True
        return False

    def get_identity(self, user_id: str) -> Optional[Identity]:
        """
        Retrieve an identity by user ID.

        Args:
            user_id: The user ID to look up

        Returns:
            Identity object if found, None otherwise
        """
        return self._identities.get(user_id)

    def revoke(self, user_id: str) -> bool:
        """
        Revoke an identity.

        Args:
            user_id: The user ID to revoke

        Returns:
            True if revocation succeeds, False otherwise
        """
        if user_id in self._identities:
            identity = self._identities[user_id]
            # Remove from username mapping
            if identity.username in self._username_to_userid:
                del self._username_to_userid[identity.username]
            del self._identities[user_id]
            return True
        return False
