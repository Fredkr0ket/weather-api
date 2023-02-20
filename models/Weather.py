from pydantic import BaseModel
class WeatherCreate(BaseModel):
  location: str
  temperature: int 
  humidity: int

class WeatherReturn(WeatherCreate):
  id: int
  date: str

class WeatherGet(BaseModel):
  id: int | None
  location: str | None
  date: str | None




