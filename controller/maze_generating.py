from model.Labyrinth import Labyrinth
from os import listdir
from sys import platform


def generate_maze():
    if platform == "win32":
        path = ".\\maps\\"
    else:
        path = "./maps/"

    list_map = []

    # We list all the files found in the specified path
    for file in listdir(path):
        if file.endswith(".txt"):
            list_map.append(file)
    k = len(list_map) +1

    # If no file are specified in the constructor,
    # a maze is automatically generated
    gen_maze = Labyrinth()

    # We write the maze into a file
    file = open(path + f"lab{k}.txt", "w")

    for i in range(gen_maze.ny):
        for j in range(gen_maze.nx):
            file.write(gen_maze.lab[i][j])
        file.write("\n")

    file.close()