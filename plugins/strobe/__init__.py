import time
import colorsys
from plugin_base import Plugin

red = int(0);
blue = int(0);
green = int(0);


class StrobePlugin(Plugin):

    def __init__(self):
        Plugin.__init__(self)
        self.hue = 0.0
        self.last_frame_time = 0

    def ready(self):
        return True

    def getNextFrame(self):

        
       
        red = int(255 * red) 
        green = int(255 * green)
        blue = int(255 * blue)
        frame = {}
        for row in self.tile_matrix:
            for tile in row:
                if tile is not None:
                    frame[tile["unit"]] = (red, green, blue)
        self.last_frame_time = time.time()
        return frame


plugin = StrobePlugin
