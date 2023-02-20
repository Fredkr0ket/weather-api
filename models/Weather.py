from pydantic import BaseModel
from datetime import datetime

class WeatherCreate(BaseModel):
  location: str
  temperature: int 
  humidity: int

class WeatherRes(WeatherCreate):
  id: int
  location: str
  temperature: int 
  humidity: int
  date: datetime

class WeatherGet(BaseModel):
  id: int | None
  location: str | None
  date: datetime | None
  





