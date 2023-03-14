from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

class Auth:
    def __init__(self, token: str):
        if token != os.getenv("API_AUTH"):
            raise HTTPException(
                status_code=401
            )