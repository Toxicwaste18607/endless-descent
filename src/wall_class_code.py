import pygame




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
    self.render_images()
    


  def render_images(self):
    self.wall_vert=pygame.image.load("src/assets/wall_type_one.png").convert_alpha()
    self.wall_vert=pygame.transform.scale(self.wall_vert,(self.width,self.height))
    self.wall_horl=pygame.image.load("src/assets/wall_type_two.png").convert_alpha()
    self.wall_horl=pygame.transform.scale(self.wall_horl,(self.width,self.height))


  def draw_wall(self,screen):
  
    screen.blit(self.wall_vert,self.x_and_y)


  

class Boarder_Walls(Walls):pass
  