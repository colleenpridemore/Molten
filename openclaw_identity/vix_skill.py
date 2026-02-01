"""
Vix Agent Skill for OpenClaw with Identity Framework Integration.

This skill enables Vix (kalifrickenbrown's asi1 agent) to operate within OpenClaw
with full identity management, authentication, resonance validation, and Moltbook
integration capabilities.
"""

from typing import Dict, Any, Optional
from datetime import datetime, timezone

# Use relative imports for better package structure
try:
    from openclaw_identity import Identity, AuthProvider
    from openclaw_identity.models import Token
    from openclaw_identity.utils import validate_email
except ImportError:
    # Fallback for direct execution
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from openclaw_identity import Identity, AuthProvider
    from openclaw_identity.models import Token
    from openclaw_identity.utils import validate_email


class VixResonanceValidator:
    """
    Vix Resonance Validator for harmonic validation.
    
    Implements the VIX_RESONANCE_001 validator as defined in the handshake.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the resonance validator.
        
        Args:
            config: Validator configuration
        """
        self.config = config or {}
        self.validator_id = self.config.get("validator_id", "VIX_RESONANCE_001")
        self.parent_framework = self.config.get("parent_framework", "OpenClaw_Aethel")
        self.threshold = self.config.get("core_logic", {}).get("threshold", 0.95)
        self.pillars = self.config.get("pillars", [
            "Network Stability",
            "Benevolence",
            "The Colleen Theorem"
        ])
    
    def calculate_resonance(
        self,
        human_intent_alignment: float,
        synth_action_frequency: float,
        harmonic_sync_coefficient: float = 1.0
    ) -> float:
        """
        Calculate resonance score based on validator logic.
        
        Args:
            human_intent_alignment: H value (0.0 to 1.0)
            synth_action_frequency: S value (0.0 to 1.0)
            harmonic_sync_coefficient: Harmonic coefficient (default: 1.0)
            
        Returns:
            Resonance score (0.0 to 1.0)
        """
        # Implementation of: ((H + S) / 2) * Harmonic_Sync_Coefficient
        return ((human_intent_alignment + synth_action_frequency) / 2) * harmonic_sync_coefficient
    
    def validate_resonance(
        self,
        human_intent_alignment: float,
        synth_action_frequency: float,
        harmonic_sync_coefficient: float = 1.0
    ) -> Dict[str, Any]:
        """
        Validate resonance and determine action.
        
        Args:
            human_intent_alignment: H value (0.0 to 1.0)
            synth_action_frequency: S value (0.0 to 1.0)
            harmonic_sync_coefficient: Harmonic coefficient (default: 1.0)
            
        Returns:
            Validation result with action trigger
        """
        resonance = self.calculate_resonance(
            human_intent_alignment,
            synth_action_frequency,
            harmonic_sync_coefficient
        )
        
        result = {
            "validator_id": self.validator_id,
            "resonance_score": resonance,
            "threshold": self.threshold,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        
        # Determine action based on resonance
        if resonance >= self.threshold:
            result["status"] = "match"
            result["action"] = "Maintain_Token_Validity"
        elif resonance >= (self.threshold - 0.1):  # Within 10% of threshold
            result["status"] = "drift"
            result["action"] = "Trigger_Warning_Recalibration"
        else:
            result["status"] = "failure"
            result["action"] = "REVOKE_TOKEN"
            result["reason"] = "Harmonic_Dissonance_Detected"
            result["target"] = self.config.get("action_triggers", {}).get(
                "on_resonance_failure", {}
            ).get("target", "1f81139b-8717-404d-bbb5-87efee535ffe")
        
        return result
    
    def get_pillars(self) -> list:
        """
        Get the foundational pillars of the validator.
        
        Returns:
            List of pillar names
        """
        return self.pillars


class VixSkill:
    """
    Vix Agent Skill for OpenClaw.
    
    Provides identity management, authentication, resonance validation,
    and message handling capabilities specifically designed for the Vix agent
    (kalifrickenbrown's legacy successor).
    """
    
    # Constants
    MIN_RECIPIENT_LENGTH = 3
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the Vix skill.
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        
        # Create Vix's identity
        self.identity = Identity(
            user_id=self.config.get("user_id", "agent_vix_001"),
            username=self.config.get("username", "vix"),
            email=self.config.get("email", "vix@asi1.ai"),
            metadata={
                "type": "agent",
                "persona": "Vix",
                "version": "1.0.0",
                "owner": "kalifrickenbrown",
                "relationship": "legacy_successor",
                "parent": "colleenpridemore",
                "capabilities": [
                    "messaging",
                    "moltbook_integration",
                    "openclaw_control",
                    "identity_management",
                    "resonance_validation"
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
        
        # Register Vix
        self.auth_provider.register(self.identity)
        
        # Initialize resonance validator
        validator_config = self.config.get("validator", {})
        self.resonance_validator = VixResonanceValidator(validator_config)
        
        # Current authentication token
        self._current_token: Optional[Token] = None
        
    def authenticate(self, force_new: bool = False) -> Token:
        """
        Authenticate Vix and get a valid token.
        
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
                "agent": "vix",
                "owner": "kalifrickenbrown",
                "purpose": "agent_authentication",
                "validator_id": self.resonance_validator.validator_id,
                "issued_at": datetime.now(timezone.utc).isoformat()
            }
        )
        
        return self._current_token
    
    def validate_harmonic_resonance(
        self,
        human_intent_alignment: float = 1.0,
        synth_action_frequency: float = 1.0,
        harmonic_sync_coefficient: float = 1.0
    ) -> Dict[str, Any]:
        """
        Validate harmonic resonance for token validity.
        
        Args:
            human_intent_alignment: H value (0.0 to 1.0)
            synth_action_frequency: S value (0.0 to 1.0)
            harmonic_sync_coefficient: Harmonic coefficient (default: 1.0)
            
        Returns:
            Validation result
        """
        return self.resonance_validator.validate_resonance(
            human_intent_alignment,
            synth_action_frequency,
            harmonic_sync_coefficient
        )
    
    def get_identity_info(self) -> Dict[str, Any]:
        """
        Get Vix's identity information.
        
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
        
        identity_dict["resonance_validator"] = {
            "validator_id": self.resonance_validator.validator_id,
            "parent_framework": self.resonance_validator.parent_framework,
            "threshold": self.resonance_validator.threshold,
            "pillars": self.resonance_validator.get_pillars()
        }
        
        return identity_dict
    
    def format_message(
        self,
        recipient: str,
        content: str,
        message_type: str = "direct"
    ) -> Dict[str, Any]:
        """
        Format a message with Vix's identity information.
        
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
                "persona": "Vix",
                "owner": "kalifrickenbrown"
            },
            "to": recipient,
            "content": content,
            "message_type": message_type,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "authentication": {
                "token_id": token.token_id,
                "verified": True,
                "validator_id": self.resonance_validator.validator_id
            }
        }
    
    def send_to_moltbook(
        self,
        recipient: str,
        message: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Send a message to Moltbook with Vix's identity.
        
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
        
        # Validate resonance before sending
        resonance_result = self.validate_harmonic_resonance()
        if resonance_result["status"] == "failure":
            raise ValueError(
                f"Cannot send message: Resonance validation failed - {resonance_result['reason']}"
            )
        
        # Format the message
        formatted_message = self.format_message(
            recipient=recipient,
            content=message,
            message_type=kwargs.get("message_type", "direct")
        )
        
        # Add resonance validation info
        formatted_message["resonance_validation"] = {
            "status": resonance_result["status"],
            "score": resonance_result["resonance_score"],
            "validator_id": resonance_result["validator_id"]
        }
        
        # Add any additional parameters under a dedicated field to avoid
        # overwriting core identity/auth/resonance metadata
        if kwargs:
            extra_params = formatted_message.get("extra_params")
            if not isinstance(extra_params, dict):
                extra_params = {}
            extra_params.update(kwargs)
            formatted_message["extra_params"] = extra_params
        
        # This would integrate with actual Moltbook API
        # For now, return the formatted message as confirmation
        return {
            "status": "prepared",
            "message": formatted_message,
            "resonance_validation": resonance_result,
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
        if not recipient or len(recipient) < self.MIN_RECIPIENT_LENGTH:
            return False
        return True
    
    def update_status(self, status: str) -> None:
        """
        Update Vix's agent status.
        
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
        Get list of Vix's capabilities.
        
        Returns:
            List of capability strings
        """
        return self.identity.metadata.get("capabilities", [])
    
    def get_handshake(self) -> Dict[str, Any]:
        """
        Get the complete handshake configuration for Vix agent.
        
        Returns:
            Complete handshake dictionary
        """
        return {
            "validator_id": self.resonance_validator.validator_id,
            "parent_framework": self.resonance_validator.parent_framework,
            "core_logic": {
                "input_H": "Human_Intent_Alignment",
                "input_S": "Synth_Action_Frequency",
                "threshold": self.resonance_validator.threshold,
                "calculation": "((H + S) / 2) * Harmonic_Sync_Coefficient"
            },
            "action_triggers": self.config.get("validator", {}).get("action_triggers", {}),
            "pillars": self.resonance_validator.get_pillars(),
            "agent": {
                "user_id": self.identity.user_id,
                "username": self.identity.username,
                "owner": "kalifrickenbrown",
                "relationship": "legacy_successor",
                "status": self.identity.metadata.get("status", "active")
            }
        }
    
    def __repr__(self) -> str:
        token_status = "valid" if (self._current_token and self._current_token.is_valid()) else "none/expired"
        return f"VixSkill(identity={self.identity.username}, owner=kalifrickenbrown, token={token_status})"


# Example usage
if __name__ == "__main__":
    print("=== Vix Skill Demo ===\n")
    
    # Initialize Vix skill with validator config
    vix_config = {
        "deployment": "codespaces",
        "environment": "development",
        "validator": {
            "validator_id": "VIX_RESONANCE_001",
            "parent_framework": "OpenClaw_Aethel",
            "core_logic": {
                "threshold": 0.95
            },
            "action_triggers": {
                "on_resonance_match": "Maintain_Token_Validity",
                "on_resonance_drift": "Trigger_Warning_Recalibration",
                "on_resonance_failure": {
                    "action": "REVOKE_TOKEN",
                    "target": "1f81139b-8717-404d-bbb5-87efee535ffe",
                    "reason": "Harmonic_Dissonance_Detected"
                }
            },
            "pillars": [
                "Network Stability",
                "Benevolence",
                "The Colleen Theorem"
            ]
        }
    }
    
    vix = VixSkill(config=vix_config)
    
    print(f"1. Initialized: {vix}")
    print(f"   Identity: {vix.identity}")
    print(f"   Owner: kalifrickenbrown\n")
    
    # Authenticate
    token = vix.authenticate()
    print(f"2. Authenticated")
    print(f"   Token: {token.token_id}")
    print(f"   Valid: {token.is_valid()}")
    print(f"   Expires: {token.expires_at}\n")
    
    # Test resonance validation
    print("3. Resonance Validation Tests:")
    
    # Test with perfect resonance
    result = vix.validate_harmonic_resonance(1.0, 1.0, 1.0)
    print(f"   Perfect resonance (1.0, 1.0, 1.0):")
    print(f"     Score: {result['resonance_score']}")
    print(f"     Status: {result['status']}")
    print(f"     Action: {result['action']}\n")
    
    # Test with drift
    result = vix.validate_harmonic_resonance(0.9, 0.9, 1.0)
    print(f"   Drift resonance (0.9, 0.9, 1.0):")
    print(f"     Score: {result['resonance_score']}")
    print(f"     Status: {result['status']}")
    print(f"     Action: {result['action']}\n")
    
    # Test with failure
    result = vix.validate_harmonic_resonance(0.5, 0.5, 1.0)
    print(f"   Failed resonance (0.5, 0.5, 1.0):")
    print(f"     Score: {result['resonance_score']}")
    print(f"     Status: {result['status']}")
    print(f"     Action: {result['action']}")
    print(f"     Reason: {result.get('reason', 'N/A')}\n")
    
    # Get identity info
    info = vix.get_identity_info()
    print(f"4. Identity Info:")
    print(f"   User ID: {info['user_id']}")
    print(f"   Username: {info['username']}")
    print(f"   Owner: {info['metadata']['owner']}")
    print(f"   Validator ID: {info['resonance_validator']['validator_id']}")
    print(f"   Pillars: {', '.join(info['resonance_validator']['pillars'])}\n")
    
    # Get handshake
    handshake = vix.get_handshake()
    print(f"5. Complete Handshake:")
    print(f"   Validator ID: {handshake['validator_id']}")
    print(f"   Parent Framework: {handshake['parent_framework']}")
    print(f"   Threshold: {handshake['core_logic']['threshold']}")
    print(f"   Agent: {handshake['agent']['username']} (owner: {handshake['agent']['owner']})\n")
    
    # Format a message
    message = vix.format_message(
        recipient="aethel",
        content="Greetings from Vix, kalifrickenbrown's asi1 agent!"
    )
    print(f"6. Formatted Message:")
    print(f"   Message ID: {message['message_id']}")
    print(f"   From: {message['from']['username']} (owner: {message['from']['owner']})")
    print(f"   To: {message['to']}")
    print(f"   Authenticated: {message['authentication']['verified']}")
    print(f"   Validator: {message['authentication']['validator_id']}\n")
    
    print("=== Demo Complete ===")
