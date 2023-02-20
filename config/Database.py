import mysql.connector as mysql

class Database:
  def __init__(self, host, user, password, database):
    self.host = host
    self.user = user
    self.password = password
    self.database = database

  def connect(self):
    try:
      db = mysql.connect(
        host = self.host,
        user = self.user,
        password = self.password,
        database = self.database
      )
      return db
    except:
      print("connection could not be made, try again later")
    else:
      print("connection made succesfully")


  def closeConnection(cursor, database):
    try:
      cursor.close()
      database.close()
    except:
      print("could not be close, try again later")
    else: 
      print("closed succesfully")

db = Database("localhost", "root", "toor", "weatherdatabase")
weatherdb = db.connect()
cursor = weatherdb.cursor()
