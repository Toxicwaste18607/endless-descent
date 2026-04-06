import pygame

green =(0, 255, 0)
blue=(0, 0, 255) 
white=(255, 255, 255) 
black=(0, 0, 0) 
red=(255,0,0)


class Player_Ghost():

    def __init__(self,screen,x,y,width,hight):
        self.x=x
        self.y=y
        self.width=width
        self.hight=hight
        self.draw_ghost(screen)
        pass

    def draw_ghost(self,screen):
        pygame.draw.rect( screen, (blue), (self.hitbox))
