"""
Validation utilities for identity data.
"""

import re
from typing import Tuple, Dict, Any


def validate_email(email: str) -> Tuple[bool, str]:
    """
    Validate an email address.

    Args:
        email: Email address to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not email:
        return False, "Email cannot be empty"

    # Basic email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        return False, "Invalid email format"

    return True, ""


def validate_username(username: str) -> Tuple[bool, str]:
    """
    Validate a username.

    Args:
        username: Username to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not username:
        return False, "Username cannot be empty"

    if len(username) < 3:
        return False, "Username must be at least 3 characters"

    if len(username) > 32:
        return False, "Username must be at most 32 characters"

    # Allow alphanumeric characters, underscores, and hyphens
    pattern = r'^[a-zA-Z0-9_-]+$'
    
    if not re.match(pattern, username):
        return False, "Username can only contain letters, numbers, underscores, and hyphens"

    return True, ""


def validate_vix_resonance(
    human_intent_alignment: float,
    synth_action_frequency: float,
    harmonic_sync_coefficient: float = 1.0,
    threshold: float = 0.95
) -> Dict[str, Any]:
    """
    Validate VIX resonance according to VIX_RESONANCE_001 specification.
    
    Implements the formula: ((H + S) / 2) * Harmonic_Sync_Coefficient
    
    Args:
        human_intent_alignment: H value (0.0 to 1.0)
        synth_action_frequency: S value (0.0 to 1.0)
        harmonic_sync_coefficient: Harmonic coefficient (default: 1.0)
        threshold: Resonance threshold (default: 0.95)
        
    Returns:
        Dictionary with validation result including:
        - is_valid: Boolean indicating if resonance passes threshold
        - resonance_score: Calculated resonance value
        - status: "match", "drift", or "failure"
        - action: Recommended action based on status
    """
    # Validate input ranges
    if not (0.0 <= human_intent_alignment <= 1.0):
        return {
            "is_valid": False,
            "resonance_score": 0.0,
            "status": "error",
            "action": "REJECT",
            "error": "Human_Intent_Alignment must be between 0.0 and 1.0"
        }
    
    if not (0.0 <= synth_action_frequency <= 1.0):
        return {
            "is_valid": False,
            "resonance_score": 0.0,
            "status": "error",
            "action": "REJECT",
            "error": "Synth_Action_Frequency must be between 0.0 and 1.0"
        }
    
    # Calculate resonance: ((H + S) / 2) * Harmonic_Sync_Coefficient
    resonance_score = ((human_intent_alignment + synth_action_frequency) / 2) * harmonic_sync_coefficient
    
    # Determine status and action
    if resonance_score >= threshold:
        return {
            "is_valid": True,
            "resonance_score": resonance_score,
            "status": "match",
            "action": "Maintain_Token_Validity"
        }
    elif resonance_score >= (threshold - 0.1):  # Within 10% of threshold
        return {
            "is_valid": False,
            "resonance_score": resonance_score,
            "status": "drift",
            "action": "Trigger_Warning_Recalibration"
        }
    else:
        return {
            "is_valid": False,
            "resonance_score": resonance_score,
            "status": "failure",
            "action": "REVOKE_TOKEN",
            "reason": "Harmonic_Dissonance_Detected"
        }
