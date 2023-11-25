from Entity import Entity
import Const as c
import pygame as pg

class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        

    def move(self, ):
        # Getting the pressed keys for user
        pressed_key = pg.key.get_pressed()
        if pressed_key[c.PLAYER_UP[self.name]]:
            if self.rect.centery < 10:
                self.rect.centery = 15
            else:
                self.rect.centery -= c.ENTITY_SPEED[self.name]
        if pressed_key[c.PLAYER_DOWN[self.name]]:
            if self.rect.centery > c.SCREEN_HEIGHT - 15:
                self.rect.centery = c.SCREEN_HEIGHT - 15
            else:
                self.rect.centery += c.ENTITY_SPEED[self.name]
        if pressed_key[c.PLAYER_RIGHT[self.name]]:
            if self.rect.centerx > c.SCREEN_WIDHT - 40:
                self.rect.centerx = c.SCREEN_WIDHT - 40
            else:
                self.rect.centerx += c.ENTITY_SPEED[self.name]
        if pressed_key[c.PLAYER_LEFT[self.name]]:
            if self.rect.centerx < 40:
                self.rect.centerx = 40
            else:
                self.rect.centerx -= 4

