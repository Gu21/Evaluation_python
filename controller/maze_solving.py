# _*_ coding:Utf8 _*_


from model.db_connector import init_connection
from model.db_connector import close_connection
from model.db_connector import insert_history
from model.Labyrinth import Labyrinth
from datetime import datetime
from shutil import move
from random import randint
from os import listdir
from sys import platform


# Select an unresolved random map
def select_map():
    # The path of the maps (depending of the OS)
    if platform == "win32":
        path = ".\\maps"
    else:
        path = "./maps"

    list_map = []

    # We list all the files found in the specified path
    for file in listdir(path):
        if file.endswith(".txt"):
            if platform == "win32":
                list_map.append(path + "\\" + file)
            else:
                list_map.append(path + "/" + file)

    # Return the name of the file
    return list_map[randint(0, len(list_map) - 1)]


# Insert a line in history
def add_history(file, solving_time):
    # Initialize connection to the db
    connection = init_connection()

    # Insert entry in the db
    insert_history(connection, file,
                   datetime.now().strftime("%Y-%m-%d"),
                   solving_time)

    # Close the connection
    close_connection(connection)


# Move the finished map in the folder
def move_map(file):
    # The path change depending of the OS
    if platform == "win32":
        move(file, ".\\maps\\resolu")
    else:
        move(file, "./maps/resolu")


# Solve the maze
def solve_maze(file):
    # Open file
    with open(file, "r") as f:
        # Create the object Labyrinth
        lab = Labyrinth(f)

        # Solve the maze
        solving_time = lab.solve()

    # Historize in the db
    add_history(file, solving_time)

    # Archive the file
    move_map(file)

    # Return Labyrinth
    return lab, solving_time
