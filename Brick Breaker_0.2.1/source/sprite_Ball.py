import random
import math

import pygame

import main_Vars
import main_Modules


class Ball(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, ballnum, isAttached=True):
        self.size = 18
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
        self.totalVel = 5
        self.totalVelSquared = math.pow(self.totalVel, 2)
        self.velX = 0
        self.velY = 0
        self.cooldownTimer = 6
        self.cooldown = 0
        print "-ballnum:", self.ballnum, " -X:", self.X, " -Y:", self.Y, " -Radius:", self.radius
        print "-innerColor:", self.color, " -outlineColor:", self.outlineColor

    def update(self):
        main_Vars.data_rect.append((self.X - 8, self.Y - 8, self.size + 16, self.size + 16))
        if self.cooldown:
            self.cooldown -= 1
        if self.attachedToBall:
            self._attached_handler()
        else:
            # FIRST PART VELOCITY ADDITION
            self._velocity_incrementer_handler()
            # SECOND PART WALL COLLISION
            if not self._wall_collision_handler():
                # THIRD PART PADDLE COLLISION
                if not self._paddle_collision_handler():
                    # FOURTH PART BRICK COLLISION
                    self._brick_collision_handler()

        main_Vars.data_ballGround.blit(self.image, [self.X, self.Y])
        main_Vars.data_rect.append((self.X - 8, self.Y - 8, self.size + 16, self.size + 16))

    def _velocity_incrementer_handler(self):
        tmpoldX = self.X
        tmpoldY = self.Y
        self.X += self.velX
        self.Y += self.velY
        self.prevX = tmpoldX
        self.prevY = tmpoldY
        self.rect.x = self.X
        self.rect.y = self.Y

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

    def _attached_handler(self):
        if main_Vars.data_left or main_Vars.data_right:
            main_Vars.data_rect.append((self.X, self.Y, self.size, self.size))
            self.X = main_Vars.data_paddleMidX - self.radius
            main_Vars.data_rect.append((self.X, self.Y, self.size, self.size))
        elif main_Vars.data_space:
            main_Vars.data_thrown.play(loops=0)
            print "$#$ | BALL", self.ballnum, "|", "is detached from | PADDLE |!"
            self.attachedToBall = False
            tmp1 = random.randint(int(self.totalVelSquared * 0.75 * 0.5), int(self.totalVelSquared * 1.25 * 0.5))
            print tmp1
            tmp2 = math.sqrt(tmp1)
            self.velX = int(random.choice([1, -1]) * tmp2)
            self.velY = -int(math.sqrt(self.totalVelSquared - tmp1))
            print "$#$ | BALL", self.ballnum, "|", "-VelX:", self.velX, " -VelY:", self.velY

    def _wall_collision_handler(self):
        if self.X + self.size > main_Vars.data_canvasX:
            main_Vars.data_brick2.play(loops=0)
            self.velX = -self.velX
            print "$#$ | BALL", self.ballnum, "|", "collided with | RIGHT WALL |  at", self.X, self.Y, ".Its new velocity is -VelX:", self.velX, " -VelY:", self.velY
            return True
        elif self.X < 0:
            main_Vars.data_brick2.play(loops=0)
            self.velX = -self.velX
            print "$#$ | BALL", self.ballnum, "|", "collided with | LEFT WALL |  at", self.X, self.Y, ".Its new velocity is -VelX:", self.velX, " -VelY:", self.velY
            return True
        elif self.Y < 0:
            main_Vars.data_brick2.play(loops=0)
            self.Y = 0
            self.velY = -self.velY
            print "$#$ | BALL", self.ballnum, "|", "collided with | UPPER WALL |  at", self.X, self.Y, ".Its new velocity is -VelX:", self.velX, " -VelY:", self.velY
            return True
        elif self.Y > main_Vars.data_canvasY:
            # main_Vars.gamemodeChanger("gameoverbad")
            self.velY = -self.velY
            return True
        else:
            return False

    def _paddle_collision_handler(self):
        if pygame.sprite.collide_rect(self, main_Vars.data_spriteGroup_paddle.sprites()[0]):
            main_Vars.data_paddleHitSound.play(loops=0)
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
        else:
            return False

    def _brick_collision_subhandler(self, tmpMid, midX, midY, bricks, update=True):
        if tmpMid[1] + (main_Vars.data_brickSizeY / 2) > midY > tmpMid[1] - (main_Vars.data_brickSizeY / 2):
            if (midX < tmpMid[0] - (main_Vars.data_brickSizeX / 2)) or (
                midX > tmpMid[0] + (main_Vars.data_brickSizeX / 2)):
                if update:
                    self.velX = -self.velX
                    self.X += self.velX
                    self.Y += self.velY
                    self.cooldown = self.cooldownTimer
                    self._brick_collision_info(bricks, "Left/Right")
                return "LR"
            else:
                return False
        elif tmpMid[0] + (main_Vars.data_brickSizeX / 2) > midX > tmpMid[0] - (main_Vars.data_brickSizeX / 2):
            if (midY < tmpMid[1] - (main_Vars.data_brickSizeY / 2)) or (
                midY > tmpMid[1] + (main_Vars.data_brickSizeY / 2)):
                if update:
                    self.velY = -self.velY
                    self.X += self.velX
                    self.Y += self.velY
                    self.cooldown = self.cooldownTimer
                    self._brick_collision_info(bricks, "Up/Down")
                return "UD"
            else:
                return False
        return False

    def _brick_collision_info(self, bricks, collisionType):
        if len(bricks) == 1:
            print "$#$ | BALL", self.ballnum, "|", "collided with | BRICK", \
                bricks[
                    0].info(), "| at", self.X, self.Y, ". Its new velocity is -VelX:", self.velX, " -VelY:", self.velY, "-Collision Type:", collisionType
        else:
            print "$#$ | BALL", self.ballnum, "|", "collided with | BRICKS", \
                bricks[0].info(), "and", bricks[
                1].info(), "| at", self.X, self.Y, ". Its new velocity is -VelX:", self.velX, " -VelY:", self.velY, "-Collision Type:", collisionType

    def _brick_collision_handler(self):
        if 1 == 1:
            if not self.cooldown:
                tmpsprites = []
                # which bricks collide
                for sprite in main_Vars.data_spriteGroup_bricks.sprites():
                    if pygame.sprite.collide_rect(sprite, self):
                        tmpsprites.append(sprite)
                        sprite.ballTrigger()
                if len(tmpsprites) == 1:
                    play = random.choice(main_Vars.data_brickHits)
                    play.play(loops=0)

                    tmpMid = tmpsprites[0].getMid()
                    midX = self.prevX + self.size / 2
                    midY = self.prevY + self.size / 2

                    if not self._brick_collision_subhandler(tmpMid, midX, midY, tmpsprites):
                        s = 0.390625
                        sNeg = -s
                        s2 = self.velY / self.velX
                        if ((midX < tmpMid[0] - (main_Vars.data_brickSizeX / 2)) and (
                            midY > tmpMid[1] + (main_Vars.data_brickSizeY / 2))) or (
                            (midX > tmpMid[0] + (main_Vars.data_brickSizeX / 2)) and (
                            midY < tmpMid[1] - (main_Vars.data_brickSizeY / 2))):
                            # bottom left / top right
                            c1 = main_Modules.linearEquation((tmpMid[0] - (main_Vars.data_brickSizeX / 2),
                                                              tmpMid[1] - (main_Vars.data_brickSizeY / 2)), sNeg)
                            p1 = ([tmpMid[0], tmpMid[1]], [0, c1])  # brick point
                            c2 = main_Modules.linearEquation((midX, midY), s2)
                            p2 = ([midX, midY], [tmpMid[0], tmpMid[0] * s2 + c2])
                            intersect = main_Modules.intersection(p1, p2)
                            if (s2 < 0) and ((midY < -s * midX + main_Modules.linearEquation(
                                    (tmpMid[0] - (main_Vars.data_brickSizeX / 2),
                                     tmpMid[1] + (main_Vars.data_brickSizeY / 2)),
                                    -s)) or (midY > -s * midX + main_Modules.linearEquation(
                                (tmpMid[0] + (main_Vars.data_brickSizeX / 2),
                                 tmpMid[1] - (main_Vars.data_brickSizeY / 2)),
                                -s))):
                                # top right/bottomleft
                                if intersect == False:
                                    self.velX = -self.velX
                                    self.X += self.velX
                                    self.Y += self.velY
                                    self.cooldown = self.cooldownTimer
                                else:
                                    self.velY = -self.velY
                                    self.X += self.velX
                                    self.Y += self.velY
                                    self.cooldown = self.cooldownTimer
                                self._brick_collision_info(tmpsprites, "TopRight/BottomLeft")
                            elif s2 < 0:
                                if intersect != False:
                                    self.velX = -self.velX
                                    self.X += self.velX
                                    self.Y += self.velY
                                    self.cooldown = self.cooldownTimer
                                else:
                                    self.velY = -self.velY
                                    self.X += self.velX
                                    self.Y += self.velY
                                    self.cooldown = self.cooldownTimer
                                self._brick_collision_info(tmpsprites, "TopRight/BottomLeft")
                        else:
                            # top left bottom right
                            print "top left/bottom right"
                            c1 = main_Modules.linearEquation((tmpMid[0] - (main_Vars.data_brickSizeX / 2),
                                                              tmpMid[1] - (main_Vars.data_brickSizeY / 2)), s)
                            p1 = (
                            [tmpMid[0] - (main_Vars.data_brickSizeX / 2), tmpMid[1] - (main_Vars.data_brickSizeY / 2)],
                            [0, c1])  # brick point
                            c2 = main_Modules.linearEquation((midX, midY), s2)
                            p2 = ([midX, midY], [tmpMid[0], tmpMid[0] * s2 + c2])
                            intersect = main_Modules.intersection(p1, p2)
                            if (s2 > 0) and ((midY > s * midX + main_Modules.linearEquation(
                                    (tmpMid[0] - (main_Vars.data_brickSizeX / 2),
                                     tmpMid[1] - (main_Vars.data_brickSizeY / 2)),
                                    s)) or (midY < s * midX + main_Modules.linearEquation(
                                (tmpMid[0] + (main_Vars.data_brickSizeX / 2),
                                 tmpMid[1] + (main_Vars.data_brickSizeY / 2)),
                                s))):
                                # top left
                                if intersect == False:
                                    self.velX = -self.velX
                                    self.X += self.velX
                                    self.Y += self.velY
                                    self.cooldown = self.cooldownTimer
                                else:
                                    self.velY = -self.velY
                                    self.X += self.velX
                                    self.Y += self.velY
                                    self.cooldown = self.cooldownTimer
                                self._brick_collision_info(tmpsprites, "TopLeft/BottomRight")
                            elif s2 > 0:
                                if intersect != False:
                                    self.velX = -self.velX
                                    self.X += self.velX
                                    self.Y += self.velY
                                    self.cooldown = self.cooldownTimer
                                else:
                                    self.velY = -self.velY
                                    self.X += self.velX
                                    self.Y += self.velY
                                    self.cooldown = self.cooldownTimer
                                self._brick_collision_info(tmpsprites, "TopLeft/BottomRight")
                elif tmpsprites != []:
                    updown = False
                    leftright = False
                    midX = self.prevX + self.size / 2
                    midY = self.prevY + self.size / 2
                    for bricks in tmpsprites:
                        tmpMid = bricks.getMid()
                        tmpUpdate = self._brick_collision_subhandler(tmpMid, midX, midY, bricks, update=False)
                        if tmpUpdate == "UD":
                            updown = True
                        elif tmpUpdate == "LR":
                            leftright = True
                    if updown:
                        self.velY = -self.velY
                        self.X += self.velX
                        self.Y += self.velY
                        self.cooldown = self.cooldownTimer
                    if leftright:
                        self.velX = -self.velX
                        self.X += self.velX
                        self.Y += self.velY
                        self.cooldown = self.cooldownTimer
                        say = "Left/Right"
                    elif updown:
                        say = "Up/Down"
                    else:
                        say = "Left/Right AND Up/Down"
                    self._brick_collision_info(tmpsprites, say)

    def _get_deltas(self, other_object):
        dx = self.rect.x - other_object.rect.x
        if dx < 0:
            dx *= -1
        dy = self.rect.y - other_object.rect.y
        if dy < 0:
            dy *= -1
        return (dx, dy)


def createBall(ballnum):
    print "=====>Ball #", ballnum, "Created<====="
    ball = Ball(ballnum)
    main_Vars.data_spriteGroup_ball.add(ball)
    main_Vars.data_spriteGroup_ball.sprites()[ballnum - 1].create()
