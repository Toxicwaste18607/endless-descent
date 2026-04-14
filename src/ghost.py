import pygame
from player import *

blue = (0, 0, 255)

class Player_ghost:
    height=70
    width=50
    def __init__(self, hitbox):
        self.hitbox = hitbox.copy()

    def draw(self, screen):
        pygame.draw.rect(screen, blue, self.hitbox)

    def load_images(self):
        self.ghost_1=pygame.image.load("scr/assets/Knigh/Ghost_2.png")
        self.ghost_1=pygame.transform.scale(self.ghost_1(self.height))