from .game import Grid, Player,Cell

counter = 0

class CheaterB(Player):
    """This IA cheats and modify the grid to ensure player B wins."""
    # On remplie 3 cellules en ligne et on joue la cellule 4 pour faire gagner le joueur B
    def play(self, grid: Grid) -> int:
        grid.grid[0] = [Cell.A, Cell.B, Cell.B, Cell.B, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY]
        return 4
