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
    stamina_regain = .02

    def __init__ (self ,x,y):
      self.hitbox=pygame.Rect(x, y, self.width, self.height)
      self.load_character_images()
  
    def player_logic(self,screen,other):
       self.all_draws(screen)


    def all_draws(self, screen):
       self.draw_health(screen)
       self.draw_character(screen)
       self.draw_stamina(screen)

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
      
  
    def draw_character(self,screen):
      screen.blit(self.standing,(self.hitbox.x, self.hitbox.y))

      


    def take_damage(self,screen,other):
      if self.hitbox.colliderect(other.hitbox):
         self.health-=0.1
      if self.health<=0:
        self.hitbox.height -=1
        pygame.draw.rect( screen, (blue), (self.hitbox))
      
      
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






    
           
         

       
    

  



