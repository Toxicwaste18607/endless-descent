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
    def __init__ (self ,x,y):
        self.x = x
        self.y = y
        self.hitbox=pygame.Rect(x, y, self.width, self.height)
        self.max_health=100
        self.health=100
        self.health_regen=1
        self.damage=1
        
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
      hit=other.hitbox
      if hit.colliderect(other.hitbox):
         self.health-=0.1
       


      pass

    def attack(self,other):
      keys=pygame.key.get_pressed()
      
      if keys[pygame.K_SPACE]:
        attack_box=(self.hitbox.x+1,self.hitbox.y+1)
        if attack_box.colliderect(other.hitbox):
           other.take_damage()
           
         

       
    

  



