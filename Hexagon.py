# --- obsolete, renamed in major update ---

# Concerning singular hexagons: shapes and such
import math


class Hexagon:

    def __init__(self, position, size):
        self._x = None
        self._y = None
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.shape = self.get_shape()

        # Neighbors using (q, r) coordinates: (list of tuples?)
        # (-1, 0), (0, -1), (+1, -1), (+1, 0), (0, +1), (-1, +1)

    # Expected type '(Any) -> None | None', got '(self: Hexagon) -> None' instead
    def get_x(self): return self._x
    def set_x(self, value): self._x = value
    def del_x(self): del self._x
    x = property(get_x, set_x, del_x, "Position on the horizontal axis.")

    def get_y(self): return self._y
    def set_y(self, value): self._y = value
    def del_y(self): del self._y
    y = property(get_y, set_y, del_y, "Position on the vertical axis.")

    def flat_hex_corner(self, i):
        angle_deg = 60 * i
        angle_rad = math.pi / 180 * angle_deg
        point = (self.x + self.size * math.cos(angle_rad), self.y + self.size * math.sin(angle_rad))
        return point

    def get_shape(self):
        shape = []
        for i in range(6):
            point = self.flat_hex_corner(i)
            shape.append(point)
        return shape
