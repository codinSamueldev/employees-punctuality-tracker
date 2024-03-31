from retrieve_data.services.useful_services import RetrieveEmployeesTable
from db.sqlite_connection import con, cursor


if __name__ == '__main__':
    print(RetrieveEmployeesTable.retrieve_all_employees())
