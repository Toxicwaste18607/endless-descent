import pygame
from wall import *
from setting import *

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
  stamina = 100
  max_stamina=100
  stamina_regain = .02
  range_multi= 2

  def __init__ (self ,x,y):
    
    self.hitbox=pygame.Rect(x, y, self.width, self.height)


  def player_logic(self,screen,other):
      self.all_draws(screen)
      self.movement()


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



  def draw_character(self,screen):
    pygame.draw.rect(screen, blue, self.hitbox)
  
  
    


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
    from ghost import Player_Ghost 
    ghost=Player_Ghost(self.hitbox.copy())

    
    
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






  def collision(self,next_move):
    for wall in Walls.all_walls:
      if next_move.colliderect(wall.wall_hitbox):
        return True
    return None
      #if next_move.colliderect():pass




    
  def movement(self):
    moving=False
    keys=pygame.key.get_pressed()

    walking=1
    sprinting=2
    speed = walking
    if keys[pygame.K_LSHIFT]:
      self.sprint()
      
      if self.sprint():
        speed = sprinting 
      else:
        speed = walking

    if keys[pygame.K_w]: #up
      next_move=self.hitbox.copy()
      next_move.y-=speed
      if not self.collision(next_move): 
          self.hitbox.y -= speed
          moving=True
      
    
    
    if keys[pygame.K_s]:#down
      next_move=self.hitbox.copy()
      next_move.y+=speed
      if not self.collision(next_move):
          self.hitbox.y+=speed
          
    
      

    if keys[pygame.K_a]:#left
      next_move=self.hitbox.copy()
      next_move.x-=speed
      if not self.collision(next_move):
        self.hitbox.x-=speed
        self.is_moving= True


    if keys[pygame.K_d]:#right
      next_move=self.hitbox.copy()
      next_move.x+=speed
      if not self.collision(next_move):
        self.hitbox.x+=speed
        self.is_moving= True
    
    if not keys[pygame.K_LSHIFT]:
      self.stamina+=self.stamina_regain

    

    if self.hitbox.x < 0: #to stop the player from going off screen 
      self.hitbox.x= 0 
    
    if self.hitbox.y<0:
      self.hitbox.y=0

    over_shoot_left= (screen_width - self.width)
    if self.hitbox.x > over_shoot_left:
      self.hitbox.x = over_shoot_left

    over_shoot_down=(screen_height- self.height)
    if self.hitbox.y> over_shoot_down:
      self.hitbox.y = over_shoot_down
