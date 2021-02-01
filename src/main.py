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
#import pygame
#pygame.font.init()

# Global Constants
## Spielfeld.
gitter = [[0,0,0,0,3,0,8,0,0],
             [9,0,3,0,7,0,2,0,5],
             [2,5,1,8,0,0,6,0,0],
             [8,0,7,0,0,0,3,0,0],
             [5,0,0,2,9,4,0,0,8],
             [0,0,0,0,8,0,5,0,4],
             [0,1,0,0,0,0,0,0,7],
             [6,0,0,9,0,8,0,3,0],
             [0,0,2,3,0,7,0,8,0]]

# Functions
def print_gitter(gi):
    print("  C 0 1 2   3 4 5   6 7 8")
    print("R   - - -   - - -   - - -")
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("    - - - - - - - - - - -")
            print(str(r) + " | ", end='')
        else:
            print(str(r) + " | ", end='')
        for c in range (9):
            if c % 3 == 0 and c != 0:
                print("| ", end='')
            print(str(gi[r][c])+ " ", end='')
        print(" ")
    print("    - - -   - - -   - - -","\n\n")



def finde_leeres_feld(gi):
    for r in range(9):
        for c in range (9):
            if gi[r][c] == 0:
                return (r, c)
            if r == 8 and c == 8:
                return False

def check_row(gi, y, n):
    for x in range(9):
        if gi[x][y] == n:
            return False
    return True

def check_column(gi, x, n):
    for y in range(9):
        if gi[x][y] == n:
            return False

    return True

def check_square(gi, x, y, n):
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
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

    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            if gi[x][y] == n:
                return False

    return True

def pruefe_ziffer(gi,x,y,n):
    if check_column(gi,x,n) and check_row(gi,y,n) and check_square(gi,x,y,n):
        return True
    return False


def loese_sudoku(gi):
    find = finde_leeres_feld(gi)
    if not find:
        return True
    else:
        x, y = find

    for n in range(1,10):
        if pruefe_ziffer(gi, x, y, n):
            gi[x][y] = n

            if loese_sudoku(gi):
                return True

            gi[x][y] = 0

    return False


print_gitter(gitter)
loese_sudoku(gitter)
print_gitter(gitter)