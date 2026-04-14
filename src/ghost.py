import pygame
from player import *

blue = (0, 0, 255)

class Player_ghost:
    def __init__(self, hitbox):
        self.hitbox = hitbox.copy()

    def draw(self, screen):
        pygame.draw.rect(screen, blue, self.hitbox)