# Weather API
**the api is still a work in progress**
Weather api created using fastapi framework.
the api gets the data from a mysql database.

eventualy the data that is going to be used is going to come from an [esp32](https://github.com/Fredkr0ket/weather-esp) with a couple of sensors.

## How to run
1. clone the repository
2. start up an MySQL Server preferably version 8.0.32
3. import the database file that is located in the`/database` directory
4. configure your database credentials into the `/.env` file
5. configure your api token you wane use in the `/.env` file
6. install all the python packages that are used by the api by running
`pip install -r requirements.txt`
7. to run the api run `uvicorn main:app --reload` 





