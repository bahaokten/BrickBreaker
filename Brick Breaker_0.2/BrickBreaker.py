from __future__ import print_function, division

import pygame
from pygame.locals import *

import main_Vars
import main_Modules

import sprite_Paddle
import sprite_Brick
import sprite_Button

"""
def redrawAll():
      #Redraws all
      print "redrawn"
      canvas.delete(ALL)
      drawGame()
      if canvas.main_Vars.data.takenNum["b"] == 15:
            canvas.data.spriteState = "finished"
            canvas.delete(ALL)
            drawGame()
            drawWinner()
      elif canvas.data.takenNum["w"] == 15:
            canvas.data.spriteState = "finished"
            canvas.delete(ALL)
            drawGame()
            drawWinner()
"""


# ================================####DRAWFUNCTIONS####================================================================================#

# listeden okumak yerine spritedan okumaya cevir
def drawLevelSelect():
    # pygame.draw.rect(main_Vars.data_buttonground, LIGHTGRAY , (0,0,main_Vars.data_canvasX,main_Vars.data_canvasY),0)
    # canvas.create_text(canvas.main_Vars.data.canvasWidth/2,50,text = "Level Select",font = "Times 30",anchor = CENTER, fill = "red")
    tmp = 50
    pygame.draw.rect(main_Vars.data_buttonground, (90, 116, 149), (tmp, tmp, 13 * 15, 5 * 26))
    drawLevel(main_Vars.data_level1, main_Vars.data_buttonground, 13, 5, False, tmp, tmp, 1)
    pygame.draw.rect(main_Vars.data_buttonground, main_Vars.BLACK, (tmp, tmp, 13 * 15, 5 * 26), 5)
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
                drawBrick(col, row, level[row][col][0], width, height, marginY, addX, addY, outline, ground=ground)


def drawBrick(col, row, cl, width, height, marginY, addX, addY, outline, ground=()):
    if ground == ():
        ground = main_Vars.data_paddleground
    # Col(x) max = 0-14
    # Row(y) max = 0-25
    # global main_Vars.data_actionground
    if col >= 15 or row >= 26:
        return False
    else:
        pygame.draw.rect(ground, cl, (addX + col * width, addY + marginY + row * height, width, height))
        pygame.draw.rect(ground, main_Vars.BLACK, (addX + col * width, addY + marginY + row * height, width, height),
                         outline)


"""
def drawMenu():
    global main_Vars.data_foreDraw
    global main_Vars.data_bgDraw
    if main_Vars.data_bgDraw:
        drawMenuBackground()
        constructor("o")
        main_Vars.data_bgDraw = False
        module_Main.fitTextDraw(main_Vars.data_fontFile1,80,30,"START",main_Vars.data_canvasX/2,main_Vars.data_canvasY/2,110,100,100,Ycorrection = 3)
        #normTextDraw(main_Vars.data_fontFile1,main_Vars.data_canvasX/2,50,12,"Brick Breaker",0,0,0,bold = False,italic = False)
        ##TEMP##
        main_Vars.data_paddle.create()
    elif main_Vars.data_foreDraw != 0:
        main_Vars.data_foreground.fill((0,0,0,0))
        drawLevelSelect()
        normTextDraw(main_Vars.data_fontFile1,main_Vars.data_canvasX/2,50,12,"Brick Breaker",0,0,0,bold = False,italic = False)
        main_Vars.data_foreDraw -= 1
    main_Vars.data_allSprites.update()
    main_Vars.data_allSprites.draw(main_Vars.data_actionground)
"""


def drawMenu():
    drawLevelSelect()
    drawMenuBackground()
    sprite_Paddle.paddleCreator()
    # self, X, Y, W, H, R1, G1, B1, R2, G2, B2, newState, text, font, R3, G3, B3, depth = 10, middle = True, bold= False, italic = False, usePrevFont = False)
    sprite_Button.buttonCreator(480, 350, 100, 50, 105, 250, 250, 50, 150, 150, "Menu", "START",
                                main_Vars.data_fontFile1, 100,
                                50, 50, mid=True, Ycor=4)
    sprite_Button.spawnCreatedButtons(main_Vars.data_buttonground)
    main_Modules.normTextDraw(main_Vars.data_fontFile1, main_Vars.data_canvasX / 2, 50, 12, "Brick Breaker", 0, 0, 0,
                              bold=False,
                              italic=False)
    main_Vars.data_tick1 = True
    # drawLevel(main_Vars.data_level1,main_Vars.data_background)
    print("done!")
    main_Vars.data_allSprites.update()
    #main_Vars.data_allSprites.draw(main_Vars.data_paddleground)


def drawMenuBackground():
    backColor = [154, 52, 53]
    curtainColor = [250, 0, 0]
    for n in xrange(18):
        pygame.draw.rect(main_Vars.data_background, backColor,
                         (n * 30, n * 20, main_Vars.data_canvasX - (60 * n), main_Vars.data_canvasY - (40 * n)))
        backColor = [154 - (n * 2), 52 + (n * 9), 53 + (n * 8)]
    for num in xrange(19):
        pygame.draw.polygon(main_Vars.data_background, curtainColor, (((num * 10), 0), (10 + (num * 10), 0), (0, 450)))
        pygame.draw.polygon(main_Vars.data_background, curtainColor, (
            (main_Vars.data_canvasX - (num * 10), 0), (main_Vars.data_canvasX, 450),
            (main_Vars.data_canvasX - 10 - (num * 10), 0)))
        pygame.draw.polygon(main_Vars.data_background, curtainColor,
                            (((num * 8), main_Vars.data_canvasY), (10 + (num * 8), main_Vars.data_canvasY), (0, 450)))
        pygame.draw.polygon(main_Vars.data_background, curtainColor, (
            (main_Vars.data_canvasX - (num * 8), main_Vars.data_canvasY),
            (main_Vars.data_canvasX - 10 - (num * 8), main_Vars.data_canvasY), (main_Vars.data_canvasX, 450)))
        if not curtainColor[0] < 20 + num:
            curtainColor[0] -= 5 + (num)
        curtainColor[1] += 20 - (num)
        curtainColor[2] += abs(num - 5)
    main_Vars.screen.blit(main_Vars.data_background, (0, 0))


###############MAIN FUNCTION###############

def drawGame():
    if not main_Vars.data_tick1:
        if main_Vars.data_state == "menu":
            drawMenu()
        else:
            main_Vars.data_background.fill((100, 255, 255))
    main_Vars.data_spriteGroup_paddle.update()


# ================================####INITIAL CALLS####================================================================================#

def main():
    pygame.init()
    pygame.time.set_timer(USEREVENT + 1, 100)

    # Convert Surface object to make blitting faster.

    # Copy background to main_Vars.screen (position (0, 0) is upper left corner).
    # Create Pygame clock object.
    clock = pygame.time.Clock()
    mainloop = True
    FPS = 30
    ###INTERACTIVES###
    ###-----------###
    playtime = 0.0
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
                    main_Vars.data_right = True
                elif event.key == pygame.K_LEFT:
                    main_Vars.data_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    main_Vars.data_right = False
                elif event.key == pygame.K_LEFT:
                    main_Vars.data_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                main_Vars.data_mousePressedPos = pygame.mouse.get_pos()
                main_Vars.data_spriteGroup_buttons.update("d")
            elif event.type == pygame.MOUSEBUTTONUP:
                main_Vars.data_mousePressedPos = ()
                main_Vars.data_spriteGroup_buttons.update("u")

        text = "Bricks Alpha 0.2 {" + "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime) + "}"
        pygame.display.set_caption(text)
        drawGame()


        main_Vars.screen.blit(main_Vars.data_background, (0, 0))
        main_Vars.screen.blit(main_Vars.data_paddleground, (0, main_Vars.data_paddleY))
        main_Vars.screen.blit(main_Vars.data_buttonground, (0, 0))
        main_Vars.screen.blit(main_Vars.data_textground, (0, 0))
        """
        #main_Vars.screen.blit(main_Vars.data_foreground, (0, 0))
        main_Vars.screen.blit(main_Vars.data_buttonground, (0, 0))
        main_Vars.screen.blit(main_Vars.data_textground, (0, 0))
        """
        pygame.display.update(main_Vars.data_rect)
        main_Vars.data_rect = []
        #pygame.display.update()

    # Finish Pygame.
    pygame.quit()


main()
