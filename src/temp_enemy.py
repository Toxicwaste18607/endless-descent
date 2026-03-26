import pygame
import time
from key_move import *

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


    def move(self):
       found_player= False
       while found_player is False:
          self.hitbox.x -= 1

       
       
       
       
       

    def attack(self,other):


      pass