from fastapi import Request, HTTPException
import jwt  # PyJWT
from app.core.config import settings
from typing import Optional


class JWTManager:
    """Every utlities related to the JWT"""

    def __init__(self, request: Request):
        self.request: Request = request
        self.__claims: Optional[dict] = None

    @property
    def claims(self) -> Optional[dict]:
        """Get the claims from the token"""
        return self.__claims

    @claims.setter
    def claims(self, value: dict):
        """Set the claims."""
        self.__claims = value

    def verify_jwt_in_request(self):
        """Verify the jwt tokens"""

        # parse jwt token from header
        encoded_token = self.get_jwt_from_header()

        # decode token
        claims = self.decode_token(encoded_token=encoded_token)

        # Set the claims for the future use
        self.claims = claims

        return True

    def get_jwt_from_header(self) -> str:
        """Parse and retrieve the jwt token from header"""
        # Extract Bearer token
        auth_header = self.request.headers.get("Authorization")
        if not auth_header:
            raise HTTPException(status_code=401, detail="Missing token")

        if not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Invalid token format")

        encoded_token = auth_header.split(" ")[1]

        # Return encoded token
        return encoded_token

    def decode_token(self, encoded_token: str):
        """decode token and return the claims."""
        try:
            claims = jwt.decode(
                jwt=encoded_token,
                key=settings.SECRET_KEY,
                algorithms=settings.ALGORITHM,
            )
        except jwt.ExpiredSignatureError as exc:
            raise HTTPException(
                status_code=401, detail="Token expired"
            ) from exc
        except jwt.InvalidTokenError as exc:
            raise HTTPException(
                status_code=401, detail="Invalid token"
            ) from exc

        return claims
