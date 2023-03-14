from pydantic import BaseModel
class DatabaseCredentials(BaseModel):
  host: str
  user: str
  password: str
  database: str