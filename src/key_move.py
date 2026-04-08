import pygame
from setting import *
from wall_class_code import *
from enemy_class import *




def collision(next_move):
  for wall in Walls.all_walls:
    if next_move.colliderect(wall.wall_hitbox):
      return True
  return None
    #if next_move.colliderect():pass




#test