from fastapi import FastAPI
from models.Weather import  WeatherRes
from datetime import datetime
from services.Weather import Weather
from config.DatabaseConnection import cursor



app = FastAPI()




@app.get("/getweather/{location}")
def read_getweather(location: str, date: str = None) -> list[WeatherRes]:
    weatherData = {"location": location, "weather_date": date}
    weather = Weather(weatherData, cursor)
    return weather.get()

