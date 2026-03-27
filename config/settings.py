import os


BASE_URL = os.getenv("BASE_URL", "http://eaapi.somee.com/")
AUTH_USER = os.getenv("AUTH_USER_NAME")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")



# If token reused across tests:
TOKEN_CACHE = ".token_cache"
