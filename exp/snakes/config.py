# from configparser import ConfigParser

# def load_config(filename='database.ini', section='postgresql'):
#     parser = ConfigParser()
#     parser.read(filename)

#     # get section, default to postgresql
#     config = {}
#     if parser.has_section(section):
#         params = parser.items(section)
#         for param in params:
#             config[param[0]] = param[1]
#     else:
#         raise Exception('Section {0} not found in the {1} file'.format(section, filename))

#     return config

# if __name__ == '__main__':
#     config = load_config()
#     print(config)

import psycopg2
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    # Create a parser
    parser = ConfigParser()
    # Read the configuration file
    parser.read(filename)

    # Get section, default to postgresql
    db_params = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_params[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in the {filename} file")

    return db_params

def authenticate_user(username, password):
    # Get PostgreSQL connection parameters from the database.ini file
    db_params = config()

    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object to perform database operations
    cur = conn.cursor()

    try:
        # Execute a SQL query to select the user ID based on the provided username and password
        cur.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))

        # Fetch the result
        user_id = cur.fetchone()

        if user_id:
            return user_id[0]  # Return the user ID if authentication is successful
        else:
            return None  # Return None if authentication fails
    except psycopg2.Error as e:
        print("Error:", e)
        return None
    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()
