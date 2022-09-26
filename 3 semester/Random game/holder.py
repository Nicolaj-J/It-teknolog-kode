from turtle import width
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((500, 500))

seguisy80 = pygame.font.SysFont("segoeuisymbol", 80)
queenblack = "\u2655"
queenblacktext = seguisy80.render(queenblack, True, BLACK)

class pieces():
    def white_pieces():
        kingwhite ="\u2654"
        queenwhite = "\u2655"
        rookwhite = "\u2656"
        bishopwhite  = "\u2657"
        knightwhite = "\u2658"
        pawnwhite = "\u2659"
    def black_pieces():
        kingblack ="\u265A"
        queenblack = "\u265B"
        rookblack = "\u265C"
        bishopblack  = "\u265D"
        knightblack = "\u265E"
        pawnblack = "\u265F"
run = True

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
while run:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    drawGrid(width,8,WHITE)
    window.blit(queenblacktext, (100, 100))
    pygame.display.flip()