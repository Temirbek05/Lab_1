# import psycopg2
# from config import load_config

# def insert_record(name, phone_number):
#     command = f"INSERT INTO phone_book(name, phone_number) VALUES('{name}', '{phone_number}')"
#     config = load_config()
#     try:
#         with psycopg2.connect(**config) as connect:
#             with connect.cursor() as cursor:
#                 cursor.execute(command)
#                 connect.commit()  # Commit the transaction
#                 print("Пользователь успешно был добавлен в базу данных.")
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)

import psycopg2
from config import load_config

def insert_or_update_record(name, surname, phone_number):
    config = load_config()
    
    try:
        with psycopg2.connect(**config) as connect:
            with connect.cursor() as cursor:
                # Check if the record already exists based on name and surname
                cursor.execute("SELECT id FROM updated_phone_book WHERE name = %s AND surname = %s", (name, surname))
                result = cursor.fetchone()

                if result:
                    # Record exists, update the phone number
                    cursor.execute("UPDATE updated_phone_book SET phone_number = %s WHERE name = %s AND surname = %s", (phone_number, name, surname))
                else:
                    # Record does not exist, insert a new record
                    cursor.execute("INSERT INTO updated_phone_book (name, surname, phone_number) VALUES (%s, %s, %s)", (name, surname, phone_number))
                
                connect.commit()
                print("Record successfully inserted or updated.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)
