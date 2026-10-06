from fastapi import HTTPException,Request
from ..envretrive import settings
async def verify_token(request: Request):
    print("Verify Token Started")
    authorization = request.headers.get("Authorization")
    if not authorization:
        raise HTTPException(
            status_code=404,
            detail="Authorization Not Found"
        )
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=404,
            detail="Invalid Authorization"
        )
    if authorization[7:] != settings.token_key:
        raise HTTPException(
            status_code=404,
            detail="Wrong Authrization key"
        )