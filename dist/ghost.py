import pygame
from player import *
from enemy_class import *

# Color used for drawing (if needed)
blue = (0, 0, 255)

# Player ghost class that inherits ALL behavior from Enemy
class Player_ghost(Enemy):
    
    # === Stats / attributes for the ghost ===
    width = 35              # width of ghost hitbox and sprite
    height = 50             # height of ghost hitbox and sprite
    agro_range = 300        # how far the ghost can detect the player
    max_health = 100        # max health
    health = 100            # current health
    health_regen = 1        # health regen rate (not used yet)
    attack_range = 5        # size of attack range
    damage = 10             # damage dealt per hit
    range_multi = 2         # multiplier for attack box size
    stamina = 100           # stamina (not used yet)
    max_stamina = 100       # max stamina
    stamina_regain = .02    # stamina regen (not used yet)
    speed = 1               # movement speed

    def __init__(self, hitbox):
        """
        Initializes the ghost.

        hitbox: starting position (usually passed from player death)
        """
        
        # Load images BEFORE calling Enemy constructor
        # so sprite is ready when used
        self.load_images()

        # Call Enemy constructor to set hitbox and add to all_enemies list
        super().__init__(hitbox)   
        

    def draw_character(self, screen):
        """
        Draws the ghost sprite at its current position.
        """
        screen.blit(self.ghost_1, (self.hitbox.x, self.hitbox.y))


    def load_images(self):
        """
        Loads and scales the ghost image.
        """
        # Load image from assets folder
        self.ghost_1 = pygame.image.load("src/assets/Knight/Ghost_2.png")

        # Scale image to match hitbox size
        self.ghost_1 = pygame.transform.scale(self.ghost_1, (self.width, self.height))