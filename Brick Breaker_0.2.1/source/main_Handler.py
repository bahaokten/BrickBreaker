from __future__ import print_function, division

import pygame

import main_Vars
import main_Modules
import sprite_Paddle
import sprite_Brick
import sprite_Button
import main_Draw


# PADDLE AND BUTTON CREATE CALLS ARE WITHIN THE MODULE FILES

def createLevel(level):
    sprite_Brick.createLevelBricks(level)


# _______________________DRAW STATE FUNCTIONS_______________________________________________
"""
drawLevelSelect(main_Vars.data_level1)
sprite_Paddle.paddleCreator()
createLevel(main_Vars.data_level1)
"""


def drawMenu():
    main_Draw.drawMenuBackGround()
    # self, X, Y, W, H, col1, col2, newState, text, font, col3, depth = 10, middle = True, bold= False, italic = False, usePrevFont = False)
    main_Modules.normTextDraw(main_Vars.data_fontFile1, main_Vars.data_canvasX / 2, 12, "Brick Breaker", main_Vars.GOLD,
                              bold=False,
                              italic=True, size=60)
    sprite_Button.buttonCreator(480, 350, 100, 50, (105, 250, 250), (50, 150, 150), "levelmenu1", "START",
                                main_Vars.data_fontFile1, (100, 50, 50), mid=True, Ycor=4)
    sprite_Button.spawnCreatedButtons()
    main_Vars.data_allSprites.update()


def drawLevelMenu(page):
    resetTextGround()
    resetBackGround()
    main_Draw.drawMenuBackGround2()
    if page == 1:
        main_Draw.drawLevelSelectMenu(page,1, level2=2, level3=2, level4=2,level5 = 2,level6 =2)
    main_Modules.normTextDraw(main_Vars.data_fontFile1, main_Vars.data_canvasX / 2, 12, "Select Level", main_Vars.BLACK,
                              bold=False,
                              italic=True, size=60)


# __________________________RESET FUNCTIONS_________________________________

def resetBackGround():
    main_Vars.data_backGround.fill((0, 0, 0), (0, 0, main_Vars.data_canvasX, main_Vars.data_canvasY))
    main_Vars.data_updateAll = True


def resetTextGround():
    main_Vars.data_textGround.fill((0, 0, 0, 0), (0, 0, main_Vars.data_canvasX, main_Vars.data_canvasY))
    main_Vars.data_updateAll = True
