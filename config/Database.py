import mysql.connector as mysql
from models.Database import DatabaseCredentials
class Database:
  def __init__(self, dbCredentials: DatabaseCredentials):
    self.host = dbCredentials["host"]
    self.user = dbCredentials["user"]
    self.password = dbCredentials["password"]
    self.database = dbCredentials["database"]

  def connect(self):
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
