# # import psycopg2
# # from config import load_config

# # def create_table(name, phone_number):
# #     command = f"INSERT INTO phone_book(name, phone_number) VALUES('{name}', '{phone_number}')"
# #     config = load_config()
# #     try:
# #         with psycopg2.connect(**config) as connect:
# #             with connect.cursor() as cursor:
# #                 cursor.execute(command)
# #                 print("Пользователь успешно был добавлен в базу данных.")
# #     except (psycopg2.DatabaseError, Exception) as error:
# #         print(error)

# # if __name__ == "__main__":
# #     create_table(input("Введите имя: "), input("Введите номер телефона: "))

# import psycopg2
# from config import load_config

# def insert_record(name, phone_number):
#     config = load_config()
#     try:
#         with psycopg2.connect(**config) as connect:
#             with connect.cursor() as cursor:
#                 command = f"INSERT INTO phone_book(name, phone_number) VALUES('{name}', '{phone_number}')"
#                 cursor.execute(command)
#                 print("Пользователь успешно был добавлен в базу данных.")
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)

# if __name__ == "__main__":
#     name = input("Введите имя: ")
#     phone_number = input("Введите номер телефона: ")
#     insert_record(name, phone_number)


import psycopg2
from config import load_config

def insert_record(name, phone_number):
    command = f"INSERT INTO phone_book(name, phone_number) VALUES('{name}', '{phone_number}')"
    config = load_config()
    try:
        with psycopg2.connect(**config) as connect:
            with connect.cursor() as cursor:
                cursor.execute(command)
                connect.commit()  # Commit the transaction
                print("Пользователь успешно был добавлен в базу данных.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
