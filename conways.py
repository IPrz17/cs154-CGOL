#
# #  * World'S GAME OF LIFE
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

    def isAlive(self)        :
        return self.status
class World ():
    def __init__ (self, x, y, ans):        
        self.x = x
        self.y = y
        self.ans = ans
        # self.grid = np.zeros((self.x, self.y), dtype=Cell)
        self.grid = [[Cell() for i in range(self.x)] for j in range(self.y)]
        # for i in startValues
        # self.grid[i[1], i[0]] = 1  #this causes error pic in chat
        self.choice(self.ans)

    # Function to determine if user wants random or manual grid
    def choice (self, ans):
        if (ans == 'T' or ans == 't'):
            print('You will now see a random generated grid')
            self.randGrid()
        else:
            print('You will now see a manual grid')
            # self.manualGrid();
        
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

    #Function for printing the grid
    def displayGrid(self):
        print('x -> Dead Cell')
        print('1 -> Alive Cell')
        for row in self.grid:
            for col in row:
                if(col.isAlive()):
                    print(1)
                else:
                    print('x')



    # def manualGrid (self):
    #     self.startValues = self.getStartValues()           #get input, ex: 1 1    
    #     #World = WOL(x=5, y=5, startValues=[[1,1], [2,3]])
    #     World = WOL(x, y, startValues)

    # def getStartValues():#gets living cells from user input, ex: 1 1...2 2...3 3 
    #     startValues = []
    #     numCells = int(input("Enter number living cells: "))
    #     print("Enter living cell coordinates: ") 
    #     for i in range(numCells):
    #         x, y = input().split()
    #         startValues.append([int(x),int(y)])
    #     return startValues

def main():
    x = int(input("Enter the width for the world: "))
    y = int(input("Enter the height for the world: "))
    val = raw_input('Would you like a random grid? (T/F) => ')
    cgl = World(x, y, val)
    cgl.randGrid()
    cgl.displayGrid()

if __name__ == "__main__":
    main()    