import pygame
from player import *

blue = (0, 0, 255)

class Player_Ghost(Player):
    def __init__(self, hitbox):
        super().__init__(hitbox.x, hitbox.y)

    def draw_character(self, screen):
        pygame.draw.rect(screen, blue, self.hitbox)