#
# #  * Conways'S GAME OF LIFE
#
# ! ------------------------------RULE 1------------------------------
# * Dead cell with exactly 3 living cells becomes ALIVE
#
# ! ------------------------------RULE 2------------------------------
# * Living cell with 2 or 3 living cells as neighbors LIVES
#
# ! ------------------------------RULE 3------------------------------
# * All other cases, cell becomes or remain DEAD
# *   Living cell has fewer than two live neighbors (UNDERPOPULATION)
# *   Living cell has more than three live neithbors (OVERPOPULATION)

import numpy as np 
from random import randint

from numpy.core.defchararray import join
class Cell:
    def __init__(self):
        self.status = False

    def setDead(self):
        self.status = False

    def setAlive(self):
        self.status = True

    def isAlive(self):
        return self.status
    
    def printStatus(self):
        if(self.status):
            print('O', end="")
        else:
            print('X', end="")
        #print(self.status) 

class World ():
    def __init__ (self, x, y, ans):        
        self.x = x
        self.y = y
        self.grid = [[Cell() for i in range(self.x)] for j in range(self.y)]
        self.choice(ans)
        
    # Function to determine if user wants random or manual grid
    def choice (self, ans):
        if (ans == 'T' or ans == 't'):
            print('You will now see a random generated grid!')
            self.randGrid()
            self.displayGrid()
        else:
            print('You will now create a manual grid!')
            self.manualGrid()
            self.displayGrid()
            #VVVVfor debuggingVVVV
            print('')
            self.getValidNeighbors(3,3)
            print('')
            self.getValidNeighbors(4,4)
            
            
        
    # Function for random grid 
    def randGrid (self):
        # create an array
        # iterate through self.rand  -> get coordinates where the value is one and store those coordinates into the blank array.
        # Iterate through self.grid;setAlive in same location
        # self.rand = np.random.randint(0,2, size=(self.x, self.y))
        for row in self.grid:
            for col in row:
                val = randint(0,2)
                if (val == 1):
                    col.setAlive()
                else:
                    col.setDead()



    # function for a user defined grid
    def manualGrid (self):
        startValues = []
        numCells = int(input("Enter number living cells: "))
        print("Enter living cell coordinates: ") 
        
        x = []
        y = []
        for i in range(numCells):
            a, b = input().split()
            x.append(int(a))
            y.append(int(b))

        for i in range(numCells):
            (self.grid[x[i]][y[i]]).setAlive()

    # Function for printing the grid
    def displayGrid(self):
        print('X -> Dead Cell')
        print('O -> Alive Cell')
        for row in self.grid:
            print('')
            for col in row:
                col.printStatus()

    def updateCells(self):
        
        listOfDeath = []  #living cells to kill with flu shots
        wildBulldogs = [] #dead cells to reincarnate as wild bulldogs

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                #get the valid neighbors to check
                neighborsToCheck = self.getValidNeighbors(row , col)
                
                listOfLife = []

                for nCell in neighborsToCheck:
                    #check status of ncell
                    if(nCell.isAlive()):
                        listOfLife.append(nCell)

                #If cell is alive check the neighbour status.
                
        #set status

    #determines if a neighbor is valid .. returns a bool
    def isValid(self, cellRow, cellCol, row, col):
        #get row and column we are checking
        thisRow = cellRow + row
        thisCol = cellCol + col
        valid = True

        #these conditions must NOT be met for the cell to be valid
        #           OUT OF BOUNDS
        if thisRow == cellRow and thisCol == cellCol:
            valid = False
        if thisRow < 0 or thisRow >= self.x or thisCol < 0 or thisCol >= self.y: 
            valid = False
        return valid



    #gets the valid neighbors of specific cell .. returns a list of cells
    def getValidNeighbors(self, cellRow , cellCol):
        
        validNeighbours = []
        #for each cell .. call helper function to check if a valid cell
        for row in range(-1, 2):
            for col in range(-1, 2):
                # if it is a valid neighbor we append the cell to the list
                if self.isValid(cellRow, cellCol, row, col):
                    x = cellRow + row
                    y = cellCol + col
                    print('ValidN ->', x, y)
                    validNeighbours.append(self.grid[x][y])

        return validNeighbours 
    

def main():
    print('')
    print('')
    print('')
    print('-----------------------------')
    print('!!!!CONWAY\'S GAME OF LIFE!!!!')
    print('-----------------------------')
    print('--------------------CSci 154-')
    print('-----------------------------')
    print('-----------------------------')
    print('')
    print('')

    x = int(input("Enter the width for the world: "))
    y = int(input("Enter the height for the world: "))
    print('')

    val = input('Would you like a random grid? (T/F) => ')
    print('')
    print('')
    print('OK! Here is the land and it\'s filled with wild Bulldogs!')
    print('Let\'s explore!')
    print('PRESS SPACE BAR TO STEP THROUGH TIME :)')
    print('Quit by pressing q')
    print('View credits with c')
    ConwayGame = World(x, y, val)
    # user_action = ' '
    # while user_action != 'q':
    #     print('')
    #     print('')
    #     user_action = input('Commands: (q) (enter) (c)')

    #     if user_action == '':
    #         print('')
    #         print('')
    #         ConwayGame.updateCells()
    #         ConwayGame.displayGrid()
    #     if user_action == 'c':
    #         print('')
    #         print('')
    #         print('CREDITS: ')

    # print('')
    # print('')
    # print('')
    print('')

if __name__ == "__main__":
    main()    