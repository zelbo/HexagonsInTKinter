"""
Game tile.
Contains hexagon geometry attribute, canvas polygon,
functions for interfacing between the two, and other game information.
leave cartesian/cubic conversion to game_manager,
this is just for adding game specific mechanics to an individual cel in the grid.
Neighbors here or in grid game_manager?
Option 1 - list of references here
Option 2 - use a find neighbor function <-- would be doing this anyway even for option 1
Depends on where we want logic to reside, and if option 1 would help streamline or just add clutter
when clicked, game_manager can just tell me what to do after the fact (Ex post facto)
"""
from hex_geometry import *
from gui.hex_colors import *
from orb import *
import constants
from gui.context_menu import *


class GameTile:
	def __init__(self, canvas, position, size, color=None):
		self.canvas = canvas
		self.hexagon = HexGeometry(position, size)
		# todo: add getter/setter properties to access underlying geometry object?
		if not color:  # could we just put the default in the argument list, or does it have to be None?
			self.color = Colors.grey
			print(constants.SEPARATOR)
			print('Default grey.')
		else:
			self.color = color
			print(constants.SEPARATOR)
			print('New color: ', self.color)
		
		self.connected_orb = None
		self.hex_widget = self._create_hex_widget()
		
		self.popup_menu = ContextMenu(self.canvas, self)
	
	def __str__(self):
		return f'Shape: {self.hexagon}, Color: {self.color}'
	
	def _create_hex_widget(self):
		return self.canvas.create_polygon(
			self.hexagon.get_shape(),
			outline=self.color.border,
			fill=self.color.dim,
			activefill=self.color.bright
		)
	
	def change_color(self, new_color):
		# TODO: reconcile color system differences, will need to be standardized for flood-fill mechanic
		self.color = new_color
		self.canvas.itemconfigure(
			self.hex_widget,
			outline='black',
			fill=darken_hex_from_name(self.canvas, self.color),
			activefill=self.color
		)
	
	def resize(self, new_size):
		self.hexagon.update_size(new_size)
		self.canvas.coords(self.hex_widget, self.hexagon.get_shape())
		if self.connected_orb:
			self.connected_orb.resize(self.hexagon.modifier)
	
	def get_size(self):
		return self.hexagon.get_size()
	
	def get_hex_widget(self):
		return self.hex_widget
	
	def connect(self, orb):  # manager should only tell tile to connect an orb, tile handles the rest
		if self.connected_orb:
			self.connected_orb.disconnect()
		self.connected_orb = orb
		self.connected_orb.connect(self)
	
	def disconnect(self):
		if self.connected_orb:
			self.connected_orb.disconnect()
		self.connected_orb = None
		
	def menu(self):
		print(constants.SEPARATOR)
		print('popup menu')
		# TODO: need to look at what coords we're using. position is relative to screen, not window?
		if self.connected_orb:
			self.popup_menu.orb_menu.tk_popup(self.hexagon.x, self.hexagon.y, 0)
		else:
			self.popup_menu.color_menu.tk_popup(int(self.hexagon.x), int(self.hexagon.y), 0)
	
	def debug(self):
		print(constants.SEPARATOR)
		print('Tile info dump: ')
		print(self.__repr__())
		print('Tile info readable: ')
		print(self.__str__())


if __name__ == "__main__":
	# tests
	pass
