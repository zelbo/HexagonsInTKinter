# Concerning multiple hexagons: arranging on screens and doing tuple math conversion between q,r,s and x,y
from Hexagon import *
import math

SQRT3 = math.sqrt(3)


class HexManager:

    def __init__(self, canvas, offset, hex_size, columns, rows):
        # keep track of columns and rows for bounds checking?
        self.canvas = canvas
        self.map_columns = columns
        self.map_rows = rows
        self.map_offset = offset
        self.hex_map = [[None] * columns for i in range(rows)]  # Local variable 'i' value is not used?
        self.hex_size = hex_size
        hex_width = 2 * hex_size
        hex_height = SQRT3 * hex_size
        self.delta_q = (.75 * hex_width, .5 * hex_height)  # over one horizontal unit, down one vertical unit
        self.delta_r = (0, hex_height)  # no horizontal change, down two vertical units
        self.populate_grid()

    def populate_grid(self):
        # is the array created by list comprehension reversed as [y][x]?
        for row in range(self.map_rows):
            for column in range(self.map_columns):
                # math out the position
                position = self.get_position(column, row)
                hexagon = Hexagon(position, self.hex_size)  # temp shape variable
                # should the Hexagon class handle drawing to the canvas?
                self.hex_map[row][column] = self.canvas.create_polygon(hexagon.shape, fill='#666',
                                                                       activefill='#ccc')  # residual polygon
                # Change properties after creation:
                # canvas.itemconfig(my_rectangle, fill='red')

    def get_position(self, q_coord, r_coord):
        # Tuple math using list comprehensions for q,r,s cubic coordinate system
        # multiply grid coordinates by their deltas, then add the vectors
        q_vector = tuple(q_coord * delta for delta in self.delta_q)  # valid?
        r_vector = tuple(r_coord * delta for delta in self.delta_r)
        delta_vector = tuple(q_v + r_v for q_v, r_v in zip(q_vector, r_vector))
        hex_position = tuple(offset + d_v for offset, d_v in zip(self.map_offset, delta_vector))
        return hex_position

# --------------------
# zip function for color combining?
# https://docs.python.org/3/library/functions.html#zip
# color_pair = (bright, dull) for active/inactive colors
# -----------------------------------------------------
# Color in Tkinter:
# - Hex Strings
# '#rgb'		Four bits per color
# '#rrggbb'		Eight bits per color
# '#rrrgggbbb'	Twelve bits per color
# - Named Colors
# The colors 'white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', and 'magenta' will always be available.
# https://www.tcl.tk/man/tcl/TkCmd/colors.html
