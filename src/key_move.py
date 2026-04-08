import pygame
from setting import *
from wall_class_code import *
from enemy_class import *




def collision(next_move):
  for wall in Walls.all_walls:
    if next_move.colliderect(wall.wall_hitbox):
      return True
  return None
    #if next_move.colliderect():pass




def movement(self):
  keys=pygame.key.get_pressed()

  walking=1
  sprinting=2
  speed = walking
  if keys[pygame.K_LSHIFT]:
    self.sprint()
    
    if self.sprint():
      speed = sprinting 
    else:
      speed = walking






  if keys[pygame.K_w]: #up
    next_move=self.hitbox.copy()
    next_move.y-=speed
    if not collision(next_move): 
        self.hitbox.y -= speed
    
   
  
  if keys[pygame.K_s]:#down
    next_move=self.hitbox.copy()
    next_move.y+=speed
    if not collision(next_move):
        self.hitbox.y+=speed
  
    

  if keys[pygame.K_a]:#left
    next_move=self.hitbox.copy()
    next_move.x-=speed
    if not collision(next_move):
      self.hitbox.x-=speed


  if keys[pygame.K_d]:#right
    next_move=self.hitbox.copy()
    next_move.x+=speed
    if not collision(next_move):
      self.hitbox.x+=speed
  
  if not keys[pygame.K_LSHIFT]:
    self.stamina+=self.stamina_regain

  

  if self.hitbox.x < 0: #to stop the player from going off screen 
    self.hitbox.x= 0 
  
  if self.hitbox.y<0:
    self.hitbox.y=0

  over_shoot_left= (screen_width - self.width)
  if self.hitbox.x > over_shoot_left:
    self.hitbox.x = over_shoot_left

  over_shoot_down=(screen_height- self.height)
  if self.hitbox.y> over_shoot_down:
    self.hitbox.y = over_shoot_down

#test