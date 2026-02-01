"""
Validation utilities for identity data.
"""

import re
from typing import Tuple


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
