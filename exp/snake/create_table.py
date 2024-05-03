#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE users (
            user_name VARCHAR(255) PRIMARY KEY,
            user_id SERIAL
        );
        """,
        """
        CREATE TABLE user_score (
            user_name VARCHAR(255),
            score INT NOT NULL,
            level INT NOT NULL,
            FOREIGN KEY (user_name)
            REFERENCES users (user_name)
            ON UPDATE CASCADE ON DELETE CASCADE
        );
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

create_tables()