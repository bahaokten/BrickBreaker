import random
import math

import pygame

import main_Vars

ballsPos = [[], [], []]
ballsGrounds = [[], [], []]


class Ball(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, ballnum, isAttached = True):
        self.size = 20
        self.radius = self.size / 2
        self.ballnum = ballnum
        self.X = main_Vars.data_canvasX / 2 - self.radius
        self.Y = main_Vars.data_paddleY - self.size
        self.attachedToBall = isAttached
        self.color = main_Vars.SILVER
        self.outlineColor = main_Vars.LIGHTBLACK
        pygame.sprite.Sprite.__init__(self)
        self.rect = []
        ballsPos[self.ballnum - 1] = [self.X, self.Y]
        self.totalVel = 10
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
                print "$#$ | Ball", self.ballnum, "|", "is detached from | Paddle |!"
                self.attachedToBall = False
                tmp1 = random.randint(int(self.totalVelSquared*0.75*0.5), int(self.totalVelSquared*1.25*0.5))
                print tmp1
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
            elif self.X < 0:
                self.velX = -self.velX
                print "$#$ | Ball", self.ballnum, "|", "-VelX:", self.velX, " -VelY:", self.velY
            elif self.Y < 0:
                self.velY = -self.velY
                print "$#$ | Ball", self.ballnum, "|", "-VelX:", self.velX, " -VelY:", self.velY
            elif self.Y > main_Vars.data_canvasY:
                main_Vars.data_state = "gameoverbad"
                main_Vars.data_tick1 = False
            elif pygame.sprite.collide_rect(self, main_Vars.data_spriteGroup_paddle.sprites()[0]):
                # puts the ball either below or above the paddle according to the collision area = upper or below
                if main_Vars.data_paddleY-self.Y > -self.radius:
                    directionUp = True
                    self.Y = main_Vars.data_paddleY - self.size
                else:
                    directionUp = False
                    self.Y = main_Vars.data_paddleY + self.size + 21

                #speed incrementer
                tmp = (main_Vars.data_paddleMidX-self.X)
                if tmp > 0:
                    difference = tmp - self.size
                else:
                    difference = tmp
                absDif = abs(difference)
                addition = ((float(absDif)/main_Vars.data_paddleWidth)*6)
                if not addition < 0.1:
                # (absDif/main_Vars.data_paddleWidth)*2 is between 0 and 1
                    if tmp < 0:
                        self.velX += addition
                    else:
                        self.velX -= addition
                else:
                    self.velY = -self.velY

                # this function determines the charge according collision area = upper area or down area
                if directionUp:
                    self.velY = -math.sqrt(abs(self.totalVelSquared - math.pow(self.velX,2)))
                else:
                    self.velX = -self.velX
                    self.velY = +math.sqrt(abs(self.totalVelSquared - math.pow(self.velX,2)))
                #eger squarerootun ici eksiyse ve x olmasi gerekenden buyuk olursa asagidaki function duzeltecek
                if math.fabs(self.velX) < self.totalVel*0.1:
                    if self.velX < 0:
                        self.velX = self.totalVel*0.15
                    else:
                        self.velX = -self.totalVel*0.15
                    self.velY = -math.sqrt(self.totalVelSquared - math.pow(self.velX,2))
                elif math.fabs(self.velX)> self.totalVel*0.9:
                    if self.velX < 0:
                        self.velX = -self.totalVel*0.85
                    else:
                        self.velX = self.totalVel*0.85
                    self.velY = -math.sqrt(self.totalVelSquared - math.pow(self.velX,2))
                print "$#$ | Ball", self.ballnum, "|", "collided with | Paddle | at", self.X,self.Y, ". Its new velocity is -VelX:", self.velX, " -VelY:", self.velY

            self.rect.x = self.X
            self.rect.y = self.Y
            """
            interesting effect
            if self.Y < 0:
                self.velY = -self.velY
            """

        main_Vars.data_rect.append((self.X, self.Y, self.size, self.size))

    def create(self):
        self.image = pygame.Surface([self.size, self.size], pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x = self.X
        self.rect.y = self.Y
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
