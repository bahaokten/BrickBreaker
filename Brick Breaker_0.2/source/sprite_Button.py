import pygame

import main_Vars
import main_Modules


class Button(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, X, Y, W, H, R1, G1, B1, R2, G2, B2, newState, text, font, R3, G3, B3, depth=10, middle=False,
                 bold=False, italic=False, usePrevFont=False, Ycor=0):
        self.X = X
        self.Y = Y
        self.W = W
        self.H = H
        self.R1 = R1
        self.G1 = G1
        self.B1 = B1
        self.R2 = R2
        self.G2 = G2
        self.B2 = B2
        self.R3 = R3
        self.G3 = G3
        self.B3 = B3
        self.bold = bold
        self.italic = italic
        self.prev = usePrevFont
        self.font = font
        self.Ycor = Ycor
        # NEW GAME STATE ISSUED
        self.newState = newState
        self.depth = depth
        self.middle = middle
        self.isPressed = False
        self.text = text
        self.selfState = "u"
        if middle:
            self.X, self.Y = main_Modules.objMid(self.X, self.Y, self.W, self.H)
            self.rect = [self.X, self.Y]
        else:
            self.rect = [X, Y]
        pygame.sprite.Sprite.__init__(self)

    def update(self, state):
        if main_Modules.mouseCollision(self.X, self.Y, self.W, self.H):
            main_Vars.data_rect.append((self.rect[0],self.rect[1],self.W,self.H))
            # self.image.fill((0,0,0,0))
            if state == "d":
                self.selfState = "d"
                pygame.draw.rect(self.image, (self.R2, self.G2, self.B2), (0, 0, self.W, self.H))
                pygame.draw.rect(self.image, (self.R2 * 0.6, self.G2 * 0.6, self.B2 * 0.6),
                                 (self.depth, self.depth, self.W - (self.depth * 2), self.H - (self.depth * 2)))
                main_Vars.data_buttonground.blit(self.image, (self.X, self.Y))

        elif state == "u" and self.selfState == "d":
            main_Vars.data_rect.append((self.rect[0],self.rect[1],self.W,self.H))
            self.selfState = "u"
            pygame.draw.rect(self.image, (self.R1, self.G1, self.B1), (0, 0, self.W, self.H))
            pygame.draw.rect(self.image, (self.R2 * 0.3, self.G2 * 0.3, self.B2 * 0.3),
                             (self.depth, self.depth, self.W - (self.depth * 2), self.H - (self.depth * 2)))
            main_Vars.data_buttonground.blit(self.image, (self.X, self.Y))

    def create(self):
        self.image = pygame.Surface([main_Vars.screen.get_size()[0], main_Vars.screen.get_size()[1]], pygame.SRCALPHA,
                                    32)
        pygame.draw.rect(self.image, (self.R1, self.G1, self.B1), (0, 0, self.W, self.H))
        pygame.draw.rect(self.image, (self.R2 * 0.3, self.G2 * 0.3, self.B2 * 0.3),
                         (self.depth, self.depth, self.W - (self.depth * 2), self.H - (self.depth * 2)))
        self.buttonTextCreate()

    def buttonTextCreate(self):
        self.draw = main_Modules.fitTextDraw(self.font, self.W - 2 * self.depth, self.H - 2 * self.depth, self.text,
                                            self.X + self.depth, self.Y + self.depth, self.R3, self.G3, self.B3,
                                            bold=self.bold, italic=self.italic, prev=self.prev, Ycorrection=self.Ycor)

    def kill(self, text):
        if text == self.text or text == "":
            # if "" is entered it means all sprites will be deleted whatsoever
            main_Vars.data_spriteGroup_buttons.remove(self)
            main_Vars.data_buttonground.fill((0, 0, 0, 0), (self.X, self.Y, self.W, self.H))
            updateButtons(main_Vars.data_buttonground)


def updateButtons(ground):
    main_Vars.data_buttonground.fill((0, 0, 0, 0))
    main_Vars.data_spriteGroup_buttons.draw(ground)


def buttonCreator(X, Y, W, H, R1, G1, B1, R2, G2, B2, newState, text, font, R3, G3, B3, depth=10, mid=False, bold=False,
                  italic=False, usePrevFont=False, Ycor=0):
    button = Button(X, Y, W, H, R1, G1, B1, R2, G2, B2, newState, text, font, R3, G3, B3, depth=depth, middle=mid,
                    bold=bold, italic=italic, usePrevFont=usePrevFont, Ycor=Ycor)
    main_Vars.data_spriteGroup_buttons.add(button)  # ,something)


def spawnCreatedButtons(ground):
    for i in xrange(len(main_Vars.data_spriteGroup_buttons.sprites())):
        main_Vars.data_spriteGroup_buttons.sprites()[i].create()
    main_Vars.data_spriteGroup_buttons.draw(ground)
