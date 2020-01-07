from serpent.game import Game

from .api.api import menghuanAPI

from serpent.utilities import Singleton




class SerpentmenghuanGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "executable"

        kwargs["window_name"] = "梦幻西游 ONLINE"

        
        
        #kwargs["executable_path"] = u"C:/Users/Administrator/Desktop/梦幻西游.lnk"
        kwargs["executable_path"] = u"D:/梦幻西游/my.exe"
        
        

        super().__init__(**kwargs)

        self.api_class = menghuanAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            "SAMPLE_REGION": (0, 0, 0, 0)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
