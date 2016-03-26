from __future__ import print_function, division

from math import pi
import random

import pygame

import main_Vars
import sprite_Button
import main_Modules


#####################RAW DRAW FUNCTIONS###############################################################


def drawMenuBackGround():
    backColor = [154, 52, 53]
    curtainColor = [250, 0, 0]
    for n in xrange(18):
        pygame.draw.rect(main_Vars.data_backGround, backColor,
                         (n * 30, n * 20, main_Vars.data_canvasX - (60 * n), main_Vars.data_canvasY - (40 * n)))
        backColor = [154 - (n * 2), 52 + (n * 9), 53 + (n * 8)]
    for num in xrange(19):
        pygame.draw.polygon(main_Vars.data_backGround, curtainColor, (((num * 10), 0), (10 + (num * 10), 0), (0, 450)))
        pygame.draw.polygon(main_Vars.data_backGround, curtainColor, (
            (main_Vars.data_canvasX - (num * 10), 0), (main_Vars.data_canvasX, 450),
            (main_Vars.data_canvasX - 10 - (num * 10), 0)))
        pygame.draw.polygon(main_Vars.data_backGround, curtainColor,
                            (((num * 8), main_Vars.data_canvasY), (10 + (num * 8), main_Vars.data_canvasY), (0, 450)))
        pygame.draw.polygon(main_Vars.data_backGround, curtainColor, (
            (main_Vars.data_canvasX - (num * 8), main_Vars.data_canvasY),
            (main_Vars.data_canvasX - 10 - (num * 8), main_Vars.data_canvasY), (main_Vars.data_canvasX, 450)))
        if not curtainColor[0] < 20 + num:
            curtainColor[0] -= 5 + (num)
        curtainColor[1] += 20 - (num)
        curtainColor[2] += abs(num - 5)
    main_Vars.data_rect.append((0, 0, main_Vars.data_canvasX, main_Vars.data_canvasY))
    main_Vars.screen.blit(main_Vars.data_backGround, (0, 0))


def drawMenuBackGround2():
    main_Vars.data_backGround.fill(main_Vars.GOLD)
    curtainColor = [250, 250, 0]
    for num in xrange(19):
        pygame.draw.polygon(main_Vars.data_backGround, curtainColor,
                            (((num * 8), main_Vars.data_canvasY), (10 + (num * 8), main_Vars.data_canvasY),
                             (0, main_Vars.data_canvasY / 2)))
        pygame.draw.polygon(main_Vars.data_backGround, curtainColor, (
            (main_Vars.data_canvasX - (num * 8), main_Vars.data_canvasY),
            (main_Vars.data_canvasX - 10 - (num * 8), main_Vars.data_canvasY),
            (main_Vars.data_canvasX, main_Vars.data_canvasY / 2)))
        pygame.draw.polygon(main_Vars.data_backGround, curtainColor, (
            (main_Vars.data_canvasX - (num * 8), 0), (main_Vars.data_canvasX, main_Vars.data_canvasY / 2),
            (main_Vars.data_canvasX - 10 - (num * 8), 0)))
        pygame.draw.polygon(main_Vars.data_backGround, curtainColor,
                            (((num * 8), 0), (10 + (num * 8), 0), (0, main_Vars.data_canvasY / 2)))
        curtainColor[0] = curtainColor[1] * 0.9
        curtainColor[2] = curtainColor[1] * 0.1
        curtainColor[1] -= 10

        # DRAW MENU LEVEL SELECT MODULE


def drawLevelGUI():
    pygame.draw.rect(main_Vars.data_buttonGround, main_Vars.LIGHTBLACK,
                     (0, main_Vars.data_canvasY - 70, main_Vars.data_canvasX, 70))
    pygame.draw.rect(main_Vars.data_buttonGround, main_Vars.EMERALD,
                     (10, main_Vars.data_canvasY - 60, main_Vars.data_canvasX - 20, 50))


def drawLevelBackground(num):
    if num == 1:
        main_Vars.data_backGround.fill(main_Vars.LIGHTBLACK)
        # Surface, color, pos, radius, width=0
        radius = 0
        for i in xrange(70):
            color = (random.randint(0, 50), random.randint(0, 90), random.randint(0, 200))
            radius = random.randint(50, 160)
            pos = (random.randint(5, main_Vars.data_canvasX), random.randint(5, main_Vars.data_canvasY - 70))
            pygame.draw.circle(main_Vars.data_backGround, color, pos, radius)
        apart = 3
        for i in xrange(int(main_Vars.data_canvasY / apart)):
            pygame.draw.line(main_Vars.data_backGround, main_Vars.LIGHTBLACK, (0, i * apart),
                             (main_Vars.data_canvasX, i * apart), 2)
        for i in xrange(int(main_Vars.data_canvasX / apart)):
            pygame.draw.line(main_Vars.data_backGround, main_Vars.BLUE, (i*apart, 0),
                             (i*apart,main_Vars.data_canvasY), 1)


"""
# self, X, Y, W, H, col1, col2, newState, text, font, col3, depth = 10, middle = True, bold= False, italic = False, usePrevFont = False)
    sprite_Button.buttonCreator(480, 350, 100, 50, (105, 250, 250),( 50, 150, 150), "levelmenu1", "START",
                                main_Vars.data_fontFile1, (100, 50, 50), mid=True, Ycor=4)
    sprite_Button.spawnCreatedButtons()
    """


def drawLevelSelectMenu(page, level1, level2=0, level3=0, level4=0, level5=0, level6=0):
    distance = 70
    midY = main_Vars.data_canvasY / 2
    midX = main_Vars.data_canvasX / 2
    # level1
    if main_Vars.isLevelHandler(level1):
        drawLevelSelect(level1, 150, midY - 130 - distance)
        sprite_Button.buttonCreator(150 + 195 / 2, midY - 30, 100, 50, (105, 250, 250), (50, 150, 150),
                                    "level" + str(level1), "PLAY",
                                    main_Vars.data_fontFile1, (100, 50, 50), mid=True, Ycor=4,
                                    usePrevFont=True)
    else:
        drawLockedLevel(150, midY - 130 - distance)
    if level2:
        if main_Vars.isLevelHandler(level2):
            drawLevelSelect(level2, midX - 195 / 2, midY - 130 - distance)
            sprite_Button.buttonCreator(midX, midY - 30, 100, 50, (105, 250, 250), (50, 150, 150),
                                        "level" + str(level2), "PLAY",
                                        main_Vars.data_fontFile1, (100, 50, 50), mid=True, Ycor=4,
                                        usePrevFont=True)
        else:
            drawLockedLevel(midX - 195 / 2, midY - 130 - distance)

    if level3:
        if main_Vars.isLevelHandler(level3):
            drawLevelSelect(level3, 615, midY - 130 - distance)
            sprite_Button.buttonCreator(615 + 195 / 2, midY - 30, 100, 50, (105, 250, 250), (50, 150, 150),
                                        "level" + str(level3), "PLAY",
                                        main_Vars.data_fontFile1, (100, 50, 50), mid=True, Ycor=4,
                                        usePrevFont=True)
        else:
            drawLockedLevel(615, midY - 130 - distance)
    if level4:
        if main_Vars.isLevelHandler(level4):
            drawLevelSelect(level4, 150, midY + distance)
            sprite_Button.buttonCreator(150 + 195 / 2, midY + 130 + distance + 15 + 25, 100, 50, (105, 250, 250),
                                        (50, 150, 150), "level" + str(level4), "PLAY",
                                        main_Vars.data_fontFile1, (100, 50, 50), mid=True, Ycor=4,
                                        usePrevFont=True)
        else:
            drawLockedLevel(150, midY + distance)
    if level5:
        if main_Vars.isLevelHandler(level5):
            drawLevelSelect(level5, midX - 195 / 2, midY + distance)
            sprite_Button.buttonCreator(midX, midY + 130 + distance + 15 + 25, 100, 50, (105, 250, 250), (50, 150, 150),
                                        "level" + str(level5), "PLAY",
                                        main_Vars.data_fontFile1, (100, 50, 50), mid=True, Ycor=4,
                                        usePrevFont=True)
        else:
            drawLockedLevel(midX - 195 / 2, midY + distance)
    if level6:
        if main_Vars.isLevelHandler(level6):
            drawLevelSelect(level6, 615, midY + distance)
            sprite_Button.buttonCreator(615 + 195 / 2, midY + 130 + distance + 15 + 25, 100, 50, (105, 250, 250),
                                        (50, 150, 150), "level" + str(level6), "PLAY",
                                        main_Vars.data_fontFile1, (100, 50, 50), mid=True, Ycor=4,
                                        usePrevFont=True)
        else:
            drawLockedLevel(615, midY + distance)
    if page > 1:
        pygame.draw.polygon(main_Vars.data_buttonGround, main_Vars.SILVER,
                            ((30, midY), (100, midY - 60), (100, midY + 60)))
        sprite_Button.buttonCreator(110, midY, 100, 50, main_Vars.SILVER,
                                    main_Vars.CHROME, "lvlmenu" + str(page - 1), "PREV",
                                    main_Vars.data_fontFile1, main_Vars.LIGHTBLACK, mid=True, Ycor=4,
                                    usePrevFont=True)
    pygame.draw.polygon(main_Vars.data_buttonGround, main_Vars.SILVER, (
        (main_Vars.data_canvasX - 30, midY), (main_Vars.data_canvasX - 100, midY - 60),
        (main_Vars.data_canvasX - 100, midY + 60)))
    sprite_Button.buttonCreator(main_Vars.data_canvasX - 110, midY, 100, 50, main_Vars.SILVER,
                                main_Vars.CHROME, "lvlmenu" + str(page + 1), "NEXT",
                                main_Vars.data_fontFile1, main_Vars.LIGHTBLACK, mid=True, Ycor=4,
                                usePrevFont=True)
    sprite_Button.spawnCreatedButtons()

    if level1:
        main_Modules.normTextDraw(main_Vars.data_fontFile2, 150 + 195 / 2, 100, "Level" + str(level1),
                                  main_Vars.DARKRED,
                                  bold=False,
                                  italic=True, size=40)
    if level2:
        main_Modules.normTextDraw(main_Vars.data_fontFile2, midX, 100, "Level" + str(level2), main_Vars.DARKRED,
                                  bold=False,
                                  italic=True, size=40)
    if level3:
        main_Modules.normTextDraw(main_Vars.data_fontFile2, 615 + 195 / 2, 100, "Level" + str(level3),
                                  main_Vars.DARKRED,
                                  bold=False,
                                  italic=True, size=40)
    if level4:
        main_Modules.normTextDraw(main_Vars.data_fontFile2, 150 + 195 / 2, 300 + distance, "Level" + str(level4),
                                  main_Vars.DARKRED,
                                  bold=False,
                                  italic=True, size=40)
    if level5:
        main_Modules.normTextDraw(main_Vars.data_fontFile2, midX, 300 + distance, "Level" + str(level5),
                                  main_Vars.DARKRED,
                                  bold=False,
                                  italic=True, size=40)
    if level6:
        main_Modules.normTextDraw(main_Vars.data_fontFile2, 615 + 195 / 2, 300 + distance, "Level" + str(level5),
                                  main_Vars.DARKRED,
                                  bold=False,
                                  italic=True, size=40)


def drawLevelSelect(level, x, y):
    # width = 195 height = 130
    pygame.draw.rect(main_Vars.data_buttonGround, (90, 116, 149), (x, y, 13 * 15, 5 * 26))
    drawLevel(level, 13, 5, False, x, y, 1)
    pygame.draw.rect(main_Vars.data_buttonGround, main_Vars.BLACK, (x, y, 13 * 15, 5 * 26), 3)
    # drawLevel(main_Vars.data_level1,main_Vars.data_buttonground,64,25)


def drawLockedLevel(x, y):
    pygame.draw.rect(main_Vars.data_buttonGround, main_Vars.GRAY, (x, y, 13 * 15, 5 * 26))
    for i in xrange(26):
        pygame.draw.line(main_Vars.data_buttonGround, main_Vars.BLACK, (x, y + i * 5 + 2), (x + 195, y + i * 5 + 2), 2)
    pygame.draw.rect(main_Vars.data_buttonGround, main_Vars.BLACK, (x, y, 13 * 15, 5 * 26), 3)
    pygame.draw.arc(main_Vars.data_buttonGround, main_Vars.SILVER, (x + 125 / 2, y + 15, 70, 90), pi, 0, 7)
    pygame.draw.rect(main_Vars.data_buttonGround, main_Vars.GOLD, (x + 125 / 2 - 5, y + 60, 80, 52))
    pygame.draw.ellipse(main_Vars.data_buttonGround, main_Vars.LIGHTBLACK, (x + 125 / 2 + 27, y + 75, 16, 16))
    pygame.draw.rect(main_Vars.data_buttonGround, main_Vars.LIGHTBLACK, (x + 125 / 2 + 31, y + 82, 8, 20))
    # 70 BY 90 LOCK


def drawLevel(level, width=0, height=0, marginY=True, addX=0, addY=0, outline=5):
    lvl = main_Vars.levelHandler(level)  # gets the level
    if width == 0:
        width = main_Vars.data_brickSizeX
    if height == 0:
        height = main_Vars.data_brickSizeY
    if marginY == True:
        marginY = main_Vars.data_brickYMargin
    else:
        marginY = 0
    rows = len(lvl)
    cols = len(lvl[0])
    for row in xrange(rows):
        for col in xrange(cols):
            if len(lvl[row][col]) != 0:
                drawBrick(col, row, lvl[row][col][0], width, height, marginY, addX, addY, outline)


def drawBrick(col, row, cl, width, height, marginY, addX, addY, outline):
    # Col(x) max = 0-14
    # Row(y) max = 0-25
    # global main_Vars.data_actionground
    if col >= 15 or row >= 26:
        return False
    else:
        pygame.draw.rect(main_Vars.data_buttonGround, cl[0],
                         (addX + col * width, addY + marginY + row * height, width, height))
        pygame.draw.rect(main_Vars.data_buttonGround, main_Vars.BLACK,
                         (addX + col * width, addY + marginY + row * height, width, height),
                         outline)
