"""
-    This script will insert into tracker table all required information in regards of employee entry hours and exit hours.
-
-    Params:
-        data_array = A list of tuples which saves basic employee info (employee_id, date, entry_hour, exit_hour).

-    Returns:
-        boolean value whether the insertion was succesfully completed or not.
"""

from db.sqlite_connection import con, cursor

# Tuple that will contain required info.
basic_data = ()

# Ask user info and save it into tuple (basic_data).
employee_id = int(input("Type employee id: "))
current_date = input("Type current date with the following format (DD/MM/YY): ").strip()
entry_hour = input("Type employee today's entry hour with the following format (10:05 AM, or, 05:41 PM): ").strip()
exit_hour = input("Type employee today's exit hour with the following format (10:05 AM, or, 05:41 PM): ").strip()

basic_data = (employee_id, current_date, entry_hour, exit_hour)

# Try to execute query, if error raised, then, rollback database.
try:
    cursor.execute("INSERT INTO tracker (employee_id, date, entry_hour, exit_hour) VALUES (?, ?, ?, ?)", basic_data)
            
    con.commit()
    con.close()
except:
    con.rollback()
