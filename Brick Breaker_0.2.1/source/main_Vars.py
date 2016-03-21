from __future__ import print_function, division
import pygame
from pygame.locals import *

RED = (255, 0, 0)
BLACK = (0, 0, 0)
LIGHTBLACK = (20, 20, 20)
WHITE = (255, 255, 255)
GREEN = (0, 155, 0)
BLUE = (0, 0, 155)
LIGHTGRAY = (136, 136, 136)
GRAY = (70, 70, 70)
ORANGE = (255, 102, 0)
YELLOW = (255, 255, 0)
DARKGREEN = (0, 80, 0)
DARKRED = (139, 0, 0)
GOLD = (212, 175, 55)
SILVER = (192, 192, 192)
CHROME = (227, 222, 219)
ROSE = (255, 0, 127)
EMERALD = (80, 200, 120)

data_updateAll = False
data_state = "menu"
data_canvasX = 960
data_canvasY = 700
# Used by button module
data_tmp = ()
# rects needed to be drawn
data_rect = [(0, 0, data_canvasX, data_canvasY)]
# tick used by menus etc
data_tick1 = False

###############################################################################################################################################3
# -------Sprites--------#
data_allSprites = pygame.sprite.Group()
# --BUTTON--#
data_spriteGroup_buttons = pygame.sprite.Group()
# ---PADDLE---#
data_spriteGroup_paddle = pygame.sprite.Group()
# ---BRICKS--#
data_spriteGroup_bricks = pygame.sprite.Group()
###############################################################################################################################################3

# ---FONTS&TEXTS---#
data_textSize = 0
data_fontFile1 = "Resources/Font_1.ttf"
data_fontFile2 = "Resources/Font_2.ttf"


# ---BRICKS---#
data_brickSizeX = 64
data_brickSizeY = 25
data_brickSizeXSelect = 13
data_brickSizeYSelect = 5
data_brickYMargin = 10

# Paddle#
data_paddleY = 300


################################################### ---INPUT---####################################3

data_left = False
data_right = False


# ###############################################3---LEVEL---##################################33
data_currentLevel = []
data_lvlLayout = [[[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]]
data_isLevel1 = True
data_isLevel2 = False
data_level1 = [
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(LIGHTBLACK)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]],
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(LIGHTBLACK)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]],
    [[], [], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1], [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1],
     [[(LIGHTBLACK)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [([(ORANGE)]), "-", 1], [], []],
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(LIGHTBLACK)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]],
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(LIGHTBLACK)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]],
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(LIGHTBLACK)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]],
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(LIGHTBLACK)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]],
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(LIGHTBLACK)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]]]

data_level2 = [[[[(GREEN)], "-", 1], [], [], [[(ORANGE)], "-", 1], [], [[(ORANGE)], "-", 1], [[(GREEN)], "-", 1], [], [], [[(GREEN)], "-", 1], [[(ORANGE)], "-", 1], [], [], [], []],
                  [[[(GREEN)], "-", 1], [[(ORANGE)], "-", 1], [], [], [], [], [], [], [[(GREEN)], "-", 1], [], [], [], [], [], [[(ORANGE)], "-", 1]]]



def levelHandler(level):
    if level == 1:
        return data_level1
    elif level ==2:
        return data_level2


def isLevelHandler(level):
    if level == 1:
        return data_isLevel1
    elif level == 2:
        return data_isLevel2

##########GROUNDS####################################
# color,powerup,lives
# [["white","-",1]]
# flags = FULLSCREEN | DOUBLEBUF
flags = DOUBLEBUF
screen = pygame.display.set_mode((960, 700))
data_backGround = pygame.Surface(screen.get_size())
data_paddleGround = pygame.Surface((960, 21))
data_foreGround = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
data_foreGround = data_foreGround.convert_alpha()
data_buttonGround = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
data_buttonGround = data_buttonGround.convert_alpha()
data_textGround = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
data_textGround = data_textGround.convert_alpha()
data_backGround = data_backGround.convert()
data_mousePressedPos = ()
data_paddleGround.set_colorkey((1, 2, 3), RLEACCEL)
