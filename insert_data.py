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
    basic_data = []

    employee_id = int(input("Type employee id: "))
    basic_data.append(employee_id)

    current_date = input("Type current date with the following format (DD/MM/YY): ").strip()
    basic_data.append(current_date)

    entry_hour = input("Type employee today's entry hour with the following format (10:05 AM, or, 05:41 PM): ").strip()
    basic_data.append(entry_hour)

    exit_hour = input("Type employee today's exit hour with the following format (10:05 AM, or, 05:41 PM): ").strip()
    basic_data.append(exit_hour)

    insert_into_tracker([tuple(basic_data)])

    ####################################################

    check = CURSOR.execute("SELECT * FROM tracker;")
    res = check.fetchall()

    print(res)

    CON.commit()
    CON.close()
