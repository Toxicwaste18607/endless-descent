import pygame
green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)




class Walls():
  all_walls = []
  def __init__(self,x,y,width,height):
    self.x=x
    self.y=y
    self.height= height
    self.width= width
    self.x_and_y=(self.x ,self.y)
    self.all_walls.append(self)
    self.wall_hitbox=pygame.Rect(self.x, self.y,self.width,self.height)




  def draw_wall(self,screen):
    pygame.draw.rect(screen, white ,self.x, self.y,self.width,self.height)


  

class Boarder_Walls(Walls):pass
  