import sys
import pygame
from Const import *
from Paddle import Paddle
from Breakable import Breakable
from Ball import Ball
from GameState import GameState

pygame.init()
pygame.display.set_caption("Breakout")
scoreBoard = pygame.font.SysFont( "arial", 30 )
screen = pygame.display.set_mode((SCREEN_WID_HT, SCREEN_WID_HT))
clock = pygame.time.Clock()

gameState = GameState(scoreBoard, screen)

# Instantiate Basic Rects
boundTop = pygame.Rect(ORIGIN, ORIGIN, SCREEN_WID_HT, BOUND_WID)
boundLeft = pygame.Rect(ORIGIN, ORIGIN, BOUND_WID, SCREEN_WID_HT)
boundRight = pygame.Rect(SCREEN_WID_HT-BOUND_WID, ORIGIN, BOUND_WID, SCREEN_WID_HT)

# Instantiate Rect-like Children
player = Paddle(PLAYER_X, PLAYER_Y, PLAYER_WID, PLAYER_HT, PLAYER_SPEED, 0)
puck = Ball(CENTER, CENTER, PUCK_WD_HT, PUCK_WD_HT, -PLAYER_SPEED, PLAYER_SPEED, gameState)
breakMe = Breakable(BLOCK_X, BLOCK_Y, BLOCK_WID, BLOCK_HT, screen, gameState)

def main():
    
    #Player Control
    def moveIt(key):
        if key[pygame.K_LEFT]:
            player.checkIt("MOVE_LEFT")
        if key[pygame.K_RIGHT]:
            player.checkIt("MOVE_RIGHT")
        
        # Handle Close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
    
    def checkIt():
        puck.checkPuck(player, boundLeft, boundRight, boundTop)
        breakMe.checkIt(puck)
        puck.checkOOB()
        
    def drawIt():
        screen.fill((BLACK))
        
        pygame.draw.rect(screen, WHITE, boundTop)
        pygame.draw.rect(screen, WHITE, boundLeft)
        pygame.draw.rect(screen, WHITE, boundRight)
        
        pygame.draw.rect(screen, RED, player)
        pygame.draw.rect(screen, WHITE, puck)
        breakMe.drawIt()
        
        if (gameState.getPLives() == 0 or breakMe.getRemaining() == 0):
            gameState.drawIt(SCORE_LBL, GAMEOVER_LBL)
            Breakable(BLOCK_X, BLOCK_Y, BLOCK_WID, BLOCK_HT, screen, gameState)
            
            pygame.display.flip()
            pygame.time.delay(3000)
            gameState.resetGame()
        else:
            gameState.drawIt(SCORE_LBL, LIVES_LBL)
        
        pygame.display.flip()
    
    while True:
        moveIt(pygame.key.get_pressed())
            
        checkIt()
        puck.movePuck()
            
        drawIt()
        clock.tick(60)

if __name__ == '__main__':
    main()