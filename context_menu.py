import tkinter as tk
from gui.HexColors import *
# TODO: prototype works, now plug it into the actual program!

root = tk.Tk()

orb_menu = tk.Menu(root,
				   activebackground='#666',
				   activeforeground='#ccc',
				   background='#111',
				   foreground='#999',
				   tearoff=0)

color_menu = tk.Menu(root,
					 activebackground='#666',
					 activeforeground='#ccc',
					 background='#111',
					 foreground='#999',
					 tearoff=0)


# TODO: pass mouse coords, or get widget ID at menu activation?
# todo: need some way to connect the command to the clicked widget (orb or hex)
# todo: also need some way to poll the tile and find out if it has an orb on it
# todo: only show remove and activate options if there is an orb present
def place_orb(color):
	pass


def remove_orb():
	pass


def activate_orb():
	pass


def context_menu(event):
	try:
		x = root.winfo_pointerx()
		y = root.winfo_pointery()

		orb_menu.tk_popup(x, y, 0)
	finally:
		orb_menu.grab_release()


orb_menu.add_cascade(label='Place Orb', menu=color_menu)
orb_menu.add_command(label='Remove Orb', command=lambda: remove_orb())
orb_menu.add_separator()
orb_menu.add_command(label='Activate Orb', command=lambda: activate_orb())

# todo: make this section less clunky?
color_menu.add_command(
	activebackground=Colors.red.bright,
	activeforeground='#000',
	background=Colors.red.dim,
	foreground='#fff',
	label='Red',
	command=lambda: place_orb('red')
)
color_menu.add_command(
	activebackground=Colors.orange.bright,
	activeforeground='#000',
	background=Colors.orange.dim,
	foreground='#fff',
	label='Orange',
	command=lambda: place_orb('orange')
)
color_menu.add_command(
	activebackground=Colors.yellow.bright,
	activeforeground='#000',
	background=Colors.yellow.dim,
	foreground='#fff',
	label='Yellow',
	command=lambda: place_orb('yellow')
)
color_menu.add_command(
	activebackground=Colors.green.bright,
	activeforeground='#000',
	background=Colors.green.dim,
	foreground='#fff',
	label='Green',
	command=lambda: place_orb('green')
)
color_menu.add_command(
	activebackground=Colors.blue.bright,
	activeforeground='#666',
	background=Colors.blue.dim,
	foreground='#fff',
	label='Blue',
	command=lambda: place_orb('blue')
)
color_menu.add_command(
	activebackground=Colors.indigo.bright,
	activeforeground='#000',
	background=Colors.indigo.dim,
	foreground='#fff',
	label='Indigo',
	command=lambda: place_orb('indigo')
)
color_menu.add_command(
	activebackground=Colors.violet.bright,
	activeforeground='#000',
	background=Colors.violet.dim,
	foreground='#fff',
	label='Violet',
	command=lambda: place_orb('violet')
)
color_menu.add_command(
	activebackground=Colors.grey.bright,
	activeforeground='#000',
	background=Colors.grey.dim,
	foreground='#fff',
	label='Clear',
	command=lambda: place_orb('clear')
)

# root.bind("<Button-1>", context_menu)
root.bind("<Button-1>", lambda e: orb_menu.tk_popup(e.x_root, e.y_root, 0))

root.mainloop()
