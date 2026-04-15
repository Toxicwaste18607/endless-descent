import pygame
from player import *
from enemy_class import *

blue = (0, 0, 255)

class Player_ghost(Enemy):
    

    width= 35
    height= 50
    agro_range=300
    max_health=100
    health=100
    health_regen=1
    attack_range = 5
    damage=20
    range_multi=2
    stamina = 100
    max_stamina=100
    stamina_regain = .02
    speed=1
    def __init__(self,hitbox):
       
        self.load_images()
        super().__init__(hitbox)   
        


    def draw_character(self, screen):
        screen.blit(self.ghost_1,(self.hitbox.x, self.hitbox.y))

    def load_images(self):
        self.ghost_1=pygame.image.load("src/assets/Knight/Ghost_2.png")
        self.ghost_1=pygame.transform.scale(self.ghost_1,(self.width,self.height))
