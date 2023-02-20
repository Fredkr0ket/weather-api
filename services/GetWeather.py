from ..config.Database import cursor
from ..models.weather import  WeatherGet, WeatherReturn 
import mysql

def GetWeather(data: WeatherGet):
    print(data)
    if (data["id"] != None):
        sql = f'SELECT * FROM weather_data WHERE id = {data["id"]}'
    elif (data["location"]):
        sql = f'SELECT * FROM weather_data WHERE location = {data["location"]}'
    elif (data["date"]):
        sql = f'SELECT * FROM weather_data WHERE weather_date = {data["date"]}'
    cursor.execute(sql)
    result = cursor.fetchall()
    return result 

  


