# import psycopg2
# from config import load_config

# def create_table():
#     config = load_config()
#     try:
#         with psycopg2.connect(**config) as connect:
#             with connect.cursor() as cursor:
#                 cursor.execute('''
#                     CREATE TABLE IF NOT EXISTS updated_phone_book (
#                         id SERIAL PRIMARY KEY,
#                         name VARCHAR(255),
#                         surname VARCHAR(255),
#                         phone_number VARCHAR(20)
#                     )
#                 ''')
#                 connect.commit()
#         print("Таблица 'updated_phone_book' успешно создана.")
#     except (psycopg2.DatabaseError, Exception) as error:
#         print("Ошибка создания таблицы:", error)

# if __name__ == "__main__":
#     create_table()

import psycopg2
from config import load_config

def create_table():
    config = load_config()
    try:
        with psycopg2.connect(**config) as connect:
            with connect.cursor() as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS updated_phone_book (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255),
                        surname VARCHAR(255),
                        phone_number VARCHAR(20)
                    )
                ''')
                connect.commit()
        print("Table 'updated_phone_book' successfully created.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error creating table:", error)

if __name__ == "__main__":
    create_table()
