from .Database import Database
import os
from dotenv import load_dotenv

load_dotenv()

db = Database(os.getenv("DB_HOST"), os.getenv("DB_USER"), os.getenv("DB_PASS"), os.getenv("DB_NAME"))
weatherdb = db.connect()
cursor = weatherdb.cursor()