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
# Basic colors used throughout the game
green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)

# keys for my self remove later 

# pygame.draw.rect( screen, (Color), (x ,y ,width, height) )


# Git commands reminder
# git add .
# git commit -m "progress update"
# git push


# ====================
# TO DO LIST (dev notes)
# ====================
# add ai attack
# fix players health and stamina to fall from the top not the bottom
# add lighting and fog of war
# add block
# add player death
# make proper borders
# make enemy only move in one direction at a time
# improve pathfinding
# make attack zone a circle
# add collision with enemy
# add player classes (assassin, knight, etc)
# add inventory
# add loot and gear
# add enemy classes (goblin, bats, etc)
# add graphics
# add player ghost
# clean up graphics
# make rooms and procedural generation
# add final boss
# move movement fully into player class
# add menus


#====================
# Pathing / asset setup
#====================

# Gets the folder path of this file
GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def get_asset_path(filename: str) -> str:
    """
    Returns full path to an asset file.
    Helps avoid hardcoding paths everywhere.
    """
    return os.path.join(GAME_PATH, "assets", filename)


#====================
# Floor setup
#====================

def floor_type_one():
  """
  Loads and scales the floor texture to fill the entire screen.
  """
  global floor_one

  # Load floor image with transparency
  floor_one = pygame.image.load("src/assets/walls_and_floors/floor_type_one.png").convert_alpha()

  # Scale it to match screen size
  floor_one = pygame.transform.scale(floor_one, (screen_width, screen_height))
  

def load_map(screen):
    """
    Draws the floor and all walls.
    """
    # Draw floor first (background)
    screen.blit(floor_one, (0, 0))

    # Draw every wall in the global wall list
    for wall in Walls.all_walls:
        wall.draw_wall(screen)


#====================
# GAME SETUP
#====================

pygame.init()  # initialize pygame

# Create window
screen = pygame.display.set_mode((screen_width, screen_height))

# Window title
pygame.display.set_caption("Endless Desent")

# Load floor
floor_type_one()

running = True   # controls game loop


#====================
# OBJECT CREATION
#====================

# Create player
player = Player(300, 300)

# Create one enemy (Skelo class)
enemy_1 = Skelo(450, 380)


#====================
# Colors (duplicate section)
#====================

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 


#====================
# WALL MAP
#====================

# Large list of walls forming the dungeon layout
walls = [
    # Each wall = (x, y, width, height)
    # This creates a grid-based maze structure

    Walls(0, 0, 64, 64),
    Walls(0, 64, 64, 64),
    Walls(0, 128, 64, 64),
    # ... continues same pattern ...
    Walls(1344, 768, 64, 64),
]


#====================
# GHOST STORAGE
#====================

# List to store player ghost instances after death
ghosts = []


#====================
# CLOCK (FPS control)
#====================

clock = pygame.time.Clock()


#====================
# MAIN GAME LOOP
#====================

while running:
  # Game code runs every frame here

  # Draw map (floor + walls)
  load_map(screen)


  #====================
  # GHOST HANDLING
  #====================

  # If player created a new ghost (on death)
  if player.new_ghost is not None:
    ghosts.append(player.new_ghost)   # store ghost
    player.new_ghost = None           # reset so it doesn't duplicate


  attacking = False  # tracks if player is attacking this frame


  # Run player logic (movement, drawing, etc)
  player.player_logic(screen, None)


  #====================
  # EVENT HANDLING
  #====================

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False  # close game

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        attacking = True  # player pressed attack


  #====================
  # ENEMY LOGIC
  #====================

  for enemy in Enemy.all_enemies:
      # Run enemy AI
      enemy.enemy_logic(screen, player)

      # If player touches enemy → player takes damage
      if player.hitbox.colliderect(enemy.hitbox):
          player.take_damage(screen, enemy)

      # If attacking → damage enemy
      if attacking:
          player.attack(screen, enemy)


  #====================
  # SCREEN UPDATE
  #====================

  pygame.display.flip()  # update display

  clock.tick(60)  # limit to 60 FPS


#====================
# CLEANUP
#====================

pygame.quit()  # close pygame properly