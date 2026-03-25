import pygame


class Player():
    width= 50
    height= 80
    def __init__ (self ,x,y):
        self.x = x
        self.y = y
  
    def draw_charicater(self,screen):
      pygame.draw.rect( screen, (0,0,255), (self.x,self.y,self.width,self.height) )

    def player_area(self):
      player_rect= pygame.Rect(self.x, self.y,self.width,self.height)
      return player_rect
