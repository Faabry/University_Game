from Background import Background
from Player import Player
from Enemy import Enemy
import random
import Const as c

class EntityFactory:

    # I don't need to create an object to use this class
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case "level1bg":
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f"level1bg{i}",
                                              position=(0, 0)))
                    list_bg.append(Background(f"level1bg{i}",
                                              position=(c.SCREEN_WIDHT, 0)))
                return list_bg

            case "player1":
                return Player(name="Player 1",
                              position= (10, c.SCREEN_HEIGHT / 2))
            case "player2":
                return Player(name="Player 2",
                              position= (10, c.SCREEN_HEIGHT / 2))
            
            case "enemy1":
                return Enemy("Enemy 1",
                             (c.SCREEN_WIDHT + 20,
                              random.randint(40, c.SCREEN_HEIGHT - 40)))
            
            case "enemy2":
                return Enemy("Enemy 2",
                             (c.SCREEN_WIDHT + 20,
                              random.randint(40, c.SCREEN_HEIGHT - 40)))
            

