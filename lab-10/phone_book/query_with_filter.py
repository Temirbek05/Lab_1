# import psycopg2
# from config import load_config

# def query_with_filter(filter_type, filter_value):
#     config = load_config()
#     try:
#         with psycopg2.connect(**config) as connect:
#             with connect.cursor() as cursor:
#                 cursor.execute(f"SELECT * FROM phone_book WHERE {filter_type} = %s", (filter_value,))
#                 rows = cursor.fetchall()
#                 if rows:
#                     print("Результаты запроса:")
#                     for row in rows:
#                         print(row)
#                 else:
#                     print("Нет данных, удовлетворяющих критериям фильтра.")
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)

# if __name__ == "__main__":
#     filter_type = input("Выберите тип фильтра (name, phone_number): ")
#     filter_value = input(f"Введите значение для фильтра {filter_type}: ")
#     query_with_filter(filter_type, filter_value)


import psycopg2
from config import load_config

def query_with_filter(filter_type, filter_value):
    config = load_config()
    try:
        with psycopg2.connect(**config) as connect:
            with connect.cursor() as cursor:
                cursor.execute(f"SELECT * FROM phone_book WHERE {filter_type} = %s", (filter_value,))
                for row in cursor.fetchall():
                    print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
