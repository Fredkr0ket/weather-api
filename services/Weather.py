
from fastapi import HTTPException
from .TupleToDict import tupleToDict
from models.Weather import WeatherGet, WeatherInput
from mysql.connector.cursor import CursorBase

class Weather:
    def __init__(self, inputData: WeatherInput, cursor: CursorBase):
        self.id = inputData["id"]
        self.date = inputData["date"]
        self.location = inputData["location"]
        self.cursor = cursor

        
    
    def __getFromDb(self):
        if (self.id != None):
            sql = f'SELECT * FROM weather_data WHERE id = {self.id}'
        elif (self.location != None):
            sql = f'SELECT * FROM weather_data WHERE location = {self.location}'
        elif (self.date != None):
            sql = f'SELECT * FROM weather_data WHERE weather_date = {self.date}'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result 


    def get(self):
        if (self.id == None and self.date == None and self.location == None):
            raise HTTPException(
                status_code=422, 
                detail="No parameters"
            )
    
        data: WeatherGet = {"id": self.id, "location": self.location, "date": self.date}
        results = self.__getFromDb()
        newResults: list[WeatherGet] = []
        dictNames = ["id", "location", "temperature", "humidity", "date"]

        for result in results:
            res = tupleToDict(result, dictNames)
            newResults.append(res)
            
        return newResults


  


