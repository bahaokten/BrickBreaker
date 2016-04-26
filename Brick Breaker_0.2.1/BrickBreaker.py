from __future__ import print_function, division

import pygame
from pygame.locals import *

import main_Vars
import main_Handler
import sprite_Ball


###############MAIN FUNCTION###############

def doGame():
    if not main_Vars.data_tick1:
        print("!-GameState-! ", main_Vars.data_state)
        if main_Vars.data_state == "menu":
            main_Handler.drawMenu()
        elif main_Vars.data_state == "lvlmenu1":
            main_Handler.drawLevelMenu(1)
        elif main_Vars.data_state == "lvlmenu2":
            main_Handler.drawLevelMenu(2)
        elif main_Vars.data_state == "level1":
            main_Handler.levelCreator(1)
        elif main_Vars.data_state == "level2":
            main_Handler.levelCreator(2,background = 2)
        elif main_Vars.data_state == "level3":
            main_Handler.levelCreator(3,background = 3)
        elif main_Vars.data_state == "gameoverbad":
            main_Vars.data_isLevel = False
        if "level" in main_Vars.data_state:
            main_Vars.playLevelMusic(main_Vars.data_musicFile1,volume = 0.75)
        main_Vars.data_tick1 = True
    if main_Vars.data_isLevel:
        main_Vars.data_spriteGroup_paddle.update()
        main_Vars.data_spriteGroup_ball.update()
    if not main_Vars.data_tick2:
        None
        main_Vars.data_tick2 = True




# ================================####INITIAL CALLS####================================================================================#

def main():
    pygame.init()
    pygame.time.set_timer(USEREVENT + 1, 100)

    # Convert Surface object to make blitting faster.

    # Copy background to main_Vars.screen (position (0, 0) is upper left corner).
    # Create Pygame clock object.
    clock = pygame.time.Clock()
    mainloop = True
    FPS = 120
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

        doGame()

        main_Vars.screen.blit(main_Vars.data_backGround, (0, 0))
        if main_Vars.data_isLevel:
            #main_Vars.screen.blit(main_Vars.data_paddleGround, (0, main_Vars.data_paddleY))
            if main_Vars.data_paddleImg:
                pos = main_Vars.data_spriteGroup_paddle.sprites()[0].info(posOnly = True)
                main_Vars.screen.blit(main_Vars.data_paddleImg, pos)
            if main_Vars.data_ballImg:
                for ball in main_Vars.data_spriteGroup_ball:
                    pos = ball.getPos()
                    main_Vars.screen.blit(main_Vars.data_ballImg, pos)
            main_Vars.screen.blit(main_Vars.data_foreGround, (0, 0))
        main_Vars.screen.blit(main_Vars.data_buttonGround, (0, 0))
        main_Vars.screen.blit(main_Vars.data_textGround, (0, 0))
        pygame.display.update(main_Vars.data_rect)
        if not main_Vars.data_updateAll:
            pygame.display.update(main_Vars.data_rect)
        else:
            pygame.display.update()
            main_Vars.data_updateAll = False
        main_Vars.data_rect = []

    # Finish Pygame.
    pygame.quit()


main()
