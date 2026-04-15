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
  floor_one=pygame.image.load("src/assets/walls_and_floors/floor_type_one.png").convert_alpha()#this loads the floor png 
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




wall_thickness = 50

# borders
top_border = Walls(40, 40, 1520, wall_thickness)
bottom_border = Walls(40, 930, 1520, wall_thickness)
left_border = Walls(40, 40, wall_thickness, 890)
right_border = Walls(1560, 40, wall_thickness, 890)

# upper left room
h1 = Walls(130, 360, 300, wall_thickness)
v1 = Walls(430, 80, wall_thickness, 280)

# upper middle room
h2 = Walls(680, 430, 360, wall_thickness)
v2 = Walls(680, 180, wall_thickness, 250)
v3 = Walls(1030, 180, wall_thickness, 250)

# upper right
v4 = Walls(1210, 170, wall_thickness, 470)
v5 = Walls(1470, 160, wall_thickness, 330)
h3 = Walls(1470, 520, 130, wall_thickness)

# lower left
h4 = Walls(180, 700, 320, wall_thickness)
v6 = Walls(500, 700, wall_thickness, 250)
v7 = Walls(310, 850, wall_thickness, 120)

# middle lower
v8 = Walls(950, 640, wall_thickness, 170)
h5 = Walls(950, 640, 300, wall_thickness)

# lower right
h6 = Walls(1010, 820, 260, wall_thickness)
v9 = Walls(1270, 520, wall_thickness, 300)
v10 = Walls(1450, 650, wall_thickness, 280)










ghosts=[]

clock = pygame.time.Clock()

while running:
  #game code goes here



    
  tile_w = 70
  tile_h = 50

  for x in range(0, 1400, tile_w):
      pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, 800))

  for y in range(0, 800, tile_h):
      pygame.draw.line(screen, (50, 50, 50), (0, y), (1400, y))
  


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



