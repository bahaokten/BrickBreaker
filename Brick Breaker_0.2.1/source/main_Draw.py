from __future__ import print_function, division

import pygame

import main_Vars




#####################RAW DRAW FUNCTIONS###############################################################


def drawMenuBackground():
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
    main_Vars.data_rect.append((0,0,main_Vars.data_canvasX,main_Vars.data_canvasY))
    main_Vars.screen.blit(main_Vars.data_backGround, (0, 0))

def drawMenuBackGround2():
    curtainColor = [250,250,0]
    for num in xrange(19):
        pygame.draw.polygon(main_Vars.data_backGround, curtainColor,
                            (((num * 8), main_Vars.data_canvasY), (10 + (num * 8), main_Vars.data_canvasY), (0, main_Vars.data_canvasY/2)))
        pygame.draw.polygon(main_Vars.data_backGround, curtainColor, (
            (main_Vars.data_canvasX - (num * 8), main_Vars.data_canvasY),
            (main_Vars.data_canvasX - 10 - (num * 8), main_Vars.data_canvasY), (main_Vars.data_canvasX, main_Vars.data_canvasY/2)))
        pygame.draw.polygon(main_Vars.data_backGround, curtainColor, (
            (main_Vars.data_canvasX - (num * 8), 0), (main_Vars.data_canvasX, main_Vars.data_canvasY/2),
            (main_Vars.data_canvasX - 10 - (num * 8), 0)))
        pygame.draw.polygon(main_Vars.data_backGround, curtainColor, (((num * 8), 0), (10 + (num * 8), 0), (0, main_Vars.data_canvasY/2)))
        curtainColor[0]= curtainColor[1]*0.9
        curtainColor[2]= curtainColor[1]*0.1
        curtainColor[1]-= 10

# DRAW MENU LEVEL SELECT MODULE


def drawLevelSelect(level):
    # pygame.draw.rect(main_Vars.data_buttonground, LIGHTGRAY , (0,0,main_Vars.data_canvasX,main_Vars.data_canvasY),0)
    # canvas.create_text(canvas.main_Vars.data.canvasWidth/2,50,text = "Level Select",font = "Times 30",anchor = CENTER, fill = "red")
    tmp = 50
    pygame.draw.rect(main_Vars.data_buttonGround, (90, 116, 149), (tmp, tmp, 13 * 15, 5 * 26))
    drawLevel(level, main_Vars.data_buttonGround, 13, 5, False, tmp, tmp, 1)
    pygame.draw.rect(main_Vars.data_buttonGround, main_Vars.BLACK, (tmp, tmp, 13 * 15, 5 * 26), 3)
    # drawLevel(main_Vars.data_level1,main_Vars.data_buttonground,64,25)


def drawLevel(level, ground, width=0, height=0, marginY=True, addX=0, addY=0, outline=5):
    if width == 0:
        width = main_Vars.data_brickSizeX
    if height == 0:
        height = main_Vars.data_brickSizeY
    if marginY == True:
        marginY = main_Vars.data_brickYMargin
    else:
        marginY = 0
    rows = len(level)
    cols = len(level[0])
    for row in xrange(rows):
        for col in xrange(cols):
            if len(level[row][col]) != 0:
                drawBrick(col, row, level[row][col][0], width, height, marginY, addX, addY, outline)


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
