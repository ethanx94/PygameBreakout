import pygame
from random import randint
from Const import *
from GameState import GameState

class Ball(pygame.Rect):
    
    def __init__(self, xpos, ypos, wid, ht, xspeed, yspeed, state):
        super(Ball, self).__init__(xpos, ypos, wid, ht)
        self.__xpos = xpos
        self.__ypos = ypos
        self.__wid = wid
        self.__ht = ht
        self.__xspeed = xspeed
        self.__yspeed = yspeed
        self.__state = state

    def checkPuck(self, player, boundLeft, boundRight, boundTop):
        if (self.colliderect(player) or self.colliderect(boundTop)):
            self.bounce("top")
        
        if (self.colliderect(boundLeft) or self.colliderect(boundRight)):
            self.bounce("side")
    
    def bounce(self, direction):
        if (direction == "top"):
            self.__yspeed *= -1
        elif(direction == "side"):
            self.__xspeed *= -1

    def movePuck(self):
        self.x += self.__xspeed
        self.y += self.__yspeed
        
    # Return to center y, flip direction, random x for variety
    def resetPuck(self):
        self.__xspeed *= -1
        self.x = randint(BOUND_WID,SCREEN_WID_HT-BOUND_WID)
        self.y = self.__ypos

    def checkOOB(self):
        if(self.y > SCREEN_WID_HT):
            self.__state.setPLives()
            self.resetPuck()