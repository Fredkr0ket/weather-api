from fastapi import FastAPI, HTTPException
from config.Database import Database, cursor
from models.Weather import WeatherGet, WeatherRes
from datetime import datetime
from services.TupleToDict import tupleToDict
# from services.GetWeather import GetWeather
# ERROR: ImportError: attempted relative import beyond top-level package 

app = FastAPI()

def GetWeather(data: WeatherGet):
    if (data["id"] != None):
        sql = f'SELECT * FROM weather_data WHERE id = {data["id"]}'
    elif (data["location"]):
        sql = f'SELECT * FROM weather_data WHERE location = {data["location"]}'
    elif (data["date"]):
        sql = f'SELECT * FROM weather_data WHERE weather_date = {data["date"]}'
    cursor.execute(sql)
    results = cursor.fetchall()
    return results



@app.get("/getweather/")
def read_getweather(id: int = None, location: str = None, date: datetime = None ):
    if (id == None and location == None and date == None):
        raise HTTPException(
            status_code=422, 
            detail="No parameters"
        )
    data: WeatherGet = {"id": id, "location": location, "date": date}
    results = GetWeather(data)
    newResults: list[GetWeather] = []
    dictNames = ["id", "location", "temperature", "humidity", "date"]
    for result in results:
        res = tupleToDict(result, dictNames)
        newResults.append(res)       
        
    return newResults
