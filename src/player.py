import pygame

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)


#to do list
#add in stamina
#add in attack
#add in colliosn with enemy






class Player():
    width= 25
    height= 50
    max_health=100
    health=100
    health_regen=1
    attack_range = 5
    damage=20
    range_multi=2

    def __init__ (self ,x,y):
      self.x = x
      self.y = y
      self.hitbox=pygame.Rect(x, y, self.width, self.height)
  
    def player_logic(self,screen,other):
       self.all_draws(screen)
       self.attack(screen,other)


    def all_draws(self, screen):
       self.draw_health(screen)
       self.draw_character(screen)

    def draw_health(self,screen):
      if self.health > 0:
        health_bar_width= (self.health / self.max_health) * 200
        health_bar_width=abs(health_bar_width)
        
      else:
         health_bar_width = 0
        
      health_bar=(20,10,health_bar_width,20)
      healthbar_cover=()
      pygame.draw.rect(screen,(red),(health_bar) )
         
  
    def draw_character(self,screen):
      pygame.draw.rect( screen, (blue), (self.hitbox ))


    def take_damage(self,other):
      if self.hitbox.colliderect(other.hitbox):
         self.health-=0.1
       

      pass

    def attack(self,screen,other):
      keys=pygame.key.get_pressed()
      
      if keys[pygame.K_SPACE]:
        attack_box=(self.hitbox.x+self.attack_range,  self.hitbox.y +self.attack_range,
                    self.hitbox.width +(self.attack_range*self.range_multi),
                    self.hitbox.height+(self.attack_range*self.range_multi))
        attack_box=pygame.Rect(attack_box)
        pygame.draw.rect(screen,green,attack_box)
        if attack_box.colliderect(other.hitbox):
           other.take_damage(self)
           
         

       
    

  



