from tkinter import *
from tkinter import ttk
# import math
from HexManager import *

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
canvas = Canvas(frame, width=640, height=480, bg="gray")
canvas.grid(column=0, row=0, columnspan=2)
ttk.Label(frame, text="Hexagons!").grid(column=0, row=1)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=1)

# define properties of hex in hexagon.py (size, shape, color, location)
# use hex_manager to group them in array
# draw the polygons here with all the other tkinter stuff, looping over the array
# or feed manager a reference to the canvas object and allow it to handle that part as well?
hex_manager = HexManager((200, 200), 50, ('blue', 'yellow'))

print('PI', math.pi)
print('Square Root of Three', math.sqrt(3))


root.mainloop()
