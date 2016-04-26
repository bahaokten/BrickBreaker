import random

import pygame

import main_Vars


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

    def ballTrigger(self):
        play = random.choice(main_Vars.data_brickHits)
        play.play(loops=0)
        self.hurt()

    def create(self):
        self.image = pygame.Surface([self.width + self.outline, self.height + self.outline])
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, main_Vars.BLACK, (0, 0, self.width + self.outline, self.height + self.outline))
        pygame.draw.rect(self.image, self.currentColor,
                         (self.outline, self.outline, self.width - self.outline, self.height - self.outline))
        main_Vars.data_rect.append((self.X, self.Y, self.width, self.height))
        main_Vars.data_foreGround.blit(self.image, [self.X - self.outline / 2, self.Y - self.outline / 2])
        self.rect.x = self.X
        self.rect.y = self.Y

    def info(self):
        return self.brickNum


def createBrick(col, row, colorList, powerup, lives):
    print "$#$ | BRICK", row * 15 + col, "|", "-row:", row, " -col:", col, " -Color List:", colorList, " -Powerup:", powerup, " -Lives:", lives
    brick = Brick(col, row, colorList, powerup, lives)
    main_Vars.data_spriteGroup_bricks.add(brick)


def createLevelBricks(level):
    rows = len(level)
    cols = len(level[0])
    for row in xrange(rows):
        for col in xrange(cols):
            if not level[row][col] == [None]:
                createBrick(col, row, level[row][col][0], level[row][col][1], level[row][col][2])
    for sprite in xrange(len(main_Vars.data_spriteGroup_bricks.sprites())):
        main_Vars.data_spriteGroup_bricks.sprites()[sprite].create()
