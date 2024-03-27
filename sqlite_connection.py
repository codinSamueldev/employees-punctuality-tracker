import sqlite3

def db_connection() -> sqlite3.cursor:
    with sqlite3.connect('employees.db') as EMPLOYEES_DB_CONNECTION:
        cursor = EMPLOYEES_DB_CONNECTION.cursor()
        
        return cursor
