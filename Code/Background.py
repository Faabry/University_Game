import Const as c
from Entity import Entity

class Background(Entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)
        pass


    def move(self):
        self.rect.centerx -= c.ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = c.SCREEN_WIDHT

