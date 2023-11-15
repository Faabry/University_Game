import pygame as pg
import Const as c
from Menu import Menu


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
            menu.run()

    

