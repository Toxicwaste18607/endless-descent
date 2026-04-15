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




TILE = 64

walls = [
    # =========================
    # OUTER BORDER
    # =========================
    Walls(0, 0, 21*TILE, TILE),
    Walls(0, 11*TILE, 21*TILE, TILE),
    Walls(0, 0, TILE, 12*TILE),
    Walls(20*TILE, 0, TILE, 12*TILE),

    # =========================
    # LEFT TOP (L)
    # =========================
    Walls(2*TILE, 2*TILE, TILE, 3*TILE),
    Walls(2*TILE, 4*TILE, 2*TILE, TILE),

    # LEFT MID HALL
    Walls(1*TILE, 7*TILE, 3*TILE, TILE),

    # LEFT BOTTOM VERTICAL
    Walls(4*TILE, 8*TILE, TILE, 3*TILE),

    # =========================
    # CENTER LEFT (U SHAPE)
    # =========================
    Walls(7*TILE, 2*TILE, TILE, 5*TILE),
    Walls(7*TILE, 7*TILE, 3*TILE, TILE),
    Walls(9*TILE, 2*TILE, TILE, 5*TILE),

    # CENTER DIVIDER
    Walls(10*TILE, 0, TILE, 8*TILE),

    # SMALL CENTER BLOCK
    Walls(8*TILE, 9*TILE, TILE, TILE),

    # =========================
    # TOP MID SMALL
    # =========================
    Walls(12*TILE, 2*TILE, TILE, TILE),
    Walls(12*TILE, 1*TILE, TILE, TILE),

    # =========================
    # RIGHT CENTER (C SHAPE)
    # =========================
    Walls(12*TILE, 7*TILE, 3*TILE, TILE),
    Walls(12*TILE, 7*TILE, TILE, 3*TILE),
    Walls(12*TILE, 9*TILE, 3*TILE, TILE),

    # INNER BOX RIGHT
    Walls(13*TILE, 7*TILE, 2*TILE, TILE),
    Walls(13*TILE, 7*TILE, TILE, 2*TILE),
    Walls(13*TILE, 8*TILE, 2*TILE, TILE),

    # =========================
    # RIGHT TOP ROOM
    # =========================
    Walls(16*TILE, 3*TILE, TILE, 3*TILE),
    Walls(16*TILE, 5*TILE, 2*TILE, TILE),

    # RIGHT MID WALL
    Walls(15*TILE, 6*TILE, 1*TILE, 2*TILE),

    # =========================
    # RIGHT LOWER PATH
    # =========================
    Walls(17*TILE, 7*TILE, 3*TILE, TILE),
    Walls(19*TILE, 7*TILE, TILE, 3*TILE),

    # BOTTOM RIGHT POST
    Walls(18*TILE, 9*TILE, TILE, 2*TILE),
]





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



