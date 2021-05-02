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
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from random import randint
from matplotlib import pyplot
import time
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
            print('@', end="")
        else:
            print('<', end="")
        #print(self.status) 
    def retOutput(self):
        if(self.status):
            return '@'
        else:
            return '<'


class World ():
    def __init__ (self, x, y, ans):        
        self.x = x
        self.y = y
        self.grid = [[Cell() for i in range(self.x)] for j in range(self.y)]
        self.choice(ans)
        
    # Function to determine users choice of type of grid
    def choice (self, ans):
        if (ans == 'R' or ans == 'r'):
            print('You will now see a random generated grid!')
            self.randGrid()
            self.displayGrid()
        elif(ans == 'M' or ans == 'm'):
            print('You will now create a manual grid!')
            self.manualGrid()
            self.displayGrid()
        elif(ans == 'L' or ans == 'l'):
            self.presets()
                    
    def presets(self):
        print('You\'ve chosen to choose a magically generated grid!')
        print('Here are your options:')
        print('Triomino patterns: (1)')
        print('Tetromino patterns: (2)')
        print('Gliders! (3)')
        print('Gosper glider gun! (4)')
       
        ans = input('Make a choice: ')
        if (ans == '1'):
            print('You will now see some triomino patterns! (use enter to view)')
            coordinates = [[2,2],[2,3],[2,4],[16,1],[15,2],[15,1],[2,16],[3,16],[1,17],[16,17],[17,16],[18,15]]
            self.presetGrid(coordinates)
            self.displayGrid()
        if (ans == '2'):
            print('You will now see some triomino patterns! (use enter to view)')
            coordinates = [[2,3],[2,4],[2,5],[3,3],[13,3],[14,3],[15,3],[16,3],[25,1],[26,2],[26,3],[26,4],[7,16],[7,17],[7,18],[6,17],[16,18],[17,16],[17,17],[18,17]]
            self.presetGrid(coordinates)
            self.displayGrid()
        if (ans == '3'):
            print('You will now see some Gliders! (use (a) to view)')
            coordinates = [[29,28],[28,27],[27,27],[27,28],[27,29],[24,28],[23,27],[22,27],[22,28],[22,29],[19,28],[18,27],[17,27],[17,28],[17,29]]
            self.presetGrid(coordinates)
            self.displayGrid()
        if (ans == '4'):
            print('You will now see Gosper glider gun! (use (a) to view)')
            coordinates = [[0,24],[1,22],[1,24],[2,12],[2,13],[2,20],[2,21],[2,34],[2,35],[3,20],[3,21],[3,34],[3,35],[3,11],[3,15],[4,0],[4,1],[5,0],[5,1],[5,10],[4,10],[4,16],[4,20],[4,21],[5,14],[5,16],[5,17],[5,22],[5,24],[6,10],[6,16],[6,24],[7,11],[7,15],[8,12],[8,13]]
            self.presetGrid(coordinates)
            self.displayGrid()
        # if (ans == '5'):
        #     print('You will now see some triomino patterns! (use enter to view)')
        #     coordinates = [[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],]
        #     self.presetGrid(coordinates)
        #     self.displayGrid()
        # if (ans == '6'):
        #     print('You will now see some triomino patterns! (use enter to view)')
        #     coordinates = [[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],]
        #     self.presetGrid(coordinates)
        #     self.displayGrid()
            
            
        
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

    # function for a preset grid
    def presetGrid (self, startCells):
        print('OK! Setting grid to 40 by 40')
        length = len(startCells)
        self.x = 37
        self.y = 37
        self.grid = [[Cell() for i in range(self.x)] for j in range(self.y)]
        x = []
        y = []
        for i in range(length):
            a, b = startCells[i]
            x.append(int(a))
            y.append(int(b))

        for i in range(length):
            (self.grid[x[i]][y[i]]).setAlive()

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
    #     print('X -> Dead Cell')
    #     print('O -> Alive Cell')
        for row in self.grid:
            print('')
            for col in row:
                col.printStatus()
            
        # for row in self.grid:
        #     for col in row:
        #         self.plot[col] = self.grid[col]
        # pyplot.figure(figsize=(self.x, self.y))
        # pyplot.imshow(self.grid)
        # pyplot.show()
        #data = np.array(ConwayGame.grid)
        #data = np.array(self.plot)
        #data = np.random.rand(10, 10) * 20

        
        # # create discrete colormap
        # cmap = colors.ListedColormap(['red', 'blue'])
        # bounds = [0,10,20]
        # norm = colors.BoundaryNorm(bounds, cmap.N)

        # fig, ax = plt.subplots()
        # ax.imshow(self.grid, cmap=cmap, norm=norm)

        # # draw gridlines
        # ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
        # #ax.set_xticks(np.arange(-.5, 10, 1))
        # #ax.set_yticks(np.arange(-.5, 10, 1))

        # plt.show()
        
    def updateCells(self):        
        liveCellsToDie = []  #list of living cells that need to die
        deadCellsToLive = [] #list of dead cells that need to become alive

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                #get the valid neighbors to check

                neighborsToCheck = self.getValidNeighbors(row , col)
                
                listOfLiving = []

                for nCell in neighborsToCheck:
                    #check status of ncell
                    
                    if(nCell.isAlive()):
                        listOfLiving.append(nCell)

                length = len(listOfLiving)
                #Check rules if cell is ALIVE
                if self.grid[row][col].isAlive() == True:
                    #RULE: Living cell has fewer than two live neighbors
                    #RULE: Living cell has more than three live neighbors
                    if length < 2 or length > 3:
                       liveCellsToDie.append(self.grid[row][col]) #Death of cell occurs

                    #RULE: Living cell with 2 or 3 living neighbors LIVES
                    if length == 2 or length == 3:
                        deadCellsToLive.append(self.grid[row][col]) #Cell becomes ALIVE
                
                #Check rules if cell is DEAD
                else:   
                    if length == 3:
                    #RULE: Dead cell with exactly 3 living cells becomes ALIVE
                        deadCellsToLive.append(self.grid[row][col]) #Cell becomes ALIVE
                        
        #Update cells
        for cItems in deadCellsToLive:
            cItems.setAlive()
        
        for cItems in liveCellsToDie:
            cItems.setDead()

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
                self.grid[row][col] = self.grid[row][col]
                if self.isValid(cellRow, cellCol, row, col):
                    x = cellRow + row
                    y = cellCol + col
                    #print('ValidN ->', x, y)
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

    print('Please choose an option:')
    print('Manually input starting grid with random living nodes => (R)')
    print('Manually input starting grid and choose living nodes => (M)')
    print('Choose from an amazing list of magical preset grids!! => (L)')
    val = input('')
    print('')
    print('')
    print('OK! Here is the land and it\'s filled with wild Bulldogs!')
    print('Let\'s explore!')
    print('PRESS ENTER TO STEP THROUGH TIME :)')
    print('Press (a) for auto run!')
    print('Quit by pressing (q)')
    print('View credits with (c)')
    print('')
    #time.sleep(10)
    ConwayGame = World(x, y, val)
    #ConwayGame.displayGrid()
    print('')

    press = ' '
    while press != 'q':
        
        press = input('Commands: (q=quit) (enter=timestep) (a=auto) (c=credits)')

        if press == 'a':
            answer = 'Y'
            while answer == 'Y' or answer == 'y':
                length = 150
                i = 0
                while i != length:
                    i = i+1
                    time.sleep(.000001)
                    ConwayGame.updateCells()
                    ConwayGame.displayGrid()
                answer = input("Continue? (Y/N)")
                if answer == 'Y':
                    continue
                elif answer == 'N':
                    break

        if press == '':
            print('')
            print('')
            ConwayGame.updateCells()
            ConwayGame.displayGrid()
        if press == 'c':
            print('')
            print('')
            print('CREDITS: ')
            print('-------------------------------')
            print('----APPROXAMITIVE IMITATORS----')
            print('-------------------------------')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')

    print('')
    print('')
    print('')
    print('')

main()  
