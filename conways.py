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

from random import randint
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

class World ():
    def __init__ (self, x, y, ans):        
        self.x = x
        self.y = y
        self.grid = [[Cell() for i in range(self.x)] for j in range(self.y)]
        #self.randGrid()
        #self.displayGrid()
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
                    
    # def presets(self):
    #     print('You\'ve chosen to choose a magically generated grid!')
    #     print('Here are your options:')
    #     print('Blinker: (1)')
    #     print('')
    #     print('')
    #     print('')
    #     print('')
    #     print('')
    #     print('')
    #     print('')
    #     ans = input('Make a choice: ')
    #     if (ans == ):
    #         print('You will now see a random generated grid!')
    #         self.randGrid()
    #         self.displayGrid()
    #     elif(ans == 'M' or ans == 'm'):
    #         print('You will now create a manual grid!')
    #         self.manualGrid()
    #         self.displayGrid()
    #     elif(ans == 'L' or ans == 'l'):
    #         self.presets()
        

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
    #     print('X -> Dead Cell')
    #     print('O -> Alive Cell')
        for row in self.grid:
            print('')
            for col in row:
                col.printStatus()

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
    # print('Choose from an amazing list of magical preset grids!! => (L)')
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
    time.sleep(10)
    ConwayGame = World(x, y, val)
    #ConwayGame.displayGrid()
    print('')

    press = ' '
    while press != 'q':
        print('')
        print('')
        press = input('Commands: (q=quit) (enter=timestep) (a=auto) (c=credits)')

        if press == 'a':
            answer = 'Y'
            while answer == 'Y' or answer == 'y':
                length = 50
                i = 0
                while i != length:
                    i = i+1
                    time.sleep(.5)
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

    print('')
    print('')
    print('')
    print('')

main()  
