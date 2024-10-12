import tkinter as tk
from tkinter import Canvas
from typing import Tuple

from gui.hex_colors import *


# TODO: connecting orbs to hexes with popup menu
# option 1: have hex manager handle orbs, connect tile back to manager and allow tile to request orb
# option 2: have tile handle orbs as a class level (static) property <-- cleanest?

class Orb:
	def __init__(self, canvas: Canvas, position: Tuple[float, float], radius, color):
		self.canvas = canvas
		self.position = position  # currently tuple, should it be a Point?
		self.radius = radius / 4
		self.color = ColorSet
		self.widget = self._create_widget()
		self.connected_tile = None
		self.visible = False
	
	def _create_widget(self):
		# TODO: use custom color system
		wonk_offset = 1  # to account for create_oval's slight wonk.
		x1 = self.position[0] - self.radius
		y1 = self.position[1] - self.radius
		x2 = self.position[0] + self.radius + wonk_offset
		y2 = self.position[1] + self.radius + wonk_offset
		oval = self.canvas.create_oval(x1, y1, x2, y2, fill='red', activefill='green')
		return oval
	
	def resize(self, modifier):  # modifier of 1 moves the widget without resizing
		x1, y1, x2, y2 = self.canvas.coords(self.widget)
		self.canvas.coords(self.widget,
						   x1 * modifier,
						   y1 * modifier,
						   x2 * modifier,
						   y2 * modifier)
	
	def connect(self, tile):  # should only be called from tile
		if self.connected_tile:
			self.connected_tile.disconnect()
		self.connected_tile = tile
		self.position = self.connected_tile.get_position()
		self.resize(1)  # is this smelly?
		self.reveal()
	
	def disconnect(self):
		if self.connected_tile:
			self.connected_tile = None
		self.position = (0, 0)
		self.resize(1)
		self.hide()
	
	def hide(self):
		self.canvas.itemconfigure(self.widget, state='hidden')
		self.visible = False
	
	def reveal(self):
		self.canvas.itemconfigure(self.widget, state='normal')
		self.visible = True


"""
def draw_circle(center_x, center_y, radius, canvas):
	wonk_offset = 1  # to account for create_oval's slight wonk.
	r = radius / 4  # make circle smaller than hex, should be defined in an .ini file
	x1 = center_x - r
	y1 = center_y - r
	x2 = center_x + r + wonk_offset
	y2 = center_y + r + wonk_offset
	oval = canvas.create_oval(x1, y1, x2, y2, fill='red', activefill='green')
	return oval


def resize_circle(canvas, circle, modifier):
	x1, y1, x2, y2 = canvas.coords(circle)
	canvas.coords(circle, x1 * modifier, y1 * modifier, x2 * modifier, y2 * modifier)
"""