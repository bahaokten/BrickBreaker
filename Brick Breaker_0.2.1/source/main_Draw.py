from __future__ import print_function, division

import pygame

import main_Vars
import main_Modules
import sprite_Paddle
import sprite_Brick
import sprite_Button


######################3RAW CREATE FUNCTIONS##############################################33
# PADDLE AND BUTTON CREATE CALLS ARE WITHIN THE MODULE FILES

def createLevel(level):
    rows = len(level)
    cols = len(level[0])
    for row in xrange(rows):
        for col in xrange(cols):
            sprite_Brick.createBrick(col, row, level[row][col][0], level[row][col][1], level[row][col][2])


#####################RAW DRAW FUNCTIONS###############################################################


def drawMenu():
    drawLevelSelect(main_Vars.data_level1)
    drawMenuBackground()
    sprite_Paddle.paddleCreator()
    # self, X, Y, W, H, R1, G1, B1, R2, G2, B2, newState, text, font, R3, G3, B3, depth = 10, middle = True, bold= False, italic = False, usePrevFont = False)
    sprite_Button.buttonCreator(480, 350, 100, 50, 105, 250, 250, 50, 150, 150, "Menu", "START",
                                main_Vars.data_fontFile1, 100,
                                50, 50, mid=True, Ycor=4)
    sprite_Button.spawnCreatedButtons(main_Vars.data_buttonGround)
    main_Modules.normTextDraw(main_Vars.data_fontFile1, main_Vars.data_canvasX / 2, 50, 12, "Brick Breaker", 0, 0, 0,
                              bold=False,
                              italic=False)
    main_Vars.data_tick1 = True
    # drawLevel(main_Vars.data_level1,main_Vars.data_background)
    print("done!")
    main_Vars.data_allSprites.update()
    # main_Vars.data_allSprites.draw(main_Vars.data_paddleground)


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
    main_Vars.screen.blit(main_Vars.data_backGround, (0, 0))


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
        pygame.draw.rect(main_Vars.data_buttonGround, cl, (addX + col * width, addY + marginY + row * height, width, height))
        pygame.draw.rect(main_Vars.data_buttonGround, main_Vars.BLACK, (addX + col * width, addY + marginY + row * height, width, height),
                         outline)
        print(main_Vars.data_buttonGround.get_size())