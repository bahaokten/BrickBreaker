from math import pi

import pygame

import main_Vars


class Paddle(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position

    def __init__(self, x, state, size, velX):
        self.state = state
        self.velX = velX
        self.size = size
        self.rect = []
        self.add = 0
        if size == "medium":
            self.add = 0
        elif size == "small":
            self.add = -20
        else:
            self.add = 20
        self.X = (main_Vars.data_canvasX - 98 + self.add) / 2
        print "-size:", size, " -Velocity:", self.velX, " -State:", self.state
        main_Vars.data_paddleWidth = 98 + self.add
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        if main_Vars.data_left:
            if self.X < 2 * self.velX:
                self.X = 0
                main_Vars.data_rect.append((0, main_Vars.data_paddleY, 98 + self.add + 2 * self.velX, 21))
            else:
                self.X -= self.velX
                main_Vars.data_rect.append((self.X, main_Vars.data_paddleY, 98 + self.add + self.velX, 21))
            #main_Vars.data_paddleGround.fill((1, 2, 3))
            #main_Vars.data_paddleGround.blit(self.image, [self.X, 0])
        elif main_Vars.data_right:
            if main_Vars.data_canvasX - self.X - self.add - 98 - self.velX < self.velX:
                self.X = main_Vars.data_canvasX - self.add - 98
                main_Vars.data_rect.append(
                    (self.X - 2 * self.velX, main_Vars.data_paddleY, 98 + self.add + 2 * self.velX, 21))
            else:
                main_Vars.data_rect.append((self.X, main_Vars.data_paddleY, 98 + self.add + self.velX, 21))
                self.X += self.velX
        main_Vars.data_paddleMidX = self.X + (98 + self.add) / 2
        #main_Vars.data_paddleGround.fill((1, 2, 3))
        #main_Vars.data_paddleGround.blit(self.image, [self.X, 0])
        self.rect.x = self.X
        self.rect.y = main_Vars.data_paddleY

    def create(self):
        self.image = pygame.Surface([self.add + 98, 21], pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x = self.X
        self.rect.y = main_Vars.data_paddleY
        # self.image = self.image.convert_alpha()
        #self.image.fill((1, 2, 3))
        pygame.draw.ellipse(self.image, main_Vars.BLACK, (0, 0, 35, 20))
        pygame.draw.arc(self.image, (55, 55, 55), (0, 0, 35, 20), pi / 2, 3 * pi / 2, 3)
        pygame.draw.ellipse(self.image, main_Vars.BLACK, (self.add + 63, 0, 35, 20))
        pygame.draw.arc(self.image, (55, 55, 55), (self.add + 63, 0, 35, 20), 3 * pi / 2, 5 * pi / 2, 3)
        pygame.draw.rect(self.image, main_Vars.BLACK, (18, 0, self.add + 62, 20))
        pygame.draw.polygon(self.image, (155, 0, 0), ((18, 20), (28, 0), (38, 20)))
        pygame.draw.polygon(self.image, (155, 0, 0), ((self.add + 80, 20), (self.add + 70, 0), (self.add + 60, 20)))
        pygame.draw.line(self.image, (55, 55, 55), (18, 0), (self.add + 80, 0), 5)
        pygame.draw.line(self.image, (55, 55, 55), (18, 20), (self.add + 80, 20), 5)
        main_Vars.data_rect.append((self.X, main_Vars.data_paddleY, 98 + self.add, 21))
        main_Vars.data_paddleImg = self.image
        #main_Vars.data_paddleGround.fill((1, 2, 3))
        #main_Vars.data_paddleGround.blit(self.image, [self.X, 0])

    def info(self,posOnly = False):
        if posOnly:
            return (self.X,main_Vars.data_paddleY)
        else:
            return (self.rect)


def paddleCreator():
    print "=====>Paddle Created<====="
    paddle = Paddle(350, "-", "medium", 5)
    main_Vars.data_spriteGroup_paddle.add(paddle)  # ,something)
    main_Vars.data_spriteGroup_paddle.sprites()[0].create()
    # main_Vars.data_spriteGroup_paddle.draw(main_Vars.data_paddleGround)
