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





# borders
'''top= Walls(0, 0, 1400, 70)        
left= Walls(0, 0, 80, 800)    
right=Walls(1320, 0, 80, 80)'''


tile = 64

# outer wall
wall_1 = Walls(0, 0, tile, 768)

# top-left section
wall_2 = Walls(64, 256, 448, tile)
wall_3 = Walls(192, 64, tile, 192)

# center-left section
wall_4 = Walls(512, 0, tile, 384)
wall_5 = Walls(512, 64, 320, tile)

# upper-right section
wall_6 = Walls(960, 0, tile, 128)
wall_7 = Walls(1152, 64, 128, tile)
wall_8 = Walls(1280, 64, tile, 128)

# middle-right long wall
wall_9 = Walls(768, 256, 640, tile)

# small blocks
wall_10 = Walls(1088, 192, tile, tile)
wall_11 = Walls(960, 384, tile, tile)

# bottom-left section
wall_12 = Walls(0, 576, 320, tile)
wall_13 = Walls(256, 576, tile, 192)

# bottom-middle / bottom-right section
wall_14 = Walls(448, 576, 832, tile)
wall_15 = Walls(1088, 576, tile, 192)

# lower small verticals
wall_16 = Walls(448, 640, tile, 128)
wall_17 = Walls(832, 640, tile, 128)







ghosts=[]

clock = pygame.time.Clock()

while running:
  #game code goes here



  
  load_map(screen)

  tile_w = 64
  tile_h = 64

  for x in range(0, 1400, tile_w):
      pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, 800))

  for y in range(0, 800, tile_h):
      pygame.draw.line(screen, (50, 50, 50), (0, y), (1400, y))
  







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



