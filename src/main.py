from db.sqlite_connection import con, cursor
from retrieve_data.employees.table import RetrieveEmployeesTable



if __name__ == '__main__':
    RetrieveEmployeesTable(con=con, cursor=cursor).retrieve_all_employees()
