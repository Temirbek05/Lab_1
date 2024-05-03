import psycopg2
from config import load_config

def display_high_scores():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT users.username, user_scores.score FROM users INNER JOIN user_scores ON users.id = user_scores.user_id ORDER BY user_scores.score DESC LIMIT 10")
                high_scores = cursor.fetchall()
                print("High Scores:")
                for username, score in high_scores:
                    print(f"{username}: {score}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
