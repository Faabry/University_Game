import pygame as pg

SCREEN_WIDHT = 576
SCREEN_HEIGHT = 324

COLOR_ORANGE = (255, 127, 0)

COLOR_WHITE = (255, 255, 255)

MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P COOPERATIVE",
               "NEW GAME 2P COMPETITIVE",
               "QUIT")

# E
ENTETY_ENEMY = pg.USEREVENT + 1
ENTITY_SPEED = {"level1bg0": 0,
                "level1bg1": 1,
                "level1bg2": 2,
                "level1bg3": 3,
                "level1bg4": 4,
                "Player 1": 4,
                "Player 2": 4,
                "Enemy 1": 3,
                "Enemy 2": 2}

PLAYER_UP = {"Player 1": pg.K_UP,
             "Player 2": pg.K_w}

PLAYER_DOWN = {"Player 1": pg.K_DOWN,
               "Player 2": pg.K_s}

PLAYER_LEFT = {"Player 1": pg.K_LEFT,
               "Player 2": pg.K_a}

PLAYER_RIGHT = {"Player 1": pg.K_RIGHT,
                "Player 2": pg.K_d}