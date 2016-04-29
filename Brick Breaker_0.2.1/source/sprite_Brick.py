import random

import pygame

import main_Vars
import pygame.gfxdraw

#CLASSIC BRICK
class Brick(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, col, row, setup, powerup="", lives=1):
        self.col = col
        self.row = row
        self.powerup = powerup
        self.lives = lives
        self.width = main_Vars.data_brickSizeX
        self.height = main_Vars.data_brickSizeY
        self.outline = main_Vars.data_brickOutline
        self.X = self.col * self.width
        self.Y = self.row * self.height + main_Vars.data_brickYMargin
        self.rect = pygame.Rect(self.X, self.Y, self.width, self.height)
        self.brickNum = self.row * 15 + self.col
        self.currentColor = list(setup[0])
        if (self.currentColor[0]) == (self.currentColor[1]) == (self.currentColor[2]):
            self.alpha = 185
        else:
            self.alpha = 80
        # color list example ((0,20,20),(255,0,0))
        #                        last     first     lives
        pygame.sprite.Sprite.__init__(self)

    def hurt(self):
        if self.lives == 1:
            pygame.sprite.Sprite.kill(self)
            main_Vars.data_foreGround.fill((0), pygame.Rect(self.X - self.outline / 2, self.Y - self.outline / 2,
                                                            self.width + self.outline, self.height + self.outline))
            for brick in main_Vars.data_spriteGroup_bricks:
                if (brick.info() == self.brickNum - 1) or (brick.info() == self.brickNum + 1) or (
                    brick.info() == self.brickNum - 15) or (brick.info() == self.brickNum + 15) or (
                    brick.info() == self.brickNum + 16) or (brick.info() == self.brickNum + 14) or (
                    brick.info() == self.brickNum - 14) or (brick.info() == self.brickNum - 16):
                    brick.redraw()
                    # main_Vars.data_foreGround.blit(main_Vars.data_brickImage, [self.X - self.outline / 2, self.Y - self.outline / 2])
                    # drop powerup
        elif self.lives != -1:
            for i in xrange(3):
                self.currentColor[i] = self.currentColor[i]*0.8
            self.create()
            self.image.blit(main_Vars.data_crackImg1,(0,0))
            self.redraw()
            self.lives -= 1
            # redraw
        main_Vars.data_rect.append((self.X - self.outline / 2, self.Y - self.outline / 2, self.width + self.outline,
                                    self.height + self.outline))

    def redraw(self):
        main_Vars.data_foreGround.blit(self.image, [self.X - self.outline / 2, self.Y - self.outline / 2])
        main_Vars.data_rect.append((self.X - self.outline / 2, self.Y - self.outline / 2, self.width + self.outline,
                                    self.height + self.outline))

    def getMid(self):
        return (self.X + self.width / 2, self.Y + self.height / 2)

    def getSize(self):
        return self.width,self.height

    def ballTrigger(self):
        if self.lives == -1:
            main_Vars.data_metalBrick.play(loops=0)
        else:
            play = random.choice(main_Vars.data_brickHits)
            play.play(loops=0)
        self.hurt()

    def create(self):
        self.image = pygame.Surface([self.width + self.outline, self.height + self.outline])
        #self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, main_Vars.BLACK, (0, 0, self.width + self.outline, self.height + self.outline))
        if self.lives == -1:
            self.image.blit(main_Vars.data_metalBrickImg,(self.outline,self.outline),(0,0,self.width-self.outline,self.height-self.outline))
        else:
            self.image.blit(main_Vars.data_brickImg,(self.outline,self.outline),(0,0,self.width-self.outline,self.height-self.outline))
        #pygame.draw.rect(self.image, self.currentColor.append(50),
        #                 (self.outline, self.outline, self.width - self.outline, self.height - self.outline))
        R,G,B = self.currentColor
        A = self.alpha
        pygame.gfxdraw.box(self.image, pygame.Rect(self.outline, self.outline, self.width - self.outline, self.height - self.outline), (R,G,B,A))
        #self.image.fill((R,G,B,A))
        main_Vars.data_rect.append((self.X, self.Y, self.width, self.height))
        main_Vars.data_foreGround.blit(self.image, [self.X - self.outline / 2, self.Y - self.outline / 2])
        self.rect.x = self.X
        self.rect.y = self.Y

    def info(self):
        return self.brickNum







#BIG BRICK
class bigBrick(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, col, row, setup, powerup="",lives = 1):
        self.col = col
        self.row = row
        self.powerup = powerup
        self.lives = 2*lives-1
        self.width = main_Vars.data_brickSizeX*lives
        self.height = main_Vars.data_brickSizeY*lives
        self.outline = main_Vars.data_brickOutline
        self.X = self.col * main_Vars.data_brickSizeX
        self.Y = self.row * main_Vars.data_brickSizeY + main_Vars.data_brickYMargin
        self.rect = pygame.Rect(self.X, self.Y, self.width, self.height)
        self.brickNum = self.row * 15 + self.col
        # color list example ((0,20,20),(255,0,0))
        #                        last     first     lives
        self.currentColor = setup[0]
        pygame.sprite.Sprite.__init__(self)

    def hurt(self):
        if self.lives == 1:
            pygame.sprite.Sprite.kill(self)
            main_Vars.data_foreGround.fill((0), pygame.Rect(self.X - self.outline / 2, self.Y - self.outline / 2,
                                                            self.width + self.outline, self.height + self.outline))
            for brick in main_Vars.data_spriteGroup_bricks:
                if (brick.info() == self.brickNum - 1) or (brick.info() == self.brickNum + 1) or (
                    brick.info() == self.brickNum - 15) or (brick.info() == self.brickNum + 15) or (
                    brick.info() == self.brickNum + 16) or (brick.info() == self.brickNum + 14) or (
                    brick.info() == self.brickNum - 14) or (brick.info() == self.brickNum - 16):
                    brick.redraw()
                    # main_Vars.data_foreGround.blit(main_Vars.data_brickImage, [self.X - self.outline / 2, self.Y - self.outline / 2])
                    # drop powerup
        else:
            main_Vars.data_foreGround.fill((0), pygame.Rect(self.X - self.outline / 2, self.Y - self.outline / 2,
                                                            self.width + self.outline, self.height + self.outline))
            main_Vars.data_rect.append((self.X - self.outline / 2, self.Y - self.outline / 2, self.width + self.outline,
                                    self.height + self.outline))
            self.lives -= 1
            self.width -= main_Vars.data_brickSizeX/2
            self.height -= main_Vars.data_brickSizeY/2
            self.create()
            self.redraw(noRect= True)
            for brick in main_Vars.data_spriteGroup_bricks:
                brick.redraw()
        main_Vars.data_rect.append((self.X - self.outline / 2, self.Y - self.outline / 2, self.width + self.outline,
                                    self.height + self.outline))

    def redraw(self,noRect = False):
        main_Vars.data_foreGround.blit(self.image, [self.X - self.outline / 2, self.Y - self.outline / 2])
        if not noRect:
            main_Vars.data_rect.append((self.X - self.outline / 2, self.Y - self.outline / 2, self.width + self.outline,
                                    self.height + self.outline))

    def getMid(self):
        return (self.X + self.width / 2, self.Y + self.height / 2)

    def getSize(self):
        return self.width,self.height

    def ballTrigger(self):
        main_Vars.data_hardBrick.play(loops=0)
        self.hurt()

    def create(self):
        self.image = pygame.Surface([self.width + self.outline, self.height + self.outline])
        pygame.draw.rect(self.image, main_Vars.BLACK, (0, 0, self.width + self.outline, self.height + self.outline))
        self.image.blit(main_Vars.data_bigBrickImg,(self.outline,self.outline),(0,0,self.width-self.outline,self.height-self.outline))
        self.rect = self.image.get_rect()
        #pygame.draw.rect(self.image, self.currentColor,
           #              (self.outline, self.outline, self.width - self.outline, self.height - self.outline))
        main_Vars.data_rect.append((self.X, self.Y, self.width, self.height))
        main_Vars.data_foreGround.blit(self.image, [self.X - self.outline / 2, self.Y - self.outline / 2])
        self.rect.x = self.X
        self.rect.y = self.Y

    def info(self):
        return self.brickNum


#YUSUF BRICK
class yusufBrick(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, col, row, setup, powerup="",lives = 1):
        self.col = col
        self.row = row
        self.powerup = powerup
        self.lives = lives
        self.multiplier = lives
        self.width = main_Vars.data_brickSizeX*self.multiplier
        self.height = main_Vars.data_brickSizeY*self.multiplier
        self.outline = main_Vars.data_brickOutline
        self.X = self.col * main_Vars.data_brickSizeX
        self.Y = self.row * main_Vars.data_brickSizeY + main_Vars.data_brickYMargin
        self.rect = pygame.Rect(self.X, self.Y, self.width, self.height)
        self.brickNum = self.row * 15 + self.col
        # color list example ((0,20,20),(255,0,0))
        #                        last     first     lives
        self.currentColor = setup[0]
        pygame.sprite.Sprite.__init__(self)

    def hurt(self):
        if self.lives != 1:
            self.kill()
            createBrick(self.col,self.row,[self.currentColor,"yusuf"],self.powerup, self.lives/2)
            createBrick(self.col+(self.lives/2),self.row,[self.currentColor,"yusuf"],self.powerup, self.lives/2)
            createBrick(self.col,self.row+(self.lives/2),[self.currentColor,"yusuf"],self.powerup, self.lives/2)
            createBrick(self.col+(self.lives/2),self.row+(self.lives/2),[self.currentColor,"yusuf"],self.powerup, self.lives/2)
        else:

            self.kill()
            main_Vars.data_foreGround.fill((0), pygame.Rect(self.X - self.outline / 2, self.Y - self.outline / 2,
                                                            self.width + self.outline, self.height + self.outline))

        main_Vars.data_rect.append((self.X - self.outline / 2, self.Y - self.outline / 2, self.width + self.outline,
                                    self.height + self.outline))

    def redraw(self,noRect = False):
        main_Vars.data_foreGround.blit(self.image, [self.X - self.outline / 2, self.Y - self.outline / 2])
        if not noRect:
            main_Vars.data_rect.append((self.X - self.outline / 2, self.Y - self.outline / 2, self.width + self.outline,
                                    self.height + self.outline))

    def getMid(self):
        return (self.X + self.width / 2, self.Y + self.height / 2)

    def getSize(self):
        return self.width,self.height

    def ballTrigger(self):
        main_Vars.data_hardBrick.play(loops=0)
        self.hurt()

    def create(self):
        self.image = pygame.Surface([self.width + self.outline, self.height + self.outline])
        pygame.draw.rect(self.image, main_Vars.BLACK, (0, 0, self.width + self.outline, self.height + self.outline))
        self.image.blit(main_Vars.data_yusufBrickImg,(self.outline,self.outline),(0,0,self.width-self.outline,self.height-self.outline))
        self.rect = self.image.get_rect()
        #pygame.draw.rect(self.image, self.currentColor,
           #              (self.outline, self.outline, self.width - self.outline, self.height - self.outline))
        main_Vars.data_rect.append((self.X, self.Y, self.width, self.height))
        main_Vars.data_foreGround.blit(self.image, [self.X - self.outline / 2, self.Y - self.outline / 2])
        self.rect.x = self.X
        self.rect.y = self.Y

    def info(self):
        return self.brickNum



def createBrick(col, row, setup, powerup, lives):
    print "$#$ | BRICK", row * 15 + col, "|", "-row:", row, " -col:", col, " -Color:", setup[0], " -Powerup:", powerup, " -Lives:", lives ,"-Setup",setup[1:]
    if len(setup) == 1:
        brick = Brick(col, row, setup, powerup, lives)
        main_Vars.data_spriteGroup_bricks.add(brick)
    elif setup[1] == "big":
        brick = bigBrick(col,row,setup,powerup,lives)
        main_Vars.data_spriteGroup_bricks.add(brick)
    elif setup[1] == "yusuf":
        print main_Vars.data_spriteGroup_bricks
        brick = yusufBrick(col,row,setup,powerup,lives)
        main_Vars.data_spriteGroup_bricks.add(brick)
        brick.create()

def createLevelBricks(level):
    rows = len(level)
    cols = len(level[0])
    for row in xrange(rows):
        for col in xrange(cols):
            if not level[row][col] == [None]:
                createBrick(col, row, level[row][col][0], level[row][col][1], level[row][col][2])
    for sprite in xrange(len(main_Vars.data_spriteGroup_bricks.sprites())):
        main_Vars.data_spriteGroup_bricks.sprites()[sprite].create()
