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
# OUTER WALLS
top_wall = Walls(0, 0, 1600, 40)
bottom_wall = Walls(0, 860, 1600, 40)
left_wall = Walls(0, 0, 40, 900)
right_wall = Walls(1560, 0, 40, 900)

# LEFT TOP L
l1_vertical = Walls(150, 190, 40, 170)
l1_horizontal = Walls(150, 330, 150, 40)

# LEFT MID HALL
left_mid_horizontal = Walls(0, 570, 280, 40)

# LEFT LOWER VERTICAL
left_lower_vertical = Walls(340, 570, 40, 330)

# CENTER LEFT U
center_u_left = Walls(540, 190, 40, 390)
center_u_bottom = Walls(540, 550, 240, 40)
center_u_right = Walls(740, 190, 40, 390)

# CENTER TALL SINGLE WALL
center_single = Walls(600, 220, 40, 430)

# CENTER DIVIDER WALLS
divider_left = Walls(840, 120, 40, 580)
divider_right = Walls(890, 120, 40, 580)

# SMALL TOP MIDDLE BLOCK
small_top_block = Walls(950, 150, 50, 80)

# RIGHT TOP U
right_u_left = Walls(1110, 220, 40, 170)
right_u_bottom = Walls(1110, 360, 180, 40)
right_u_right = Walls(1250, 260, 40, 220)

# SMALL CENTER RIGHT BLOCK
small_mid_block = Walls(1090, 220, 50, 120)

# RIGHT SIDE LOWER LAYOUT
right_mid_horizontal = Walls(1310, 560, 240, 40)
right_mid_left = Walls(1310, 560, 40, 150)
right_mid_inner = Walls(1310, 680, 40, 150)

# LOWER CENTER MAZE
lower_center_left = Walls(900, 530, 40, 250)
lower_center_top = Walls(900, 530, 210, 40)
lower_center_right = Walls(1070, 530, 40, 180)
lower_center_bottom = Walls(900, 740, 110, 40)

# LOWER RIGHT LONG HORIZONTAL
lower_right_horizontal = Walls(1020, 620, 260, 40)

# LOWER RIGHT VERTICAL
lower_right_vertical = Walls(1230, 620, 40, 220)

# SMALL BOTTOM CENTER BLOCK
small_bottom_block = Walls(580, 760, 80, 40)

# FAR RIGHT LOWER SMALL VERTICAL
far_right_small = Walls(1360, 760, 40, 120)







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



