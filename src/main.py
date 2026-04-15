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




top= Walls(0, 0, 1400, 70)        
bottom= Walls(0, 780, 1400, 40) 
left= Walls(0, 0, 80, 800)    
right=Walls(1320, 0, 80, 800)





# ===== INTERIOR WALLS =====

# top-left room shape
w1  = Walls(200, 30, 34, 239)
w2  = Walls(68, 266, 444, 26)

# big center divider
w3  = Walls(508, 0, 27, 350)

# upper middle platform
w4  = Walls(532, 90, 282, 21)

# upper right hanging wall
w5  = Walls(949, 0, 33, 141)

# upper right L-shape
w6  = Walls(1120, 59, 152, 24)
w7  = Walls(1253, 83, 32, 99)

# small top-right block
w8  = Walls(1161, 168, 33, 32)

# long middle platform
w9  = Walls(776, 265, 573, 21)

# small middle block
w10 = Walls(993, 392, 31, 28)

# bottom-left L-shape
w11 = Walls(36, 515, 276, 21)
w12 = Walls(275, 534, 33, 137)

# long bottom platform
w13 = Walls(465, 503, 794, 24)

# bottom-right support
w14 = Walls(1101, 527, 33, 201)

# bottom center supports
w15 = Walls(466, 566, 33, 162)
w16 = Walls(827, 583, 31, 145)













ghosts=[]

clock = pygame.time.Clock()

while running:
  #game code goes here

  


  load_map(screen)




  if player.new_ghost is not None:
    ghosts.append(player.new_ghost)
    player.new_ghost = None


  attacking = False

  load_map(screen)
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



