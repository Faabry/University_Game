import pygame as pg
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name, position: tuple):
        self.name = name
        self.surface = pg.image.load("./asset/" + name + ".png")
        self.speed = 0
        self.rect = self.surface.get_rect(left=position[0],
                                       top= position[1])

    @abstractmethod
    def move(self, ):
        pass

