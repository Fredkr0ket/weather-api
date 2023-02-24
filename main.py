from fastapi import Depends, FastAPI
from models.Weather import  WeatherRes, WeatherCreate
from services.Weather import Weather
from services.Auth import Auth
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
def get_weather(location: str, token: str, date: str = None) -> list[WeatherRes]:
    Auth(token)
    weatherData = {"location": location, 
                   "weather_date": date }
    weather = Weather(weatherData, db)
    result = weather.get()
    return result

@app.post("/addweather/")
def post_weather(weatherData: WeatherCreate, token: str):
    Auth(token)
    weather = Weather(weatherData, db)
    weather.post()

    

