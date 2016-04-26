from __future__ import print_function, division

import copy

import pygame
from pygame.locals import *

import main_Vars




# ================================####INITIAL CALLS####================================================================================#
brickWidth = main_Vars.data_brickSizeX
brickHeight = main_Vars.data_brickSizeY
marginY = main_Vars.data_brickYMargin
initial = False
cols = int(main_Vars.data_canvasX / brickWidth)
rows = int((main_Vars.data_canvasY - marginY) / brickHeight)
brickList = []
selectedBrick = []
empty = pygame.Surface(main_Vars.screen.get_size(), pygame.SRCALPHA, 32)
colorList = [main_Vars.YELLOW, main_Vars.ORANGE, main_Vars.RED, main_Vars.DARKRED, main_Vars.LIGHTGRAY, main_Vars.GRAY,
             main_Vars.BLACK, main_Vars.GREEN, main_Vars.DARKGREEN, main_Vars.BLUE, main_Vars.SILVER, main_Vars.GOLD,
             main_Vars.EMERALD, main_Vars.CHROME, main_Vars.ROSE]
cPress = False
lives = False

print(
    "press _c_ to change selected brick's color, press _+_ to increase brick's lives by 1, press _-_ to decrease brick's lives by 1, press _backspace_ to delete the selected brick, press _right_arrow_key_ to get the print get the level layout")


def drawStripes():
    for stroke in xrange(cols + 1):
        pygame.draw.line(main_Vars.data_backGround, (155, 55, 55), (stroke * brickWidth, marginY),
                         (stroke * brickWidth, main_Vars.data_canvasY), 5)
    for stroke2 in xrange(rows):
        pygame.draw.line(main_Vars.data_backGround, (155, 55, 55), (0, marginY + (stroke2 * brickHeight)),
                         (main_Vars.data_canvasX, marginY + (stroke2 * brickHeight)), 5)


def initializeBricks():
    global brickList
    tmp = []
    for numcol in xrange(cols):
        tmp += [[None]]
    for numrow in xrange(rows):
        brickList += [copy.deepcopy(tmp)]


def mousePress(point):
    global selectedBrick
    global brickList
    x = point[0]
    y = point[1]
    col = int(x / brickWidth)
    row = int((y - marginY) / brickHeight)
    if brickList[row][col] == [None] and selectedBrick != []:
        selectedBrick = []
    elif brickList[row][col] == [None]:
        brickList[row][col] = [[(main_Vars.YELLOW)], "-", 1]
    else:
        selectedBrick = (row, col)
        print("$ row:", selectedBrick[0], "col:", selectedBrick[1], "Lives = ",
              brickList[selectedBrick[0]][selectedBrick[1]][2], "Powerup =",
              brickList[selectedBrick[0]][selectedBrick[1]][1])
        # pygame.draw.rect(main_Vars.data_foreGround, main_Vars.GRAY, (giveRect(col, row)))


def giveRect(col, row):
    return (col * brickWidth, marginY + row * brickHeight, brickWidth, brickHeight)


def drawLevel(lvl, width=0, height=0, marginY=True, addX=0, addY=0, outline=5):
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
            if lvl[row][col] != [None]:
                drawBrick(col, row, [lvl[row][col][0][0]], width, height, marginY, addX, addY, outline)


def drawBrick(col, row, cl, width, height, marginY, addX, addY, outline):
    # Col(x) max = 0-14
    # Row(y) max = 0-25
    # global main_Vars.data_actionground
    if col >= 15 or row >= 26:
        return False
    else:
        pygame.draw.rect(main_Vars.data_foreGround, cl[0],
                         (addX + col * width, addY + marginY + row * height, width, height))
        pygame.draw.rect(main_Vars.data_foreGround, main_Vars.BLACK,
                         (addX + col * width, addY + marginY + row * height, width, height),
                         outline)


def selected():
    global brickList
    if selectedBrick != []:
        if cPress:
            for i in xrange(len(colorList) - 1):
                if colorList[i] == brickList[selectedBrick[0]][selectedBrick[1]][0][0]:
                    if brickList[selectedBrick[0]][selectedBrick[1]][2] == -1:
                         brickList[selectedBrick[0]][selectedBrick[1]][0] = [colorList[i + 1]]
                    else:
                        brickList[selectedBrick[0]][selectedBrick[1]][0] = []
                        for n in xrange(brickList[selectedBrick[0]][selectedBrick[1]][2]):
                            brickList[selectedBrick[0]][selectedBrick[1]][0].append(colorList[i + 1])
                    print("$ row:", selectedBrick[0], "col:", selectedBrick[1], "Lives = ",
                          brickList[selectedBrick[0]][selectedBrick[1]][2], "Powerup =",
                          brickList[selectedBrick[0]][selectedBrick[1]][1])
                    return
            brickList[selectedBrick[0]][selectedBrick[1]][0] = [colorList[0]]
        elif lives != False:
            if lives == "+":
                if brickList[selectedBrick[0]][selectedBrick[1]][2] == -1:
                    brickList[selectedBrick[0]][selectedBrick[1]][2] = 1
                else:
                    brickList[selectedBrick[0]][selectedBrick[1]][2] += 1
                    #brickList[selectedBrick[0]][selectedBrick[1]][0].append(
                        #brickList[selectedBrick[0]][selectedBrick[1]][0][0])
            elif lives == "-" and brickList[selectedBrick[0]][selectedBrick[1]][2] > 1:
                brickList[selectedBrick[0]][selectedBrick[1]][2] -= 1
                #del brickList[selectedBrick[0]][selectedBrick[1]][0][-1]
            else:
                brickList[selectedBrick[0]][selectedBrick[1]][2] = -1
        print("$ row:", selectedBrick[0], "col:", selectedBrick[1], "Lives = ",
              brickList[selectedBrick[0]][selectedBrick[1]][2], "Powerup =",
              brickList[selectedBrick[0]][selectedBrick[1]][1])

def main():
    global initial
    global cPress
    global selectedBrick
    global lives
    pygame.init()
    pygame.time.set_timer(USEREVENT + 1, 100)

    # Convert Surface object to make blitting faster.

    # Copy background to main_Vars.screen (position (0, 0) is upper left corner).
    # Create Pygame clock object.
    clock = pygame.time.Clock()
    mainloop = True
    FPS = 60
    ###INTERACTIVES###
    ###-----------###
    playtime = 0.0
    initializeBricks()
    while mainloop:
        # Do not go faster than this framerate.
        milliseconds = clock.tick(FPS)
        playtime += milliseconds / 1000.0
        for event in pygame.event.get():
            # User presses QUIT-button.
            if event.type == pygame.QUIT:
                mainloop = False
            elif event.type == pygame.KEYDOWN:
                # User presses ESCAPE-Key
                if event.key == pygame.K_ESCAPE:
                    mainloop = False
                elif event.key == pygame.K_RIGHT:
                    print(brickList)
                    main_Vars.data_right = True
                elif event.key == pygame.K_LEFT:
                    main_Vars.data_left = True
                elif event.key == pygame.K_SPACE:
                    main_Vars.data_space = True
                elif event.key == pygame.K_c:
                    cPress = True
                    selected()
                elif event.key == pygame.K_BACKSPACE:
                    if selectedBrick != []:
                        brickList[selectedBrick[0]][selectedBrick[1]] = [None]
                        selectedBrick = []
                        initial = False
                elif event.key == pygame.K_KP_PLUS:
                    lives = "+"
                    selected()
                elif event.key == pygame.K_KP_MINUS:
                    lives = "-"
                    selected()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    main_Vars.data_right = False
                elif event.key == pygame.K_LEFT:
                    main_Vars.data_left = False
                elif event.key == pygame.K_SPACE:
                    main_Vars.data_space = False
                elif event.key == pygame.K_c:
                    cPress = False
                elif event.key == pygame.K_PLUS:
                    lives = False
                elif event.key == pygame.K_MINUS:
                    lives = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected()
                mousePress(pygame.mouse.get_pos())
                main_Vars.data_spriteGroup_buttons.update("d")
            elif event.type == pygame.MOUSEBUTTONUP:
                main_Vars.data_mousePressedPos = ()
                main_Vars.data_spriteGroup_buttons.update("u")

        text = "Bricks Alpha 0.2 {" + "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime) + "}"
        pygame.display.set_caption(text)
        main_Vars.data_foreGround = empty
        main_Vars.data_foreGround = main_Vars.data_foreGround.convert_alpha()
        if not initial:
            main_Vars.data_backGround.fill((50, 25, 50))
            drawStripes()
            initial = True
        drawLevel(brickList)
        if selectedBrick != []:
            pygame.draw.rect(main_Vars.data_foreGround, (255, 200, 200), (giveRect(selectedBrick[1], selectedBrick[0])),
                             5)
        main_Vars.screen.blit(main_Vars.data_backGround, (0, 0))
        main_Vars.screen.blit(main_Vars.data_foreGround, (0, 0))
        pygame.display.flip()

    # Finish Pygame.
    pygame.quit()


main()
