import pygame
from enemy_class import *

# Basic colors (used for debugging / drawing if needed)
green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)

# This is a specific enemy type (Skeleton) that inherits from Enemy
class Skelo(Enemy):

   # List for enemies of this type (not really needed since Enemy already has one)
   all_enemies =[]

   # Detection range for chasing player
   agro_range=300
   
   # Size of the skeleton
   width= 35
   height= 50

   # === Stats ===
   max_health=100
   health=100
   health_regen=1
   attack_range = 5
   damage=20
   range_multi=2
   stamina = 100
   max_stamina=100
   stamina_regain = .02
   speed=1

   def __init__ (self ,x,y):
        """
        Creates a skeleton enemy at position (x, y).
        """

        # Create hitbox for position and collision
        hitbox = pygame.Rect(x, y, self.width, self.height)

        # Call parent (Enemy) constructor
        super().__init__(hitbox)

        # Load skeleton image
        self.load_image()

        # Reassign hitbox (keeps same values)
        self.hitbox = hitbox
        
  
   def load_image(self):
      """
      Loads and scales the skeleton sprite.
      """
      self.standing = pygame.image.load("src/assets/skelo.png")

      # Scale image to match hitbox size
      self.standing = pygame.transform.scale(self.standing,(self.width,self.height))


   def draw_character(self,screen):
      """
      Draws the skeleton on screen.
      """
      screen.blit(self.standing,(self.hitbox.x,self.hitbox.y))


   def collision(self,screen,next_move,other):
         """
         Checks if the skeleton's next move collides with something.

         next_move: predicted position
         other: usually the player

         Returns True if blocked.
         """

         for wall in Walls.all_walls:
            # Check collision with walls
            if next_move.colliderect(wall.wall_hitbox):
               return True

            # Check collision with player
            if next_move.colliderect(other.hitbox):
               self.attack(screen, other)  # attack if touching player
               return True