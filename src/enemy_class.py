import pygame
from wall_class_code import *





 

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)

#this will be enemy base code used in all enemy classes
class Enemy():
   all_enemies =[]

   def __init__ (self ,hitbox):
        self.hitbox=pygame.Rect(hitbox.x, hitbox.y, self.width, self.height)
        Enemy.all_enemies.append(self)

        
  

   def enemy_logic(self,screen,other):
      if self.health>0:
         self.draw_character(screen)
         self.search (screen,other)

      else:
         pass





   def  collision(self,screen,next_move,other):
         for wall in Walls.all_walls:
            if next_move.colliderect(wall.wall_hitbox):
               return True
            if next_move.colliderect(other.hitbox):
               self.attack(screen, other)
               return True

   def path_finding(self,screen,blocked,other):
       #key 1 means right, 2 means up, 3 means left, 4 means down 
       ## x+ = right, x- = left, y+ = down, y- = up

       if blocked == 1:
         next_move=self.hitbox.copy()
         next_move.x-=self.speed
         if not self.collision(screen,next_move,other):
            self.hitbox.x-=self.speed
         else:
            blocked= 3
         

       if blocked == 2:
         next_move=self.hitbox.copy()
         next_move.y-=self.speed
         if not self.collision(screen,next_move,other):
            self.hitbox.y-=self.speed
         else:
            blocked=4


       if blocked == 3:
         next_move=self.hitbox.copy()
         next_move.x+=self.speed
         if not self.collision(screen,next_move,other):
            self.hitbox.x+=self.speed
         else:
            blocked=1

       if blocked == 4:
         next_move=self.hitbox.copy()
         next_move.y+=self.speed
         if not self.collision(screen,next_move,other):
            self.hitbox.y+=self.speed
         else:
            blocked=2



   def check_dist(self,other):
       self.distance_x= (other.hitbox.x - self.hitbox.x)
       self.distance_y= (other.hitbox.y - self.hitbox.y)

    
   def search (self,screen,other):
       self.check_dist(other)
       if abs(self.distance_x)<self.agro_range and abs(self.distance_y)<self.agro_range: 
         self.agro(screen,other)
       else:
          self.wander()


   def agro(self,screen,other): #right
      if self.distance_x > 0:
         next_move=self.hitbox.copy()
         next_move.x+=self.speed
         if not self.collision(screen,next_move,other):
            self.hitbox.x+=self.speed
         else:
            blocked=1
            self.path_finding(screen,blocked,other)
      
      
      if self.distance_y >0:#up
         next_move=self.hitbox.copy()
         next_move.y+=self.speed
         if not self.collision(screen,next_move,other):
            self.hitbox.y+=self.speed
         else:
            blocked=2
            self.path_finding(screen,blocked,other)

      if self.distance_x <0:#left
         next_move=self.hitbox.copy()
         next_move.x-= self.speed
         if not self.collision(screen,next_move,other):
            self.hitbox.x -= self.speed
         else:
            blocked=3
            self.path_finding(screen,blocked,other)
      


      if self.distance_y<0:#down
         next_move=self.hitbox.copy()
         next_move.y-=self.speed
         if not self.collision(screen,next_move,other):
            self.hitbox.y-=self.speed
         else:
            blocked=4
            self.path_finding(screen,blocked,other)



   def wander(self):
       pass

       

    
   def take_damage (self,other):
      if self.health > 0:
         self.health -= other.damage
         if self.health<= 0:
            self.all_enemies.remove(self)
    

   def attack(self,screen,other):
      attack_box=(self.hitbox.x-self.attack_range,  self.hitbox.y -self.attack_range,
                  self.hitbox.width +(self.attack_range*self.range_multi),
                  self.hitbox.height+(self.attack_range*self.range_multi))
      attack_box=pygame.Rect(attack_box)
      pygame.draw.rect(screen,green,attack_box)
      if attack_box.colliderect(other.hitbox):
         other.take_damage(self,other)
         
   