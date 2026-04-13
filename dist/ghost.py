import pygame
from player import *

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)


class Player_Ghost(Player):

    def __init__(self,screen,hitbox):
        super().__init__(x, y) 
        

    def draw_ghost(self,screen):
        pygame.draw.rect( screen, (blue), (self.hitbox))
