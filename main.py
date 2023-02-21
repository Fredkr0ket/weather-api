from fastapi import FastAPI, HTTPException
from config.Database import cursor
from models.Weather import WeatherGet, WeatherRes
from datetime import datetime
from services.TupleToDict import tupleToDict
from services.Weather import Weather
# ERROR: ImportError: attempted relative import beyond top-level package 

app = FastAPI()

# def GetWeather(data: WeatherGet):
#     if (data["id"] != None):
#         sql = f'SELECT * FROM weather_data WHERE id = {data["id"]}'
#     elif (data["location"]):
#         sql = f'SELECT * FROM weather_data WHERE location = {data["location"]}'
#     elif (data["date"]):
#         sql = f'SELECT * FROM weather_data WHERE weather_date = {data["date"]}'
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     return results



@app.get("/getweather/")
def read_getweather(id: int = None, location: str = None, date: datetime = None ) -> list[WeatherRes]:
    pass
