import pygame


#====================
# WALL CLASS
#====================

class Walls():
  # Stores ALL wall instances in the game
  all_walls = []

  def __init__(self,x,y,width,height):
    """
    Creates a wall at position (x, y) with given size.
    """

    # Position
    self.x = x
    self.y = y

    # Size
    self.height = height
    self.width = width

    # Tuple for drawing position
    self.x_and_y = (self.x ,self.y)

    # Add this wall to the global list
    self.all_walls.append(self)

    # Create hitbox for collision detection
    self.wall_hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    # Load and prepare wall images
    self.render_images()
    


  def render_images(self):
    """
    Loads and scales wall textures (vertical + horizontal).
    """

    # Vertical wall image
    self.wall_vert = pygame.image.load("src/assets/walls_and_floors/wall_type_two_v.png").convert_alpha()
    self.wall_vert = pygame.transform.scale(self.wall_vert,(self.width,self.height))
    
    # Horizontal wall image
    self.wall_horl = pygame.image.load("src/assets/walls_and_floors/wall_type_two_h.png").convert_alpha()
    self.wall_horl = pygame.transform.scale(self.wall_horl,(self.width,self.height))


  def draw_wall(self,screen):
    """
    Draws the wall on screen.
    Chooses vertical or horizontal image based on shape.
    """
    
    # If taller than wide → vertical wall
    if self.height > self.width:
      screen.blit(self.wall_vert, self.x_and_y)

    # Otherwise → horizontal wall
    else:
      screen.blit(self.wall_horl, self.x_and_y)


#====================
# BORDER WALL CLASS
#====================

# Inherits everything from Walls (currently no changes)
class Boarder_Walls(Walls):
  pass