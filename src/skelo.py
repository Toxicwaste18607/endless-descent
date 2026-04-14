import pygame
from enemy_class import *





 

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)

#this will be enemy base code used in all enemy classes
class Skelo(Enemy):
   all_enemies =[]
   agro_range=300
   
   width= 50
   height= 70

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