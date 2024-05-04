import psycopg2
from config import load_config

def create_table():
    command = """CREATE TABLE phone_book(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50),
                    phone_number VARCHAR(12)
                )"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as connect:
            with connect.cursor() as cursor:
                cursor.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    create_table()