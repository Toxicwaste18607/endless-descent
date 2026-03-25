import pygame




class Walls():
  all_walls = []
  def __init__(self,x,y,width,height):
    self.x=x
    self.y=y
    self.height= height
    self.width= width
    self.all_walls.append(self)
    self.wall_hitbox=pygame.Rect(self.x, self.y,self.width,self.height)



  def draw_wall(self,screen):
    pygame.draw.rect(screen,(255,255,255), (self.x,self.y,self.width,self.height))


  

class Boarder_Walls(Walls):pass
  