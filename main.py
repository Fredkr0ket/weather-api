from fastapi import  FastAPI
import uvicorn
from models.Weather import  WeatherRes, WeatherCreate
from services.Weather import Weather
from services.Auth import Auth
from dotenv import load_dotenv
from config.Database import Database
from services.Functions import checkItems
import os


# link: https://github.com/Fredkr0ket/weather-api

app = FastAPI()
load_dotenv()

# getting the database credentials from the .env file and putting them into a dbCredentials dictionary
dbCredentials = {"host": os.getenv("DB_HOST"),
                 "user": os.getenv("DB_USER"),
                 "password": os.getenv("DB_PASS"),
                 "database": os.getenv("DB_NAME")}

# creating an instance of the Database class using the the dbCreadentials and connecting to that instance
db = Database(dbCredentials).connect()


@app.get("/getweather/{location}")
def get_weather(location: str, token: str, date: str = None, date_end: str = None) -> list[WeatherRes] | WeatherRes:
    '''
    Use this endpoint to get data from the weatherdata database
    Location: string = location of the weatherdata
    Token: string = authentication token that you configured in the .env file

    if you use Date and Date_end together you get all the data of the period between the to time points,
    but if you only use te Date you only get the weather data of that single time point.

    Example:
    you wane get the data between 2022 and 2023 you Date should be: 2022-01-01 00:00:00 and Date_end should be: 2023-01-01 00:00:00

    Date: datetime string = the data of any calculated data.
    Date_end: datetime string = the end date.
    '''
    Auth(token)
    date =  checkItems(date, date_end)
    weatherData = {"weather_location": location,
                   "weather_date": date}

    weather = Weather(weatherData, db)
    result = weather.get()
    return result

# weatherSetter
@app.post("/addweather/")
def post_weather(weatherData: WeatherCreate, token: str):
    '''
    Use this end point to add data to the database.
    Token: string = authentication token that you configured in the .env file
    Request body: {
        location: string,
        temperature: integer,
        humidity: integer
    }
    '''
    Auth(token)
    weather = Weather(weatherData, db)
    weather.post()

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
