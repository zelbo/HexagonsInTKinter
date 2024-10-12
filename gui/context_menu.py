"""
Prototype/mockup
"""
import tkinter as tk
from gui.hex_colors import *


class ContextMenu:
	def __init__(self, parent, tile):
		self.parent = parent
		
		self.tile = tile  # send this in from calling tile, use to send back commands

		self.color_menu = self.menu_create_color()
		self.orb_menu = self.menu_create_orb()
	
	def menu_create_orb(self):
		menu = tk.Menu(self.parent, activebackground='#666', activeforeground='#ccc',
					   background='#111', foreground='#999', tearoff=0)
		
		menu.add_cascade(label='Place Orb', menu=self.color_menu)
		menu.add_command(label='Remove Orb', command=lambda: self.remove_orb())
		menu.add_separator()
		menu.add_command(label='Activate Orb', command=lambda: self.activate_orb())
		return menu
	
	def menu_create_color(self):
		menu = tk.Menu(self.parent, activebackground='#666', activeforeground='#ccc',
					   background='#111', foreground='#999', tearoff=0)
		
		# todo: make this section less clunky?
		menu.add_command(
			activebackground=Colors.red.bright,
			activeforeground='#000',
			background=Colors.red.dim,
			foreground='#fff',
			label='Red',
			command=lambda: self.place_orb('red')
		)
		menu.add_command(
			activebackground=Colors.orange.bright,
			activeforeground='#000',
			background=Colors.orange.dim,
			foreground='#fff',
			label='Orange',
			command=lambda: self.place_orb('orange')
		)
		menu.add_command(
			activebackground=Colors.yellow.bright,
			activeforeground='#000',
			background=Colors.yellow.dim,
			foreground='#fff',
			label='Yellow',
			command=lambda: self.place_orb('yellow')
		)
		menu.add_command(
			activebackground=Colors.green.bright,
			activeforeground='#000',
			background=Colors.green.dim,
			foreground='#fff',
			label='Green',
			command=lambda: self.place_orb('green')
		)
		menu.add_command(
			activebackground=Colors.blue.bright,
			activeforeground='#666',
			background=Colors.blue.dim,
			foreground='#fff',
			label='Blue',
			command=lambda: self.place_orb('blue')
		)
		menu.add_command(
			activebackground=Colors.indigo.bright,
			activeforeground='#000',
			background=Colors.indigo.dim,
			foreground='#fff',
			label='Indigo',
			command=lambda: self.place_orb('indigo')
		)
		menu.add_command(
			activebackground=Colors.violet.bright,
			activeforeground='#000',
			background=Colors.violet.dim,
			foreground='#fff',
			label='Violet',
			command=lambda: self.place_orb('violet')
		)
		menu.add_command(
			activebackground=Colors.grey.bright,
			activeforeground='#000',
			background=Colors.grey.dim,
			foreground='#fff',
			label='Clear',
			command=lambda: self.place_orb('clear')
		)
		return menu
	
	# TODO: instead of using feeder methods, just shortcut directly through lambdas
	
	def place_orb(self, color):
		pass
	
	def remove_orb(self):
		pass
	
	def activate_orb(self):
		pass
	

if __name__ == "__main__":
	root = tk.Tk()
	
	context_menu = ContextMenu(root, None)
	
	# root.bind("<Button-1>", context_menu)
	root.bind("<Button-3>", lambda e: context_menu.orb_menu.tk_popup(e.x_root, e.y_root, 0))
	
	root.mainloop()