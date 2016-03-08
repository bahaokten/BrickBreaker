from math import pi
from pygame import event
import pygame

import main_Vars


class Paddle(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position

    def __init__(self, x, y, state, size, velX):
        self.state = state
        self.velX = velX
        self.size = size
        self.rect = [x, y]
        self.add = 0
        if size == "medium":
            self.add = 0
        elif size == "small":
            self.add = -20
        else:
            self.add = 20
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        if main_Vars.data_left:
            self.rect[0] -= self.velX
            #pygame.draw.rect(main_Vars.data_actionground, (0,0,0,0), (self.rect[0]+self.add+78,self.rect[1],40,21))
            main_Vars.data_actionground.fill((1, 2, 3))
            main_Vars.data_actionground.blit(self.image, self.rect)
            main_Vars.screen.blit(main_Vars.data_actionground, (0, 0))
        elif main_Vars.data_right:
            self.rect[0] += self.velX
            #pygame.draw.rect(main_Vars.data_actionground, (0,0,0,0), (self.rect[0]-self.velX,self.rect[1],self.velX +20 , 21))
            main_Vars.data_actionground.blit(self.image, self.rect)
            main_Vars.screen.blit(main_Vars.data_actionground, (0, 0))

    def create(self):
        self.image = pygame.Surface([self.add + 98, 21])
        #self.image = self.image.convert_alpha()
        pygame.draw.ellipse(self.image, main_Vars.BLACK, (0, 0, 35, 20))
        pygame.draw.arc(self.image, (55, 55, 55), (0, 0, 35, 20), pi / 2, 3 * pi / 2, 3)
        pygame.draw.ellipse(self.image, main_Vars.BLACK, (self.add + 63, 0, 35, 20))
        pygame.draw.arc(self.image, (55, 55, 55), (self.add + 63, 0, 35, 20), 3 * pi / 2, 5 * pi / 2, 3)
        pygame.draw.rect(self.image, main_Vars.BLACK, (18, 0, self.add + 62, 20))
        pygame.draw.polygon(self.image, (155, 0, 0), ((18, 20), (28, 0), (38, 20)))
        pygame.draw.polygon(self.image, (155, 0, 0), ((self.add + 80, 20), (self.add + 70, 0), (self.add + 60, 20)))
        pygame.draw.line(self.image, (55, 55, 55), (18, 0), (self.add + 80, 0), 5)
        pygame.draw.line(self.image, (55, 55, 55), (18, 20), (self.add + 80, 20), 5)


    def info(self):
        print(self.rect)


def paddleCreator():
    paddle = Paddle(350, 200, "-", "medium", 15)
    main_Vars.data_spriteGroup_paddle.add(paddle)  # ,something)
    # assert isinstance(main_Vars.data_spriteGroup_paddle.sprites().create, object)
    main_Vars.data_spriteGroup_paddle.sprites()[0].create()
    main_Vars.data_spriteGroup_paddle.draw(main_Vars.data_actionground)
    main_Vars.screen.blit(main_Vars.data_actionground, (0, 0))
