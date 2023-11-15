import pygame as pg
import Const as c

class Menu:
    def __init__(self, window):
        self.screen: pg.Surface = window

        # Loading the Menu's backgrounds
        self.bg1 = pg.image.load("../assets/city 3/1.png")
        self.bg2 = pg.image.load("../assets/city 3/4.png")

        # Getting the rectangle of the image
        self.rect = self.bg1.get_rect(left=0, top=0)
        
        

    def run(self):
        # Loading and playing the Menu's music
        pg.mixer_music.load("../assets/Sounds/fase1.wav")
        pg.mixer_music.play(-1)
        while True:
            # Updating the images into the window
            self.screen.blit(source=self.bg1, dest=self.rect)
            self.screen.blit(source=self.bg2, dest=self.rect)

             # Creating the title of the game
            self.menu_text(text="City's War",
                           text_size=45,
                           color=(255, 127, 0),
                           text_center_pos=(c.SCREEN_WIDHT / 3, 50))
            
            # Update the window
            pg.display.flip()

            
            pressed_key = pg.key.get_pressed()
            if pressed_key[pg.QUIT]:
                break

    # Creating the Game's title
    def menu_text(self, text, text_size,
                  color: tuple, text_center_pos: tuple):
        text_font = pg.font.SysFont(name="Bookman Old Style",
                                    size=text_size)
        text_surf = text_font.render(text, True, color)
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_center_pos)

