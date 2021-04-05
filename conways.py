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

class WOL ():
    def __init__ (self, x, y, startValues):        
        self.x = x 
        self.y = y
        self.grid = np.zeros((self.x, self.y), dtype=int)         # Creates a grid that is X by Y

        for i in startValues:
            self.grid[i[0], i[0]] = 1
        
        print(self.grid)                                          # Print grid

conway = WOL(4,4,[[1,1], [2,3]])