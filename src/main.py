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




h1= Walls(100, 100, 300, 50)
h2 = Walls(200, 200, 280, 50)
h3 = Walls(200, 380, 280, 50)
h4 = Walls(300, 530, 230, 50)
h5 = Walls(600, 330, 200, 50)
h6 = Walls(750, 450, 100, 50)
h7 = Walls(600, 600, 250, 50)
h8 = Walls(100, 650, 400, 50)

v1 = Walls(100, 150, 50, 150)
v2 = Walls(480, 250, 50, 130)
v3 = Walls(200, 430, 50, 100)
v4 = Walls(530, 430, 50, 100)
v5 = Walls(600, 100, 50, 230)
v6 = Walls(800, 150, 50, 180)
v7 = Walls(850, 200, 50, 250)
v8 = Walls(400, 580, 50, 70)





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



