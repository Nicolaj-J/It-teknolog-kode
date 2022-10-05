from typing import Tuple

import pygame
import sys
import os

'''
Variables
'''

worldx = 920
worldy = 720
fps = 60
ani = 2
steps = 5
world = pygame.display.set_mode([worldx, worldy])

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

'''
Objects
'''


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """
    frontidleimage = ["Character\elf_front_idle\elf_front_idle.png"]
    backidleimage = ["Character\elf_back_idle\elf_back_idle.png"]
    rightidleimage = ["Character\elf_side01_idle\elf_side01_idle.png"]
    leftidleimage = ["Character\elf_side02_idle\elf_side02_idle.png"]
    frontwalkani = ["Character\elf_front_walk\elf_front_walk1.png","Character\elf_front_walk\elf_front_walk2.png","Character\elf_front_walk\elf_front_walk3.png","Character\elf_front_walk\elf_front_walk4.png","Character\elf_front_walk\elf_front_walk5.png","Character\elf_front_walk\elf_front_walk6.png","Character\elf_front_walk\elf_front_walk7.png","Character\elf_front_walk\elf_front_walk8.png"]
    backwalkani = []
    rightwalkani = []
    leftwalkani = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.idleimages = []
        for i in range(1, 5):
            imgfront = pygame.image.load("Character\elf_front_idle\elf_front_idle.png").convert()
            imgfront.convert_alpha()  # optimise alpha
            imgfront.set_colorkey(ALPHA)  # set alpha
            self.idleimages.append(imgfront)
            self.image = self.idleimages[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.idleimages[self.frame // ani], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.idleimages[self.frame//ani]


'''
Setup
'''

backdrop = pygame.image.load("Minifantasy_ForgottenPlains_v3.5_Free_Version\Minifantasy_ForgottenPlains_Assets\Minifantasy_ForgottenPlainsMockup.png")
backdrop = pygame.transform.scale(backdrop, (1280, 720))
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)


'''
Main Loop
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, -steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, steps)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, -steps)

    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)