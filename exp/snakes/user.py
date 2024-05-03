import psycopg2
from config import load_config

def authenticate_user(username, password):
    """
        Authenticates a user with the given username and password.

    Args:
        username (str): The username provided by the user.
        password (str): The password provided by the user.

    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))
                user_id = cursor.fetchone()
                if user_id:
                    return user_id[0]
                else:
                    return None
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        return None

def record_score(user_id, score):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO user_scores (user_id, score) VALUES (%s, %s)", (user_id, score))
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
