from fastapi import HTTPException
from .Functions import tupleToDict
from models.Weather import WeatherCreate, WeatherGet, WeatherInput
from mysql.connector import MySQLConnection

class Weather:
    def __init__(self, inputData: WeatherInput | WeatherCreate, db: MySQLConnection):
        self.data = inputData
        self.db = db

        
    def __getFromDb(self):
        with self.db.cursor() as cursor:
            location = '"' + self.data['location'] + '"'
            query = f'SELECT * FROM weather_data WHERE location = {location}'

            for key in self.data:
                value = self.data[key]

                if key == 'location' or key == None:
                    continue 

                if type(value) == dict:
                    value1 = '"' + value['value1'] + '"'
                    value2 = '"' + value['value2'] + '"'
                    queryAdd = f'and {key} >= {value1} and {key} <= {value2}'
                    query += queryAdd

                elif value != None:
                    newValue = '"' + value + '"'
                    queryAdd = f' and {key} = {newValue}'
                    query += queryAdd

            cursor.execute(query)
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
        if len(newResults) <= 1:
            return newResults
        return newResults
    
    def post(self) -> HTTPException:
        location = '"' + self.data.location + '"'
        temperature = self.data.temperature
        humidity = self.data.humidity
        postQuery = f'INSERT INTO weather_data (`location`, `temperature`, `humidity`) VALUES ({location}, {temperature}, {humidity})'
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





  


