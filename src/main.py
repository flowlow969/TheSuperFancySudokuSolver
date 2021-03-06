import pygame, sys
import sudoku_solver as ss

pygame.init()
#Anzeige Parameter
windowsizex = 560
windowsizey = 560
gameBorderYLeft = 100
gameBorderYRight = 700
win = pygame.display.set_mode((windowsizex,windowsizey))
run = True
activFlag = 0

#Text Parameter
pygame.display.set_caption("Sudoku Solver")
font = pygame.font.SysFont('comicsans', 36, True)
font1 = pygame.font.SysFont('comicsans', 100, True)

clockspeed = pygame.time.Clock()




black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255, 0)
width = 40
hight = 40


class Button(object):
    def __init__(self, x, y, width, hight, text):
        #Startposition
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.text = text

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.hight),2)
        text = font.render(self.text, 1, red)
        win.blit(text, ((self.x + 10), (self.y + 5)))





    def select(self, pos):
        if (self.x <= pos[0]) and ((self.x+self.width) >= pos[0]):
            if (self.y <= pos[1]) and ((self.y + self.hight) >= pos[1]):
                return True
        else:
            return False



class platz(object):
    def __init__(self, x, y, value):
        #Startposition
        self.x = x
        self.y = y
        #Wert
        self.value = value
        #Activ
        self.active = False

    def draw(self, win):

        if self.active:
            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, width, hight),2)
            text = font.render(str(self.value), 1, red)
            win.blit(text, ((self.x + 10), (self.y + 5)))
        else:
            pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, width, hight), 2)
            text = font.render(str(self.value), 1, black)
            win.blit(text, ((self.x + 15), (self.y + 10)))


    def select(self, pos):
        if (self.x <= pos[0]) and ((self.x+width) >= pos[0]):
            if (self.y <= pos[1]) and ((self.y + hight) >= pos[1]):
                return True
        else:
            return False


def draw():
    global spielfeld, solve, clear, quiter
    win.fill(white)
    solve.draw(win)
    clear.draw(win)
    for feld in spielfeld:
        feld.draw(win)
    pygame.draw.line(win, black, [220, 80], [220, 480],5)
    pygame.draw.line(win, black, [80, 220], [480, 220],5)
    pygame.draw.line(win, black, [340, 80], [340, 480], 5)
    pygame.draw.line(win, black, [80, 340], [480, 340], 5)

    pygame.display.update()


def quitGame():
    pygame.quit()

def init_sudoku():
    global spielfeld, solve, clear, quiter
    spielfeld = []
    for x in range(9):
        for y in range(9):
            spielfeld.append(platz((100 + 40 * x), (100 + 40 * y), 0))
    solve = Button(400,500,100,30,"Solve")
    clear = Button(80,500,100,30,"Clear")




init_sudoku()
draw()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #Active Felder abwählen
            if activFlag == 1:
                for feld in spielfeld:
                    feld.active = False
                activFlag = 0
            #Auswahl Solver
            if solve.select(pos):
                #Umrechnen in 2D Array aus liste
                cnt = 0
                y = 0
                x = 0
                temp = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
                for feld in spielfeld:
                    if (cnt ) % 9 == 0:
                        y = y + 1
                    x = (cnt ) - ((y - 1) * 9)
                    temp[x][y-1] = int(feld.value)
                    cnt = cnt + 1
                is_solved = ss.loese_sudoku(temp)
                if is_solved:
                    cnt = 0
                    for x in range(9):
                        for y in range(9):
                            spielfeld[cnt].value = temp[y][x]
                            cnt += 1

            if clear.select(pos):
                for feld in spielfeld:
                    feld.value = 0


            for feld in spielfeld:
                if feld.select(pos):
                    activFlag = 1
                    feld.active = True
        if event.type  == pygame.KEYDOWN:
            for feld in spielfeld:
                if feld.active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_0:
                            key = 0
                            activFlag = 0
                        if event.key == pygame.K_1:
                            key = 1
                            activFlag = 0
                        if event.key == pygame.K_2:
                            key = 2
                            activFlag = 0
                        if event.key == pygame.K_3:
                            key = 3
                            activFlag = 0
                        if event.key == pygame.K_4:
                            key = 4
                            activFlag = 0
                        if event.key == pygame.K_5:
                            key = 5
                            activFlag = 0
                        if event.key == pygame.K_6:
                            key = 6
                            activFlag = 0
                        if event.key == pygame.K_7:
                            key = 7
                            activFlag = 0
                        if event.key == pygame.K_8:
                            key = 8
                            activFlag = 0
                        if event.key == pygame.K_9:
                            key = 9
                            activFlag = 0
                        if event.key == pygame.K_DELETE:
                            key = None
                        feld.value = key
                        if event.key == pygame.K_RETURN:
                            for feld in spielfeld:
                                feld.active = False




    draw()



    clockspeed.tick(4)

quitGame()