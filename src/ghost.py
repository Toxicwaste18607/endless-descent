import pygame
from player import *

blue = (0, 0, 255)

class Player_ghost:
    
    def __init__(self, hitbox):
        self.hitbox = hitbox.copy()
        self.height=70
        self.width=50
        self.load_images()


    def draw(self, screen):
        screen.blit(self.ghost_1(self.hitbox.x, self.hitbox.y))

    def load_images(self):
        self.ghost_1=pygame.image.load("src/assets/Knight/Ghost_2.png")
        self.ghost_1=pygame.transform.scale(self.ghost_1,(self.width,self.height))