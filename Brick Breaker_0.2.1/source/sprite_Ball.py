import random
import math

import pygame

import main_Vars

ballsPos = [[], [], []]
ballsGrounds = [[], [], []]


class Ball(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, ballnum):
        self.size = 20
        self.radius = self.size / 2
        self.ballnum = ballnum
        self.X = main_Vars.data_canvasX / 2 - self.radius
        self.Y = main_Vars.data_paddleY - self.size
        self.attachedToBall = True
        self.color = main_Vars.SILVER
        self.outlineColor = main_Vars.LIGHTBLACK
        pygame.sprite.Sprite.__init__(self)
        self.rect = (self.X, self.Y)
        ballsPos[self.ballnum - 1] = [self.X, self.Y]
        self.totalVel = 20
        self.totalVelSquared = math.pow(self.totalVel, 2)
        self.velX = 0
        self.velY = 0
        print "-ballnum:", self.ballnum, " -X:", self.X, " -Y:", self.Y, " -Radius:", self.radius
        print "-innerColor:", self.color, " -outlineColor:", self.outlineColor

    def update(self):
        main_Vars.data_rect.append((self.X, self.Y, self.size, self.size))
        if self.attachedToBall:
            if main_Vars.data_left or main_Vars.data_right:
                main_Vars.data_rect.append((self.X, self.Y, self.size, self.size))

                self.X = main_Vars.data_paddleMidX - self.radius
                ballsPos[self.ballnum - 1][0] = self.X

                main_Vars.data_rect.append((self.X, self.Y, self.size, self.size))
            elif main_Vars.data_space:
                print "$#$ | Ball", self.ballnum, "|", "is detached from the paddle!"
                self.attachedToBall = False
                tmp1 = random.randint(150, 250)
                tmp2 = math.sqrt(tmp1)
                self.velX = int(random.choice([1, -1]) * tmp2)
                self.velY = -int(math.sqrt(self.totalVelSquared - tmp1))
                print "$#$ | Ball", self.ballnum, "|", "-VelX:", self.velX, " -VelY:", self.velY
        else:
            self.X += self.velX
            ballsPos[self.ballnum - 1][0] = self.X
            self.Y += self.velY
            ballsPos[self.ballnum - 1][1] = self.Y
            if self.X + self.size > main_Vars.data_canvasX:
                self.velX = -self.velX
                print "$#$ | Ball", self.ballnum, "|", "-VelX:", self.velX, " -VelY:", self.velY
            if self.X < 0:
                self.velX = -self.velX
                print "$#$ | Ball", self.ballnum, "|", "-VelX:", self.velX, " -VelY:", self.velY
            if self.Y < 0:
                self.velY = -self.velY
                print "$#$ | Ball", self.ballnum, "|", "-VelX:", self.velX, " -VelY:", self.velY
            if self.Y > main_Vars.data_canvasY:
                main_Vars.data_state = "gameoverbad"
                main_Vars.data_tick1 = False
            """
            interesting effect
            if self.Y < 0:
                self.velY = -self.velY
            """

        main_Vars.data_rect.append((self.X, self.Y, self.size, self.size))

    def create(self):
        self.image = pygame.Surface([self.size, self.size], pygame.SRCALPHA, 32)
        # self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, self.outlineColor, (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius - 3)
        main_Vars.data_rect.append((self.X, self.Y, self.size, self.size))
        ballsGrounds[self.ballnum - 1] = self.image
        # main_Vars.data_foreGround.blit(self.image, [self.X, self.Y ])


def createBall(ballnum):
    print "=====>Ball #", ballnum, "Created<====="
    ball = Ball(ballnum)
    main_Vars.data_spriteGroup_ball.add(ball)
    main_Vars.data_spriteGroup_ball.sprites()[ballnum - 1].create()


def drawBalls():
    for i in xrange(3):
        if ballsPos[i] != []:
            main_Vars.screen.blit(ballsGrounds[i], (ballsPos[i][0], ballsPos[i][1]))
