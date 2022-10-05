import pygame 
from pygame.locals import *
import data
import time
pygame.init()  
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
sizenormal = 45
sizehighlight = 65
# assigning values to height and width variable   
height = 400  
width = 400  
# creating the display surface object   
# of specific dimension..e(X, Y).   
display_surface = pygame.display.set_mode((height, width))  
seguisy80_45 = pygame.font.SysFont("segoeuisymbol", sizenormal)
seguisy80_65 = pygame.font.SysFont("segoeuisymbol", sizehighlight)

def drawGrid(w, rows, surface):  
    sizeBtwn = w // rows  
  
    x = 0  
    y = 0  
    for l in range(rows):  
        x = x + sizeBtwn  
        y = y + sizeBtwn  
        # draw grid line  
        pygame.draw.line(surface, (0, 0, 0), (x, 0), (x, w))  
        pygame.draw.line(surface, (0, 0, 0), (0, y), (w, y))
# infinite loop
def setup2(mousepos0, pressedpiece):
    for key, value in data.chessboard.piecepos.items():
        color = key[-6:-1]
        piece = key[0:-6]
        piececolor = key[0:-1]
        fullpiece = key
        position = value
        if str(color) == "black":
            color = (0, 0, 0)
        elif color == "white":
            color =(255, 255, 255)
        if position == "":
            pass
        elif mousepos0 == position and pressedpiece == True:
            display_surface.blit(seguisy80_65.render(data.chessboard.unicode[piececolor], True, color),data.chessboard.Lo(position))
        else:
            display_surface.blit(seguisy80_45.render(data.chessboard.unicode[piececolor], True, color),data.chessboard.Lo(position))

mouse_presses = pygame.mouse.get_pressed()
mousepos = None
def resetpos():
    for x in data.chessboard.whiteofficerpositions:
        for y in data.chessboard.startwhiteofficerpositions:
            xpiece = x[0]
            ypiece = y[0]
            if xpiece == ypiece:
                xposition = x[1]
                yposition = y[1]
def changepiecepos():
    while True:
        for x in data.chessboard.vandretpos:
            mousevandret2, mouselodret2 = pygame.mouse.get_pos()
            if mousevandret2 > x[1] and mousevandret2 < x[2]:
                mouseposvandret2 = str(x[0])
            else:
                pass
            
        for x in data.chessboard.lodretpos:
            if mouselodret2 > x[1] and mouselodret2 < x[2]:
                mouseposlodret2 = str(x[0])
            else:
                pass
        try:
            mousepos2 = mouseposvandret2 + mouseposlodret2
            
            for key, value in data.chessboard.piecepos.items():
                if value == mousepos:
                    piececheck(mousepos2, key)
                    data.chessboard.piecepos[key] = str(mousepos2)
            
            setup2(None, pressedpiece)
            pygame.event.wait()
            pygame.event.clear()
            time.sleep(0.1)
            break
        except:
            break

def piececheck(position, piece):
    for key, value in data.chessboard.piecepos.items():
        if key == piece:
            pass
        else:
            if value == position:
                data.chessboard.piecepos[key] = ""
def turncheck(piece):
    pass

resetpos()
pressedpiece = False
setup2(mousepos, pressedpiece)
while True:  
    display_surface.fill(BLUE)  
    drawGrid(width,8,display_surface)  
    if pygame.mouse.get_pressed()[0] == True and pressedpiece == False:
        pygame.event.get()
        mousevandret, mouselodret = pygame.mouse.get_pos()
        for x in data.chessboard.vandretpos:
            if mousevandret > x[1] and mousevandret < x[2]:
               mouseposvandret = str(x[0]) 
        for x in data.chessboard.lodretpos:
            if mouselodret > x[1] and mouselodret < x[2]:
                mouseposlodret = str(x[0])
        mousepos = mouseposvandret + mouseposlodret
        piece = data.Get_piece(mousepos)
        data.chessboard.piecehighlight["highlight"] = piece
        pressedpiece = True
        setup2(mousepos, pressedpiece)
        pygame.event.wait()
        time.sleep(0.1)
    elif pygame.mouse.get_pressed()[0] == True and pressedpiece == True:
        changepiecepos()
        pressedpiece = False
    setup2(mousepos, pressedpiece)



    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()  
            # quit the program.   
            quit()  
        # Draws the surface object to the screen.   
        pygame.display.update()   