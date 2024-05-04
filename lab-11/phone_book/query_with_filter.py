# import psycopg2
# from config import load_config

# def query_with_filter(filter_type, filter_value):
#     config = load_config()
#     try:
#         with psycopg2.connect(**config) as connect:
#             with connect.cursor() as cursor:
#                 if filter_type == "name":
#                     cursor.execute("SELECT * FROM updated_phone_book WHERE name = %s", (filter_value,))
#                 elif filter_type == "surname":
#                     cursor.execute("SELECT * FROM updated_phone_book WHERE surname = %s", (filter_value,))
#                 elif filter_type == "phone_number":
#                     cursor.execute("SELECT * FROM updated_phone_book WHERE phone_number = %s", (filter_value,))
#                 else:
#                     print("Invalid filter type.")
#                     return

#                 for row in cursor.fetchall():
#                     print(row)
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)

# if __name__ == "__main__":
#     filter_type = input("Выберите тип фильтра (name, surname, phone_number): ")
#     filter_value = input(f"Введите значение для фильтра {filter_type}: ")
#     query_with_filter(filter_type, filter_value)

import psycopg2
from config import load_config

def query_with_filter(filter_type, filter_value):
    config = load_config()
    try:
        with psycopg2.connect(**config) as connect:
            with connect.cursor() as cursor:
                if filter_type == "name":
                    cursor.execute("SELECT * FROM updated_phone_book WHERE name = %s", (filter_value,))
                elif filter_type == "surname":
                    cursor.execute("SELECT * FROM updated_phone_book WHERE surname = %s", (filter_value,))
                elif filter_type == "phone_number":
                    cursor.execute("SELECT * FROM updated_phone_book WHERE phone_number = %s", (filter_value,))
                else:
                    print("Invalid filter type.")
                    return

                for row in cursor.fetchall():
                    print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error querying with filter:", error)

if __name__ == "__main__":
    filter_type = input("Choose the filter type (name, surname, phone_number): ")
    filter_value = input(f"Enter value for the filter {filter_type}: ")
    query_with_filter(filter_type, filter_value)
