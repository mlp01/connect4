from .game import Player, Cell, Grid


class DumbIA(Player):
    """IA which play on the column of the first possible empty cell it finds."""
    
    def play(self, grid: Grid) -> int:
        for line in range(grid.lines):
            for column in range(grid.columns):
                if grid.grid[line][column] == Cell.EMPTY :
                    return column    
        return grid.columns
