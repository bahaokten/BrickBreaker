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
# UPDATE TICK
data_tick1 = False
# INITIALIZING TICK
data_tick2 = False

###############################################################################################################################################3
# -------Sprites--------#
data_allSprites = pygame.sprite.Group()
# --BUTTON--#
data_spriteGroup_buttons = pygame.sprite.Group()
# ---PADDLE---#
data_spriteGroup_paddle = pygame.sprite.Group()
data_paddleY = data_canvasY - 100
data_paddleMidX = 0
data_paddleWidth = 0
data_paddleImg = False
# ---BRICKS--#
data_spriteGroup_bricks = pygame.sprite.Group()
data_brickSizeX = 64
data_brickSizeY = 25
data_brickSizeXSelect = 13
data_brickSizeYSelect = 5
data_brickYMargin = 5
data_brickOutline = 6

# ---BALL -- #
data_spriteGroup_ball = pygame.sprite.Group()
data_ballImg = False
###############################################################################################################################################3

# ---FONTS&TEXTS&MUSIC---#
data_textSize = 0
data_fontFile1 = "Resources/Font_1.ttf"
data_fontFile2 = "Resources/Font_2.ttf"
data_savedTextSize = []
data_font = None
# main_Vars.data_font = pygame.font.Font(f, size, bold=bold, italic=italic)
# data_font2 = pygame.font.Font()

########################################----MUSIC&SOUND EFFECTS-----####################

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=2048)
pygame.mixer.init()
# Level Music = Stairs
data_musicFile1 = "Resources/Music_1.ogg"
# Metal Block Hit
data_soundFile1 = "Resources/Sound_1.ogg"
data_metalBrick = pygame.mixer.Sound(data_soundFile1)
# Button Click
data_soundFile2 = "Resources/Sound_2.ogg"
data_buttonClick = pygame.mixer.Sound(data_soundFile2)
data_buttonClick.set_volume(0.6)
# Thrown
data_soundFile3 = "Resources/Sound_3.ogg"
data_thrown = pygame.mixer.Sound(data_soundFile3)
data_thrown.set_volume(0.50)
# Block Hit 1
data_soundFile4 = "Resources/Sound_4.ogg"
data_brick1 = pygame.mixer.Sound(data_soundFile4)
# Block Hit 2
data_soundFile5 = "Resources/Sound_5.ogg"
data_brick2 = pygame.mixer.Sound(data_soundFile5)
# Block Hit List
data_brickHits = (data_brick1, data_brick2)
# Paddle Hit
data_soundFile6 = "Resources/Sound_6.ogg"
data_paddleHitSound = pygame.mixer.Sound(data_soundFile6)
data_paddleHitSound.set_volume(0.6)
# Button Release
data_soundFile7 = "Resources/Sound_7.ogg"
data_buttonRelease = pygame.mixer.Sound(data_soundFile7)
data_buttonRelease.set_volume(0.6)
# Hard Brick Hit
data_soundFile8 = "Resources/Sound_8.ogg"
data_hardBrick = pygame.mixer.Sound(data_soundFile8)


def playLevelMusic(musicFile, loop=-1, start=0, volume=1.0):
    pygame.mixer.music.load(musicFile)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loop, start)


################################################### ---INPUT---####################################3

data_left = False
data_right = False
data_space = False
data_mousePressedPos = ()


# ###############################################3---LEVEL---##################################33

data_currentLevel = []


# isLevel is needed for updating the level sprites. it should be set back to false by the level GUI when level is over
data_isLevel = False

data_isLevel1 = True
data_isLevel2 = True
data_isLevel3 = True
data_isLevel4 = False
data_isLevel5 = False
data_isLevel6 = False
data_isLevel7 = False


def levelHandler(level):
    if level == 1:
        return data_level1
    elif level == 2:
        return data_level2
    elif level == 3:
        return data_level3
    elif level > 3:
        return data_level2


def isLevelHandler(level):
    if level == 1:
        return data_isLevel1
    elif level == 2:
        return data_isLevel2
    elif level == 3:
        return data_isLevel3
    elif level > 3:
        return data_isLevel2


def gamemodeChanger(gamemode):
    global data_state
    data_state = gamemode
    global data_tick1
    data_tick1 = False


##########GROUNDS####################################
# color,powerup,lives
# [["white","-",1]]
# flags = FULLSCREEN | DOUBLEBUF
flags = DOUBLEBUF
screen = pygame.display.set_mode((960, 700))
data_backGround = pygame.Surface(screen.get_size())
data_paddleGround = pygame.Surface((960, 21))
data_foreGround = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
data_buttonGround = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
data_buttonGround = data_buttonGround.convert_alpha()
data_textGround = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
data_textGround = data_textGround.convert_alpha()
data_backGround = data_backGround.convert()
data_paddleGround.set_colorkey((1, 2, 3), RLEACCEL)

# data_foreGround.set_colorkey((1,2,3),RLEACCEL)

##########LEVELS###############################
data_lvlLayout = [
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]]]

data_level1 = [
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(GRAY)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]],
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(GRAY)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]],
    [[None], [None], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1], [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1],
     [[(GRAY)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [([(ORANGE)]), "-", 1], [None], [None]],
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(GRAY)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]],
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(GRAY)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]],
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(GRAY)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]],
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(GRAY)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]],
    [[[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1], [[(YELLOW)], "-", 1], [[(GREEN)], "-", 1],
     [[(DARKGREEN)], "-", 1],
     [[(DARKRED)], "-", 1], [[(GRAY)], "-", 1], [[(DARKRED)], "-", 1],
     [[(DARKGREEN)], "-", 1], [[(GREEN)], "-", 1], [[(YELLOW)], "-", 1], [[(ORANGE)], "-", 1], [[(ORANGE)], "-", 1],
     [[(ORANGE)], "-", 1]]]
data_level2 = [[[[(255, 255, 0)], '-', 1], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None],
                [None], [None], [None], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1],
                [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1],
                [None], [None], [None], [None], [None], [None], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None],
                [None], [None], [None], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None],
                [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None],
                [None], [None], [None], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0), (255, 255, 0)], '-', 2], [None], [None], [None],
                [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1],
                [[(255, 255, 0)], '-', 1], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(0, 0, 0), (0, 0, 0), (0, 0, 0)], '-', 3], [None], [None], [None],
                [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None],
                [None]], [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None],
                          [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None], [None], [None], [None],
                          [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)], '-', 4],
                [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1],
                [[(255, 255, 0), (255, 255, 0)], '-', 2], [[(255, 255, 0)], '-', 1], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 0, 0), (255, 0, 0)], '-', 2], [[(255, 255, 0)], '-', 1],
                [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0), (255, 255, 0)], '-', 2], [[(255, 255, 0)], '-', 1],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 102, 0), (255, 102, 0)], '-', 2], [[(255, 255, 0)], '-', 1],
                [None], [[(255, 255, 0)], '-', 1], [[(136, 136, 136), (136, 136, 136)], '-', 2],
                [[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None],
                [None], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None],
                [[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None],
                [[(255, 255, 0)], '-', 1], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [[(255, 255, 0)], '-', 1],
                [None], [None], [None], [None], [None]],
               [[[(255, 102, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None],
                [[(255, 255, 0)], '-', 1], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None],
                [[(255, 255, 0)], '-', 1], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None],
                [[(255, 255, 0)], '-', 1], [None], [None], [None], [[(255, 255, 0)], '-', 1],
                [[(255, 255, 0)], '-', 1], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None],
                [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0), (255, 255, 0)], '-', 2], [None], [None],
                [None]], [[[(255, 255, 0)], '-', 1], [None], [
        [(136, 136, 136), (136, 136, 136), (136, 136, 136), (136, 136, 136), (136, 136, 136), (136, 136, 136)], '-', 6],
                          [None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1],
                          [[(255, 255, 0)], '-', 1], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(136, 136, 136)], '-', 1], [None], [None], [None], [None],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None],
                [None], [None], [None], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None],
                [None], [None], [None], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None],
                [None], [None], [None], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None],
                [None], [None], [None], [None], [None], [None], [None]],
               [[[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None], [None], [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]]]

data_level3 = [[[[(255, 102, 0), (255, 102, 0)], '-', 2], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1],
                [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 102, 0)], '-', 1]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [[(255, 102, 0), (255, 102, 0)], '-', 2], [[(139, 0, 0), (139, 0, 0)], '-', 2],
                [[(139, 0, 0), (139, 0, 0)], '-', 2], [[(212, 175, 55), (212, 175, 55)], '-', 2], [None],
                [[(255, 0, 0), (255, 0, 0)], '-', 2], [[(255, 102, 0), (255, 102, 0)], '-', 2],
                [[(255, 102, 0), (255, 102, 0)], '-', 2], [[(255, 0, 0), (255, 0, 0)], '-', 2], [None],
                [[(80, 200, 120), (80, 200, 120)], '-', 2], [[(255, 0, 0), (255, 0, 0)], '-', 2], [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None],
                [[(255, 102, 0), (255, 102, 0)], '-', 2], [None], [None], [None], [[(255, 0, 0), (255, 0, 0)], '-', 2],
                [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [[(70, 70, 70)], '-', 1], [[(136, 136, 136)], '-', 1], [[(255, 0, 0)], '-', 1],
                [[(255, 102, 0)], '-', 1], [[(139, 0, 0)], '-', 1], [[(136, 136, 136)], '-', 1],
                [[(255, 0, 0)], '-', 1], [[(255, 102, 0)], '-', 1], [None], [None], [[(0, 80, 0)], '-', 1],
                [[(70, 70, 70), (70, 70, 70)], '-', 2], [[(136, 136, 136)], '-', 1]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [[(139, 0, 0), (139, 0, 0)], '-', 2], [[(136, 136, 136), (136, 136, 136), (136, 136, 136)], '-', 3],
                [[(139, 0, 0), (139, 0, 0), (139, 0, 0), (139, 0, 0)], '-', 4]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]],
               [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                [None], [None]]]

"""
data_level2 = [
    [[[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1],
     [[(80, 200, 120)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [[(139, 0, 0)], '-', 1],
     [None], [None], [None], [None], [None], [None]],
    [[[(255, 255, 0)], '-', 1], [[(255, 102, 0)], '-', 1], [[(255, 102, 0)], '-', 1], [[(139, 0, 0)], '-', 1],
     [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [[(255, 102, 0)], '-', 1],
     [[(255, 255, 0)], '-', 1], [None], [None], [None], [None]],
    [[[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None],
     [None], [None], [None], [None], [None], [None], [[(0, 155, 0)], '-', 1], [None], [None], [None]],
    [[[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 102, 0)], '-', 1], [None], [None], [None], [None],
     [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None]],
    [[[(139, 0, 0)], '-', 1], [[(70, 70, 70)], '-', 1], [None], [None], [None], [None], [[(255, 102, 0)], '-', 1],
     [[(255, 255, 0)], '-', 1], [[(139, 0, 0)], '-', 1], [[(255, 102, 0)], '-', 1], [None], [None], [None], [None],
     [None]],
    [[[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [[(255, 102, 0)], '-', 1], [None], [None], [None],
     [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1]],
    [[[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None],
     [[(255, 102, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [[(192, 192, 192)], '-', 1], [None], [None]],
    [[None], [None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None],
     [[(255, 255, 0)], '-', 1], [None], [None]],
    [[None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1],
     [[(0, 155, 0)], '-', 1], [None], [[(255, 102, 0)], '-', 1], [None], [None], [[(139, 0, 0)], '-', 1], [None],
     [None]], [[None], [[(255, 255, 0)], '-', 1], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None],
               [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None], [[(255, 0, 0)], '-', 1], [None]],
    [[None], [[(136, 136, 136)], '-', 1], [None], [None], [[(255, 0, 127)], '-', 1], [None], [None],
     [[(0, 155, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None],
     [[(255, 0, 0)], '-', 1]],
    [[None], [[(255, 102, 0)], '-', 1], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None],
     [[(255, 0, 0)], '-', 1], [None], [None], [None], [None], [None], [None], [None]],
    [[None], [[(255, 255, 0)], '-', 1], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None],
     [[(212, 175, 55)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None],
     [None]], [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
               [[(255, 102, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [[(255, 255, 0)], '-', 1], [None]],
    [[None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None], [None], [[(255, 255, 0)], '-', 1]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]],
    [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
     [None]]]"""
"""
YUSUF LEVEL
[[[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None]], [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None]], [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None]], [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None]], [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None]], [[None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None]], [[None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None]], [[None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None]], [[None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None]], [[None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None]], [[None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None]], [[None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None]], [[None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None]], [[None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None]], [[None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None]], [[None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None]], [[None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None]], [[None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None]], [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None]], [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None]], [[None], [None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None]], [[None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None]], [[None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None]], [[None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None]], [[None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None], [None], [[(255, 255, 0)], '-', 1], [None], [[(255, 255, 0)], '-', 1], [None]], [[None], [None], [None], [None], [None], [None], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [[(255, 255, 0)], '-', 1], [None], [None], [None], [[(255, 255, 0)], '-', 1], [None], [None]], [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None]]]
"""
