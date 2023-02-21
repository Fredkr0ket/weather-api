from fastapi import FastAPI
from models.Weather import  WeatherRes
from datetime import datetime
from services import Weather
from config.DatabaseConnection import cursor
from config.Database import Database
# ERROR: ImportError: attempted relative import beyond top-level package 

app = FastAPI()




@app.get("/getweather/")
def read_getweather(id: int = None, location: str = None, date: datetime = None ) -> list[WeatherRes]:
    weatherData = {"id": id, "location": location, "date": date}
    weather = Weather.Weather(weatherData)
    return weather.get(cursor)

