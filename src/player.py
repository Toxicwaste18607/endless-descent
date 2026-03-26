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
        self.health=100
        self.health_regen=1
        
    def all_draws(self, screen):
       self.draw_health(screen)
       self.draw_character(screen)

    def draw_health(self,screen):
       #health_bar=(20,10,health_bar_width,20)
       health_bar_width= (self.health / self.max_health) * 200
       healthbar_cover=()
       print (health_bar_width)
       #pygame.draw.rect(screen,(red),(health_bar) )
  
    def draw_character(self,screen):
      pygame.draw.rect( screen, (blue), (self.hitbox ))

    def player_agro(self,other):
      
      pass

p= Player(5,5)

p.draw_health(4)
