from __future__ import print_function, division

import pygame
from pygame.locals import *

import main_Vars
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
            main_Draw.drawMenu()
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
        doGame()


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
