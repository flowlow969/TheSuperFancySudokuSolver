spielfeld = [[1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9],
             [1,4,5,0,0,3,2,0,9]]


def print_to_cli(feld):
    for y in range(9):
        for x in range (9):
            print(feld[y][x])
        print("\n")


print_to_cli(spielfeld)