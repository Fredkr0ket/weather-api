import mysql.connector as mysql
from models.Database import DatabaseCredentials
class Database:
  def __init__(self, dbCredentials: DatabaseCredentials):
    '''
     This is a constructor method which initializes the database credentials provided in the argument.
     It creates instance variables for host, user, password and database which are used for establishing a connection.
    '''
    self.host = dbCredentials["host"]
    self.user = dbCredentials["user"]
    self.password = dbCredentials["password"]
    self.database = dbCredentials["database"]

  def connect(self):
    '''
    This method tries to establish a connection to the MySQL database using the credentials provided in the constructor. 
    If the connection is successful, it returns the database object. 
    If the connection fails, an error message is displayed and None is returned.
    '''
    try:
      db = mysql.connect(
        host = self.host,
        user = self.user,
        password = self.password,
        database = self.database
      )
    except:
      print("❌ database connection could not be made, try again later ❌")
    else:
      print("🔗 database connection made succesfully 🔗")
      return db
