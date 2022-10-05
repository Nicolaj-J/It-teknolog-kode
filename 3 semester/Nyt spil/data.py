import pygame

class person(pygame.sprite.Sprite):
    def __init__(self, width, height) -> None:
        super().__init__(self)
        pygame.draw.rect(self.image,pygame.Rect(0,0,width,height))
        self.image = "Top-Down-Character/elf_back_idle/elf_back_idle.png"
        
p1 = person(5,5