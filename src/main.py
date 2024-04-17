import time
from db.sqlite_connection import con, cursor
from retrieve_data.employees.table import RetrieveEmployeesTable
from retrieve_data.schedules.table import RetrieveSchedulesTable
from retrieve_data.tracker.table import RetrieveTrackerTable
from input_data.tracker.insert_new_data_to_tracker import InsertIntoTrackerTable
from input_data.schedules.insert_schedule_script import InsertIntoSchedulesTable
from input_data.employees.insert_into_employees_table_script import InsertIntoEmployeeTable
from useful_strings import INITIAL_WELCOME_OPTIONS, RETRIEVAL_OPTIONS, INSERT_OPTIONS, GOODBYE, NOT_VALID_OPTION


def main():
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
                RetrieveTrackerTable(con=con, cursor=cursor).retrieve_tardiness_tracker()
                break
        elif user_initial_choice == 2:
            user_insert_options = int(input(INSERT_OPTIONS))

            if user_insert_options == 1:
                InsertIntoEmployeeTable(con=con, cursor=cursor).add_new_employee()
                break
            elif user_insert_options == 2:
                InsertIntoSchedulesTable(con=con, cursor=cursor).insert_new_schedule()
                break
            elif user_insert_options == 3:
                InsertIntoTrackerTable(con=con, cursor=cursor).insert_new_data_to_tracker()
                break
        elif user_initial_choice == 3:
            print(GOODBYE)
            break
        else:
            print(NOT_VALID_OPTION)
            time.sleep(3)

if __name__ == '__main__':
    main()
