import pygame

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)





class Player():
    width= 25
    height= 50
    def __init__ (self ,x,y):
        self.x = x
        self.y = y
        self.hitbox=pygame.Rect(x, y, self.width, self.height)
        self.max_health=100
        self.current_health=100
        self.health_regen=1
        
    def all_draws(self, screen):
       self.draw_character()

    def draw_health(self,screen):
       healthbar=()
       healthbar_cover=()
       pygame.draw.rect(screen,())
  
    def draw_character(self,screen):
      pygame.draw.rect( screen, (blue), (self.hitbox ))

    def player_agro(self,other):
      
      pass

    
