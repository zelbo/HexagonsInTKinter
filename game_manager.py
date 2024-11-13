# Todo: clean up comments
# TODO: handle orb switching here- hide old one, reveal new one, max one of each color.
from orb import Orb
from redblob_hexagons import *
import game_tile as ht
from helper_functions import *
import random
import constants
from gui.context_menu import *

import settings

options = settings.options


class GameManager:
	global options
	
	def __init__(self):
		# keep track of columns and rows for bounds checking?
		
		# self.map_offset = Point(offset[0], offset[1])
		
		self.current_color = Colors.grey
		self.hex_map = []
		# TODO: size handled by tile.geometry
		# use tile.geometry.size, keep width and height for calculations here.
		self.starting_size = options.hexagon_size
		
		# should this part be in geometry?
		hexagon_width = 2 * self.starting_size
		hexagon_height = constants.SQRT3 * self.starting_size
		# this part for sure here, because it has to do with display of items in a map layout
		self.delta_q = (.75 * hexagon_width, .5 * hexagon_height)  # over one, down one
		self.delta_r = (0, hexagon_height)  # no horizontal change, down two
		
		self.populate_grid()
		
		self.orbs = self.create_orbs()
	
	def on_click(self, event):
		# find the widget, get the location of that widget
		clicked_item = event.widget.find_withtag("current")  # more accurate than find_closest
		clicked_coordinates = options.window_canvas.coords(clicked_item)
		center = find_center(clicked_coordinates)
		
		print(constants.SEPARATOR)
		print('Clicked Item: ', clicked_item)
		print('Averaged: ', center)
		
		# from location of the clicked widget, find the game tile
		# make this a function?
		# todo: -------------------------------------------------
		# todo: After recent changes, this section could use a closer look, possible refactor
		# todo: -------------------------------------------------
		first_tile = self.hex_map[0][0]
		radius = float(first_tile.get_size())  # switch to global options?
		size = Point(radius, radius)
		offset_modifier = radius / self.starting_size
		new_offset = Point(options.hexagon_offset.x * offset_modifier,
						   options.hexagon_offset.y * offset_modifier)
		
		layout = Layout(layout_flat, size, new_offset)
		complex_coord = pixel_to_hex(layout, center)
		rounded = hex_round(complex_coord)
		
		print(constants.SEPARATOR)
		print('Complex Coordinate from point_to_hex', complex_coord)
		print('Rounded:', rounded)
		
		tile = self.hex_map[rounded.r][rounded.q]
		tile.debug()
		tile.menu()
	
	def populate_grid(self):
		for row in range(options.map_rows):
			row_list = []
			for column in range(options.map_columns):
				position = self.get_position(column, row)
				color = random.choice(color_list)
				tile = ht.GameTile(options.window_canvas, position, options.hexagon_size, color)
				options.window_canvas.tag_bind(tile.get_hex_widget(), '<ButtonPress-3>', self.on_click)
				options.window_canvas.addtag_withtag("hexagon", tile.get_hex_widget())
				row_list.append(tile)
			self.hex_map.append(row_list)
			
			print(constants.SEPARATOR)
			print(self.hex_map)
	
	def get_position(self, q_coord, r_coord):
		"""
		Tuple math using list comprehensions for cubic(q,r,s) coordinate system.
		Multiply grid coordinates by their deltas, then add the vectors.
		
		:param q_coord: correlates to column in a grid
		:param r_coord: correlates to row in a grid
		:return: returns a 2D position in the form of a tuple of floats
		"""
		q_vector = tuple(q_coord * delta for delta in self.delta_q)
		r_vector = tuple(r_coord * delta for delta in self.delta_r)
		delta_vector = tuple(q_v + r_v for q_v, r_v in zip(q_vector, r_vector))
		hex_position = tuple(offset + d_v for offset, d_v in zip(options.hexagon_offset, delta_vector))
		return hex_position
	
	def resize(self, new_size):
		# TODO: -------------------------------------------------
		# TODO: HERE IS ZOOM ISSUE! FIND CORRECT VALUES FOR ZOOM!
		# TODO: -------------------------------------------------
		# old_size = self.hexagon.get_size()  # use proto_hex
		# options.hexagon_size = new_size
		# modifier = float(new_size) / float(old_size)

		for row in range(options.map_rows):
			for column in range(options.map_columns):
				self.hex_map[row][column].resize(new_size)
				print(constants.SEPARATOR)
				print('Game Manager - Resize')
				print('Row: ', row, 'Column: ', column, 'Size: ', new_size)
		
		settings.update_scroll_region()
		options.window_canvas.update_idletasks()
		options.window_canvas.update()
	
	def change_color(self, color_set):
		# Todo: shift responsibility to tile.
		self.current_color = color_set
	
	def create_orbs(self):
		orbs = []
		for c in color_list:
			o = Orb(options.window_canvas, (0, 0), self.starting_size, c)
			options.window_canvas.tag_bind(o, '<ButtonPress-3>', self.on_click)
			options.window_canvas.addtag_withtag("orb", o)
			orbs.append(o)
		return orbs


if __name__ == "__main__":
	# tests
	pass
