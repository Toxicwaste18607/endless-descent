#IMPORTS

import os
import pygame
import random
from player import Player
from setting import *
from enemy_class import *
from ghost import *







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

enemy_1=Enemy(500,300)


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



#Top left
h1 = Walls(100, 100, 320, 50)
v1 = Walls(100, 100, 50, 220)

# UPPER MIDDLE ROOM
h2 = Walls(250, 220, 320, 50)
v2 = Walls(570, 220, 50, 220)
h3 = Walls(250, 440, 320, 50)
v3 = Walls(250, 440, 50, 170)

# CENTER LOWER CONNECTION
h4 = Walls(350, 610, 260, 50)
v4 = Walls(560, 490, 50, 120)

# BOTTOM LEFT
#h5 

# RIGHT MAIN STRUCTURE
v5 = Walls(700, 100, 50, 300)
h6 = Walls(700, 400, 280, 50)
v6 = Walls(930, 180, 50, 270)
v7 = Walls(830, 220, 50, 180)

# RIGHT SIDE EXTRA PATHS
h7 = Walls(860, 560, 150, 50)
#h8 

# CENTER SMALL LINK
#v8 




ghosts=[]

clock = pygame.time.Clock()

while running:
  #game code goes here

  


  load_map(screen)

  enemy_1.enemy_logic(screen , player)
  player.player_logic(screen,enemy_1)


  if player.health <= 0:
     print ("dead")
     bob= (Player_ghost(player.hitbox.copy()))
     ghosts.append(bob)

  print (ghosts)
  

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        player.attack(screen, enemy_1)




  




  pygame.display.flip()
  clock.tick(60)

pygame.quit()  # teardown



