import pygame

import main_Vars
import main_Modules


class Button(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, X, Y, W, H, color1, color2, newState, text, font, color3, depth=10, middle=False,
                 bold=False, italic=False, usePrevFont=False, Ycor=0, oneUse=True):
        self.X = X
        self.Y = Y
        self.W = W
        self.H = H
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.bold = bold
        self.italic = italic
        self.prev = usePrevFont
        self.font = font
        self.Ycor = Ycor
        # if oneUse is not true, button wont be destroyed after pressed. To destroy it, spritegroup must be called to kill.(to kill all text = "")
        self.oneUse = oneUse
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
            main_Vars.data_rect.append((self.rect[0], self.rect[1], self.W, self.H))
            # self.image.fill((0,0,0,0))
            if state == "d":
                main_Vars.data_buttonClick.play(loops=0)
                self.selfState = "d"
                pygame.draw.rect(self.image, self.color2, (0, 0, self.W, self.H))
                pygame.draw.rect(self.image, (self.color2[0] * 0.6, self.color2[1] * 0.6, self.color2[2] * 0.6),
                                 (self.depth, self.depth, self.W - (self.depth * 2), self.H - (self.depth * 2)))
                main_Vars.data_buttonGround.blit(self.image, (self.X, self.Y))

        elif state == "u" and self.selfState == "d":
            main_Vars.data_buttonRelease.play(loops=0)
            main_Vars.data_rect.append((self.rect[0], self.rect[1], self.W, self.H))
            self.selfState = "u"
            pygame.draw.rect(self.image, self.color1, (0, 0, self.W, self.H))
            pygame.draw.rect(self.image, (self.color2[0] * 0.3, self.color2[1] * 0.3, self.color2[2] * 0.3),
                             (self.depth, self.depth, self.W - (self.depth * 2), self.H - (self.depth * 2)))
            main_Vars.data_buttonGround.blit(self.image, (self.X, self.Y))
            main_Vars.gamemodeChanger(self.newState)
            main_Vars.data_tick1 = False
            if self.oneUse:
                self.kill(self.text)

    def create(self):
        self.image = pygame.Surface([main_Vars.screen.get_size()[0], main_Vars.screen.get_size()[1]], pygame.SRCALPHA,
                                    32)
        pygame.draw.rect(self.image, self.color1, (0, 0, self.W, self.H))
        pygame.draw.rect(self.image, (self.color2[0] * 0.3, self.color2[1] * 0.3, self.color2[2] * 0.3),
                         (self.depth, self.depth, self.W - (self.depth * 2), self.H - (self.depth * 2)))
        self.buttonTextCreate()

    def buttonTextCreate(self):
        if not self.prev:
            self.draw = main_Modules.fitTextDraw(self.font, self.W - 2 * self.depth, self.H - 2 * self.depth, self.text,
                                                 self.X + self.depth, self.Y + self.depth, self.color3,
                                                 bold=self.bold, italic=self.italic, prev=self.prev,
                                                 Ycorrection=self.Ycor, save=True)
        else:
            self.draw = main_Modules.normTextDraw(self.font, self.X + self.W / 2,
                                                  self.Y + (main_Vars.data_savedTextSize[1]) / 2 + self.Ycor,
                                                  self.text, self.color3, bold=self.bold, italic=self.italic,
                                                  size=main_Vars.data_fitTextSize, mid=True)

    def kill(self, text):
        if text == self.text or text == "":
            # if "" is entered it means all sprites will be deleted whatsoever
            main_Vars.data_spriteGroup_buttons.remove(self)
            main_Vars.data_buttonGround.fill((0, 0, 0, 0), (self.X, self.Y, self.W, self.H))
            main_Vars.data_textGround.fill((0, 0, 0, 0), (self.X, self.Y, self.W, self.H))
            updateButtons()


def updateButtons():
    main_Vars.data_buttonGround.fill((0, 0, 0, 0))
    main_Vars.data_spriteGroup_buttons.draw(main_Vars.data_buttonGround)


def buttonCreator(X, Y, W, H, color1, color2, newState, text, font, color3, depth=10, mid=False, bold=False,
                  italic=False, usePrevFont=False, Ycor=0):
    button = Button(X, Y, W, H, color1, color2, newState, text, font, color3, depth=depth, middle=mid,
                    bold=bold, italic=italic, usePrevFont=usePrevFont, Ycor=Ycor)
    main_Vars.data_spriteGroup_buttons.add(button)  # ,something)


def spawnCreatedButtons():
    for i in xrange(len(main_Vars.data_spriteGroup_buttons.sprites())):
        main_Vars.data_spriteGroup_buttons.sprites()[i].create()
    main_Vars.data_spriteGroup_buttons.draw(main_Vars.data_buttonGround)
