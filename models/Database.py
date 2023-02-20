from pydantic import BaseModel
class DatabaseConnect(BaseModel):
  host: str
  user: str
  password: str
  database: str


  