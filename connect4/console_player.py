from .game import Grid, Player
import os
import time

class ConsolePlayer(Player):
    """Allow a human to see the grid in its shell, and input a column from the
    keyboard."""

    def play(self, grid: Grid) -> int:
        input_uti = '' # Input de l'utilisateur
        mode = "clear" # "cls" pour windows 
        os.system(mode) # Effacer la console sous linux
        print(grid)

        # Boucle permettant de verifier si l'input est un chiffre compris entre 0 et 6
        while input_uti is not int:          
            try:   
                input_uti = int(input('Entrer une colonne: '))
                if (0 <= input_uti < 7):
                    break    
                os.system(mode)
                print(grid)
                print('La colonne doit etre un chiffre compris entre 0 et 6')
            except ValueError:
                os.system(mode)
                print(grid)
                print('La colonne doit etre un chiffre compris entre 0 et 6')
        os.system(mode)
        
        return input_uti