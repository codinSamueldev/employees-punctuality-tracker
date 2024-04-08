import os.path
import sqlite3


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "employees.db")


con = sqlite3.connect(db_path)
cursor = con.cursor()
