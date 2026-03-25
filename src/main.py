#IMPORTS

import os
import pygame
from player import Player

#====================

#keys for my self remove later 

# draw key (x cord, y cord, width, hight)

#git add .
#git commit -m "progress update"
#git push
#===================
#setting
screen_width= 1000
screen_height= 800

#=====================

#For logic pathing

GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def get_asset_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(GAME_PATH, "assets", filename)

#============================

#Classes in use

player=Player(200, 200)

#===============
#Defs
def movement():
  keys=pygame.key.get_pressed()

  if keys[pygame.K_w]:
    player.y-=1 
  
  if keys[pygame.K_s]:
    player.y+=1

  if keys[pygame.K_a]:
    player.x-=1

  if keys[pygame.K_d]:
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


  movement()


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  screen.fill((0,0,0))
  
  pygame.draw.rect( screen, (0,0,255), (player.x,player.y,player.width, player.height) )



  pygame.display.flip()
  clock.tick(60)

pygame.quit()  # teardown

