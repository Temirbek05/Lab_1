import psycopg2
from config import config

def create_table():
    command = """CREATE TABLE IF NOT EXISTS user_score(
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            score INTEGER NOT NULL,
            level INTEGER NOT NULL
                )"""
    db_config = config()  # Renamed variable to avoid conflict
    try:
        with psycopg2.connect(**db_config) as connect:
            with connect.cursor() as cursor:
                cursor.execute(command)
                connect.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    create_table()
