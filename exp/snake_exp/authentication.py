import psycopg2
from config import config

def authenticate_user(username):
    # Database query to check if the username exists
    sql = "SELECT username FROM user_score WHERE username = %s"
    params = config()  # Retrieve database configuration

    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username,))
        result = cur.fetchone()  # Retrieve the first result
        
        # Print debug information
        print(f"Checking username: {username}")
        print(f"Query result: {result}")

        # If a result is found, authentication is successful
        if result is None:
            return True
        
        # Otherwise, authentication failed
        return False
    
    except Exception as error:
        print(f"Database error: {error}")
        return False
    
    finally:
        # Close the connection
        if conn:
            cur.close()
            conn.close()
