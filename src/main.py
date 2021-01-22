"""! @brief A Super Fancy Susoku Solver with Backtracking."""
##
# @mainpage Sudoku Solver mit Backtracking
#
# @section Für unser Python Programmier Projekt haben  wir einen Susoku Solver mit Backtracking gebaut.
#
# @section Notizen
# - Das GUI ist ein Oprionaler bestanfdteil.

##
# @file mail.py
#
# @brief Main Datei des Sudoku Solvers.
#
# @section description_doxygen_example Description
# Example Python program with Doxygen style comments.
#
# @section libraries_main Libraries/Modules
# - time standard library (https://docs.python.org/3/library/time.html)
#   - Access to sleep function.
# - sensors module (local)
#   - Access to Sensor and TempSensor classes.
#
# @section notes_doxygen_example Notes
# - Comments are Doxygen compatible.
#
# @section todo_doxygen_example TODO
# - Funktionen Verstehen.
#
# @section author_doxygen_example Author(s)
# - Created by Florian Herrmann on 20/01/2021.
# - Modified by John Woolsey on 06/11/2020.
#
# Imports


# Global Constants
## Spielfeld.
spielfeld = [[1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9]]

# Functionsss
def print_to_cli(feld):
    for x in range(9):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - -")
        for y in range (9):
            if y % 3 == 0 and y != 0:
                print("| ", end='')
            print(str(feld[x][y])+ " ", end='')
        print("")

def posibiel(feld, x, y, n):


    return



print_to_cli(spielfeld)
