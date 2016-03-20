import pygame

import main_Vars


class Brick(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, col, row, colorList, powerup="", lives=1):
        self.col = col
        self.row = row
        self.powerup = powerup
        self.lives = lives
        self.colorList = colorList
        self.width = main_Vars.data_brickSizeX
        self.height = main_Vars.data_brickSizeY
        self.outline = 6
        self.X = self.col * self.width
        self.Y = self.row * self.height + main_Vars.data_brickYMargin
        # color list example ((0,20,20),(255,0,0))
        #                        last     first     lives
        self.currentColor = colorList[self.lives - 1]
        pygame.sprite.Sprite.__init__(self)

    def hurt(self):
        if self.lives == 1:
            None
            # kill
            # drop powerup
        else:
            self.lives -= 1
            self.currentColor = self.colorList[self.lives - 1]
            # redraw

    def create(self):
        self.image = pygame.Surface([self.width + self.outline, self.height + self.outline], pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, main_Vars.BLACK, (0, 0, self.width + self.outline, self.height + self.outline))
        pygame.draw.rect(self.image, self.currentColor,
                         (self.outline, self.outline, self.width - self.outline, self.height - self.outline))
        main_Vars.data_rect.append((self.X, self.Y, self.width, self.height))
        main_Vars.data_foreGround.blit(self.image, [self.X - self.outline / 2, self.Y - self.outline / 2])


def createBrick(col, row, colorList, powerup, lives):
    brick = Brick(col, row, colorList, powerup, lives)
    main_Vars.data_spriteGroup_bricks.add(brick)


def createLevelBricks(level):
    rows = len(level)
    cols = len(level[0])
    for row in xrange(rows):
        for col in xrange(cols):
            if not level[row][col] == []:
                createBrick(col, row, level[row][col][0], level[row][col][1], level[row][col][2])
    for sprite in xrange(len(main_Vars.data_spriteGroup_bricks.sprites())):
        main_Vars.data_spriteGroup_bricks.sprites()[sprite].create()
        print ("done", sprite)
