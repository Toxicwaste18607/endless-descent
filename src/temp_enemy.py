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
    def __init__ (self ,x,y):
        self.x = x
        self.y = y
        self.hitbox=pygame.Rect(x, y, self.width, self.height)
        self.all_enemies.append(self)
        
  
    def draw_charicater(self,screen):
      pygame.draw.rect( screen, (255,0,0), (self.hitbox ))

    
    def check_dist(self,other):
       self.distance_x= (other.hitbox.x - self.hitbox.x)
       self.distance_y= (other.hitbox.y - self.hitbox.y)

    
    def search (self,other):
       self.check_dist(other)
       #add agro distance here 
       self.agro()


    def agro(self):
      if self.distance_x > 0:
         self.hitbox.x+=1
      
      if self.distance_y >0:
         self.hitbox.y+=1

      if self.distance_x <0:
         self.hitbox.x += 1
      
      if self.distance_y<0:
         self.hitbox.y+=1
       


    def move(self):
       self.hitbox.x= random.choice(+1,-1)

       
    
    def attack(self,other):


      pass
    
   
