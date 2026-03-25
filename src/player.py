import pygame


class Player():
  width= 50
  height= 80
  def __init__ (self ,x,y):
    self.x = x
    self.y = y
  
  def draw_charicater(self,screen):
      pygame.draw.rect( screen, (0,0,255), (player.x,player.y,player.width, player.height) )

    
player=Player(200, 200)
