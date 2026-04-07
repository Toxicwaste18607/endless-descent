#not in use


import pygame
from setting import *


def load_images():

  global floor_one
  floor_one=pygame.image.load("src/assets/walls_and_floors/floor_type_one.png").convert_alpha()#this loads the floor png 
  floor_one=pygame.transform.scale(floor_one, (screen_width,screen_height))


#standing=pygame.image.load("src/assets/Knight/standing.png")
#standing=pygame.transform.scale(standing,(player.width,player.height))

#self.walking_1=pygame.image.load()
#self.walking_1=pygame.transform.scale(self.walking_1, (self.width,self.height))

#self.walking_2=pygame.image.load()
#self.walking_2=pygame.transform.scale(self.walking_2, (self.width,self.height))


#self.walking_3=pygame.image.load()
#self.walking_3=pygame.transform.scale(self.walking_3, (self.width,self.height))

#self.
#self.

#self.
#self.

#self.
#self.

#self.
#self.

#self.
#self.



