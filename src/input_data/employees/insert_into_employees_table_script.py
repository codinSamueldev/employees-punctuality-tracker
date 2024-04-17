import sqlite3, time

class InsertIntoEmployeeTable:
    def __init__(self, con: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
        self.con = con
        self.cursor = cursor

    def add_new_employee(self) -> bool:
        """ 
        Insert new employee in the database. 
        
        Params:
            None

        Returns:
            boolean value whether it was succesfully added the data or not. 
        """
        # Try to execute query, if error raised, then, rollback database.
        try:
            # Tuple that will contain required info.
            basic_data = ()

            # Ask user info and save it into tuple (basic_data).
            employee_name = input("""
        Type employee's first name: """).strip()
            employee_last_name = input("""
        Type employee's last name: """).strip()

            basic_data = (employee_name, employee_last_name)

            print("""
        Processing data... One moment please : ) """)
            time.sleep(3)
        
            self.cursor.execute("INSERT INTO employees (employee_name, employee_last_name) VALUES (?, ?)", basic_data)
                    
            self.con.commit()
            self.con.close()
            print("""
        That's great! Data was added successfully :D """)
            return True
        except Exception as e:
            self.con.rollback()
            print(e)
            return False
