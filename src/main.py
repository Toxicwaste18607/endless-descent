#IMPORTS

import os
import pygame
from player import Player
from setting import *
from key_move import *
from enemy_class import *

#====================

#keys for my self remove later 

# pygame.draw.rect( screen, (Color), (x ,y ,width, height) )


#git add .
#git commit -m "progress update"
#git push


# to do list 
# make a better path finding 
#make enemy only move in one direction at a time
#add in the 


#===================

#For logic pathing

GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def get_asset_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(GAME_PATH, "assets", filename)

#============================

#Classes in use
player=Player(50,50)

enemy_1=Enemy(70,90)

#===================
# Colors

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 

#walls 




top= Walls(0, 0, 1000, 40)        
bottom= Walls(0, 780, 1000, 20) 
left= Walls(0, 0, 20, 800),         
right=Walls(980, 0, 20, 800), 
a= Walls(100, 100, 300, 20),
b= Walls(100, 100, 20, 200),

c= Walls(200, 200, 300, 20),
d=Walls(480, 200, 20, 200),

q=Walls(200, 380, 300, 20),
w=Walls(200, 380, 20, 150),

g=Walls(300, 530, 250, 20),
o=Walls(530, 450, 20, 100),

p=Walls(600, 100, 20, 250),
m=Walls(600, 330, 200, 20),

n=Walls(700, 150, 20, 250),
v=Walls(750, 450, 180, 20),

aa=Walls(850, 200, 20, 270),
x=Walls(600, 600, 250, 20),

z=Walls(100, 650, 400, 20),
y=Walls(400, 500, 20, 170),

#==========================
    
   
    
    



  

#=================

#Game Code

pygame.init()                                  # initialize pygame
screen = pygame.display.set_mode( (screen_width, screen_height) ) # create a window
pygame.display.set_caption("Endless Desent")      # set window title

running = True   # event loop

clock = pygame.time.Clock()

while running:
  #game code goes here

  screen.fill((black))
  for wall in Walls.all_walls:
    wall.draw_wall(screen)

  

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  
  player.all_draws(screen)
  enemy_1.draw_character(screen)
  enemy_1.search(player)

  movement(player)  

  pygame.display.flip()
  clock.tick(60)

pygame.quit()  # teardown



