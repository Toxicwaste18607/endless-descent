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


w1  = Walls(1, 5, 4, 1)   # left middle horizontal
w2  = Walls(4, 5, 1, 7)   # left middle vertical down

w3  = Walls(3, 1, 1, 3)   # upper-left vertical
w4  = Walls(1, 3, 1, 1)   # small upper-left horizontal

w5  = Walls(8, 2, 4, 1)   # upper-middle horizontal
w6  = Walls(8, 1, 1, 3)   # upper-middle left vertical
w7  = Walls(12, 1, 1, 3)  # upper-middle right vertical

w8  = Walls(15, 1, 1, 6)  # upper-right tall vertical
w9  = Walls(11, 6, 5, 1)  # middle-right horizontal
w10 = Walls(11, 6, 1, 3)  # middle-right vertical down

w11 = Walls(18, 1, 1, 4)  # far-right upper vertical
w12 = Walls(18, 5, 2, 1)  # far-right small horizontal

w13 = Walls(17, 6, 2, 1)  # right-center small horizontal
w14 = Walls(18, 6, 1, 6)  # right-center vertical down

w15 = Walls(14, 11, 4, 1) # bottom-right horizontal
w16 = Walls(14, 11, 1, 1) # bottom-right little left nub

w17 = Walls(8, 5, 1, 2)   # small center pillar
w18 = Walls(11, 11, 1, 2) # bottom-center small pillar











ghosts=[]

clock = pygame.time.Clock()

while running:
  #game code goes here

  load_map(screen)


    
  tile_w = 70
  tile_h = 50

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



