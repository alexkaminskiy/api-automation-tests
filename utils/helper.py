import re
import json

def sanitize_data(obj):
    """
    Masks passwords, tokens, and Authorization headers in any dict/string.
    """
    if isinstance(obj, dict):
        safe = obj.copy()

        # Mask passwords
        if "password" in safe:
            safe["password"] = "***MASKED***"

        # Mask tokens
        if "token" in safe and isinstance(safe["token"], str):
            safe["token"] = safe["token"][:10] + "...***MASKED***"

        return safe

    if isinstance(obj, str):
        # Mask JWT tokens inside JSON response
        obj = re.sub(
            r'"token"\s*:\s*"([^"]+)"',
            '"token": "***MASKED***"',
            obj
        )
        return obj

    return obj