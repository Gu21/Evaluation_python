# _*_ coding:Utf8 _*_

from model.db_connector import init_connection
from model.db_connector import close_connection
from model.db_connector import select_history
from model.db_connector import drop_table


# Connect to the database and retrieve the history
def get_history():
    # Initialize connection to the db
    connection = init_connection()

    # Read the history in the db
    rows = select_history(connection)

    # Close the connection
    close_connection(connection)

    # Return an array with the history
    return rows


# Drop the table
def drop_history():
    connection = init_connection()
    drop_table(connection)
    close_connection(connection)
