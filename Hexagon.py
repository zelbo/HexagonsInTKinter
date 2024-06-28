import math


class Hexagon:

    def __init__(self, position: tuple, size: int, color: tuple) -> None:
        # use properties for extracting x,y from position tuple
        # for now, quick and dirty way:
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.color_bright = color[0]
        self.color_dull = color[1]
        self.shape = self.get_shape(position, size)
        print('Hexagon initialized')

    @staticmethod
    def flat_hex_corner(position, size, i):
        # find a hexagon corner given a number from 0 to 5
        angle_deg = 60 * i
        angle_rad = math.pi / 180 * angle_deg
        return angle_rad  # not right, but not what we're working on right now

    def get_shape(self, position, size):
        # get list of tuples to feed to canvas.draw_polygon
        shape = list()
        for i in range(6):
            shape.append(self.flat_hex_corner(position, size, i))
        return shape
