#IMPORTS

import os
import pygame
from player import Player
from setting import *
#====================

#keys for my self remove later 

# pygame.draw.rect( screen, (Color), (x ,y ,width, height) )


#git add .
#git commit -m "progress update"
#git push
#===================

#For logic pathing

GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def get_asset_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(GAME_PATH, "assets", filename)

#============================

#Classes in use
player=Player(100, 200)


#===================
# Colors

#===============
#Defs and classes 

class Walls():
  def __init__(self,x,y,width,height):
    self.x=x
    self.y=y
    self.height= height
    self.width= width
  
  def draw_wall(self,screen):
    pygame.draw.rect(screen,(255,255,255), (self.x,self.y,self.width,self.height))

  def wall_area(self):
    wall_rect=pygame.Rect(self.x, self.y,self.width,self.height)
    return wall_rect



wall_1= Walls(200,200,50,50)

def collision():
  keys=pygame.key.get_pressed()

  if player.player_area().colliderect(wall_1.wall_area()):
    
    if keys[pygame.K_w]:
      move_up= player.y + 1
      move_up_rect= pygame.Rect(player.x,move_up, player.width, player.height)
      if not move_up_rect.colliderect(wall_1.wall_area()):
        player.y=move_up
    


    if keys[pygame.K_s]:
      move_down= player.y -1
      move_down_rect= pygame.Rect(player.x, move_down,player.width, player.height)
      if not move_down_rect.colliderect(wall_1.wall_area()):
        player.y = move_down


    if keys[pygame.K_a]:
      move_left=player.x - 1
      move_left_rect=pygame.Rect(move_left,player.y,player.width,player.height)
      if not move_left_rect.colliderect(wall_1.wall_area()):
        player.x=move_left


    if keys[pygame.K_d]:
      move_right= player.x +1
      move_right_rect=pygame.Rect(move_right,player.y,player.width,player.height)
      if not move_right_rect.colliderect(wall_1.wall_area()):
        player.x=move_right


    
      
      

   
    
    

  
def movement():
  keys=pygame.key.get_pressed()

  if keys[pygame.K_w]:
    collision()
    player.y-=1 
  
  if keys[pygame.K_s]:
    collision()
    player.y+=1

  if keys[pygame.K_a]:
    collision()
    player.x-=1

  if keys[pygame.K_d]:
    collision()
    player.x+=1

  if player.x < 0: #to stop the player from going off screen 
    player.x= 0 
  
  if player.y<0:
    player.y=0

  over_shoot_left= (screen_width - player.width)
  if player.x > over_shoot_left:
    player.x = over_shoot_left

  over_shoot_down=(screen_height- player.height)
  if player.y> over_shoot_down:
    player.y = over_shoot_down



  

#=================

#Game Code

pygame.init()                                  # initialize pygame
screen = pygame.display.set_mode( (screen_width, screen_height) ) # create a window
pygame.display.set_caption("Endless Desent")      # set window title

running = True   # event loop

clock = pygame.time.Clock()

while running:
  #game code goes here

  screen.fill((0,0,0))

  movement()  

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  
  player.draw_charicater(screen)
  wall_1.draw_wall(screen)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()  # teardown

