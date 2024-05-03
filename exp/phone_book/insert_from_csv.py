import csv
import psycopg2
from config import load_config

def insert_from_csv(file_path):
    config = load_config()
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                insert_record(row['name'], row['phone_number'])
        print("Данные успешно загружены из CSV файла в базу данных.")
    except (FileNotFoundError, psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_record(name, phone_number):
    command = f"INSERT INTO phone_book(name, phone_number) VALUES('{name}', '{phone_number}')"
    config = load_config()
    try:
        with psycopg2.connect(**config) as connect:
            with connect.cursor() as cursor:
                cursor.execute(command)
                connect.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    file_path = input("Введите путь к CSV файлу: ")
    insert_from_csv(file_path)
