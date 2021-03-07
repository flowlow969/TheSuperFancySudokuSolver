"""! @brief A Super Fancy Sudoku Solver with Backtracking."""
##
# @mainpage Sudoku Solver mit Backtracking
#
# @section Für unser Python Programmier Projekt haben  wir einen Susoku Solver mit Backtracking gebaut.
#
# @section Notizen
# - Das GUI ist ein optionaler Bestandteil.

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

"""
Der Funktion loese_sudoku wird ein ungelöstes Sudoku-Gitter beliebiger Größe übergeben (leere Felder werden mit der Ziffer 0 gekennzeichnet),
diese Funktion löst das Sudoku mittels Backtracking und ändert dementsprechend die Ziffern im übergebenen Sudoku.
Dafür werden die Funktionen:    finde_leeres_Feld
                                check_row
                                check_column
                                check_square
                                pruefe_Ziffer benutzt.
Mithilfe von print_gitter lässt sich das Sudoku-Gitter vor und nach dem Lösen ausgeben.                            
"""

import numpy as np
    
def print_gitter(gi,dimension):
    """ Ausgabe eines Sudoku-Gitters beliebiger Größe.

    Args:
        gi(list):  Das Sudokugitter als 2-dimensionsales Array.
                   Jedes Element der Liste ist wieder eine Liste mit den Ziffern einer Zeile.
        dimension: Die Anzahl der Felder in einer Zeile oder Spalte des Sudokus.
    """
    d = int(np.sqrt(dimension))
    for r in range(d*d):
        if r % d == 0:
            for i in range(d):
                print(d*"  _ ",end = "  ")
                if i == d-1:
                    print("\n")
        print("", end = "")
        for c in range (d*d):
            if c % d == 0 and c != 0:
                print("| ", end='')
            if len(str(gi[r][c]))== 2:
                   print(" ", end='')
            else: print ("  ",end="")
            print(str(gi[r][c])+ " ", end='')
        print(" ")
    
    for i in range(d):
        print(d*"  _ ",end = "  ")
        if i == d-1:
            print("\n")
        
    print("\n\n")


def finde_leeres_feld(gi,d):
    """ Auffinden eines leeren Feldes im Sudoku-Gitter.

    Args:
        gi(list):  Das Sudokugitter als 2-dimensionsales Array.
                   Jedes Element der Liste ist wieder eine Liste mit den Ziffern einer Zeile.
        d:         Wurzel von dimension.

    Returns:       Tupel mit Koordinaten (r = row, c = column) des gefundenen leeren Feldes
    """
    
    for r in range(d*d):
        for c in range(d*d):
            if gi[r][c] == 0:
                return(r, c)
    return False


def check_row(gi,r,n,d):
    """Prüft in der Reihe des Feldes, ob Ziffer n noch nicht vorhanden ist."""
    for c in range(d*d):
        if gi[r][c] == n:
            return False
    return True


def check_column(gi,c,n,d):
    """Prüft in der Spalte des Feldes, ob Ziffer n noch nicht vorhanden ist."""
    for r in range(d*d):
        if gi[r][c] == n:
            return False
    return True


def check_square(gi,r,c,n,d):
    """Prüft in dem d*d Quadrat des Feldes, ob Ziffer n noch nicht vorhanden ist."""
    r0 = (r//d)*d
    c0 = (c//d)*d
    
    for i in range(0,d):
        for j in range(0,d):
            if gi[r0+i][c0+j] == n:
                return False
    return True


def pruefe_ziffer(gi,r,c,n,d):
    """Prüft in der Reihe, Spalte und d*d-Quadrat des Feldes, ob Ziffer n noch nicht vorhanden ist."""
    if check_column(gi,c,n,d) and check_row(gi,r,n,d) and check_square(gi,r,c,n,d):
        return True
    return False


def loese_sudoku(gi,dimension = 9):
    """Löst ein Sudoku-Gitter beliebiger Größe.

     Args:
        gi(list):  Das Sudokugitter als 2-dimensionsales Array.
                   Jedes Element der Liste ist wieder eine Liste mit den Ziffern einer Zeile.
        dimension: Die Anzahl der Felder in einer Zeile oder Spalte des Sudokus.
    """
    d = int(np.sqrt(dimension))
    find = finde_leeres_feld(gi,d)
    if not find:
        return True
    else:
        r, c = find

    for n in range(1,(d*d)+1):
        if pruefe_ziffer(gi,r,c,n,d):
            gi[r][c] = n

            if loese_sudoku(gi,dimension):
                return True

            gi[r][c] = 0
            
    return False


#Testmöglichkeit

#Ein 9x9-Gitter zum Testen
testgitter9x9 = [[7,8,0,4,0,0,1,2,0],
                 [6,0,0,0,7,5,0,0,9],
                 [0,0,0,6,0,1,0,7,8],
                 [0,0,7,0,4,0,2,6,0],
                 [0,0,1,0,5,0,9,3,0],
                 [9,0,4,0,6,0,0,0,5],
                 [0,7,0,3,0,0,0,1,2],
                 [1,2,0,0,0,7,4,0,0],
                 [0,4,9,2,0,6,0,0,7]]

#Ein 16x16-Gitter zum Testen
testgitter16x16 = [[0,0,5,0,0,0,0,9,13,0,0,0,0,0,0,0],
                    [16,7,3,12,4,6,1,8,15,11,10,2,9,13,5,14],
                    [11,13,9,4,3,15,16,2,7,12,14,5,6,10,1,8],
                    [8,10,14,1,12,5,11,13,9,3,6,16,7,4,15,2],               
                    [0,0,0,0,0,0,0,0,0,15,9,0,14,0,0,0],
                    [9,14,13,16,11,2,12,3,8,10,7,4,5,15,6,1],
                    [5,15,7,11,14,4,9,1,2,6,3,12,10,8,16,13],
                    [10,8,4,6,15,13,5,7,14,1,16,11,2,12,9,3],          
                    [7,0,0,0,0,1,0,0,16,2,15,9,8,6,13,0],
                    [13,6,8,14,9,12,2,16,1,5,11,7,4,3,10,15],
                    [4,9,11,2,13,3,8,15,10,14,12,6,1,16,7,5],
                    [15,1,16,5,6,10,7,11,3,13,4,8,12,2,14,9],
                    [0,4,10,0,0,0,14,0,11,9,0,0,3,0,0,0],
                    [14,11,2,9,10,7,13,6,12,8,5,3,15,1,4,16],
                    [12,5,15,13,8,9,3,4,6,16,1,10,11,14,2,7],
                    [3,16,6,8,1,11,15,5,4,7,2,14,13,9,12,10]]


#9*9 Sudoku lösen

#print_gitter(testgitter9x9,9)
#loese_sudoku(testgitter9x9,9)
#print_gitter(testgitter9x9,9)


#16*16 Sudoku lösen

#print_gitter(testgitter16x16,16)
#loese_sudoku(testgitter16x16,16)
#print_gitter(testgitter16x16,16)
