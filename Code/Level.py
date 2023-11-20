import pygame as pg
from Entity import Entity
from EntityFactory import EntityFactory

class Level:
    def __init__(self, screen, name, menu_option):
        self.name = name
        self.screen: pg.Surface = screen
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(entity_name="level1bg"))

    def level_up(self):
        pass

    def run(self):
        while True:
            for ent in self.entity_list:
                self.screen.blit(source=ent.surface, dest=ent.rect)
                ent.move()
            pg.display.flip()

