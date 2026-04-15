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






# Outer border
top_border = Walls(0, 0, 1600, 50)
bottom_border = Walls(0, 850, 1600, 50)
left_border = Walls(0, 0, 50, 900)
right_border = Walls(1550, 0, 50, 900)

# Top-left room "L"
wall_1 = Walls(140, 170, 40, 190)   # vertical
wall_2 = Walls(140, 320, 160, 40)   # horizontal

# Far-left middle wall
wall_3 = Walls(0, 540, 280, 40)     # horizontal from left side inward

# Bottom-left vertical
wall_4 = Walls(310, 540, 40, 320)   # vertical

# Center large U shape
wall_5 = Walls(520, 190, 40, 390)   # vertical
wall_6 = Walls(520, 540, 250, 40)   # bottom horizontal
wall_7 = Walls(730, 50, 40, 530)    # right vertical

# Divider between left and middle-top sections
wall_8 = Walls(780, 50, 40, 530)    # vertical divider

# Small top-middle block
wall_9 = Walls(960, 160, 50, 110)

# Right-top upside-down U / corner shape
wall_10 = Walls(1120, 360, 180, 40) # bottom horizontal
wall_11 = Walls(1260, 230, 40, 170) # right vertical

# Divider between middle and right sections
wall_12 = Walls(1120, 50, 40, 350)  # vertical divider

# Middle-bottom maze shape
wall_13 = Walls(880, 510, 250, 40)  # top horizontal
wall_14 = Walls(880, 510, 40, 270)  # left vertical
wall_15 = Walls(880, 740, 120, 40)  # bottom horizontal
wall_16 = Walls(1080, 550, 40, 160) # right vertical inner

# Bottom-center small block
wall_17 = Walls(560, 740, 90, 40)

# Right-middle shape
wall_18 = Walls(1310, 540, 240, 40) # horizontal
wall_19 = Walls(1310, 540, 40, 150) # left vertical

# Bottom-right small vertical
wall_20 = Walls(1360, 740, 40, 120)










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



