import pygame
from player import *
from enemy_class import *

blue = (0, 0, 255)

class Player_ghost(Enemy):
    
    def __init__(self,screen,  hitbox):
        super().__init__(hitbox)   
        self.width = 50
        self.height = 70
        self.load_images(screen)


    def draw(self, screen):
        screen.blit(self.ghost_1,(self.hitbox.x, self.hitbox.y))

    def load_images(self):
        self.ghost_1=pygame.image.load("src/assets/Knight/Ghost_2.png")
        self.ghost_1=pygame.transform.scale(self.ghost_1,(self.width,self.height))