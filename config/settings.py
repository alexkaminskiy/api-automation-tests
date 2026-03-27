import os


BASE_URL = os.getenv("BASE_URL", "http://eaapi.somee.com/")
AUTH_USER = os.getenv("AUTH_USER_NAME")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")

print(f"Using base URL: {BASE_URL}")
print(f"Using auth user: {AUTH_USER}")
print(f"Using auth password: {'*' * len(AUTH_PASSWORD) if AUTH_PASSWORD else None}")

# If token reused across tests:
TOKEN_CACHE = ".token_cache"
