import pygame, sys
import sudoku_solver as ss

pygame.init()
#Anzeige Parameter
windowsizex = 560
windowsizey = 560

win = pygame.display.set_mode((windowsizex,windowsizey))
#Betriebszustände
run = True      #Schleife wiederhohlt sich
activFlag = 0   #Ein Feld ist aktiv

#Fenster Tittel Festlegen
pygame.display.set_caption("Sudoku Solver")

#Text Parameter
font = pygame.font.SysFont('comicsans', 36, True)
font1 = pygame.font.SysFont('comicsans', 100, True)

#Initalisierung der Clock
clockspeed = pygame.time.Clock()

#Festlegen der Standart Farben
black = (0,0,0)             #RGB wert für Farbe Schwarz
white = (255,255,255)       #RGB wert für Farbe Weiss
red = (255,0,0)             #RGB wert für Farbe Rot

#Abmasse der eingabe Felder
width = 40
hight = 40

#Klasse für einen Button im Spiel
class Button(object):
    def __init__(self, x, y, width, hight, text):
        """ Initalisiert eine Instanz eines Objekts
                    Args:
                            self:   Instanz eines Objekts.
                            x:      x Positzion des Felds
                            y:      y Positzion des Felds
                            width:  Breite des Buttons
                            hight:  Höhe des Buttons
                            Text:   Beschriftung des Felds"""
        #Startposition
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.text = text

    def draw(self, win):
        """Übergibt die Grafische darstellung an pygame
                        Args:
                            self:   Instanz eines Objekts.
                            win:    Fenster in dem dargestelt wird. """
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.hight),2)
        text = font.render(self.text, 1, red)
        win.blit(text, ((self.x + 10), (self.y + 5)))

    def select(self, pos):
        """Prüft ob die Maus diesen Button angeklickt hat
               Args:
                   self:   Instanz eines Objekts.
                   pos:    Positzion des Mausklicks.

               Returns:    Bool für Button angeklickt oder nicht. """
        if (self.x <= pos[0]) and ((self.x+self.width) >= pos[0]):
            if (self.y <= pos[1]) and ((self.y + self.hight) >= pos[1]):
                return True
        else:
            return False



class platz(object):
    def __init__(self, x, y, value):
        """ Initalisiert eine Instanz eines Objekts
            Args:
                    self:   Instanz eines Objekts.
                    x:      x Positzion des Felds
                    y:      y Positzion des Felds
                    value:  Wert des Felds"""
        #Startposition
        self.x = x
        self.y = y
        #Wert
        self.value = value
        #Activ
        self.active = False

    def draw(self, win):
        """Übergibt die Grafische darstellung an pygame
                Args:
                    self:   Instanz eines Objekts.
                    win:    Fenster in dem dargestelt wird. """
        if self.active:
            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, width, hight),2)
            text = font.render(str(self.value), 1, red)
            win.blit(text, ((self.x + 10), (self.y + 5)))
        else:
            pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, width, hight), 2)
            text = font.render(str(self.value), 1, black)
            win.blit(text, ((self.x + 15), (self.y + 10)))


    def select(self, pos):
        """Prüft ob die Maus diesen Button angeklickt hat
        Args:
            self:   Instanz eines Objekts.
            pos:    Positzion des Mausklicks.

        Returns:    Bool für Platz angeklickt oder nicht. """
        if (self.x <= pos[0]) and ((self.x+width) >= pos[0]):
            if (self.y <= pos[1]) and ((self.y + hight) >= pos[1]):
                return True
        else:
            return False


def redraw():
    """Zeigt alle Elemente des GUI's aus."""
    global spielfeld, solve, clear, quiter,demo
    win.fill(white)
    solve.draw(win)
    clear.draw(win)
    demo.draw(win)
    for feld in spielfeld:
        feld.draw(win)
    pygame.draw.line(win, black, [220, 80], [220, 480],5)
    pygame.draw.line(win, black, [80, 220], [480, 220],5)
    pygame.draw.line(win, black, [340, 80], [340, 480], 5)
    pygame.draw.line(win, black, [80, 340], [480, 340], 5)
    pygame.display.update()

def fill_fields(temp):
    """Nimmt eine Liste entgegen und befült damit das Sudoku
        Args:
            temp:   9*9 Liste mit werten zwischen 0-9"""
    global spielfeld
    cnt = 0
    for x in range(9):
        for y in range(9):
            spielfeld[cnt].value = temp[y][x]
            cnt += 1

def quitGame():
    """Beendet das Spiel"""
    pygame.quit()

def init_sudoku():
    """Initalisiert alle Objekte des GUI's"""
    global spielfeld, solve, clear, quiter, demo
    spielfeld = []
    for x in range(9):
        for y in range(9):
            spielfeld.append(platz((100 + 40 * x), (100 + 40 * y), 0))
    solve = Button(400,500,100,30,"Solve")
    clear = Button(60,500,100,30,"Clear")
    demo = Button(230,500,100,30,"Demo")



#GUI Initalisieren
init_sudoku()

#Spielschleife:
while run:
    #Abfangen von eingabe Ereignisen
    for event in pygame.event.get():
        #Abfangen des Fenster schliesen ereignis
        if event.type == pygame.QUIT:
            run = False
        #Abfangen von Mausclicks
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
                    fill_fields(temp)

            #Einsetzten eines Demo Felds
            if demo.select(pos):
                temp = ss.test_sudoku()
                fill_fields(temp)

            #Bereinigen aller Felder
            if clear.select(pos):
                for feld in spielfeld:
                    feld.value = 0

            #Auswählen eines Felds
            for feld in spielfeld:
                if feld.select(pos):
                    activFlag = 1
                    feld.active = True
        #Abfangen von eingabe über Tastatur
        if event.type  == pygame.KEYDOWN:
            for feld in spielfeld:
                if feld.active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_0:
                            key = 0
                            activFlag = 0
                            feld.active = False
                        if event.key == pygame.K_1:
                            key = 1
                            activFlag = 0
                            feld.active = False
                        if event.key == pygame.K_2:
                            key = 2
                            activFlag = 0
                            feld.active = False
                        if event.key == pygame.K_3:
                            key = 3
                            activFlag = 0
                            feld.active = False
                        if event.key == pygame.K_4:
                            key = 4
                            activFlag = 0
                            feld.active = False
                        if event.key == pygame.K_5:
                            key = 5
                            activFlag = 0
                            feld.active = False
                        if event.key == pygame.K_6:
                            key = 6
                            activFlag = 0
                            feld.active = False
                        if event.key == pygame.K_7:
                            key = 7
                            activFlag = 0
                            feld.active = False
                        if event.key == pygame.K_8:
                            key = 8
                            activFlag = 0
                            feld.active = False
                        if event.key == pygame.K_9:
                            key = 9
                            activFlag = 0
                            feld.active = False
                        if event.key == pygame.K_DELETE:
                            key = None
                        feld.value = key
                        if event.key == pygame.K_RETURN:
                            for feld in spielfeld:
                                feld.active = False

    redraw()
    clockspeed.tick(4)

quitGame()