# import csv
# import psycopg2
# from config import load_config

# def insert_from_csv(file_path):
#     config = load_config()
#     try:
#         with open(file_path, newline='') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for row in reader:
#                 insert_record(row['name'], row['surname'], row['phone_number'])
#         print("Данные успешно загружены из CSV файла в базу данных.")
#     except (FileNotFoundError, psycopg2.DatabaseError, Exception) as error:
#         print(error)

# def insert_record(name, surname, phone_number):
#     command = "INSERT INTO phone_book(name, surname, phone_number) VALUES(%s, %s, %s)"
#     data = (name, surname, phone_number)
#     config = load_config()
#     try:
#         with psycopg2.connect(**config) as connect:
#             with connect.cursor() as cursor:
#                 cursor.execute(command, data)
#                 connect.commit()
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)

# if __name__ == "__main__":
#     file_path = input("Введите путь к CSV файлу: ")
#     insert_from_csv(file_path)

import csv
import psycopg2
from config import load_config
from insert_or_update_record import insert_or_update_record  # Importing the function

def insert_from_csv(file_path):
    config = load_config()
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                insert_or_update_record(row['name'], row['surname'], row['phone_number'])
        print("Data successfully loaded from CSV file into the database.")
    except (FileNotFoundError, psycopg2.DatabaseError, Exception) as error:
        print("Error loading data from CSV:", error)

if __name__ == "__main__":
    file_path = input("Enter the path to the CSV file: ")
    insert_from_csv(file_path)
