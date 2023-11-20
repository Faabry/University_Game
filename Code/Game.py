import pygame as pg
import Const as c
from Menu import Menu
from Level import Level
import sys


class Game:
    def __init__(self):
        # Initializing the game
        pg.init()

        # Creating the window
        self.screen = pg.display.set_mode(size=(c.SCREEN_WIDHT,
                                                c.SCREEN_HEIGHT))

    def run(self):
        while True:
            # Creating the menu
            menu = Menu(self.screen)
            menu_return = menu.run()

            if menu_return in [c.MENU_OPTION[0],
                               c.MENU_OPTION[1],
                               c.MENU_OPTION[2]]:
                level = Level(self.screen, "Level 1", menu_return)
                level.run()
            else:
                pg.quit()
                sys.exit()
    
            
