"""
Basic geometry:
size, position, and shape
no color, let game tile handle that
deals only with cartesian x,y coordinates
no canvas interaction here
"""
import math
from helper_functions import *
from typing import Any
import constants


class HexGeometry:
	def __init__(self, position, size):
		self._shape = []
		print(constants.SEPARATOR)
		print('Position: ', position)
		self._position = Point(position[0], position[1])  # do we have three different 2D vector styles now?
		self._size = size
		self.create_shape()
		self.modifier = 1
	
	@property
	def x(self) -> float: return float(self._position.x)
	
	@x.setter
	def x(self, value: Any) -> None: self._position.x = float(value)
	
	@x.deleter
	def x(self) -> None: raise AttributeError("Cannot delete x coordinate")
	
	@property
	def y(self) -> float: return float(self._position.y)
	
	@y.setter
	def y(self, value: Any) -> None: self._position.y = float(value)
	
	@y.deleter
	def y(self) -> None: raise AttributeError("Cannot delete y coordinate")
	
	def get_size(self):
		return self._size
	
	def update_size(self, new_size):  # should this math be moved to game tile?
		old_size = self._size
		self._size = new_size
		self.modifier = float(new_size) / float(old_size)
		self.update_position(self.modifier)
		self.update_shape(self.modifier)
	
	def update_position(self, modifier):
		self._position = Point(self._position.x * modifier, self._position.y * modifier)
	
	def update_shape(self, modifier):  # candidate for list comprehension?
		new_shape = []
		for point in self._shape:
			new_point = Point(point.x * modifier, point.y * modifier)
			new_shape.append(new_point)
		self._shape = new_shape
	
	def flat_hex_corner(self, i):
		angle_in_degrees = 60 * i
		angle_in_radians = math.pi / 180 * angle_in_degrees
		point = Point(self._position.x + float(self._size) * math.cos(angle_in_radians),
					  self._position.y + float(self._size) * math.sin(angle_in_radians))
		return point
	
	def get_shape(self):
		return flatten_list(self._shape)
	
	def create_shape(self):
		shape = []
		for i in range(6):
			point = self.flat_hex_corner(i)
			shape.append(point)
		self._shape = shape


if __name__ == "__main__":
	# tests
	testing_hex = HexGeometry((50, 50), 25)
	print(" - hex_geometry.py - ")
	print("x, y: ", testing_hex.x, testing_hex.y)
	print("Size: ", testing_hex.get_size())
	print("Shape: ", testing_hex.get_shape())
