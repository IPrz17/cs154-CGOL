# CONWAY'S GAME OF LIFE
#
#------------------------------RULE 1------------------------------
# Dead cell with exactly 3 living cells becomes ALIVE
#
#------------------------------RULE 2------------------------------
# Living cell with 2 or 3 living cells as neighbors LIVES
#
#------------------------------RULE 3------------------------------
# All other cases, cell becomes or remain DEAD
#   Living cell has fewer than two live neighbors (UNDERPOPULATION)
#   Living cell has more than three live neithbors (OVERPOPULATION)

import numpy as np 
from random import randint

class Cell:
    def __init__(self):
        self.status = False

    def setDead(self):
        self.status = False

    def setAlive(self):
        self.status = True

    def isAlive(self):
        return self.status

class WOL ():
    
    def __init__ (self, x, y, startValues):           
        self.x = x 
        self.y = y
        
        # Creates a grid that is X by Y
        #self.grid = [[Cell() for column_cells in range(self.x)] for row_cells in range(self.y)]
        self.grid = np.zeros((self.x, self.y), dtype=Cell)
        for i in startValues:
            self.grid[i[1], i[0]] = 1  #this causes error pic in chat

        print(self.grid)                                          # Print grid


class Conway ():
    def __init__ (self):
        #x, y = Conway.getDimensions()                   #get input, ex: 5 5
        #startValues = Conway.getStartValues()           #get input, ex: 1 1    
        x, y, startValues = Conway.getRandomStartValues()           #get input, ex: 1 1
        #conway = WOL(x=5, y=5, startValues=[[1,1], [2,3]])
        conway = WOL(x, y, startValues)

    def getDimensions():
        x, y = input("Enter dimensions for the world: ").split()
        return int(x), int(y)   #  5 * 6     0-4 0-5 

    def getRandomStartValues():#gets living cells from user input, ex: 1 1...2 2...3 3 
            startValues = []

            x, y = Conway.getDimensions()

            numCells = int(input("Enter number living cells: "))
            for i in range(numCells):
                startValues.append([int(x)-i, int(y)-i])

            return int(x), int(y), startValues

    def getStartValues():#gets living cells from user input, ex: 1 1...2 2...3 3 
        startValues = []

        numCells = int(input("Enter number living cells: "))
        print("Enter living cell coordinates: ") 
        for i in range(numCells):
            x, y = input().split()
            startValues.append([int(x),int(y)])
        


        return startValues


Conway()    #runs game