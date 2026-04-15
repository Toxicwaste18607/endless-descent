import pygame
from wall_class_code import *


class Enemy():
   # List that stores ALL enemy instances in the game
   all_enemies = []

   def __init__(self, hitbox):
        """
        Creates a new enemy.

        hitbox: a pygame.Rect (or something with x/y) used as the starting position.
        """
        # Create the enemy's hitbox using given position + preset width/height
        self.hitbox = pygame.Rect(hitbox.x, hitbox.y, self.width, self.height)

        # Add this enemy to the global list so the game can track all enemies
        Enemy.all_enemies.append(self)


   def enemy_logic(self, screen, other):
      """
      Main update function for the enemy.
      Runs every frame.

      screen: where things are drawn
      other: usually the player
      """
      if self.health > 0:
         self.draw_character(screen)   # draw enemy
         self.search(screen, other)    # decide what to do (chase or wander)
      else:
         pass   # dead enemies do nothing


   def collision(self, screen, next_move, other):
         """
         Checks if a movement would hit something.

         next_move: a copy of the hitbox showing where the enemy WANTS to go
         other: usually the player

         Returns True if blocked, False if free.
         """
         for wall in Walls.all_walls:
            if next_move.colliderect(wall.wall_hitbox):
               return True  # blocked by wall

            if next_move.colliderect(other.hitbox):
               self.attack(screen, other)  # attack if touching player
               return True

         return False  # no collision


   def path_finding(self, screen, blocked, other):
       """
       Handles movement when the enemy gets stuck.

       blocked:
       1 = right blocked
       2 = up blocked
       3 = left blocked
       4 = down blocked

       Enemy will try another direction if blocked.
       """

       if blocked == 1:  # blocked moving right → try left
         next_move = self.hitbox.copy()
         next_move.x -= self.speed
         if not self.collision(screen, next_move, other):
            self.hitbox.x -= self.speed
         else:
            blocked = 3

       if blocked == 2:  # blocked moving up → try down
         next_move = self.hitbox.copy()
         next_move.y -= self.speed
         if not self.collision(screen, next_move, other):
            self.hitbox.y -= self.speed
         else:
            blocked = 4

       if blocked == 3:  # blocked moving left → try right
         next_move = self.hitbox.copy()
         next_move.x += self.speed
         if not self.collision(screen, next_move, other):
            self.hitbox.x += self.speed
         else:
            blocked = 1

       if blocked == 4:  # blocked moving down → try up
         next_move = self.hitbox.copy()
         next_move.y += self.speed
         if not self.collision(screen, next_move, other):
            self.hitbox.y += self.speed
         else:
            blocked = 2


   def check_dist(self, other):
       """
       Calculates distance from enemy to player (x and y separately).
       """
       self.distance_x = (other.hitbox.x - self.hitbox.x)
       self.distance_y = (other.hitbox.y - self.hitbox.y)


   def search(self, screen, other):
       """
       Decides if the enemy should chase the player or wander.

       If player is within agro_range → chase
       Otherwise → wander
       """
       self.check_dist(other)

       if abs(self.distance_x) < self.agro_range and abs(self.distance_y) < self.agro_range:
         self.agro(screen, other)
       else:
          self.wander()


   def agro(self, screen, other):
      """
      Moves enemy toward the player.

      Uses distance to decide direction.
      If blocked → uses pathfinding.
      """

      # Move RIGHT
      if self.distance_x > 0:
         next_move = self.hitbox.copy()
         next_move.x += self.speed
         if not self.collision(screen, next_move, other):
            self.hitbox.x += self.speed
         else:
            blocked = 1
            self.path_finding(screen, blocked, other)

      # Move DOWN
      if self.distance_y > 0:
         next_move = self.hitbox.copy()
         next_move.y += self.speed
         if not self.collision(screen, next_move, other):
            self.hitbox.y += self.speed
         else:
            blocked = 2
            self.path_finding(screen, blocked, other)

      # Move LEFT
      if self.distance_x < 0:
         next_move = self.hitbox.copy()
         next_move.x -= self.speed
         if not self.collision(screen, next_move, other):
            self.hitbox.x -= self.speed
         else:
            blocked = 3
            self.path_finding(screen, blocked, other)

      # Move UP
      if self.distance_y < 0:
         next_move = self.hitbox.copy()
         next_move.y -= self.speed
         if not self.collision(screen, next_move, other):
            self.hitbox.y -= self.speed
         else:
            blocked = 4
            self.path_finding(screen, blocked, other)


   def wander(self):
       """
       What the enemy does when NOT chasing the player.
       (Currently empty — you can add random movement here)
       """
       pass


   def take_damage(self, other):
      """
      Reduces enemy health when hit.

      other: the attacker (player)
      """
      if self.health > 0:
         self.health -= other.damage

         if self.health <= 0:
            Enemy.all_enemies.remove(self)  # remove from game


   def attack(self, screen, other):
      """
      Creates an attack box around the enemy.

      If player is inside → deal damage.
      """
      attack_box = (
          self.hitbox.x - self.attack_range,
          self.hitbox.y - self.attack_range,
          self.hitbox.width + (self.attack_range * self.range_multi),
          self.hitbox.height + (self.attack_range * self.range_multi)
      )

      attack_box = pygame.Rect(attack_box)

      # Draw attack box (for debugging)
      pygame.draw.rect(screen, green, attack_box)

      if attack_box.colliderect(other.hitbox):
         other.take_damage(self, other)