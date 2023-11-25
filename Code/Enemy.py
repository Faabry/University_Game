import Const as c
from Entity import Entity

class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= c.ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = c.SCREEN_WIDHT

