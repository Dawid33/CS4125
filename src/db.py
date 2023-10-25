import os
import sqlite3

conn = None

def get_db():
    global conn
    if conn is None:
        if not os.path.exists("sqlite.db"):
            with open('init.sql', 'r') as sql_file:
                sql_script = sql_file.read()

            db = sqlite3.connect("sqlite.db")
            cursor = db.cursor()
            cursor.executescript(sql_script)
            db.commit()
            db.close()

        conn = sqlite3.connect("sqlite.db")

    return conn

