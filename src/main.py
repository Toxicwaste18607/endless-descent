#IMPORTS

import os
import pygame
import random
from player import Player
from setting import *
from enemy_class import *
from ghost import *
from skelo import *






#====================
green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)

#keys for my self remove later 

# pygame.draw.rect( screen, (Color), (x ,y ,width, height) )


#git add .
#git commit -m "progress update"
#git push


# to do list 
#add ai attack
#fix players health and stamina to fall from the top not the bottem
#add in lighting and player fog of war
#add block
#add in player death
#make proper borders
#make enemy only move in one direction at a time
#make a better path finding 
#make attack zone a circle
#add in colliosn with enemy
#make player classes(assasin, knight, maybe more)
#add in invintory 
#add in loot and gear
#add in enemy classes(goblin, bats ect)
#player and enemy graphics
#add in player ghoast
#clean up all grapics
#make rooms and ai gen them together
#add in final boss 
#put movement into player class
#add in menus







def floor_type_one():
  global floor_one
  floor_one=pygame.image.load("src/assets/walls_and_floors/floor_layout.png").convert_alpha()#this loads the floor png 
  floor_one=pygame.transform.scale(floor_one, (screen_width,screen_height))
  

def load_map(screen):
    screen.blit(floor_one, (0, 0))

    for wall in Walls.all_walls:
        wall.draw_wall(screen)

#===================

#For logic pathing

GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def get_asset_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(GAME_PATH, "assets", filename)

#============================


#==========================
    
   
    
    



  

#=================

#Game Code

pygame.init()                                  # initialize pygame
screen = pygame.display.set_mode( (screen_width, screen_height) ) # create a window
pygame.display.set_caption("Endless Desent")      # set window title
floor_type_one()
running = True   # event loop


#Classes in use
player=Player(300,300)

enemy_1=Skelo(500,300)


#===================
# Colors

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 

#walls 



# OUTER BORDER
Walls(0, 0, 1344, 64)          # top
Walls(0, 0, 64, 768)           # left
Walls(0, 704, 1344, 64)        # bottom
Walls(1280, 0, 64, 768)        # right


# LEFT ROOM (L shape)
Walls(128, 128, 64, 192)
Walls(128, 320, 192, 64)

# LEFT MID HALL
Walls(0, 448, 256, 64)

# CENTER LEFT WALL
Walls(320, 512, 64, 256)

# CENTER BIG U SHAPE
Walls(512, 128, 64, 384)
Walls(512, 512, 256, 64)
Walls(768, 128, 64, 384)

# TOP CENTER DIVIDER
Walls(768, 0, 64, 256)

# SMALL TOP BLOCK
Walls(896, 128, 64, 64)

# RIGHT TOP U SHAPE
Walls(1024, 128, 64, 256)
Walls(1024, 384, 192, 64)
Walls(1216, 128, 64, 256)

# CENTER RIGHT BOX
Walls(896, 448, 192, 64)
Walls(896, 448, 64, 192)
Walls(1024, 512, 64, 128)

# RIGHT MID HALL
Walls(1152, 512, 192, 64)

# SMALL BOTTOM BLOCK
Walls(512, 640, 128, 64)

# BOTTOM RIGHT SMALL WALL
Walls(1152, 640, 64, 128)

# outer wall








ghosts=[]

clock = pygame.time.Clock()

while running:
  #game code goes here



  
  load_map(screen)

  







  if player.new_ghost is not None:
    ghosts.append(player.new_ghost)
    player.new_ghost = None


  attacking = False

  player.player_logic(screen, None)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        player.attack(screen, enemy_1)
        attacking= True

  

  for enemy in Enemy.all_enemies:
      enemy.enemy_logic(screen, player)

      if player.hitbox.colliderect(enemy.hitbox):
          player.take_damage(screen, enemy)

      if attacking:
          player.attack(screen, enemy)




    






  pygame.display.flip()
  clock.tick(60)

pygame.quit()  # teardown



