from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from starlette import status
import os

VALID_KEYS = {
    "api_password": "user",
}

X_API_KEY = APIKeyHeader(name='X-Api-Key')

def verify_token(x_api_key: str = Depends(X_API_KEY)):
    try:
        return VALID_KEYS[x_api_key]
    except KeyError:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API Key",
    )