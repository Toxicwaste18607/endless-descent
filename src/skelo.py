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
        hitbox=pygame.Rect(x, y, self.width, self.height)
        super().__init__(hitbox)
        self.load_image()
        self.hitbox=hitbox
        
  


   def load_image(self):
      self.standing=pygame.image.load("src/assets/skelo.png")
      self.standing=pygame.transform.scale(self.standing,(self.width,self.height))




   def draw_character(self,screen):
      screen.blit(self.standing,(self.hitbox.x,self.hitbox.y))
   def  collision(self,screen,next_move,other):
         for wall in Walls.all_walls:
            if next_move.colliderect(wall.wall_hitbox):
               return True
            if next_move.colliderect(other.hitbox):
               self.attack(screen, other)
               return True


      
   