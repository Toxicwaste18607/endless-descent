import pygame
import time
from ghost import *
from wall_class_code import *
from setting import *
import random

# Basic colors used for UI / debugging
green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)


#====================
# PLAYER CLASS
#====================

class Player():
  # === Player stats / attributes ===
  width= 35
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
    """
    Creates player at given x,y position.
    """
    # Create hitbox for collision and position
    self.hitbox=pygame.Rect(x, y, self.width, self.height)

    # Load all player images
    self.load_character_images()

    # Store walking animation frames
    self.walk_frames = [self.walking_1, self.walking_2, self.walking_3]

    # Will hold a ghost when player dies
    self.new_ghost=None
  

  def player_logic(self,screen,other):
      """
      Main player update function (runs every frame).
      """
      self.all_draws(screen)  # draw UI + player
      self.movement()         # handle movement


  #====================
  # DRAWING
  #====================

  def all_draws(self, screen):
    """
    Draws everything related to player (UI + character).
    """
    self.draw_stamina(screen)
    self.draw_health(screen)

    if self.health > 0:
      self.draw_character(screen)
    else:
      pass  # dead player doesn't draw (yet)



  def draw_health(self,screen):
    """
    Draws health bar on screen.
    """
    health_bar_hight= (self.health / self.max_health) * 200
    health_bar_hight=abs(health_bar_hight)
      
    health_bar=(20,550,20,health_bar_hight)
    healthbar_cover=()  # unused (placeholder)
    pygame.draw.rect(screen,(red),(health_bar) )
  

  def draw_stamina(self,screen):
    """
    Draws stamina bar on screen.
    """
    x= 1350
    y=550
    width= 20

    # Clamp stamina so it doesn't go over max
    if self.stamina>self.max_stamina:
      self.stamina=self.max_stamina

    stamina_bar_hight=(self.stamina/self.max_stamina) *200
    stamina_bar_hight=abs(stamina_bar_hight)
    
    stamina_bar=(x,y,width,stamina_bar_hight )
    pygame.draw.rect(screen,blue, stamina_bar )


  def draw_character(self,screen):
    """
    Handles which animation to draw.
    """
    #screen.blit(self.standing,(self.hitbox.x, self.hitbox.y))
    self.walking(screen)



  def standing(self,screen):
    """
    Draws standing sprite.
    """
    screen.blit(self.standing,(self.hitbox.x, self.hitbox.y))



  def walking(self, screen):
    """
    Handles walking animation (currently simplified).
    """
    '''if self.is_moving:

        frame = self.walk_frames[self.current_frame]'''
    # Currently always uses standing frame
    frame = self.standing

    screen.blit(frame, (self.hitbox.x, self.hitbox.y))


  #====================
  # IMAGE LOADING
  #====================

  def load_character_images(self):
    """
    Loads and scales all player sprites.
    """

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


  #====================
  # DAMAGE / DEATH
  #====================

  def take_damage(self,screen,other):
    """
    Handles player taking damage from enemy.
    """
    if self.hitbox.colliderect(other.hitbox):
      if self.health >0: 
        self.health-=1

        if self.health <=0:
          self.player_death(screen)

      elif self.health<=0:
        self.player_death(screen)
        pass

    if not self.hitbox.colliderect(other.hitbox):  
      pass
  

  def player_death(self,screen):  
    """
    Handles player death and respawn.
    Also creates a ghost at death location.
    """
    # Create ghost at current position
    self.new_ghost = Player_ghost(self.hitbox.copy())

    # Try random respawn positions
    for x in range (200):

      check_area_x= random.randint(0,screen_width-self.width)
      check_area_y= random.randint(0,screen_height-self.height)
      
      test_rect = pygame.Rect(check_area_x,check_area_y,self.width,self.height)

      # Only respawn if not colliding with wall
      if not self.collision(test_rect):
        self.hitbox.x= check_area_x
        self.hitbox.y=check_area_y
        self.health = self.max_health
        self.stamina = self.max_stamina
        return


  #====================
  # ATTACK
  #====================

  def attack(self,screen,other):
    """
    Creates attack box and damages enemy if inside.
    """
    attack_box=(self.hitbox.x-self.attack_range,  self.hitbox.y -self.attack_range,
                self.hitbox.width +(self.attack_range*self.range_multi),
                self.hitbox.height+(self.attack_range*self.range_multi))

    attack_box=pygame.Rect(attack_box)

    # Draw attack box (debug)
    pygame.draw.rect(screen,green,attack_box)

    if attack_box.colliderect(other.hitbox):
        other.take_damage(self)


  #====================
  # COLLISION
  #====================

  def collision(self,next_move):
    """
    Checks if player would hit a wall.
    """
    for wall in Walls.all_walls:
      if next_move.colliderect(wall.wall_hitbox):
        return True
    return False
 

  #====================
  # MOVEMENT
  #====================

  def movement(self):
    """
    Handles player movement and sprinting.
    """
    moving=False
    keys=pygame.key.get_pressed()

    walking=1
    sprinting=2
    speed = walking

    # Sprint logic (uses stamina)
    if keys[pygame.K_LSHIFT]:
      if self.stamina>0:
        self.stamina-=.2
        speed = sprinting 
      else:
        speed = walking

    # UP
    if keys[pygame.K_w]:
      next_move=self.hitbox.copy()
      next_move.y-=speed
      if not self.collision(next_move): 
          self.hitbox.y -= speed
          moving=True

    # DOWN
    if keys[pygame.K_s]:
      next_move=self.hitbox.copy()
      next_move.y+=speed
      if not self.collision(next_move):
          self.hitbox.y+=speed

    # LEFT
    if keys[pygame.K_a]:
      next_move=self.hitbox.copy()
      next_move.x-=speed
      if not self.collision(next_move):
        self.hitbox.x-=speed
        self.is_moving= True

    # RIGHT
    if keys[pygame.K_d]:
      next_move=self.hitbox.copy()
      next_move.x+=speed
      if not self.collision(next_move):
        self.hitbox.x+=speed
        self.is_moving= True
    
    # Regenerate stamina when not sprinting
    if not keys[pygame.K_LSHIFT]:
      self.stamina+=self.stamina_regain

    #====================
    # SCREEN BOUNDARIES
    #====================

    # Prevent going off left/top
    if self.hitbox.x < 0:
      self.hitbox.x= 0 
    
    if self.hitbox.y<0:
      self.hitbox.y=0

    # Prevent going off right
    over_shoot_left= (screen_width - self.width)
    if self.hitbox.x > over_shoot_left:
      self.hitbox.x = over_shoot_left

    # Prevent going off bottom
    over_shoot_down=(screen_height- self.height)
    if self.hitbox.y> over_shoot_down:
      self.hitbox.y = over_shoot_down