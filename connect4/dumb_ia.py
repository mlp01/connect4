from .game import Player
from .game import Cell

class DumbIA(Player):
    def play(self, grid):    
        for line in range(grid.lines):
            for column in range(grid.columns):
                if grid.grid[line][column] == Cell.EMPTY :
                    return column    
        return grid.columns

#tessssssst