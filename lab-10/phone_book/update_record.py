# import psycopg2
# from config import load_config

# def update_record(name, new_phone_number):
#     config = load_config()
#     try:
#         with psycopg2.connect(**config) as connect:
#             with connect.cursor() as cursor:
#                 cursor.execute("UPDATE phone_book SET phone_number = %s WHERE name = %s", (new_phone_number, name))
#                 print("Запись успешно обновлена в базе данных.")
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)

# if __name__ == "__main__":
#     name = input("Введите имя для обновления записи: ")
#     new_phone_number = input("Введите новый номер телефона: ")
#     update_record(name, new_phone_number)

import psycopg2
from config import load_config

def update_record(name, new_phone_number):
    config = load_config()
    try:
        with psycopg2.connect(**config) as connect:
            with connect.cursor() as cursor:
                cursor.execute("UPDATE phone_book SET phone_number = %s WHERE name = %s", (new_phone_number, name))
                connect.commit()  # Commit the transaction
                print("Запись успешно обновлена в базе данных.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)