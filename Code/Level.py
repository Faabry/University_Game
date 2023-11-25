import pygame as pg
import Const as c
from Entity import Entity
from EntityFactory import EntityFactory
import random
import sys

class Level:
    def __init__(self, screen, name, menu_option):
        self.name = name
        self.screen: pg.Surface = screen
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("level1bg"))
        self.entity_list.append(EntityFactory.get_entity("player1"))
        if menu_option in [c.MENU_OPTION[1], c.MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity("player2"))
        # Create a new enemy every 2000 miliseconds
        pg.time.set_timer(c.ENTETY_ENEMY, 2000) 


    def level_up(self):
        pass

    def run(self):
        # Loading and playing the Level's music
        pg.mixer_music.load(f"asset/{self.name}.mp3")
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        while True:
            clock.tick(100)
            for ent in self.entity_list:
                # Drawing the entities
                self.screen.blit(source=ent.surface, dest=ent.rect)
                # Name of the level
                self.level_text(text_size= 20,
                                text= self.name,
                                color= c.COLOR_ORANGE,
                                text_pos= (10, 10))

                self.level_text(text_size=14,
                                text=f"fps: {round(clock.get_fps(), 2)}",
                                color= c.COLOR_ORANGE,
                                text_pos= (10, 40))
                ent.move()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == c.ENTETY_ENEMY:
                    choice = random.choice(("enemy1", "enemy2"))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # Update the screen frames
            pg.display.flip()


    # Creating the Game's title
    def level_text(self,
                   text,
                   text_size,
                   color: tuple,
                   text_pos: tuple):
        text_font = pg.font.SysFont(name="Bookman Old Style",
                                    size=text_size)
        text_surf = text_font.render(text, True, color)
        text_rect = text_surf.get_rect(center=text_pos)
        self.screen.blit(source=text_surf, dest=text_pos)
