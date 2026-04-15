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

def W(col, row, w, h):
    return Walls(col * 70, row * 50, w * 70, h * 50)

# outer walls
top = Walls(0, 0, 1400, 70)
bottom = Walls(0, 780, 1400, 40)
left = Walls(0, 0, 80, 800)
right = Walls(1320, 0, 80, 800)

# ===== INNER WALLS =====

# small top-left block
w1  = W(1, 3, 1, 1)

# left big L
w2  = W(1, 5, 4, 1)
w3  = W(4, 5, 1, 7)

# top pillars
w4  = W(3, 1, 1, 3)
w5  = W(9, 1, 1, 3)
w6  = W(14, 1, 1, 3)

# top-center U
w7  = W(10, 2, 4, 1)

# top-right tall wall
w8  = W(17, 1, 1, 5)

# far-right top shape
w9  = W(19, 1, 1, 4)
w10 = W(18, 5, 2, 1)

# small center pillar
w11 = W(9, 5, 1, 2)

# middle-right L
w12 = W(12, 6, 5, 1)
w13 = W(12, 6, 1, 3)

# small right-middle block
w14 = W(18, 6, 2, 1)

# lower center small pillar
w15 = W(12, 11, 1, 2)

# bottom-right big L
w16 = W(15, 11, 5, 1)
w17 = W(19, 6, 1, 6)











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



