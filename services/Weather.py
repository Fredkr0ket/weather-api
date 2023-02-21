from fastapi import HTTPException
from .TupleToDict import tupleToDict
from ..models.Weather import WeatherGet, WeatherInput
from ..config.Database import cursor

class Weather:
    def __init__(data, inputData: WeatherInput, cursor):
        data.id = inputData["id"]
        data.date = inputData["date"]
        data.location = inputData["location"]
        data.cursor = cursor

    
    def __getFromDb(data):
        if (data.date != None):
            sql = f'SELECT * FROM weather_data WHERE id = {data.id}'
        elif (data.location):
            sql = f'SELECT * FROM weather_data WHERE location = {data.location}'
        elif (data.date):
            sql = f'SELECT * FROM weather_data WHERE weather_date = {data.date}'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result 


    def get(data):
        if (data.id == None and data.date == None and data.location == None):
            raise HTTPException(
                status_code=422, 
                detail="No parameters"
            )
    
        data: WeatherGet = {"id": data.id, "location": data.location, "date": data.date}
        results = Weather.Get(data, data.cursor)
        newResults: list[WeatherGet] = []
        dictNames = ["id", "location", "temperature", "humidity", "date"]

        for result in results:
            res = tupleToDict(result, dictNames)
            newResults.append(res)
            
        return newResults


  


