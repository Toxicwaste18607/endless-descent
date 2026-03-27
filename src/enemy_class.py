import pygame
from key_move import *


#to do list 
#make enemy only move in one direction at a time
# make a better path finding 





green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)

#this will be enemy base code used in all enemy classes
class Enemy():
    all_enemies =[]
    width= 25
    height= 50
    speed=1
    agro_range=300
    def __init__ (self ,x,y):
        self.x = x
        self.y = y
        self.hitbox=pygame.Rect(x, y, self.width, self.height)
        Enemy.all_enemies.append(self)
        
  
    def draw_character(self,screen):
      pygame.draw.rect( screen, (red), (self.hitbox ))

    def  collision(self,next_move,other):
         for wall in Walls.all_walls:
            if next_move.colliderect(wall.wall_hitbox):
               return True
         if next_move.colliderect(other.hitbox):
            return True

    def path_finding(self,blocked,other):
       #key 1 means right, 2 means up, 3 means left, 4 means down 
       ## x+ = right, x- = left, y+ = down, y- = up

       if blocked == 1:
         next_move=self.hitbox.copy()
         next_move.x-=self.speed
         if not self.collision(next_move,other):
            self.hitbox.x-=self.speed
         else:
            blocked= 3
         

       if blocked == 2:
         next_move=self.hitbox.copy()
         next_move.y-=self.speed
         if not self.collision(next_move,other):
            self.hitbox.y-=self.speed
         else:
            blocked=4


       if blocked == 3:
         next_move=self.hitbox.copy()
         next_move.x+=self.speed
         if not self.collision(next_move,other):
            self.hitbox.x+=self.speed
         else:
            blocked=1

       if blocked == 4:
         next_move=self.hitbox.copy()
         next_move.y+=self.speed
         if not self.collision(next_move,other):
            self.hitbox.y+=self.speed
         else:
            blocked=2



    def check_dist(self,other):
       self.distance_x= (other.hitbox.x - self.hitbox.x)
       self.distance_y= (other.hitbox.y - self.hitbox.y)

    
    def search (self,other):
       self.check_dist(other)
       if abs(self.distance_x)<self.agro_range and abs(self.distance_y)<self.agro_range: 
         self.agro(other)
       else:
          self.wander()


    def agro(self,other): #right
      if self.distance_x > 0:
         next_move=self.hitbox.copy()
         next_move.x+=self.speed
         if not self.collision(next_move,other):
            self.hitbox.x+=self.speed
         else:
            blocked=1
            self.path_finding(blocked,other)
      
      
      if self.distance_y >0:#up
         next_move=self.hitbox.copy()
         next_move.y+=self.speed
         if not self.collision(next_move,other):
            self.hitbox.y+=self.speed
         else:
            blocked=2
            self.path_finding(blocked,other)

      if self.distance_x <0:#left
         next_move=self.hitbox.copy()
         next_move.x-= self.speed
         if not self.collision(next_move,other):
            self.hitbox.x -= self.speed
         else:
            blocked=3
            self.path_finding(blocked,other)
      


      if self.distance_y<0:#down
         next_move=self.hitbox.copy()
         next_move.y-=self.speed
         if not self.collision(next_move,other):
            self.hitbox.y-=self.speed
         else:
            blocked=4
            self.path_finding(blocked,other)



    def wander(self):
       pass

       
    
    def attack(self,other):


      pass
    
   
