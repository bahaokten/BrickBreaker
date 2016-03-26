from __future__ import print_function, division

import pygame
from pygame.locals import *

import main_Vars
import main_Handler
import sprite_Ball
import main_Draw


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

###############MAIN FUNCTION###############

def doGame():
    if not main_Vars.data_tick1:
        if main_Vars.data_state == "menu":
            main_Handler.drawMenu()
        elif main_Vars.data_state == "lvlmenu1":
            main_Handler.drawLevelMenu(1)
        elif main_Vars.data_state == "lvlmenu2":
            main_Handler.drawLevelMenu(2)
        elif main_Vars.data_state == "level1":
            main_Handler.levelCreator(1)
        main_Vars.data_tick1 = True
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
                if event.key == pygame.K_SPACE:
                    main_Vars.data_space = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    main_Vars.data_right = False
                elif event.key == pygame.K_LEFT:
                    main_Vars.data_left = False
                if event.key == pygame.K_SPACE:
                    main_Vars.data_space = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                main_Vars.data_mousePressedPos = pygame.mouse.get_pos()
                main_Vars.data_spriteGroup_buttons.update("d")
            elif event.type == pygame.MOUSEBUTTONUP:
                main_Vars.data_mousePressedPos = ()
                main_Vars.data_spriteGroup_buttons.update("u")

        text = "Bricks Alpha 0.2 {" + "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime) + "}"
        pygame.display.set_caption(text)
        if "level" in main_Vars.data_state:
            main_Vars.data_paddleGround.fill((1, 2, 3))

        doGame()


        main_Vars.screen.blit(main_Vars.data_backGround, (0, 0))
        if "level" in main_Vars.data_state:
            main_Vars.screen.blit(main_Vars.data_paddleGround, (0, main_Vars.data_paddleY))
            main_Vars.screen.blit(main_Vars.data_foreGround, (0, 0))
        main_Vars.screen.blit(main_Vars.data_buttonGround, (0, 0))
        main_Vars.screen.blit(main_Vars.data_textGround, (0, 0))
        sprite_Ball.drawBalls()
        if not main_Vars.data_updateAll:
            pygame.display.update(main_Vars.data_rect)
        else:
            pygame.display.update()
            main_Vars.data_updateAll = False
        print (main_Vars.data_rect)
        main_Vars.data_rect = []
        #pygame.display.update()

    # Finish Pygame.
    pygame.quit()


main()
