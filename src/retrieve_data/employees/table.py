import sqlite3

class RetrieveEmployeesTable:
    def __init__(self, con: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
        self.con = con
        self.cursor = cursor

    def retrieve_all_employees(self) -> list:
        """ 
        Query employees table and retrieve all data. 
        
        Params:
            None

        Returns:
            An unsorted array of tuples which contains employees info. 
        """
        try:
            self.cursor.execute("SELECT * FROM employees;")
            res = self.cursor.fetchall()
            print(res)

            self.con.close()

            return res
        except Exception as e:
            self.con.rollback()
            return e
