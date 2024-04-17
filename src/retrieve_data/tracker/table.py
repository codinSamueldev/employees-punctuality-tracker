import sqlite3

class RetrieveTrackerTable:
    def __init__(self, con: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
        self.con = con
        self.cursor = cursor

    def retrieve_tardiness_tracker(self) -> list:
        """ 
        Query tardiness tracker table and retrieve all data. 
        
        Params:
            None

        Returns:
            An unsorted array of tuples with tracker info. 
        """
        try:
            self.cursor.execute("SELECT * FROM tracker;")
            res = self.cursor.fetchall()
            print(res)

            self.con.close()

            return res
        except Exception as e:
            self.con.rollback()
            print(e)
            return e
