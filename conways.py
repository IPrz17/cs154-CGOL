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
            print('|', end="")
        else:
            print('X', end="")
        #print(self.status) 

class World ():
    def __init__ (self, x, y, ans):        
        self.x = x
        self.y = y
        self.grid = [[Cell() for i in range(self.x)] for j in range(self.y)]
        self.choice(ans)
        # for i in startValues
        # self.grid[i[1], i[0]] = 1  #this causes error pic in chat
        
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
        
        for i in range(numCells):
            x, y = input().split()
            startValues.append([(x,y)])

        print(startValues)
        for row in self.grid:
            for col in row:
                 
                #if (sV in startValues):
                
                val = randint(0,2)
                if (val == 1):
                    col.setAlive()
                else:
                    col.setDead()
                
                col.printStatus

    # Function for printing the grid
    def displayGrid(self):
        print('X -> Dead Cell')
        print('O -> Alive Cell')
        for row in self.grid:
            print('')
            for col in row:
                col.printStatus()

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

    cgl = World(x, y, val)
    
    print('')
    print('')
    print('')
    print('')

if __name__ == "__main__":
    main()    