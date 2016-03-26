import pygame

import main_Vars

ballsPos = [[],[],[]]
ballsGrounds = [[],[],[]]

class Ball(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self,ballnum):
        self.size = 20
        self.ballnum = ballnum
        self.X = main_Vars.data_canvasX/2
        self.Y = main_Vars.data_paddleY - self.size + 10
        self.attachedToBall = True
        self.color = main_Vars.EMERALD
        pygame.sprite.Sprite.__init__(self)
        self.rect = (self.X,self.Y)
        ballsPos.append((self.X,self.Y))

    def update(self):
        if self.attachedToBall:
            if main_Vars.data_left or main_Vars.data_right:
                None



    def create(self):
        self.image = pygame.Surface([self.size,self.size], pygame.SRCALPHA, 32)
        pygame.draw.circle(main_Vars.data_backGround,self.color,(self.X,self.Y),self.size/2)
        main_Vars.data_rect.append((self.X, self.Y, self.size, self.size))
        ballsGrounds.append(self.image)
        #main_Vars.data_foreGround.blit(self.image, [self.X, self.Y ])


def createBall(ballnum):
    ball = Ball(ballnum)
    main_Vars.data_spriteGroup_ball.add(ball)
    main_Vars.data_spriteGroup_ball.sprites()[ballnum-1].create()

def drawBalls():
    for i in xrange(3):
        if ballsPos[i] != []:
            main_Vars.screen.blit(ballsGrounds[i],(ballsPos[i][0],ballsPos[i][1]))
