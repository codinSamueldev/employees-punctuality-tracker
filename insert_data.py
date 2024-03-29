from sqlite_connection import db_connection, db_cursor

CON = db_connection()
CURSOR = db_cursor()

def insert_into_tracker(data_array: list) -> bool:
    """ 
    This function will insert into tracker table all required information in regards of employee entry hours and exit hours. 
    
    Params:
        data_array = A list of tuples which saves basic employee info (employee_id, date, entry_hour, exit_hour).

    Returns:
        boolean value whether the insertion was succesfully completed or not.
    """

    try:
        print(data_array)
        CURSOR.executemany("INSERT INTO tracker (employee_id, date, entry_hour, exit_hour) VALUES (?, ?, ?, ?)", data_array)
                
        CON.commit()

        return True
    except:

        CON.rollback()

        return False
        

if __name__ == "__main__":
    basic_data = [(5, "28/03/2024", "05:55 PM", "10:00 PM")]

    insert_into_tracker(basic_data)

    ####################################################

    check = CURSOR.execute("SELECT * FROM tracker;")
    res = check.fetchall()

    print(res)

    CON.commit()
    CON.close()
