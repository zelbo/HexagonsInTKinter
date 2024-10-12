import tkinter as tk
from tkinter import ttk

import gui.configuration as config
# todo: remove this entirely since we have mouse wheel zoom working, and no longer using color buttons?


class ControlPanel:
	def __init__(self, parent, hex_gui):
		self.hex_gui = hex_gui
		self.controls = ttk.Frame(parent, padding=10)
		self.controls.grid(column=2, row=0, rowspan=2, sticky='ns')
		self.controls.columnconfigure(0, weight=1)
		self.slider = self._init_slider()
	
	def _init_slider(self):
		slider = tk.Scale(self.controls, from_=config.GUIConfig.zoom_minimum, to=config.GUIConfig.zoom_maximum,
						  command=self.hex_gui.update_scale)
		slider.grid(column=0, row=0, sticky="ns")
		slider.set(config.HexConfig.starting_size)
		return slider
