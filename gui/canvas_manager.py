import tkinter as tk
from tkinter import ttk

import gui.Point
import settings

options = settings.options


class CanvasManager:
	global options
	
	def __init__(self, parent):
		self.canvas_frame = ttk.Frame(parent, width=options.window_width, height=options.window_height)
		self.canvas_frame.grid(column=0, row=0, columnspan=2, sticky=tk.NSEW)
		self.canvas_frame.grid_columnconfigure(0, weight=1)
		self.canvas_frame.grid_rowconfigure(0, weight=1)
		
		options.window_canvas = tk.Canvas(self.canvas_frame, bg='black')  # should be only place canvas is defined
		options.window_canvas.grid(column=0, row=0, sticky=tk.NSEW)
		
		self._init_scrollbars()
	
	def _init_scrollbars(self):
		self.h_bar = tk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL, command=options.window_canvas.xview)
		self.h_bar.grid(row=1, column=0, sticky=tk.EW)
		self.v_bar = tk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=options.window_canvas.yview)
		self.v_bar.grid(row=0, column=1, sticky=tk.NS)
		options.window_canvas.config(
			scrollregion=(0, 0, 1000, 10000),  # hacky, use bbox and dynamically update values ("all" tag?)
			xscrollcommand=self.h_bar.set,
			yscrollcommand=self.v_bar.set
		)
	
	def update_scroll_region(self):
		options.window_canvas.update_idletasks()
		options.window_canvas.config(scrollregion=options.window_canvas.bbox("hexagon"))
		bbox = options.window_canvas.bbox("hexagon")
		if bbox:
			options.window_canvas.config(scrollregion=bbox)
	
	def resize_canvas(self, event):
		options.window_canvas.config(width=event.width, height=event.height)
		self.update_scroll_region()
