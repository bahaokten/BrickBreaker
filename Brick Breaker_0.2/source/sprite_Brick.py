import pygame

import main_Vars
import main_Modules


class Brick(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, col, row, colorList , powerup = "", lives=1):
        self.col = col
        self.row = row
        self.powerup = powerup
        self.lives = lives
        self.colorList = colorList
        self.width = main_Vars.data_brickSizeX
        self.height = main_Vars.data_brickSizeY
        self.outline = 5
        self.X= self.col*self.width
        self.Y= self.row*self.height
        # color list example ((0,20,20),(255,0,0))
        #                        last     first     lives
        self.currentColor = colorList[self.lives-1]
        pygame.sprite.Sprite.__init__(self)

    def hurt(self):
        if self.lives == 1:
            None
            #kill
            #drop powerup
        else:
            self.lives -= 1
            self.currentColor = self.colorList[self.lives-1]
            #redraw

    def create(self):
        self.image = pygame.Surface([98, 21], pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, self.currentColor, (self.X,  self.Y, self.width, self.height))
        pygame.draw.rect(self.image, main_Vars.BLACK, (self.X, self.Y, self.width, self.height), self.outline)
        main_Vars.data_rect.append((self.X,self.Y,self.width,self.height))


def createBrick(col,row,colorList,powerup,lives):
    brick = Brick(col,row,colorList,powerup,lives)
    main_Vars.data_spriteGroup_bricks.add(brick)