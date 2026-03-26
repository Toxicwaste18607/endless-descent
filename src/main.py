#IMPORTS

import os
import pygame
from player import Player
from setting import *
from key_move import *
from temp_enemy import *

#====================

#keys for my self remove later 

# pygame.draw.rect( screen, (Color), (x ,y ,width, height) )


#git add .
#git commit -m "progress update"
#git push
#===================

#For logic pathing

GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def get_asset_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(GAME_PATH, "assets", filename)

#============================

#Classes in use
player=Player(25,25)

enemy_1=Enemy(60,90)

#===================
# Colors



#walls 




top= Walls(0, 0, 1000, 20)        
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

  screen.fill((0,0,0))

  

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  
  player.draw_charicater(screen)
  enemy_1.draw_charicater(screen)
  enemy_1.move()


  for wall in Walls.all_walls:
    wall.draw_wall(screen)

  movement(player)  

  pygame.display.flip()
  clock.tick(60)

pygame.quit()  # teardown



