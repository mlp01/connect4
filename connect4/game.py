from enum import Enum
import time
import os


class Cell(Enum):
    """Enumeration representing a Connect4 Cell."""

    EMPTY = "."
    A = "X"
    B = "O"


class Grid:
    """Grid of 42 Cells."""

    lines = 6
    columns = 7

    def __init__(self):
        """Initialize a "self.grid" member: a list of list of Cells."""
        self.grid = [[Cell.EMPTY] * self.columns for _ in range(self.lines)]

    def __str__(self) -> str:
        """Reprensent this Grid as an ASCII image."""
        ret = ""
        for line in range(self.lines - 1, -1, -1):
            ret += "|"
            for column in range(self.columns):
                ret += self.grid[line][column].value
            ret += "|\n"
        ret += "+" + "-" * self.columns + "+\n"
        ret += " " + "".join(str(i) for i in range(self.columns)) + "\n"
        return ret

    def place(self, column: int, cell: Cell) -> int:
        """Put one Cell into one of the 7 columns of this grid. Return the line where
        the token stops."""
        for line in range(self.lines):
            if self.grid[line][column] == Cell.EMPTY:
                self.grid[line][column] = cell
                return line
        raise ValueError(f"Column {column} is full.")

    def win(self, line: int, column: int) -> bool:
        """Check if the Cell at "line" / "column" is part of 4 Cells from the same
        player in a horizontal / vertical / diagonal line."""
        adjacent = 0
        color = self.grid[line][column]
        # Horizontal
        for cell in self.grid[line]:
            if cell == color:
                adjacent += 1
                if adjacent == 4:
                    return True
            else:
               adjacent = 0

        # TODO: Vertical
        # On regarde pour chaque ligne et pour la colonne donnée, si il existe 4 cellules
        # remplies par le même joueur l'une en dessous de l'autre.
        adjacent = 0
        for i in range(Grid.lines):
            if self.grid[i][column] == color:
                adjacent += 1
                if adjacent == 4:
                    return True
            else:
                adjacent = 0

        # TODO: Diagonal
        # Pour la diagonale, on test chaque diagonale de la grille.
        adjacent = 0
        col = column - line # On initialise l'indice de colonne tel que l'origine 
        # de notre diagonale soit à 0 en hauteur (ligne). 
        lign=0
        for col in range(Grid.lines):
            if col>=0: # tant qu'on est dans des cellules fictives on n'essaye pas de les placer
                if self.grid[lign][col] == color:
                    adjacent += 1
                    if adjacent == 4:
                        return True
                else:
                    adjacent = 0
            lign+=1

        return False

    def tie(self) -> bool:
        """Check if the grid is full."""
        col=0
        for col in range(Grid.columns):
            if self.grid[Grid.lines-1][col]== Cell.EMPTY:
                return False
        return True



class Player:
    """Abstract base class for Players in this game."""

    def play(self, grid: Grid) -> int:
        """Main method for the player: show them the current grid, and ask them on which
        column they want to play."""
        raise NotImplementedError


class Game:
    """Main class of this project."""

    def __init__(self, player_a: Player, player_b: Player):
        """Initialize a new game with 2 Players and a Grid."""
        self.player_a = player_a
        self.player_b = player_b
        self.grid = Grid()

    def main(self):
        """Let players play until one of the win or the grid is full."""
        while True:
            if self.play(self.player_a, Cell.A):
                print(self.grid)
                print("A wins !")
                break
            if self.grid.tie():
                print(self.grid)
                print("Tie.")
                break
            if self.play(self.player_b, Cell.B):
                print(self.grid)
                print("B wins !")
                break
            if self.grid.tie():
                print(self.grid)
                print("Tie.")
                break

    def play(self, player: Player, cell: Cell) -> bool:
        """Process one turn for one player.

        Ask the player on which column they want to play, ask the grid on which line
        the token stops, and check if this was a winning move."""
        column = player.play(self.grid)
        line = self.grid.place(column, cell)
        os.system("clear")
        print(self.grid)
        time.sleep(0.75)
        return self.grid.win(line, column)
