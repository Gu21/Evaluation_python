# _*_ coding:Utf8 _*_

import sqlite3
from sqlite3 import Error
from model.History import History


# Initializing the connection to the database
def init_connection():
    try:
        connection = sqlite3.connect("History.db")
        create_table(connection)
    except Error as e:
        raise f"A SQLite error occured: {e}"

    return connection


# Closing the connection to the database
def close_connection(connection):
    try:
        connection.close()
    except Error as e:
        raise f"A SQLite error occured: {e}"


# Deleting history table if existing
def drop_table(connection):
    req_drop = """DROP TABLE IF EXISTS history"""

    try:
        cur_drop = connection.cursor()
        cur_drop.execute(req_drop)
        connection.commit()
    except Error as e:
        raise f"A SQLite error occured: {e}"


# Creating history table if it exists
def create_table(connection):
    req_create = """CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY NOT NULL,
                    file_name TEXT NOT NULL,
                    solving_date DATE NOT NULL,
                    solving_time REAL NOT NULL
                 )
                 """

    try:
        cur_create = connection.cursor()
        cur_create.execute(req_create)
    except Error as e:
        raise f"A SQLite error occured: {e}"


# Inserting a row in the history
def insert_history(connection, file_name, solving_date, solving_time):
    req_insert_history = """
                            INSERT INTO history(
                                file_name,
                                solving_date,
                                solving_time
                            )
                            VALUES
                            (?, ?, ?)
                         """

    tuple_insert_hist = (file_name, solving_date, solving_time)

    try:
        cur_insert_history = connection.cursor()
        cur_insert_history.execute(req_insert_history, tuple_insert_hist)
        connection.commit()
    except Error as e:
        raise f"A SQLite error occured: {e}"


# Reading the history
def select_history(connection):
    list_history = []
    req_select_all = """SELECT * FROM history"""

    try:
        cur_select_all = connection.cursor()
        cur_select_all.execute(req_select_all)
        rows = cur_select_all.fetchall()

        for row in rows:
            history = History(row[1], row[2], row[3])

            list_history.append(history)

    except Error as e:
        raise f"A SQLite error occured: {e}"

    return list_history
