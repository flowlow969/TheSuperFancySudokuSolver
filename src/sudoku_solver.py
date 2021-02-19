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
import numpy as np
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

def get_gitter():
    matrix = np.zeros((9,9))
    print("Bitte Zahlen in 3er-Grüppchen, getrennt durch ein Leerzeichen eingeben. Wenn Feld frei bitte 0 eingeben.")
    for l in range(1,10):
        line = input("Bitte Zeile {} eingeben! ".format(l))
        line = [x for x in str(line)]
        index = [3,7]
        line_new = np.delete(line,index)
        matrix[l-1,:]= line_new
    return matrix.astype(int)

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
    return False

def check_row(gi, r, n):
    for c in range(9):
        if gi[r][c] == n:
            return False
    return True

def check_column(gi, c, n):
    for r in range(9):
        if gi[r][c] == n:
            return False

    return True

def check_square(gi, r, c, n):
    rmin = 0
    rmax = 0
    cmin = 0
    cmax = 0
    if r >= 0 and r <= 2:
        rmin = 0
        rmax = 2

    elif r >= 3 and r <= 5:
        rmin = 3
        rmax = 5

    elif r >= 6 and r <= 8:
        rmin = 6
        rmax = 8

    else:
        print("Error r value tu high")
        return 1

    if c >= 0 and c <= 2:
        cmin = 0
        cmax = 2

    elif c >= 3 and c <= 5:
        cmin = 3
        cmax = 5

    elif c >= 6 and c <= 8:
        cmin = 6
        cmax = 8

    else:
        print("Error c value tu high")
        return 1

    for r in range(rmin, rmax+1):
        for c in range(cmin, cmax+1):
            if gi[r][c] == n:
                return False

    return True

def pruefe_ziffer(gi,r,c,n):
    if check_column(gi,c,n) and check_row(gi,r,n) and check_square(gi,r,c,n):
        return True
    return False


def loese_sudoku(gi):
    find = finde_leeres_feld(gi)
    if not find:
        return True
    else:
        r, c = find

    for n in range(1,10):
        if pruefe_ziffer(gi, r, c, n):
            gi[r][c] = n

            if loese_sudoku(gi):
                return True

            gi[r][c] = 0

    return False
