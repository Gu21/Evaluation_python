# _*_ coding:Utf8 _*_

from time import time
from random import randint

class Labyrinth(object):

    #Constructs a Labyrinth object with an empty path
    def __init__(self, file=None):
        if file is not None :
            self.import_labyrinth(file)
        else :
            self.generate_labyrinth()
        self.path = []
        self.solved = False

    def __str__(self):
        return f"Labyrinth ({self.nx}x{self.ny})"

    def __repr__(self):
        return f"object = Labyrinth(open_file)"

    def add_walls(self, walls, i, j):
        if i > 1 and self.lab[i-1][j] == "#":
            walls.append((i-1, j))
        if j > 1 and self.lab[i][j-1] == "#":
            walls.append((i, j-1))
        if i < self.ny-2 and self.lab[i+1][j] == "#":
            walls.append((i+1, j))
        if j < self.nx-2 and self.lab[i][j+1] == "#":
            walls.append((i, j+1))

    # Generating a perfect maze
    def generate_labyrinth(self):
        self.nx = randint(15,100)
        self.ny = randint(15,100)

        #Initialize a matrix full of walsl
        self.lab = [["#" for _ in range(self.nx)] for _ in range(self.ny)]

        walls = []
        cells = []

        #Pick a random cell in the labyrinth
        cell = (randint(1,self.ny-2),randint(1,self.nx-2))
        self.lab[cell[0]][cell[1]] = " "
        cells.append(cell)

        #Add the adjacent walls to the cells to a list of walls
        self.add_walls(walls,cell[0],cell[1])

        #While the list of walls is not empty
        while len(walls) > 0:
            #Pick a random wall in the list
            wall = walls[randint(0,len(walls)-1)]

            #Check the cells adjacent to the wall
            adj_cells = self.find_neighbours(wall[0],wall[1])
            nb_visited = 0

            for c in adj_cells:
                if c in cells:
                    nb_visited += 1

            #If the wall has only one neighbouring visited cell
            #Break the wall and mark is as visited
            #Add the neighbouring walls to the list
            if nb_visited == 1:
                self.lab[wall[0]][wall[1]] = " "
                cells.append(wall)
                self.add_walls(walls,wall[0],wall[1])

            #Remove the wall from the list
            walls.remove(wall)

        self.start = (0,0)
        self.end = (0,0)

        #Find start and end positions in the outer walls
        #that have at least one free cell nearby
        while self.start == self.end:
            while len(self.find_neighbours(self.start[0],self.start[1])) != 1:
                self.start = self.find_entrance()

            while len(self.find_neighbours(self.end[0],self.end[1])) != 1:
                self.end = self.find_entrance()

        self.lab[self.start[0]][self.start[1]] = "S"
        self.lab[self.end[0]][self.end[1]] = "F"

    #Pick random position in the outer walls of the labyrinth
    def find_entrance(self):
        outer_walls = randint(1,4)
        match outer_walls:
            case 1:
                res = (0, randint(1,self.nx-1))
            case 2:
                res = (randint(1,self.ny-1), 0)
            case 3:
                res = (self.ny-1, randint(1,self.nx-1))
            case 4:
                res = (randint(1,self.ny-1), self.nx-1)
        return res


    #Creates a matrix containg the labyrinth data from the file
    #Initializes width (nx) and height (ny) of the labyrinth
    #Initializes starting and end positions of the labyrinth
    def import_labyrinth(self, file):
        self.lab = [] #Labyrinth matrix
        self.ny = 0

        for line in file:
            self.lab.append(list(line.strip()))
            self.ny += 1
        self.nx = len(self.lab[0])

        for i in range(0, self.ny):
            for j in range (0, self.nx):
                #Starting position of the labyrinth
                if self.lab[i][j] == "S":
                    self.start = (i, j)
                    self.lab[i][j] = " "

                #Finish position of the labyrinth
                if self.lab[i][j] == "F":
                    self.end = (i, j)
                    self.lab[i][j] = " "

    #Returns adjacent free spaces of (i,j) in the labyrinth
    def find_neighbours(self, i, j):
        neighbours = []
        if i > 0 and self.lab[i-1][j] == " ":
            neighbours.append((i-1, j))
        if j > 0 and self.lab[i][j-1] == " ":
            neighbours.append((i, j-1))
        if i < self.ny-1 and self.lab[i+1][j] == " ":
            neighbours.append((i+1, j))
        if j < self.nx-1 and self.lab[i][j+1] == " ":
            neighbours.append((i, j+1))
        return neighbours

    #Recursive depth-first labyrinth solver
    def recursive_solve(self, passed_through, position):
        if not self.solved:
            #Records the positions the solver already went through
            passed_through.append(position)

            #Adds current position to the path
            self.path.append(position)

            if position != self.end:
                #Adjacent free spaces of the current position
                neighbours = self.find_neighbours(position[0], position[1])

                #Check if the solver already passed by the next position
                #Recursively go through all adjacent valid spaces
                for p in neighbours:
                    if p not in passed_through:
                        self.recursive_solve(passed_through, p)

                #Remove current position from the path
                # can't continue from this pos)
                if not self.solved:
                    self.path.pop()
            else:
                self.solved = True


    #Launches the labyrinth solver and returns its execution time
    def solve(self):
        #Starts timer
        start_time = time()

        #Positions the solver already passed by
        passed_through = []
        pos = self.start

        #Launches the solver at starting position
        self.recursive_solve(passed_through, pos)

        #Ends timer
        end_time = time()

        #Return execution time
        return end_time - start_time

