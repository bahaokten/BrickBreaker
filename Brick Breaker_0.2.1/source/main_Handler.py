from __future__ import print_function, division

import main_Vars
import main_Modules
import sprite_Paddle
import sprite_Brick
import sprite_Button
import main_Draw
import sprite_Ball


# PADDLE AND BUTTON CREATE CALLS ARE WITHIN THE MODULE FILES




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
    sprite_Button.buttonCreator(480, 350, 100, 50, (105, 250, 250), (50, 150, 150), "lvlmenu1", "START",
                                main_Vars.data_fontFile1, (100, 50, 50), mid=True, Ycor=4)
    sprite_Button.spawnCreatedButtons()
    main_Vars.data_allSprites.update()


def drawLevelMenu(page):
    resetGeneral()
    main_Draw.drawMenuBackGround2()
    if page == 1:
        main_Draw.drawLevelSelectMenu(page, 1, level2=2, level3=3, level4=2, level5=2, level6=2)
    elif page == 2:
        main_Draw.drawLevelSelectMenu(page, 1, level2=1, level3=2)
    main_Modules.normTextDraw(main_Vars.data_fontFile1, main_Vars.data_canvasX / 2, 12, "Select Level", main_Vars.BLACK,
                              bold=False,
                              italic=True, size=60)


def levelCreator(level):
    # isLevel is needed for updating the level sprites. it should be set back to false by the level GUI when level is over
    main_Vars.data_isLevel = True
    resetGeneral()
    tmp = main_Vars.levelHandler(level)
    main_Draw.drawLevelGUI()
    main_Draw.drawLevelBackground(1)
    sprite_Brick.createLevelBricks(tmp)
    sprite_Paddle.paddleCreator()
    sprite_Ball.createBall(1)


# __________________________RESET FUNCTIONS_________________________________

def resetGeneral():
    resetBackGround()
    resetButtons()
    resetButtonGround()
    resetTextGround()


def resetBackGround():
    main_Vars.data_backGround.fill((0, 0, 0), (0, 0, main_Vars.data_canvasX, main_Vars.data_canvasY))
    main_Vars.data_updateAll = True


def resetTextGround():
    main_Vars.data_textGround.fill((0, 0, 0, 0), (0, 0, main_Vars.data_canvasX, main_Vars.data_canvasY))
    main_Vars.data_updateAll = True


def resetButtonGround():
    main_Vars.data_buttonGround.fill((0, 0, 0, 0), (0, 0, main_Vars.data_canvasX, main_Vars.data_canvasY))
    main_Vars.data_updateAll = True


def resetButtons():
    main_Vars.data_spriteGroup_buttons.empty()
