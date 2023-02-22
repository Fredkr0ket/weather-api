from fastapi import FastAPI
from models.Weather import  WeatherRes
from datetime import datetime
from services.Weather import Weather
from config.DatabaseConnection import cursor



app = FastAPI()




@app.get("/getweather/")
def read_getweather(id: int = None, location: str = None, date: datetime = None ) -> list[WeatherRes]:
    weatherData = {"id": id, "location": location, "date": date}
    weather = Weather(weatherData, cursor)
    return weather.get()

