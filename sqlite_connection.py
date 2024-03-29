import sqlite3

def db_connection() -> sqlite3.Connection:
        con = sqlite3.connect('employees.db')
        
        return con
    
def db_cursor() -> sqlite3.Cursor:
    con = db_connection()
    cursor = con.cursor()

    return cursor
