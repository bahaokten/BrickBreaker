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
ORANGE = (255, 102, 0)
YELLOW = (255, 255, 0)
DARKGREEN = (0, 80, 0)
DARKRED = (139, 0, 0)
GOLD = (212,175,55)
SILVER = (192,192,192)
CHROME = (227,222,219)
ROSE = (255, 0, 127)
EMERALD = (80,200,120)

data_state = "menu"
data_canvasX = 960
data_canvasY = 700
data_tmp = ()
data_tick1 = False
# --BUTTON--#
data_spriteGroup_buttons = pygame.sprite.Group()
# ---PADDLE---#
data_spriteGroup_paddle = pygame.sprite.Group()

# ---FONTS&TEXTS---#
data_textSize = 0
# data_fontFile1 = "Resources/Mona Shark.otf"
data_fontFile1 = "Resources/Font_1.ttf"
# ---BRICKS---#
data_brickSizeX = 64
data_brickSizeY = 25
data_brickSizeXSelect = 13
data_brickSizeYSelect = 5
data_brickYMargin = 10
# ---Sprites---#
data_allSprites = pygame.sprite.Group()
# Paddle#
data_paddleY = 300
# ---INPUT---#
data_left = False
data_right = False
# ---LEVEL---#
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
data_level1 = [
    [[ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [YELLOW, "-", 1], [GREEN, "-", 1], [DARKGREEN, "-", 1],
     [DARKRED, "-", 1], [LIGHTBLACK, "-", 1], [DARKRED, "-", 1],
     [DARKGREEN, "-", 1], [GREEN, "-", 1], [YELLOW, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1]],
    [[ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [YELLOW, "-", 1], [GREEN, "-", 1], [DARKGREEN, "-", 1],
     [DARKRED, "-", 1], [LIGHTBLACK, "-", 1], [DARKRED, "-", 1],
     [DARKGREEN, "-", 1], [GREEN, "-", 1], [YELLOW, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1]],
    [[], [], [ORANGE, "-", 1], [YELLOW, "-", 1], [GREEN, "-", 1], [DARKGREEN, "-", 1], [DARKRED, "-", 1],
     [LIGHTBLACK, "-", 1], [DARKRED, "-", 1],
     [DARKGREEN, "-", 1], [GREEN, "-", 1], [YELLOW, "-", 1], [ORANGE, "-", 1], [], []],
    [[ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [YELLOW, "-", 1], [GREEN, "-", 1], [DARKGREEN, "-", 1],
     [DARKRED, "-", 1], [LIGHTBLACK, "-", 1], [DARKRED, "-", 1],
     [DARKGREEN, "-", 1], [GREEN, "-", 1], [YELLOW, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1]],
    [[ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [YELLOW, "-", 1], [GREEN, "-", 1], [DARKGREEN, "-", 1],
     [DARKRED, "-", 1], [LIGHTBLACK, "-", 1], [DARKRED, "-", 1],
     [DARKGREEN, "-", 1], [GREEN, "-", 1], [YELLOW, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1]],
    [[ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [YELLOW, "-", 1], [GREEN, "-", 1], [DARKGREEN, "-", 1],
     [DARKRED, "-", 1], [LIGHTBLACK, "-", 1], [DARKRED, "-", 1],
     [DARKGREEN, "-", 1], [GREEN, "-", 1], [YELLOW, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1]],
    [[ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [YELLOW, "-", 1], [GREEN, "-", 1], [DARKGREEN, "-", 1],
     [DARKRED, "-", 1], [LIGHTBLACK, "-", 1], [DARKRED, "-", 1],
     [DARKGREEN, "-", 1], [GREEN, "-", 1], [YELLOW, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1]],
    [[ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [YELLOW, "-", 1], [GREEN, "-", 1], [DARKGREEN, "-", 1],
     [DARKRED, "-", 1], [LIGHTBLACK, "-", 1], [DARKRED, "-", 1],
     [DARKGREEN, "-", 1], [GREEN, "-", 1], [YELLOW, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1], [ORANGE, "-", 1]]]
# color,powerup,lives
# [["white","-",1]]
#flags = FULLSCREEN | DOUBLEBUF
flags = DOUBLEBUF
screen = pygame.display.set_mode((960, 700),flags)
data_background = pygame.Surface(screen.get_size())
data_actionground = pygame.Surface(screen.get_size(),flags)
#data_actionground = data_actionground.convert_alpha()
data_foreground = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
data_foreground = data_foreground.convert_alpha()
data_buttonground = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
data_buttonground = data_buttonground.convert_alpha()
data_textground = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
data_textground = data_textground.convert_alpha()
data_background = data_background.convert()
data_mousePressedPos = ()
data_actionground.set_colorkey((1,2,3),RLEACCEL)

"""
def init():
    global data_state
    data_state = "menu"
    #---GENERAL---#
    global data_canvasX
    data_canvasX = 960
    global data_canvasY
    data_canvasY = 700
    global data_tmp
    data_tmp = ()
    global data_tick1
    data_tick1 = False
    data_textSize = 0

    ####SPRITES####

    #--BUTTON--#
    global data_spriteGroup_buttons
    data_spriteGroup_buttons = pygame.sprite.Group()
    #---PADDLE---#
    global data_paddle
    data_paddle = ()

    #---FONTS&TEXTS---#
    global data_textSize
    data_textSize = 0
    global data_fontFile1
    #data_fontFile1 = "Resources/Mona Shark.otf"
    data_fontFile1 = "Resources/Font_1.ttf"
    #---BRICKS---#
    global data_brickSizeX
    data_brickSizeX = 64
    global data_brickSizeY
    data_brickSizeY = 3
    global data_brickSizeXSelect
    data_brickSizeXSelect = 13
    global data_brickSizeYSelect
    data_brickSizeYSelect = 5
    global data_brickYMargin
    data_brickYMargin = 10
    #---Sprites---#
    global data_allSprites
    data_allSprites = pygame.sprite.Group()
    #Paddle#
    #global data_paddle
    data_paddle = ()
    global data_paddleY
    data_paddleY = 300
    #---INPUT---#
    global data_left
    data_left = False
    global data_right
    data_right = False
    #---LEVEL---#
    global data_currentLevel
    data_currentLevel = []
    global data_lvlLayout
    data_lvlLayout   =   [[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]
    global data_level1
    data_level1      =   [[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],[ORANGE,"-",1],[YELLOW,"-",1],[GREEN,"-",1],[DARKGREEN,"-",1],[DARKRED,"-",1],[LIGHTBLACK,"-",1],[DARKRED,"-",1],\
                            [DARKGREEN,"-",1],[GREEN,"-",1],[YELLOW,"-",1],[ORANGE,"-",1],[],[]],\
                          [[],[],[ORANGE,"-",1],[YELLOW,"-",1],[GREEN,"-",1],[DARKGREEN,"-",1],[DARKRED,"-",1],[LIGHTBLACK,"-",1],[DARKRED,"-",1],\
                            [DARKGREEN,"-",1],[GREEN,"-",1],[YELLOW,"-",1],[ORANGE,"-",1],[],[]]]
    #color,powerup,lives
    #[["white","-",1]]
    global screen
    screen=pygame.display.set_mode((960,700))
    global data_background
    data_background = pygame.Surface(screen.get_size())
    global data_actionground
    data_actionground = pygame.Surface(screen.get_size(),pygame.SRCALPHA,32)
    data_actionground = data_actionground.convert_alpha()
    global data_foreground
    data_foreground = pygame.Surface(screen.get_size(),pygame.SRCALPHA,32)
    data_foreground = data_foreground.convert_alpha()
    global data_buttonground
    data_buttonground = pygame.Surface(screen.get_size(),pygame.SRCALPHA,32)
    data_buttonground = data_buttonground.convert_alpha()
    global data_textground
    data_textground = pygame.Surface(screen.get_size(),pygame.SRCALPHA,32)
    data_textground = data_textground.convert_alpha()
    data_background = data_background.convert()
    global data_mousePressedPos
    data_mousePressedPos = ()
"""
