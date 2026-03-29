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
#add in menus

def floor_type_one():
  global floor_one
  floor_one=pygame.image.load("src/assets/walls_and_floors/floor_type_one.png").convert_alpha()
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
player=Player(250,250)

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
left= Walls(0, 0, 20, 800)    
right=Walls(980, 0, 20, 800)
a= Walls(100, 100, 300, 20)
b= Walls(100, 100, 20, 200)




h1 = Walls(100, 100, 300, 20)
h2 = Walls(200, 200, 300, 20)
h3 = Walls(200, 380, 300, 20)
h4 = Walls(300, 530, 250, 20)
h5 = Walls(600, 330, 200, 20)
h6 = Walls(750, 450, 180, 20)
h7 = Walls(600, 600, 250, 20)
h8 = Walls(100, 650, 400, 20)

v1 = Walls(100, 100, 20, 200)
v2 = Walls(480, 200, 20, 200)
v3 = Walls(200, 380, 20, 150)
v4 = Walls(530, 450, 20, 100)
v5 = Walls(600, 100, 20, 250)
v6 = Walls(700, 150, 20, 250)
v7 = Walls(850, 200, 20, 270)
v8 = Walls(400, 500, 20, 170)





clock = pygame.time.Clock()

while running:
  #game code goes here
  
  

  

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        player.attack(screen, enemy_1)
  load_map(screen)


  enemy_1.enemy_logic(screen , player)
  player.player_logic(screen,enemy_1)



  movement(player)  

  pygame.display.flip()
  clock.tick(60)

pygame.quit()  # teardown



