import tkinter as tk
from tkinter import ttk

import gui.configuration


class CanvasManager:
	def __init__(self, parent, config: gui.configuration.GUIConfig):
		self.config = config
		self.canvas_frame = ttk.Frame(parent, width=config.window_width, height=config.window_height)
		self.canvas_frame.grid(column=0, row=0, columnspan=2, sticky=tk.NSEW)
		self.canvas_frame.grid_columnconfigure(0, weight=1)
		self.canvas_frame.grid_rowconfigure(0, weight=1)
		
		self.canvas = tk.Canvas(self.canvas_frame, bg='black')
		self.canvas.grid(column=0, row=0, sticky=tk.NSEW)
		
		self._init_scrollbars()
		
	def _init_scrollbars(self):
		self.h_bar = tk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
		self.h_bar.grid(row=1, column=0, sticky=tk.EW)
		self.v_bar = tk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
		self.v_bar.grid(row=0, column=1, sticky=tk.NS)
		self.canvas.config(
			scrollregion=(0, 0, 1000, 10000),  # hacky, use bbox and dynamically update values ("all" tag?)
			xscrollcommand=self.h_bar.set,
			yscrollcommand=self.v_bar.set
		)
	
	def get_canvas(self):
		return self.canvas
	
	def resize_canvas(self, event):
		self.canvas.config(width=event.width, height=event.height)
		# self.update_scroll_region()
