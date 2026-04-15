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




#For logic pathing

GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def get_asset_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(GAME_PATH, "assets", filename)



def floor_type_one():
  global floor_one
  floor_one=pygame.image.load("src/assets/walls_and_floors/floor_type_one.png").convert_alpha()#this loads the floor png 
  floor_one=pygame.transform.scale(floor_one, (screen_width,screen_height))
  

def load_map(screen):
    screen.blit(floor_one, (0, 0))

    for wall in Walls.all_walls:
        wall.draw_wall(screen)

#===================


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

enemy_1=Skelo(450,380)


#===================
# Colors

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 


walls = [
    Walls(0, 0, 64, 64),
    Walls(0, 64, 64, 64),
    Walls(0, 128, 64, 64),
    Walls(0, 192, 64, 64),
    Walls(0, 256, 64, 64),
    Walls(0, 320, 64, 64),
    Walls(0, 384, 64, 64),
    Walls(0, 448, 64, 64),
    Walls(0, 512, 64, 64),
    Walls(0, 576, 64, 64),
    Walls(0, 640, 64, 64),
    Walls(0, 704, 64, 64),
    Walls(0, 768, 64, 64),
    Walls(64, 0, 64, 64),
    Walls(64, 768, 64, 64),
    Walls(128, 0, 64, 64),
    Walls(128, 256, 64, 64),
    Walls(128, 768, 64, 64),
    Walls(192, 0, 64, 64),
    Walls(192, 256, 64, 64),
    Walls(192, 320, 64, 64),
    Walls(192, 384, 64, 64),
    Walls(192, 448, 64, 64),
    Walls(192, 576, 64, 64),
    Walls(192, 640, 64, 64),
    Walls(192, 768, 64, 64),
    Walls(256, 0, 64, 64),
    Walls(256, 64, 64, 64),
    Walls(256, 128, 64, 64),
    Walls(256, 448, 64, 64),
    Walls(256, 768, 64, 64),
    Walls(320, 0, 64, 64),
    Walls(320, 448, 64, 64),
    Walls(320, 768, 64, 64),
    Walls(384, 0, 64, 64),
    Walls(384, 256, 64, 64),
    Walls(384, 448, 64, 64),
    Walls(384, 512, 64, 64),
    Walls(384, 576, 64, 64),
    Walls(384, 704, 64, 64),
    Walls(384, 768, 64, 64),
    Walls(448, 0, 64, 64),
    Walls(448, 256, 64, 64),
    Walls(448, 576, 64, 64),
    Walls(448, 768, 64, 64),
    Walls(512, 0, 64, 64),
    Walls(512, 64, 64, 64),
    Walls(512, 128, 64, 64),
    Walls(512, 256, 64, 64),
    Walls(512, 576, 64, 64),
    Walls(512, 768, 64, 64),
    Walls(576, 0, 64, 64),
    Walls(576, 256, 64, 64),
    Walls(576, 320, 64, 64),
    Walls(576, 384, 64, 64),
    Walls(576, 448, 64, 64),
    Walls(576, 512, 64, 64),
    Walls(576, 576, 64, 64),
    Walls(576, 768, 64, 64),
    Walls(640, 0, 64, 64),
    Walls(640, 768, 64, 64),
    Walls(704, 0, 64, 64),
    Walls(704, 768, 64, 64),
    Walls(768, 0, 64, 64),
    Walls(768, 320, 64, 64),
    Walls(768, 448, 64, 64),
    Walls(768, 512, 64, 64),
    Walls(768, 576, 64, 64),
    Walls(768, 704, 64, 64),
    Walls(768, 768, 64, 64),
    Walls(832, 0, 64, 64),
    Walls(832, 64, 64, 64),
    Walls(832, 128, 64, 64),
    Walls(832, 192, 64, 64),
    Walls(832, 320, 64, 64),
    Walls(832, 576, 64, 64),
    Walls(832, 768, 64, 64),
    Walls(896, 0, 64, 64),
    Walls(896, 192, 64, 64),
    Walls(896, 320, 64, 64),
    Walls(896, 576, 64, 64),
    Walls(896, 768, 64, 64),
    Walls(960, 0, 64, 64),
    Walls(960, 192, 64, 64),
    Walls(960, 576, 64, 64),
    Walls(960, 768, 64, 64),
    Walls(1024, 0, 64, 64),
    Walls(1024, 192, 64, 64),
    Walls(1024, 768, 64, 64),
    Walls(1088, 0, 64, 64),
    Walls(1088, 320, 64, 64),
    Walls(1088, 384, 64, 64),
    Walls(1088, 448, 64, 64),
    Walls(1088, 512, 64, 64),
    Walls(1088, 576, 64, 64),
    Walls(1088, 704, 64, 64),
    Walls(1088, 768, 64, 64),
    Walls(1152, 0, 64, 64),
    Walls(1152, 64, 64, 64),
    Walls(1152, 128, 64, 64),
    Walls(1152, 192, 64, 64),
    Walls(1152, 448, 64, 64),
    Walls(1152, 768, 64, 64),
    Walls(1216, 0, 64, 64),
    Walls(1216, 448, 64, 64),
    Walls(1216, 768, 64, 64),
    Walls(1280, 0, 64, 64),
    Walls(1280, 768, 64, 64),
    Walls(1344, 0, 64, 64),
    Walls(1344, 64, 64, 64),
    Walls(1344, 128, 64, 64),
    Walls(1344, 192, 64, 64),
    Walls(1344, 256, 64, 64),
    Walls(1344, 320, 64, 64),
    Walls(1344, 384, 64, 64),
    Walls(1344, 448, 64, 64),
    Walls(1344, 512, 64, 64),
    Walls(1344, 576, 64, 64),
    Walls(1344, 640, 64, 64),
    Walls(1344, 704, 64, 64),
    Walls(1344, 768, 64, 64),
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



