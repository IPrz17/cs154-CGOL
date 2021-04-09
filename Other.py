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
def update_board(self):
        '''
        method that updates the board based on
        the check of each cell pr. generation
        '''
        #cells list for living cells to kill and cells to resurrect or keep alive
        goes_alive = []
        gets_killed = []

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                #check neighbour pr. square:
                check_neighbour = self.check_neighbour(row , column)
                
                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    #check live status for neighbour_cell:
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self.grid[row][column]
                status_main_cell = cell_object.is_alive()

                #If the cell is alive, check the neighbour status.
                if status_main_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append(cell_object)

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)