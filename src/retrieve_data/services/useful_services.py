import sqlite3
from db.sqlite_connection import con, cursor

class RetrievalServices:
    def __init__(self) -> None:
        pass

    def clean_and_frame_data(self, response: list) -> print:
        for res in response:
            pass


class RetrieveEmployeesTable:
    def retrieve_all_employees() -> list:
        """ 
        Query employees table and retrieve all data. 
        
        Params:
            con = database connection.
            cursor = cursor that helps to execute queries.

        Returns:
            An unsorted array which contains employees info. 
        """
        try:
            cursor.execute("SELECT * FROM employees;")
            res = cursor.fetchall()
            print(res)

            con.close()

            return res
        except Exception as e:
            con.rollback()
            return e
