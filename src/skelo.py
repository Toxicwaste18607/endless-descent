import pygame
from enemy_class import *





 

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)

#this will be enemy base code used in all enemy classes
class Skelo(Enemy):
   
   def __init__ (self ,x,y):
        self.hitbox=pygame.Rect(x, y, self.width, self.height)
        Enemy.all_enemies.append(self)
        self.load_image()
   
      
   def attack(self,screen,other):
    attack_box=(self.hitbox.x-self.attack_range,  self.hitbox.y -self.attack_range,
                self.hitbox.width +(self.attack_range*self.range_multi),
                self.hitbox.height+(self.attack_range*self.range_multi))
    attack_box=pygame.Rect(attack_box)
    pygame.draw.rect(screen,green,attack_box)
    if attack_box.colliderect(other.hitbox):
        other.take_damage(self,other)