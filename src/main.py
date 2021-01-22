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

# Functions
def print_to_cli(feld):
    for x in range(9):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - -")
        for y in range (9):
            if y % 3 == 0 and y != 0:
                print("| ", end='')
            print(str(feld[x][y])+ " ", end='')
        print("")

def finde_zeros(feld):
    for x in range(9):
        for y in range (9):
            if feld[x][y] == 0:
                return (x, y)

def check_row(feld, y, n):
    for x in range(9):
        if feld[x][y] == n:
            return False
        else:
            return True
def check_colume(feld, x, n):
    for y in range(9):
        if feld[x][y] == n:
            return False
        else:
            return True

def check_sqear(feld, x, y, n):
    xmin, xmax, ymin, ymax = 0
    if x >= 0 and x <= 2:
        xmin = 0
        xmax = 2
    elif x >= 3 and x <= 5:
        xmin = 3
        xmax = 5
    elif x >= 6 and x <= 8:
        xmin = 6
        xmax = 8
    else:
        print("Error x value tu high")
        return 1

    if y >= 0 and y <= 2:
        ymin = 0
        ymax = 2
    elif y >= 3 and y <= 5:
        ymin = 3
        ymax = 5
    elif y >= 6 and y <= 8:
        ymin = 6
        ymax = 8
    else:
        print("Error y value tu high")
        return 1
    for x in range(xmin,xmax):
        for y in range(ymin, ymax):
            if feld[x][y] == n:
                return False
            else:
                return True





print_to_cli(spielfeld)
print(finde_zeros(spielfeld))