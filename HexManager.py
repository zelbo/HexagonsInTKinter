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
		# self.hex_map = [[None] * columns for row in range(rows)]
		self.hex_map = []
		self.hex_size = hex_size
		hex_width = 2 * hex_size
		hex_height = SQRT3 * hex_size
		self.delta_q = (.75 * hex_width, .5 * hex_height)  # over one horizontal unit, down one vertical unit
		self.delta_r = (0, hex_height)  # no horizontal change, down two vertical units
		self.populate_grid()
	
	def on_click(self, event):
		print('Got object click', event.x, event.y)
		print(event.widget.find_closest(event.x, event.y))
		self.canvas.itemconfigure(event.widget, fill='blue')
	
	# _tkinter.TclError: invalid boolean operator in tag search expression
	
	def populate_grid(self):
		# is the array created by list comprehension reversed as [y][x]?
		for row in range(self.map_rows):
			for column in range(self.map_columns):
				position = self.get_position(column, row)
				hexagon = Hexagon(position, self.hex_size)  # temp shape variable
				# should the Hexagon class handle drawing to the canvas? make a GUI manager?
				tile = self.canvas.create_polygon(hexagon.shape, outline='#000', fill='#666', activefill='#ccc')
				self.hex_map.append(tile)  # residual polygon
				self.canvas.tag_bind(tile, '<ButtonPress-1>', self.on_click)
			# maybe add row and column to the callback arg list, and use the array instead of event.widget?
	
	def get_position(self, q_coord, r_coord):
		# Tuple math using list comprehensions for q,r,s cubic coordinate system
		# multiply grid coordinates by their deltas, then add the vectors
		q_vector = tuple(q_coord * delta for delta in self.delta_q)
		r_vector = tuple(r_coord * delta for delta in self.delta_r)
		delta_vector = tuple(q_v + r_v for q_v, r_v in zip(q_vector, r_vector))
		hex_position = tuple(offset + d_v for offset, d_v in zip(self.map_offset, delta_vector))
		return hex_position
	
	def adjust_grid(self):
		# cut and past to unskew drawn hexmap
		# segment = columns - 2
		# if segment > 0, move those cels to the bottom of the grid
		# should we use an object pool of hexes?
		# delete and recreate hexes?
		segment = self.map_columns - 2
		if segment > 0:
			for i in range(self.map_rows):
				for j in range(segment):
					print('Honestly, this is getting silly. Time to revisit redblob.')

# Change properties after creation:
# canvas.itemconfig(my_rectangle, fill='red')

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
# https://en.wikipedia.org/wiki/Web_colors
