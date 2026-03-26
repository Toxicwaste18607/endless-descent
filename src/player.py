import pygame







class Player():
    width= 25
    height= 50
    def __init__ (self ,x,y):
        self.x = x
        self.y = y
        self.hitbox=pygame.Rect(x, y, self.width, self.height)
        
  
  
    def draw_character(self,screen):
      pygame.draw.rect( screen, (0,0,255), (self.hitbox ))

    def player_agro(self,other):
      
      pass

    
