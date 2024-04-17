import sqlite3, time

class InsertIntoSchedulesTable:
    def __init__(self, con: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
        self.con = con
        self.cursor = cursor

    def insert_new_schedule(self) -> bool:
        """ 
        Insert new data into schedule table. 
        
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
            start_time = input("""
        Type employee today's entry hour with the following format (10:05 AM, or, 05:41 PM): """).strip()
            end_time = input("""
        Type employee today's exit hour with the following format (10:05 AM, or, 05:41 PM): """).strip()

            basic_data = (employee_id, start_time, end_time)

            print("""
        Processing data... One moment please : ) """)
            time.sleep(3)
        
            self.cursor.execute("INSERT INTO tracker (employee_id, start_time, end_time) VALUES (?, ?, ?)", basic_data)
                    
            self.con.commit()
            self.con.close()
            print("""
        That's great! Data was added successfully :D """)
            return True
        except Exception as e:
            self.con.rollback()
            print(e)
            return False
