from pydantic import BaseModel
from datetime import datetime

class WeatherInput(BaseModel):
  id: int | None = None
  location: str | None = None
  date: datetime | None = None
class WeatherCreate(BaseModel):
  location: str
  temperature: int 
  humidity: int

class WeatherRes(WeatherCreate):
  id: int
  date: datetime

class WeatherGet(BaseModel):
  id: int | None
  location: str | None
  date: datetime | None
  





