"""
Main entry point for interface controller.
"""
# TODO: slider and mouse wheel need to be combined, use one function if possible
import tkinter as tk
from tkinter import ttk

import gui.Point as config

import gui.canvas_manager
import gui.control_panel

from helper_functions import *

import constants
import settings

options = settings.options


class MainGUI:
	global options
	
	def __init__(self):
		self.root = tk.Tk()
		self.root.title(options.window_title)
		self.root.grid_columnconfigure(0, weight=1)
		self.root.grid_rowconfigure(0, weight=1)
		
		self._init_style()
		self._init_frame()
		
		self.canvas_manager = gui.canvas_manager.CanvasManager(self.frame)
		self.control_panel = gui.control_panel.ControlPanel(self.frame, self)
		
		self._bind_events()
		
		self.game_manager = None
	
	def _init_style(self):
		self.style = ttk.Style()
		self.style.theme_use(options.window_theme)
	
	def _init_frame(self):
		self.frame = ttk.Frame(self.root)
		self.frame.grid(sticky=tk.NSEW)
		self.frame.grid_columnconfigure(0, weight=1)
		self.frame.grid_rowconfigure(0, weight=1)
	
	def _bind_events(self):
		self.root.bind('<Configure>', self._on_window_resize)
		# self.canvas_manager.get_canvas().bind('<Configure>', self.canvas_manager.resize_canvas)
		# ^ this one is whacky. uncomment for fun.
		options.window_canvas.bind("<MouseWheel>", self.zoom)
		options.window_canvas.bind("<Button-4>", self.zoom)
		options.window_canvas.bind("<Button-5>", self.zoom)
	
	def zoom(self, event):
		# TODO: not quite there... something is off...
		step_value = .1
		new_value = 0
		if event.num == 5 or event.delta == -120:  # Zoom out
			print(constants.SEPARATOR)
			print('Zoom out (main_gui)')
			options.zoom_scale -= step_value
			#new_value = options.hexagon_size - step_value
		if event.num == 4 or event.delta == 120:  # Zoom in
			print(constants.SEPARATOR)
			print('Zoom in (main_gui)')
			options.zoom_scale += step_value
			#new_value = options.hexagon_size + step_value
		options.zoom_scale = clamp(options.zoom_scale, .1, 10)
		#new_value = clamp(new_value, options.zoom_minimum, options.zoom_maximum)
		#self.update_scale(new_value)
		# options.zoom_scale = int(value)
		# Keep zoom centered on mouse position
		x = options.window_canvas.canvasx(event.x)
		y = options.window_canvas.canvasy(event.y)
		
		# options.zoom_scale = max(3, min(int(options.zoom_scale), 100))
		
		# TODO: -------------------------------------------------
		# TODO: HERE IS ZOOM ISSUE! FIND CORRECT VALUES FOR ZOOM!
		# TODO: -------------------------------------------------
		# options.window_canvas.scale("all", 0, 0, x, y)
	
	# self.canvas_manager.canvas.scale("hexagon", 0, 0, self.zoom_modifier, self.zoom_modifier)
	
	def _on_window_resize(self, event):
		self.root.update_idletasks()
		self.root.update()
	
	def connect_game_manager(self, manager):
		self.game_manager = manager
	
	def change_color(self, new_color_set):
		if self.game_manager:
			self.game_manager.change_color(new_color_set)
	
	def update_scale(self, value):
		# TODO: -------------------------------------------------
		# TODO: HERE IS ZOOM ISSUE! FIND CORRECT VALUES FOR ZOOM!
		# TODO: -------------------------------------------------
		
		# If we are going to update the scroll region of the canvas, trigger it from here.
		# there has to be a better way to connect these values
		print(constants.SEPARATOR)
		print('Main GUI - Update Scale')
		print('--------------------------------------------------------------------------------')
		print('Value: ', value, 'Zoom Scale: ', options.zoom_scale, 'Hexagon Size: ', options.hexagon_size)
		self.control_panel.slider.set(value)
		options.hexagon_size = int(value)
		print('Value: ', value, 'Zoom Scale: ', options.zoom_scale, 'Hexagon Size: ', options.hexagon_size)
		print('--------------------------------------------------------------------------------')

		if self.game_manager:
			self.game_manager.resize(value)
		
		self.root.update_idletasks()
		self.root.update()
	
	def run(self):
		settings.set_minimum_canvas_size()  # Why use a function with no parameters for this? Just set default value.
		self.root.mainloop()


if __name__ == "__main__":
	test_GUI = MainGUI()
	test_GUI.run()
