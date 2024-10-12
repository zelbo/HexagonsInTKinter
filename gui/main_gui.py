"""
Main entry point for interface controller.
"""
import tkinter as tk
from tkinter import ttk

import gui.configuration as config

import gui.canvas_manager
import gui.control_panel

import constants


class MainGUI:
	def __init__(self):
		self.config = config.GUIConfig()
		self.root = tk.Tk()
		self.root.title(self.config.title)
		self.root.grid_columnconfigure(0, weight=1)
		self.root.grid_rowconfigure(0, weight=1)
		
		self._init_style()
		self._init_frame()
		
		self.scale: float = 25
		
		self.canvas_manager = gui.canvas_manager.CanvasManager(self.frame, self.config)
		self.control_panel = gui.control_panel.ControlPanel(self.frame, self)
		
		self._bind_events()

		self.zoom_modifier: float = 1
		self.scroll_offset = config.Position()
		self.game_manager = None
	
	def _init_style(self):
		self.style = ttk.Style()
		self.style.theme_use(self.config.theme)
	
	def _init_frame(self):
		self.frame = ttk.Frame(self.root)
		self.frame.grid(sticky=tk.NSEW)
		self.frame.grid_columnconfigure(0, weight=1)
		self.frame.grid_rowconfigure(0, weight=1)
		
	def _bind_events(self):
		self.root.bind('<Configure>', self._on_window_resize)
		self.canvas_manager.get_canvas().bind("<MouseWheel>", self.zoom)
		self.canvas_manager.get_canvas().bind("<Button-4>", self.zoom)
		self.canvas_manager.get_canvas().bind("<Button-5>", self.zoom)
	
	def _set_minimum_canvas_size(self):
		self.canvas_manager.get_canvas().config(width=300, height=300)
		
	def zoom(self, event):
		if event.num == 5 or event.delta == -120:  # Zoom out
			print(constants.SEPARATOR)
			print('Zoom out')
			self.scale -= 2
		if event.num == 4 or event.delta == 120:  # Zoom in
			print(constants.SEPARATOR)
			print('Zoom in')
			self.scale += 2
		
		# Keep zoom centered on mouse position
		x = self.canvas_manager.get_canvas().canvasx(event.x)
		y = self.canvas_manager.get_canvas().canvasy(event.y)
		
		self.scale = max(3, min(int(self.scale), 100))
		self.update_scale(self.scale)
	
	def _on_window_resize(self, event):
		pass
		
	def get_canvas(self):
		return self.canvas_manager.get_canvas()
	
	def connect_game_manager(self, manager):
		self.game_manager = manager
	
	def change_color(self, new_color_set):
		if self.game_manager:
			self.game_manager.change_color(new_color_set)
	
	def update_scale(self, value):
		# If we are going to update the scroll region of the canvas, trigger it from here.
		# there has to be a better way to connect these values
		self.control_panel.slider.set(value)
		self.scale = int(value)
		
		if self.game_manager:
			self.game_manager.resize(value)
	
	def run(self):
		self._set_minimum_canvas_size()
		self.root.mainloop()


if __name__ == "__main__":
	test_GUI = MainGUI()
	test_GUI.run()
