# _*_ coding:Utf8 _*_

from time import time

class Labyrinth(object):

    #Constructs a Labyrinth object with an empty path
    def __init__(self, file):
        self.import_labyrinth(file)
        self.path = []
        self.solved = False

    def __str__(self):
        return f"Labyrinth ({self.nx}x{self.ny})"

    def __repr__(self):
        return f"object = Labyrinth(open_file)"
    
    
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

