import datetime
from mysqlx import Column
from pydantic import BaseModel


class WeatherItem(BaseModel):
  __tablename__ = "weatherdata"

  id = Column(int, primary_key=True, index=True)
  location = Column(str, default=None)
  temperature = Column(int, default=False)
  humidity = Column(int, default=False)
  weather_date = Column(datetime.datatime)
