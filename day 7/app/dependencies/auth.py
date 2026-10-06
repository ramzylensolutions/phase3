from fastapi import Request
from fastapi import HTTPException
from ..config import settings
async def verify_token(request:Request):
    authorization = request.headers.get("Authorization")
    if not authorization:
        raise HTTPException(
            status_code=404,
            detail="Authorization not found"
        )
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=404,
            detail="Invalid Authorization"
        )
    if authorization[7: ] != settings.token_id:
        raise HTTPException(
            status_code=404,
            detail="Wrong Credentials"
        )