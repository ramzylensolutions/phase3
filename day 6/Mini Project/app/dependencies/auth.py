from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from ..config import settings


bearer_scheme = HTTPBearer()


async def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)
):
    token = credentials.credentials

    api_key = settings.api_key

    if api_key != token:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )