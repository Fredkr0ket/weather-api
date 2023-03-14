from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

class Auth:
    """
    A class for authenticating API requests using a token.
    Attributes:
        token (str): The token to use for authentication.
    """
    def __init__(self, token: str):
        """
        Initializes the Auth class with the given token.
        Args:
            token (str): The token to use for authentication.
        Raises:
            HTTPException: If the provided token does not match the expected API_AUTH token.
        """
        if token != os.getenv("API_AUTH"):
            raise HTTPException(
                status_code=401
            )