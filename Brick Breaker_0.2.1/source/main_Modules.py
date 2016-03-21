from __future__ import print_function, division

import pygame

import main_Vars


# --FitTextDraw Module--#

def fitTextDraw(font, limW, limH, text, X1, Y1, color, Ycorrection=0, Xcorrection=0, bold=False, italic=False,
                prev=False):
    if not prev:
        tmp = 100
        createText(font, tmp, text=text, bold=bold, italic=italic)
        while main_Vars.data_textSize[0] > limW or main_Vars.data_textSize[1] > limH:
            createText(font, tmp, text=text, bold=bold, italic=italic)
            tmp -= 1
    else:
        tmp = pygame.font.Font.size(main_Vars.data_font, text)
        main_Vars.data_textSize = tmp
    drawText(X1 + (limW - main_Vars.data_textSize[0]) / 2, Y1 + (limH - main_Vars.data_textSize[1]) / 2, text, (color),
             ycor=Ycorrection, xcor=Xcorrection)


def drawText(x, y, text, color, ycor=0, xcor=0):
    txt = main_Vars.data_font.render(text, 10, color)
    main_Vars.data_textGround.blit(txt, (x + xcor, y + ycor))


def createText(f, size, text="", bold=False, italic=False):
    main_Vars.data_font = pygame.font.Font(f, size, bold=bold, italic=italic)
    tmp = pygame.font.Font.size(main_Vars.data_font, text)
    main_Vars.data_textSize = tmp


def normTextDraw(font, x, y, text, color, bold=False, size = False,italic=False,mid=True):
    #if size is not changed there is no point in changing bold and italic variables since the function wont create a new font for the text
    if size and not mid:
        createText(font, size, text=text, bold=bold, italic=italic)
        drawText(x, y, text, color)
    if mid and size:
        createText(font, size, text=text, bold=bold, italic=italic)
        drawText(x-main_Vars.data_textSize[0]/2, y, text, color)
    elif mid and not size:
        tmp = pygame.font.Font.size(main_Vars.data_font, text)
        drawText(x-tmp[0]/2,y,text,color)
    else:
        drawText(x,y,text,color)


# Collision Detection

def mouseCollision(X1, Y1, W, H):
    if main_Vars.data_mousePressedPos != ():
        if X1 < main_Vars.data_mousePressedPos[0] < (X1 + W) and Y1 < main_Vars.data_mousePressedPos[1] < (Y1 + H):
            return True
        else:
            return False

# Object Middle

def objMid(X1, Y1, W, H):
    return X1 - (W / 2), Y1 - (H / 2)
