import sqlite3

class RetrieveSchedulesTable:
    def __init__(self, con: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
        self.con = con
        self.cursor = cursor

    def retrieve_employees_schedules(self) -> list:
        """ 
        Query employee's schedules table and retrieve all data. 
        
        Params:
            None

        Returns:
            An unsorted array of tuples which contains employee's schedules info. 
        """
        try:
            self.cursor.execute("SELECT * FROM schedules;")
            res = self.cursor.fetchall()
            print(res)

            self.con.close()

            return res
        except Exception as e:
            self.con.rollback()
            return e
