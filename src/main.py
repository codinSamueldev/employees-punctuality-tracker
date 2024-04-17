from db.sqlite_connection import con, cursor
from retrieve_data.employees.table import RetrieveEmployeesTable
from retrieve_data.schedules.table import RetrieveSchedulesTable
from input_data.tracker.insert_new_data_to_tracker import InsertIntoTrackerTable
from useful_strings import INITIAL_WELCOME_OPTIONS, RETRIEVAL_OPTIONS, INSERT_OPTIONS, GOODBYE


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
                pass
                break
        elif user_initial_choice == 2:
            user_insert_options = int(input(INSERT_OPTIONS))

            if user_insert_options == 1:
                # Code here TODO...
                pass
                break
            elif user_insert_options == 2:
                # Code here TODO...
                pass
                break
            elif user_insert_options == 3:
                InsertIntoTrackerTable(con=con, cursor=cursor).insert_new_data_to_tracker()
                pass
                break
        elif user_initial_choice == 3:
            print(GOODBYE)
            break


if __name__ == '__main__':
    main()
