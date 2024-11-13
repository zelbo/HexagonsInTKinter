import tkinter as tk
from tkinter import ttk

import gui.Point as config
# todo: remove this entirely since we have mouse wheel zoom working, and no longer using color buttons?
import settings

options = settings.options


class ControlPanel:
	def __init__(self, parent, main_gui):
		self.main_gui = main_gui
		self.controls = ttk.Frame(parent, padding=10)
		self.controls.grid(column=2, row=0, rowspan=2, sticky='ns')
		self.controls.columnconfigure(0, weight=1)
		self.slider = self._init_slider()
	
	def _init_slider(self):
		slider = tk.Scale(self.controls,
						  from_=options.zoom_minimum,
						  to=options.zoom_maximum,
						  command=self.main_gui.update_scale)
		slider.grid(column=0, row=0, sticky="ns")
		slider.set(options.hexagon_size)
		return slider
