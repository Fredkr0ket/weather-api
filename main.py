from typing import Union
from fastapi import FastAPI, HTTPException
from config.Database import Database
from models.Weather import WeatherGet
from config.Database import cursor
# from services.GetWeather import GetWeather
# ERROR: ImportError: attempted relative import beyond top-level package 

app = FastAPI()

def GetWeather(data: WeatherGet):
    print(data)
    if (data["id"] != None):
        sql = f'SELECT * FROM weather_data WHERE id = {data["id"]}'
    elif (data["location"]):
        sql = f'SELECT * FROM weather_data WHERE location = {data["location"]}'
    elif (data["date"]):
        sql = f'SELECT * FROM weather_data WHERE weather_date = {data["date"]}'
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return result 


@app.get("/getweather/")
def read_getweather(id: int = None, location: str = None, date: str = None ):
    if (id == None and location == None and date == None):
        raise HTTPException(
            status_code=422, 
            detail="No parameters"
        )
    data = {"id": id, "location": location, "date": date}
    result = GetWeather(data)
    return result
    # return {"id": id, "location": location, "date": date}


