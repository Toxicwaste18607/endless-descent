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

enemy_1=Skelo(500,300)


#===================
# Colors

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 


TILE = 64

# paste your raw coordinates here
raw = [
(0,0),(0,64),(0,128),(0,192),(0,256),(0,320),(0,384),(0,448),(0,512),(0,576),(0,640),(0,704),(0,768),
(64,0),(64,768),
(128,0),(128,256),(128,768),
(192,0),(192,256),(192,320),(192,384),(192,448),(192,576),(192,640),(192,768),
(256,0),(256,64),(256,128),(256,448),(256,768),
(320,0),(320,448),(320,768),
(384,0),(384,256),(384,448),(384,512),(384,576),(384,704),(384,768),
(448,0),(448,256),(448,576),(448,768),
(512,0),(512,64),(512,128),(512,256),(512,576),(512,768),
(576,0),(576,256),(576,320),(576,384),(576,448),(576,512),(576,576),(576,768),
(640,0),(640,768),
(704,0),(704,768),
(768,0),(768,320),(768,448),(768,512),(768,576),(768,704),(768,768),
(832,0),(832,64),(832,128),(832,192),(832,320),(832,576),(832,768),
(896,0),(896,192),(896,320),(896,576),(896,768),
(960,0),(960,192),(960,576),(960,768),
(1024,0),(1024,192),(1024,768),
(1088,0),(1088,320),(1088,384),(1088,448),(1088,512),(1088,576),(1088,704),(1088,768),
(1152,0),(1152,64),(1152,128),(1152,192),(1152,448),(1152,768),
(1216,0),(1216,448),(1216,768),
(1280,0),(1280,768),
(1344,0),(1344,64),(1344,128),(1344,192),(1344,256),(1344,320),(1344,384),(1344,448),(1344,512),(1344,576),(1344,640),(1344,704),(1344,768)
]

tiles = set(raw)
visited = set()
walls = []

for (x, y) in tiles:
    if (x, y) in visited:
        continue

    # grow width
    w = TILE
    while (x + w, y) in tiles and (x + w, y) not in visited:
        w += TILE

    # grow height
    h = TILE
    done = False
    while not done:
        for dx in range(0, w, TILE):
            if (x + dx, y + h) not in tiles or (x + dx, y + h) in visited:
                done = True
                break
        if not done:
            h += TILE

    # mark visited
    for dx in range(0, w, TILE):
        for dy in range(0, h, TILE):
            visited.add((x + dx, y + dy))

    walls.append((x, y, w, h))


# PRINT FINAL WALLS
print("\nwalls = [")
for x, y, w, h in walls:
    print(f"    Walls({x}, {y}, {w}, {h}),")
print("]")

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



