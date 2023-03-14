from pydantic import BaseModel
from datetime import datetime

class WeatherInput(BaseModel):
  location: str 
  date: datetime | None = None
class WeatherCreate(BaseModel):
  location: str
  temperature: int
  humidity: int

class WeatherRes(WeatherCreate):
  id: int
  date: datetime

class WeatherGet(WeatherCreate):
  id: int
  date: datetime






