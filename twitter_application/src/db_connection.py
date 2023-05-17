import sqlite3

local_path = "sqlite/twitter.db"
connection = sqlite3.connect(local_path)


def get_db_connection():
    return connection


