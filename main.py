from fastapi import FastAPI, HTTPException
from models.Weather import  WeatherRes, WeatherCreate
from services.Weather import Weather
from dotenv import load_dotenv
from config.Database import Database
import os

app = FastAPI()
load_dotenv()
dbCredentials = {"host": os.getenv("DB_HOST"), 
                 "user": os.getenv("DB_USER"), 
                 "password": os.getenv("DB_PASS"),
                 "database": os.getenv("DB_NAME")}
db = Database(dbCredentials).connect()


@app.get("/getweather/{location}")
def get_weather(location: str, date: str = None) -> list[WeatherRes]:
    weatherData = {"location": location, 
                   "weather_date": date }
    weather = Weather(weatherData, db)
    return weather.get()

@app.post("/addweather/")
def post_weather(weatherData: WeatherCreate):
    weather = Weather(weatherData, db)
    weather.post()

    

