import psycopg2
from config import load_config

def delete_record(criteria):
    config = load_config()
    command = "DELETE FROM phone_book WHERE name = %s OR phone_number = %s"
    data = (criteria, criteria)
    try:
        with psycopg2.connect(**config) as connect:
            with connect.cursor() as cursor:
                cursor.execute(command, data)
                connect.commit()  # Commit the transaction
                print("Запись успешно удалена из базы данных.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    delete_record(input("Введите имя или номер телефона для удаления: "))
