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






walls = [
    # OUTER BORDER
    Walls(0, 0, 1400, 20),
    Walls(0, 780, 1400, 20),
    Walls(0, 0, 20, 800),
    Walls(1380, 0, 20, 800),

    # LEFT ROOM (L shape)
    Walls(100, 100, 20, 200),
    Walls(100, 280, 120, 20),

    # LEFT MID
    Walls(80, 500, 200, 20),
    Walls(250, 520, 20, 250),

    # CENTER LEFT (U shape)
    Walls(450, 100, 20, 300),
    Walls(450, 380, 200, 20),
    Walls(650, 100, 20, 300),

    # CENTER SMALL BLOCK
    Walls(600, 600, 80, 20),

    # CENTER DIVIDER
    Walls(720, 0, 20, 500),

    # RIGHT TOP SMALL
    Walls(850, 100, 60, 20),

    # RIGHT MID (C shape)
    Walls(820, 400, 200, 20),
    Walls(820, 400, 20, 200),
    Walls(820, 580, 200, 20),

    # RIGHT TOP ROOM
    Walls(1050, 200, 20, 200),
    Walls(1050, 380, 120, 20),

    # RIGHT LOWER
    Walls(1100, 550, 200, 20),
    Walls(1300, 550, 20, 150),

    # EXIT GAPS (like your red/blue)
    # leave space manually — no walls here
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



