import pygame as pg

class Menu:
    def __init__(self, window):
        self.screen: pg.Surface = window

        # Loading the background for menu
        self.bg1 = pg.image.load("../assets/city 3/1.png")
        self.bg2 = pg.image.load("../assets/city 3/4.png")

        # Getting the rectangle of the image
        self.rect = self.bg1.get_rect(left=0, top=0)
        
        

    def run(self):
        while True:
            self.screen.blit(source=self.bg1, dest=self.rect)
            self.screen.blit(source=self.bg2, dest=self.rect)
            pg.display.flip()

            pressed_key = pg.key.get_pressed()
            if pressed_key[pg.QUIT]:
                break

