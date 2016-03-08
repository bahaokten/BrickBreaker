from __future__ import print_function, division

import pygame

import main_Vars


# --FitTextDraw Module--#

def fitTextDraw(font, limW, limH, text, X1, Y1, R, G, B, Ycorrection=0, Xcorrection=0, bold=False, italic=False,
                prev=False):
    if not prev:
        tmp = 100
        createText(font, tmp, text=text, bold=bold, italic=italic)
        while main_Vars.data_textSize[0] > limW or main_Vars.data_textSize[1] > limH:
            createText(font, tmp, text=text, bold=bold, italic=italic)
            tmp -= 1
    drawText(X1 + (limW - main_Vars.data_textSize[0]) / 2, Y1 + (limH - main_Vars.data_textSize[1]) / 2, text, R, G, B,
             ycor=Ycorrection, xcor=Xcorrection)


def drawText(x, y, text, R, G, B, ycor=0, xcor=0):
    txt = main_Vars.data_font.render(text, 10, (R, G, B))
    main_Vars.data_textground.blit(txt, (x + xcor, y + ycor))


def createText(f, size, text="", bold=False, italic=False):
    main_Vars.data_font = pygame.font.Font(f, size, bold=bold, italic=italic)
    tmp = pygame.font.Font.size(main_Vars.data_font, text)
    main_Vars.data_textSize = tmp


def normTextDraw(font, x, y, size, text, R, G, B, bold=False, italic=False, create=False):
    if create:
        createText(font, size, text=text, bold=bold, italic=italic)
    drawText(x, y, text, R, G, B)


# Collision Detection

def mouseCollision(X1, Y1, W, H):
    if main_Vars.data_mousePressedPos != ():
        if X1 < main_Vars.data_mousePressedPos[0] < (X1 + W) and Y1 < main_Vars.data_mousePressedPos[1] < (Y1 + H):
            return True
        else:
            return False


def objMid(X1, Y1, W, H):
    return X1 - (W / 2), Y1 - (H / 2)
