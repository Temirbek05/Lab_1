# import psycopg2
# from config import load_config

# def update_record(name, surname, new_phone_number):
#     config = load_config()
#     try:
#         with psycopg2.connect(**config) as connect:
#             with connect.cursor() as cursor:
#                 cursor.execute("UPDATE updated_phone_book SET phone_number = %s WHERE name = %s AND surname = %s", (new_phone_number, name, surname))
#                 connect.commit()  # Commit the transaction
#                 print("Запись успешно обновлена в базе данных.")
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)

# if __name__ == "__main__":
#     name = input("Введите имя пользователя, которого хотите обновить: ")
#     surname = input("Введите фамилию пользователя, которого хотите обновить: ")
#     new_phone_number = input("Введите новый номер телефона: ")
#     update_record(name, surname, new_phone_number)

import psycopg2
from config import load_config

def update_record(name, surname, new_phone_number):
    config = load_config()
    try:
        with psycopg2.connect(**config) as connect:
            with connect.cursor() as cursor:
                cursor.execute("UPDATE updated_phone_book SET phone_number = %s WHERE name = %s AND surname = %s", (new_phone_number, name, surname))
                connect.commit()  # Commit the transaction
                print("Record successfully updated in the database.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error updating record:", error)

if __name__ == "__main__":
    name = input("Enter the user's name you want to update: ")
    surname = input("Enter the user's surname you want to update: ")
    new_phone_number = input("Enter the new phone number: ")
    update_record(name, surname, new_phone_number)
