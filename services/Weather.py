from fastapi import HTTPException
from .Functions import tupleToDict
from models.Weather import WeatherCreate, WeatherGet, WeatherInput
from mysql.connector import MySQLConnection

class Weather:
    def __init__(self, inputData: WeatherInput | WeatherCreate, db: MySQLConnection):
        # Initialize the class with input data and a database connection
        self.data = inputData
        self.db = db

    # Private method to get weather data from the database
    def __getFromDb(self):
        with self.db.cursor() as cursor:
            # Build the query using the location from the input data
            location = '"' + self.data['location'] + '"'
            query = f'SELECT * FROM weather_data WHERE location = {location}'

            # Add additional search criteria based on the input data
            for key in self.data:
                value = self.data[key]

                # Skip location and None values
                if key == 'location' or key == None:
                    continue 

                # For dictionary values, add range search criteria
                if type(value) == dict:
                    value1 = '"' + value['value1'] + '"'
                    value2 = '"' + value['value2'] + '"'
                    queryAdd = f'and {key} >= {value1} and {key} <= {value2}'
                    query += queryAdd

                # For other values, add exact search criteria
                elif value != None:
                    newValue = '"' + value + '"'
                    queryAdd = f' and {key} = {newValue}'
                    query += queryAdd

            # Execute the query and get the results
            cursor.execute(query)
            result = cursor.fetchall()

             # If no results were found, raise an HTTPException with a 400 status code
            if result == []:
                raise HTTPException(
                    status_code=400
                )
            return result 

    # Method to retrieve weather data from the database
    def get(self) -> list[WeatherGet]:
        # Call the __getFromDb method to retrieve the data
        results = self.__getFromDb()
        # Convert the tuples to dictionaries with specified key names
        newResults: list[WeatherGet] = []
        dictNames = ["id", "location", "temperature", "humidity", "date"]
        for result in results:
            res = tupleToDict(result, dictNames)
            newResults.append(res)

        # Return the results
        if len(newResults) <= 1:
            return newResults
        return newResults

    # Method to add weather data to the database
    def post(self) -> HTTPException:
        # Build the insert query using the input data
        location = '"' + self.data.location + '"'
        temperature = self.data.temperature
        humidity = self.data.humidity
        postQuery = f'INSERT INTO weather_data (`weather_location`, `temperature`, `humidity`) VALUES ({location}, {temperature}, {humidity})'

        # Execute the insert query or trow error code
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