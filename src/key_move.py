import pygame
from setting import *
from wall_class_code import *
from enemy_class import *




def collision(next_move):
  for wall in Walls.all_walls:
    if next_move.colliderect(wall.wall_hitbox):
      return True
    #return False
    #if next_move.colliderect():pass




def movement(player):
  keys=pygame.key.get_pressed()

  walking=1
  sprinting=2
  speed = walking
  if keys[pygame.K_LSHIFT]:
    player.sprint()
    
    if player.sprint():
      speed = sprinting 
    else:
      speed = walking






  if keys[pygame.K_w]: #up
    next_move=player.hitbox.copy()
    next_move.y-=speed
    if not collision(next_move): 
        player.hitbox.y -= speed
    
   
  
  if keys[pygame.K_s]:#down
    next_move=player.hitbox.copy()
    next_move.y+=speed
    if not collision(next_move):
        player.hitbox.y+=speed
  
    
    

  if keys[pygame.K_a]:#left
    next_move=player.hitbox.copy()
    next_move.x-=speed
    if not collision(next_move):
      player.hitbox.x-=speed


  if keys[pygame.K_d]:#right
    next_move=player.hitbox.copy()
    next_move.x+=speed
    if not collision(next_move):
      player.hitbox.x+=speed
  
  if not keys[pygame.K_LSHIFT]:
    player.stamina+=player.stamia_regain

  

  if player.hitbox.x < 0: #to stop the player from going off screen 
    player.hitbox.x= 0 
  
  if player.hitbox.y<0:
    player.hitbox.y=0

  over_shoot_left= (screen_width - player.width)
  if player.hitbox.x > over_shoot_left:
    player.hitbox.x = over_shoot_left

  over_shoot_down=(screen_height- player.height)
  if player.hitbox.y> over_shoot_down:
    player.hitbox.y = over_shoot_down

#test