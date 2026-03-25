#IMPORTS

import os
import pygame
from player import Player

#====================

#keys for my self remove later 

# draw key (x cord, y cord, width, hight)

#=====================

#For logic pathing

GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def get_asset_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(GAME_PATH, "assets", filename)

#============================

#Classes in use

player1=Player(200, 200)




#=================

#Game Code

pygame.init()                                  # initialize pygame
screen = pygame.display.set_mode( (1000, 800) ) # create a window
pygame.display.set_caption("Endless Desent")      # set window title

running = True   # event loop

clock = pygame.time.Clock()

while running:
  #game code goes here


  #keys
  keys=pygame.key.get_pressed()

  if keys[pygame.K_w]:
    player1.y-=1 
  
  if keys[pygame.K_s]:
    player1.y+=1

  if keys[pygame.K_a]:
    player1.x-=1

  if keys[pygame.K_d]:
    player1.x+=1



  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  screen.fill((0,0,0))
  
  pygame.draw.rect( screen, (0,0,255), (player1.x,player1.y,player1.width, player1.height) )



  pygame.display.flip()
  clock.tick(60)

pygame.quit()  # teardown

