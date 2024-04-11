import sqlite3

class InsertIntoTrackerTable:
    def __init__(self, con: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
        self.con = con
        self.cursor = cursor

    def insert_new_data_to_tracker(self) -> list:
        """ 
        Insert new data to the tracker table. 
        
        Params:
            None

        Returns:
            boolean value whether it was succesfully inserted the data or not. 
        """
        # Try to execute query, if error raised, then, rollback database.
        try:
            # Tuple that will contain required info.
            basic_data = ()

            # Ask user info and save it into tuple (basic_data).
            employee_id = int(input("""
        Type employee id:  """))
            current_date = input("""
        Type current date with the following format (DD/MM/YY):  """).strip()
            entry_hour = input("""
        Type employee today's entry hour with the following format (10:05 AM, or, 05:41 PM): """).strip()
            exit_hour = input("""
        Type employee today's exit hour with the following format (10:05 AM, or, 05:41 PM): """).strip()

            basic_data = (employee_id, current_date, entry_hour, exit_hour)
        
            self.cursor.execute("INSERT INTO tracker (employee_id, date, entry_hour, exit_hour) VALUES (?, ?, ?, ?)", basic_data)
                    
            self.con.commit()
            self.con.close()
            return True
        except Exception as e:
            self.con.rollback()
            print(e)
            return False
