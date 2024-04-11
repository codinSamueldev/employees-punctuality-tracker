from db.sqlite_connection import con, cursor
from retrieve_data.employees.table import RetrieveEmployeesTable
from retrieve_data.schedules.table import RetrieveSchedulesTable



if __name__ == '__main__':
    # RetrieveEmployeesTable(con=con, cursor=cursor).retrieve_all_employees()
    RetrieveSchedulesTable(con=con, cursor=cursor).retrieve_employees_schedules()
