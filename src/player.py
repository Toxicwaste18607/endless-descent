import pygame
import time

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)









class Player():
    width= 25
    height= 50
    max_health=100
    health=100
    health_regen=1
    attack_range = 5
    damage=20
    range_multi=2
    stamina = 100
    max_stamina=100
    stamina_regain = 2

    def __init__ (self ,x,y):
      self.x = x
      self.y = y
      self.hitbox=pygame.Rect(x, y, self.width, self.height)
  
    def player_logic(self,screen,other):
       self.all_draws(screen)


    def all_draws(self, screen):
       self.draw_health(screen)
       self.draw_character(screen)

    def draw_health(self,screen):
      if self.health > 0:
        health_bar_hight= (self.health / self.max_health) * 200
        health_bar_hight=abs(health_bar_hight)
        
      else:
         health_bar_hight = 0
        
      health_bar=(20,550,20,health_bar_hight)
      healthbar_cover=()
      pygame.draw.rect(screen,(red),(health_bar) )
    
    def draw_stamina(self,screen):
      stamina_bar_hight=(self.stamina/self.max_stamina) *200
      stamina_bar_hight=abs(stamina_bar_hight)
      
      pygame.draw.rect(screen,)

         
  
    def draw_character(self,screen):
      pygame.draw.rect( screen, (blue), (self.hitbox ))


    def take_damage(self,other):
      if self.hitbox.colliderect(other.hitbox):
         self.health-=0.1
      
      
    def  sprint(self):
      
      if self.stamina > 0:
       self.stamina-=.2
       return True
        
      else:
       pass

      

    def attack(self,screen,other):
      attack_box=(self.hitbox.x-self.attack_range,  self.hitbox.y -self.attack_range,
                  self.hitbox.width +(self.attack_range*self.range_multi),
                  self.hitbox.height+(self.attack_range*self.range_multi))
      attack_box=pygame.Rect(attack_box)
      pygame.draw.rect(screen,green,attack_box)
      if attack_box.colliderect(other.hitbox):
          other.take_damage(self)






    
           
         

       
    

  



