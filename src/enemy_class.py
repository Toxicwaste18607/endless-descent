import pygame
import time
import random
from key_move import *
from player import *


#this will be enemy base code used in all enemy classes
class Enemy():
    all_enemies =[]
    width= 25
    height= 50
    speed=1
    def __init__ (self ,x,y):
        self.x = x
        self.y = y
        self.hitbox=pygame.Rect(x, y, self.width, self.height)
        self.all_enemies.append(self)
        
  
    def draw_character(self,screen):
      pygame.draw.rect( screen, (255,0,0), (self.hitbox ))

    def  collision(self,next_move):
         for wall in Walls.all_walls or Player.hitbox:
            if next_move.colliderect(wall.wall_hitbox or Player.hitbox):
               return True



    def check_dist(self,other):
       self.distance_x= (other.hitbox.x - self.hitbox.x)
       self.distance_y= (other.hitbox.y - self.hitbox.y)

    
    def search (self,other):
       self.check_dist(other)
       if self.distance_x<5 or self.distance_y<5: #agro distance 
         self.agro()
       else:
          self.wander()


    def agro(self):
      if self.distance_x > 0:
         next_move=self.hitbox.x + self.speed
         if not self.collision(next_move):
            self.hitbox.x+=self.speed
      
      
      if self.distance_y >0:
         next_move=self.hitbox.y + self.speed
         if not self.collision(next_move):
            self.hitbox.y+=self.speed

      if self.distance_x <0:
         next_move=self.hitbox.x + self.speed
         if not self.collision(next_move):
            self.hitbox.x -= self.speed
      


      if self.distance_y<0:
         next_move=self.hitbox.y +self.speed
         if not self.collision(next_move):
            self.hitbox.y-=1
       


    def wander(self):
       pass

       
    
    def attack(self,other):


      pass
    
   
