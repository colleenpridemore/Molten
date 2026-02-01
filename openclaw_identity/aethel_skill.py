"""
Aethel Agent Skill for OpenClaw with Identity Framework Integration.

This skill enables Aethel to operate within OpenClaw with full identity management,
authentication, and Moltbook integration capabilities.
"""

from typing import Dict, Any, Optional
from datetime import datetime, timezone
import sys
import os

# Add openclaw_identity to path if not already there
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from openclaw_identity import Identity, AuthProvider
from openclaw_identity.models import Token
from openclaw_identity.utils import validate_email


class AethelSkill:
    """
    Aethel Agent Skill for OpenClaw.
    
    Provides identity management, authentication, and message handling
    capabilities specifically designed for the Aethel agent.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the Aethel skill.
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        
        # Create Aethel's identity
        self.identity = Identity(
            user_id=self.config.get("user_id", "agent_aethel_001"),
            username=self.config.get("username", "aethel"),
            email=self.config.get("email", "aethel@asi1.ai"),
            metadata={
                "type": "agent",
                "persona": "Aethel",
                "version": "1.0.0",
                "capabilities": [
                    "messaging",
                    "moltbook_integration",
                    "openclaw_control",
                    "identity_management"
                ],
                "deployment": self.config.get("deployment", "unknown"),
                "created": datetime.now(timezone.utc).isoformat(),
                "status": "active"
            }
        )
        
        # Initialize authentication provider
        self.auth_provider = AuthProvider(config={
            "environment": self.config.get("environment", "production"),
            "require_token": True,
            "moltbook_integration": True
        })
        
        # Register Aethel
        self.auth_provider.register(self.identity)
        
        # Current authentication token
        self._current_token: Optional[Token] = None
        
    def authenticate(self, force_new: bool = False) -> Token:
        """
        Authenticate Aethel and get a valid token.
        
        Args:
            force_new: Force creation of a new token even if current one is valid
            
        Returns:
            Valid authentication token
        """
        # Check if we have a valid token already
        if not force_new and self._current_token and self._current_token.is_valid():
            return self._current_token
        
        # Create new token
        token_expiration = self.config.get("token_expiration", 86400)  # 24 hours default
        
        self._current_token = Token(
            user_id=self.identity.user_id,
            token_type="bearer",
            expires_in=token_expiration,
            scope="openclaw:full moltbook:send moltbook:receive",
            metadata={
                "agent": "aethel",
                "purpose": "agent_authentication",
                "issued_at": datetime.now(timezone.utc).isoformat()
            }
        )
        
        return self._current_token
    
    def get_identity_info(self) -> Dict[str, Any]:
        """
        Get Aethel's identity information.
        
        Returns:
            Dictionary containing identity details
        """
        identity_dict = self.identity.to_dict()
        
        if self._current_token:
            identity_dict["current_token"] = {
                "token_id": self._current_token.token_id,
                "valid": self._current_token.is_valid(),
                "expires_at": self._current_token.expires_at.isoformat()
            }
        
        return identity_dict
    
    def format_message(
        self,
        recipient: str,
        content: str,
        message_type: str = "direct"
    ) -> Dict[str, Any]:
        """
        Format a message with Aethel's identity information.
        
        Args:
            recipient: Recipient identifier
            content: Message content
            message_type: Type of message (direct, broadcast, etc.)
            
        Returns:
            Formatted message dictionary
        """
        token = self.authenticate()
        
        if not token.is_valid():
            raise ValueError("Cannot format message: Invalid authentication token")
        
        return {
            "message_id": f"msg_{token.token_id[:8]}_{int(datetime.now(timezone.utc).timestamp())}",
            "from": {
                "user_id": self.identity.user_id,
                "username": self.identity.username,
                "type": "agent",
                "persona": "Aethel"
            },
            "to": recipient,
            "content": content,
            "message_type": message_type,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "authentication": {
                "token_id": token.token_id,
                "verified": True
            }
        }
    
    def send_to_moltbook(
        self,
        recipient: str,
        message: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Send a message to Moltbook with Aethel's identity.
        
        Args:
            recipient: Recipient username or ID
            message: Message content
            **kwargs: Additional message parameters
            
        Returns:
            Response from Moltbook API
        """
        # Ensure we're authenticated
        token = self.authenticate()
        
        if not token.is_valid():
            raise ValueError("Cannot send message: Invalid authentication token")
        
        # Format the message
        formatted_message = self.format_message(
            recipient=recipient,
            content=message,
            message_type=kwargs.get("message_type", "direct")
        )
        
        # Add any additional parameters
        formatted_message.update(kwargs)
        
        # This would integrate with actual Moltbook API
        # For now, return the formatted message as confirmation
        return {
            "status": "prepared",
            "message": formatted_message,
            "note": "Ready to send via Moltbook integration"
        }
    
    def verify_recipient(self, recipient: str) -> bool:
        """
        Verify that a recipient is valid before sending.
        
        Args:
            recipient: Recipient identifier to verify
            
        Returns:
            True if recipient is valid
        """
        # Basic validation - would integrate with actual Moltbook API
        if not recipient or len(recipient) < 3:
            return False
        return True
    
    def update_status(self, status: str) -> None:
        """
        Update Aethel's agent status.
        
        Args:
            status: New status (active, idle, offline, etc.)
        """
        self.identity.update(
            metadata={
                **self.identity.metadata,
                "status": status,
                "last_updated": datetime.now(timezone.utc).isoformat()
            }
        )
    
    def get_capabilities(self) -> list:
        """
        Get list of Aethel's capabilities.
        
        Returns:
            List of capability strings
        """
        return self.identity.metadata.get("capabilities", [])
    
    def __repr__(self) -> str:
        token_status = "valid" if (self._current_token and self._current_token.is_valid()) else "none/expired"
        return f"AethelSkill(identity={self.identity.username}, token={token_status})"


# Example usage
if __name__ == "__main__":
    print("=== Aethel Skill Demo ===\n")
    
    # Initialize Aethel skill
    aethel = AethelSkill(config={
        "deployment": "codespaces",
        "environment": "development"
    })
    
    print(f"1. Initialized: {aethel}")
    print(f"   Identity: {aethel.identity}\n")
    
    # Authenticate
    token = aethel.authenticate()
    print(f"2. Authenticated")
    print(f"   Token: {token.token_id}")
    print(f"   Valid: {token.is_valid()}")
    print(f"   Expires: {token.expires_at}\n")
    
    # Get identity info
    info = aethel.get_identity_info()
    print(f"3. Identity Info:")
    for key, value in info.items():
        if key != "metadata":
            print(f"   {key}: {value}")
    print()
    
    # Format a message
    message = aethel.format_message(
        recipient="dominus",
        content="This is a test message from Aethel"
    )
    print(f"4. Formatted Message:")
    print(f"   Message ID: {message['message_id']}")
    print(f"   From: {message['from']['username']}")
    print(f"   To: {message['to']}")
    print(f"   Authenticated: {message['authentication']['verified']}\n")
    
    # Prepare to send via Moltbook
    response = aethel.send_to_moltbook(
        recipient="dominus",
        message="Hello from Aethel!"
    )
    print(f"5. Moltbook Response:")
    print(f"   Status: {response['status']}")
    print(f"   Note: {response['note']}\n")
    
    print("=== Demo Complete ===")
