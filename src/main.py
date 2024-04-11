from db.sqlite_connection import con, cursor
from retrieve_data.employees.table import RetrieveEmployeesTable
from retrieve_data.schedules.table import RetrieveSchedulesTable
from useful_strings import INITIAL_WELCOME_OPTIONS, RETRIEVAL_OPTIONS, GOODBYE



if __name__ == '__main__':
    while True:
        user_initial_choice = int(input(INITIAL_WELCOME_OPTIONS))

        if user_initial_choice == 1:
            user_retrieval_options = int(input(RETRIEVAL_OPTIONS))

            if user_retrieval_options == 1:
                RetrieveEmployeesTable(con=con, cursor=cursor).retrieve_all_employees()
                break
            elif user_retrieval_options == 2:
                RetrieveSchedulesTable(con=con, cursor=cursor).retrieve_employees_schedules()
                break
            elif user_retrieval_options == 3:
                pass
                break
        elif user_initial_choice == 2:
            pass
            break
        elif user_initial_choice == 3:
            print(GOODBYE)
            break
