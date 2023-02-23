from fastapi import HTTPException
from .TupleToDict import tupleToDict
from models.Weather import WeatherCreate, WeatherGet, WeatherInput
from mysql.connector import MySQLConnection

class Weather:
    def __init__(self, inputData: WeatherInput | WeatherCreate, db: MySQLConnection):
        self.data = inputData
        self.db = db

        
    def __getFromDb(self):
        with self.db.cursor() as cursor:
            location = '"' + self.data['location'] + '"'
            sql = f'SELECT * FROM weather_data WHERE location = {location}'
            for key in self.data:
                if key == 'location':
                    continue
                value = self.data[key]
                if value:
                    newValue = '"' + value + '"'
                    newSql = f' and {key} = {newValue}'
                    sql += newSql
                    print(sql)

            cursor.execute(sql)
            result = cursor.fetchall()

            if result == []:
                raise HTTPException(
                    status_code=400
                )
            return result 


    def get(self) -> list[WeatherGet]:
        results = self.__getFromDb()
        newResults: list[WeatherGet] = []
        dictNames = ["id", "location", "temperature", "humidity", "date"]
        for result in results:
            res = tupleToDict(result, dictNames)
            newResults.append(res)
        return newResults
    
    def post(self) -> HTTPException:
        location = '"' + self.data.location + '"'
        temperature = self.data.temperature
        humidity = self.data.humidity
        postQuery = f'INSERT INTO weather_data (`location`, `temperature`, `humidity`) VALUES ({location}, {temperature}, {humidity})'
        print(postQuery)
        with self.db.cursor() as cursor:
            try:
                cursor.execute(postQuery)
                self.db.commit()
            except:
                raise HTTPException(
                    status_code=400
                )
            else:
                raise HTTPException(
                    status_code=200
                )





  


