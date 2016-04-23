import random
import math

import pygame

import main_Vars
import main_Modules


class Ball(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, ballnum, isAttached=True):
        self.size = 20
        self.radius = self.size / 2
        self.ballnum = ballnum
        self.X = main_Vars.data_canvasX / 2 - self.radius
        self.Y = main_Vars.data_paddleY - self.size
        self.prevX = 0
        self.prevY = 0
        self.attachedToBall = isAttached
        self.color = main_Vars.SILVER
        self.outlineColor = main_Vars.LIGHTBLACK
        pygame.sprite.Sprite.__init__(self)
        self.rect = []
        self.totalVel = 5
        self.totalVelSquared = math.pow(self.totalVel, 2)
        self.velX = 0
        self.velY = 0
        self.cooldown = 0
        print "-ballnum:", self.ballnum, " -X:", self.X, " -Y:", self.Y, " -Radius:", self.radius
        print "-innerColor:", self.color, " -outlineColor:", self.outlineColor

    def update(self):
        tmpoldX = self.X
        tmpoldY = self.Y
        if self.cooldown:
            self.cooldown -= 1
        if self.attachedToBall:
            if main_Vars.data_left or main_Vars.data_right:
                main_Vars.data_rect.append((self.X, self.Y, self.size, self.size))

                self.X = main_Vars.data_paddleMidX - self.radius

                main_Vars.data_rect.append((self.X, self.Y, self.size, self.size))
            elif main_Vars.data_space:
                main_Vars.data_thrown.play(loops = 0)
                print "$#$ | BALL", self.ballnum, "|", "is detached from | PADDLE |!"
                self.attachedToBall = False
                tmp1 = random.randint(int(self.totalVelSquared * 0.75 * 0.5), int(self.totalVelSquared * 1.25 * 0.5))
                print tmp1
                tmp2 = math.sqrt(tmp1)
                self.velX = int(random.choice([1, -1]) * tmp2)
                self.velY = -int(math.sqrt(self.totalVelSquared - tmp1))
                print "$#$ | BALL", self.ballnum, "|", "-VelX:", self.velX, " -VelY:", self.velY
        else:
            # FIRST PART VELOCITY ADDITION
            self.X += self.velX
            self.Y += self.velY
            # SECOND PART WALL/PADDLE COLLISION
            if self.X + self.size > main_Vars.data_canvasX:
                main_Vars.data_brick2.play(loops = 0)
                self.velX = -self.velX
                print "$#$ | BALL", self.ballnum, "|", "collided with | RIGHT WALL |  at", self.X, self.Y, ".Its new velocity is -VelX:", self.velX, " -VelY:", self.velY
            elif self.X < 0:
                main_Vars.data_brick2.play(loops = 0)
                self.velX = -self.velX
                print "$#$ | BALL", self.ballnum, "|", "collided with | LEFT WALL |  at", self.X, self.Y, ".Its new velocity is -VelX:", self.velX, " -VelY:", self.velY
            elif self.Y < 0:
                main_Vars.data_brick2.play(loops = 0)
                self.Y = 0
                self.velY = -self.velY
                print "$#$ | BALL", self.ballnum, "|", "collided with | UPPER WALL |  at", self.X, self.Y, ".Its new velocity is -VelX:", self.velX, " -VelY:", self.velY
            elif self.Y > main_Vars.data_canvasY:
                # main_Vars.gamemodeChanger("gameoverbad")
                self.velY = -self.velY
            elif pygame.sprite.collide_rect(self, main_Vars.data_spriteGroup_paddle.sprites()[0]):
                main_Vars.data_paddleHitSound.play(loops = 0)
                # puts the ball either below or above the paddle according to the collision area = upper or below
                if main_Vars.data_paddleY - self.Y > -self.radius:
                    directionUp = True
                    self.Y = main_Vars.data_paddleY - self.size
                else:
                    directionUp = False
                    self.Y = main_Vars.data_paddleY + self.size + 21

                # speed incrementer
                tmp = (main_Vars.data_paddleMidX - self.X)
                if tmp > 0:
                    difference = tmp - self.size
                else:
                    difference = tmp
                absDif = abs(difference)
                addition = ((float(absDif) / main_Vars.data_paddleWidth) * 12)
                if addition > 0.1 and addition < self.velX and addition / 2 < self.velX:
                    # (absDif/main_Vars.data_paddleWidth)*2 is between 0 and 1
                    if tmp < 0:
                        self.velX += addition
                    else:
                        self.velX -= addition
                elif addition > 0.1:
                    if tmp < 0:
                        self.velX += addition / 2
                    else:
                        self.velX -= addition / 2
                else:
                    self.velY = -self.velY

                # this function determines the charge according collision area = upper area or down area
                if directionUp:
                    self.velY = -math.sqrt(abs(self.totalVelSquared - math.pow(self.velX, 2)))
                else:
                    self.velX = -self.velX
                    self.velY = +math.sqrt(abs(self.totalVelSquared - math.pow(self.velX, 2)))
                # eger squarerootun ici eksiyse ve x olmasi gerekenden buyuk olursa asagidaki function duzeltecek
                if math.fabs(self.velX) < self.totalVel * 0.10:
                    if self.velX < 0:
                        self.velX = -self.totalVel * 0.15
                    else:
                        self.velX = self.totalVel * 0.15
                    self.velY = -math.sqrt(self.totalVelSquared - math.pow(self.velX, 2))
                elif math.fabs(self.velX) > self.totalVel * 0.95:
                    if self.velX < 0:
                        self.velX = -self.totalVel * 0.90
                    else:
                        self.velX = self.totalVel * 0.90
                    self.velY = -math.sqrt(self.totalVelSquared - math.pow(self.velX, 2))
                print "$#$ | BALL", self.ballnum, "|", "collided with | PADDLE | at", self.X, self.Y, ". Its new velocity is -VelX:", self.velX, " -VelY:", self.velY
            # THIRD PART BRICK COLLISION
            elif not self.cooldown:
                tmpsprites = []
                for sprite in xrange(len(main_Vars.data_spriteGroup_bricks.sprites())):
                    if pygame.sprite.collide_rect(main_Vars.data_spriteGroup_bricks.sprites()[sprite], self):
                        tmpsprites.append(sprite)
                        print tmpsprites
                # which brick decider:
                if tmpsprites != []:
                    play = random.choice(main_Vars.data_brickHits)
                    play.play(loops=0)
                    shortest = 1000
                    chosenbrick = False
                    for bricks in tmpsprites:
                        tmpMid = main_Vars.data_spriteGroup_bricks.sprites()[bricks].getMid()
                        if (main_Modules.length(tmpMid, (self.X + self.size / 2, self.Y + self.size / 2))) < shortest:
                            shortest = main_Modules.length(tmpMid, (self.X + self.size / 2, self.Y + self.size / 2))
                            chosenbrick = bricks
                    tmpsprites = []
                    print "$#$ | BALL", self.ballnum, "|", "collided with | BRICK", \
                    main_Vars.data_spriteGroup_bricks.sprites()[
                        chosenbrick].info(), "| at", self.X, self.Y, ". Its new velocity is -VelX:", self.velX, " -VelY:", self.velY
                    tmpMid = main_Vars.data_spriteGroup_bricks.sprites()[chosenbrick].getMid()
                    # print ("BRICK COLLISION!")
                    # 4 functions
                    # MID CONTROL
                    midX = self.prevX + self.size
                    midY = self.prevY + self.size
                    slope = 20
                    # capraz da burada yapilabilir
                    if (midY > slope* midX + main_Modules.linearEquation(
                            (tmpMid[0] - (main_Vars.data_brickSizeX / 2), tmpMid[1] - (main_Vars.data_brickSizeY / 2)),
                            slope) and midY < -slope * midX + main_Modules.linearEquation(
                        (tmpMid[0] - (main_Vars.data_brickSizeX / 2), tmpMid[1] + (main_Vars.data_brickSizeY / 2)),
                        -slope)):
                        # SOL
                        # self.X -= (tmpMid[0]-(main_Vars.data_brickSizeX/2)-self.X) + 3
                        self.velX = -self.velX
                        self.cooldown = 10
                    elif (midY > -slope * midX + main_Modules.linearEquation(
                            (tmpMid[0] + (main_Vars.data_brickSizeX / 2), tmpMid[1] - (main_Vars.data_brickSizeY / 2)),
                            -slope) and midY < slope * midX + main_Modules.linearEquation(
                        (tmpMid[0] + (main_Vars.data_brickSizeX / 2), tmpMid[1] + (main_Vars.data_brickSizeY / 2)),
                        slope)):
                        # SAg
                        # self.X += (self.X-tmpMid[0]-(main_Vars.data_brickSizeX/2)) + 3
                        self.velX = -self.velX
                        self.cooldown = 10
                    else:
                        self.velY= -self.velY
                        self.cooldown = 10

                    """
                    if midX < tmpMid[0]-(main_Vars.data_brickSizeX/2) or midX > tmpMid[0]+(main_Vars.data_brickSizeX/2):
                            self.velX = -self.velX
                            self.cooldown = 5
                    """
                    """
                    if tmpMid[1]+(main_Vars.data_brickSizeY/2) > midY > tmpMid[1]-(main_Vars.data_brickSizeY/2):
                        if midX < tmpMid[0]-(main_Vars.data_brickSizeX/2) or midX > tmpMid[0]+(main_Vars.data_brickSizeX/2):
                            self.velX = -self.velX
                    elif tmpMid[0]+(main_Vars.data_brickSizeX/2) > midX > tmpMid[0]-(main_Vars.data_brickSizeX/2):
                        if midY < tmpMid[1]-(main_Vars.data_brickSizeY/2) or midY > tmpMid[1]+(main_Vars.data_brickSizeY/2):
                            if self.velY<0:
                                self.velY = -self.velY
                                self.Y += self.size
                            else:
                                self.velY = -self.velY
                                self.Y -= self.size
                    """
                    # CAPRAZ

            self.rect.x = self.X
            self.rect.y = self.Y
            self.prevX = tmpoldX
            self.prevY = tmpoldY

            """
            interesting effect
            if self.Y < 0:
                self.velY = -self.velY
            """
        main_Vars.data_ballGround.blit(self.image, [self.X, self.Y])
        main_Vars.data_rect.append((self.X - 8, self.Y - 8, self.size + 16, self.size + 16))

    def create(self):
        self.image = pygame.Surface([self.size, self.size], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.X
        self.rect.y = self.Y
        # self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, self.outlineColor, (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius - 3)
        main_Vars.data_rect.append((self.X, self.Y, self.size, self.size))
        main_Vars.data_ballGround.blit(self.image, [self.X, self.Y])
        # main_Vars.data_foreGround.blit(self.image, [self.X, self.Y ])


def createBall(ballnum):
    print "=====>Ball #", ballnum, "Created<====="
    ball = Ball(ballnum)
    main_Vars.data_spriteGroup_ball.add(ball)
    main_Vars.data_spriteGroup_ball.sprites()[ballnum - 1].create()
