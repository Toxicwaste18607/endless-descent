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




# outer walls
top = Walls(0, 0, 1400, 70)
bottom = Walls(0, 780, 1400, 40)
left = Walls(0, 0, 80, 800)
right = Walls(1320, 0, 80, 800)

# ===== INTERIOR WALLS =====

# upper-left
w1  = Walls(232, 86, 24, 216)
w2  = Walls(109, 303, 422, 20)

# center divider + upper middle shelf
w3  = Walls(544, 45, 24, 330)
w4  = Walls(555, 145, 315, 19)

# upper-right
w5  = Walls(975, 44, 24, 125)
w6  = Walls(1188, 106, 124, 20)
w7  = Walls(1288, 106, 24, 96)
w8  = Walls(1166, 205, 24, 22)

# mid-right long shelf + middle small block
w9  = Walls(792, 304, 536, 20)
w10 = Walls(1003, 420, 24, 22)

# lower-left
w11 = Walls(82, 547, 268, 20)
w12 = Walls(312, 548, 24, 149)

# long lower shelf
w13 = Walls(494, 525, 720, 20)

# lower supports
w14 = Walls(1118, 548, 24, 188)
w15 = Walls(500, 594, 24, 145)
w16 = Walls(844, 617, 24, 121)










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



