import pygame
import time
from ghost import *

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)









class Player():
    width= 50
    height= 70
    max_health=100
    health=100
    health_regen=1
    attack_range = 5
    damage=20
    range_multi=2
    stamina = 100
    max_stamina=100
    stamina_regain = .02

    def __init__ (self ,x,y):
      
      self.hitbox=pygame.Rect(x, y, self.width, self.height)
      self.load_character_images()
  
    def player_logic(self,screen,other):
       self.all_draws(screen)


    def all_draws(self, screen):
      self.draw_stamina(screen)
      self.draw_health(screen)

      if self.health > 0:
        self.draw_character(screen)
      else:
        pass



    def draw_health(self,screen):
      
      health_bar_hight= (self.health / self.max_health) * 200
      health_bar_hight=abs(health_bar_hight)
        
    
        
      health_bar=(20,550,20,health_bar_hight)
      healthbar_cover=()
      pygame.draw.rect(screen,(red),(health_bar) )
    
    def draw_stamina(self,screen):
      x= 1350
      y=550
      width= 20
      if self.stamina>self.max_stamina:
        self.stamina=self.max_stamina
      stamina_bar_hight=(self.stamina/self.max_stamina) *200
      stamina_bar_hight=abs(stamina_bar_hight)
      
      stamina_bar=(x,y,width,stamina_bar_hight )
      pygame.draw.rect(screen,blue, stamina_bar )

    def load_character_images(self):
      self.standing=pygame.image.load("src/assets/Knight/standing.png")
      self.standing=pygame.transform.scale(self.standing,(self.width,self.height))

      self.walking_1=pygame.image.load("src/assets/Knight/walking_1.png")
      self.walking_1=pygame.transform.scale(self.walking_1, (self.width,self.height))

      self.walking_2=pygame.image.load("src/assets/Knight/walking_2.png")
      self.walking_2=pygame.transform.scale(self.walking_2, (self.width,self.height))

      
      self.walking_3=pygame.image.load("src/assets/Knight/walking_3.png")
      self.walking_3=pygame.transform.scale(self.walking_3, (self.width,self.height))

      self.att_1=pygame.image.load("src/assets/Knight/attack_1.png")
      self.att_1=pygame.transform.scale(self.att_1, (self.width,self.height))

      self.att_2=pygame.image.load("src/assets/Knight/attack_2.png")
      self.att_2=pygame.transform.scale(self.att_2, (self.width,self.height))

      self.att_3=pygame.image.load("src/assets/Knight/attack_3.png")
      self.att_3=pygame.transform.scale(self.att_3, (self.width,self.height))

      self.blc_1=pygame.image.load("src/assets/Knight/Blocking.png")
      self.blc_1=pygame.transform.scale(self.blc_1, (self.width,self.height))

      self.blc_2=pygame.image.load("src/assets/Knight/Blocking_1.png")
      self.blc_2=pygame.transform.scale(self.blc_2, (self.width,self.height))


      self.dth_1=pygame.image.load("src/assets/Knight/Death_1.png")
      self.dth_1=pygame.transform.scale(self.dth_1, (self.width,self.height))

      self.dth_2=pygame.image.load("src/assets/Knight/Death_2.png")
      self.dth_2=pygame.transform.scale(self.dth_2, (self.width,self.height))

      self.gh_1=pygame.image.load("src/assets/Knight/Ghost_1.png")
      self.gh_1=pygame.transform.scale(self.gh_1, (self.width,self.height))

      self.gh_2=pygame.image.load("src/assets/Knight/Ghost_2.png")
      self.gh_2=pygame.transform.scale(self.gh_2, (self.width,self.height))




    def draw_character(self,screen):
      screen.blit(self.standing,(self.hitbox.x, self.hitbox.y))

      


    def take_damage(self,screen,other):
      if self.hitbox.colliderect(other.hitbox):
        if self.health >0: 
          self.health-=1
        elif self.health<=0:
          self.player_death(screen)
          pass
      if not self.hitbox.colliderect(other.hitbox):  
        pass
    
    def player_death(self,screen):  
      ghost=Player_Ghost(self.hitbox)

      
      
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








    
           
         

       
    

  



