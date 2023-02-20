from ..config.Database import cursor
from ..models.weather import  WeatherGet, WeatherReturn 
import mysql

def GetWeather(data: WeatherGet):
  if (data.id):
    sql = f'SELECT * FROM {data.table} WHERE id = {data.id}'
  elif (data.location):
    sql = f'SELECT * FROM {data.table} WHERE location = {data.location}'
  elif (data.location):
    sql = f'SELECT * FROM {data.table} WHERE weather_date = {data.weather_date}'
  cursor.execute(sql)
  result: WeatherReturn = cursor.fetchall()
  return result 
  

  


