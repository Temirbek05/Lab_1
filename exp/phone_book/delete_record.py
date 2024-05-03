# import psycopg2
# from config import load_config

# def delete_record(criteria):
#     config = load_config()
#     try:
#         with psycopg2.connect(**config) as connect:
#             with connect.cursor() as cursor:
#                 # Construct SQL query to delete record by username or phone number
#                 cursor.execute("DELETE FROM phone_book WHERE name = %s OR phone_number = %s", (criteria, criteria))
#                 print("Record(s) successfully deleted from the database.")
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)

# if __name__ == "__main__":
#     criteria = input("Enter the username or phone number to delete: ")
#     delete_record(criteria)

import psycopg2
from config import load_config

def delete_record(criteria):
    config = load_config()
    command = "DELETE FROM phone_book WHERE name = %s OR phone_number = %s"
    data = (criteria, criteria)
    try:
        with psycopg2.connect(**config) as connect:
            with connect.cursor() as cursor:
                cursor.execute(command, data)
                connect.commit()  # Commit the transaction
                print("Запись успешно удалена из базы данных.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    delete_record(input("Введите имя или номер телефона для удаления: "))
