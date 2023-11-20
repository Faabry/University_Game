from Background import Background
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
            

