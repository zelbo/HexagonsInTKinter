from Hexagon import *
import math

class HexManager:
    def __init__(self, position, size, color):
        # make an array of hexagons
        self.my_hexagon = Hexagon((200, 200), 50, ('blue', 'yellow'))
        print('Manager initialized')