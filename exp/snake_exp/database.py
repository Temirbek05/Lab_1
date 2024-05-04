import psycopg2
import json
from config import config

def save_game_state(username, state, filename='final_game_state.json'):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("INSERT INTO game_state (username, state) VALUES (%s, %s) ON CONFLICT (username) DO UPDATE SET state = %s",
                    (username, json.dumps(state), json.dumps(state)))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Database error: {error}")
    finally:
        if conn:
            cur.close()
            conn.close()
    with open(filename, 'w') as file:
        file.write(json.dumps(state, indent=4))

def save_score(username, score, level):
    try:
        conn = None
        cur = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT score, level FROM user_score WHERE username=%s", (username,))
        result = cur.fetchone()
        if result:
            if score > result[0] and level > result[1]:
                cur.execute("UPDATE user_score SET score=%s, level=%s WHERE username=%s", (score, level, username))
        else:
            cur.execute("INSERT INTO user_score (username, score, level) VALUES (%s, %s, %s)", (username, score, level))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()
