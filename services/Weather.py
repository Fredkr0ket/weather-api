from .TupleToDict import tupleToDict
from models.Weather import WeatherGet, WeatherInput
from mysql.connector.cursor import CursorBase

class Weather:
    def __init__(self, inputData: WeatherInput, cursor: CursorBase):
        self.data = inputData
        self.cursor = cursor

        
    def __getFromDb(self):
        location = '"' + self.data['location'] + '"'
        sql = f'SELECT * FROM weather_data WHERE location = {location}'
        print(self.data)
        for key in self.data:
            if key == 'location':
                continue
            value = self.data[key]
            if value != None:
                
                newSql = f' and {key} = {value}'
                sql += newSql
                print(sql)

        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result 


    def get(self):
        results = self.__getFromDb()
        newResults: list[WeatherGet] = []
        dictNames = ["id", "location", "temperature", "humidity", "date"]

        for result in results:
            res = tupleToDict(result, dictNames)
            newResults.append(res)
            
        return newResults


  


