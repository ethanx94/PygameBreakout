import pygame
from Const import *

class Paddle(pygame.Rect):
    __xspeed = None
    __yspeed = None
    
    def __init__(self, xpos, ypos, wid, ht, xspeed, yspeed):
        super(Paddle, self).__init__(xpos, ypos, wid, ht)
        self.__xspeed = xspeed
        self.__yspeed = yspeed

    def checkIt(self, direction):
        if (direction == "MOVE_LEFT" and self.x >= 2*BOUND_WID):
            self.x -= self.__xspeed   
        elif (direction == "MOVE_RIGHT" and self.x <= SCREEN_WID_HT-PLAYER_WID-2*BOUND_WID):
            self.x += self.__xspeed
