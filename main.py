import tkinter as tk
from tkinter import ttk
# import math  # already imported with other packages?
from HexManager import *

root = tk.Tk()
root.title("Hexagons in Tkinter")
frame = ttk.Frame(root, padding=10)
frame.grid()

canvas = tk.Canvas(frame, width=640, height=480, bg='black')
canvas.grid(column=0, row=0, columnspan=2)  # needs to be on two lines to avoid 'object has no attribute' error
ttk.Label(frame, text="Hexagons!").grid(column=0, row=1)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=1)

offset = (50, 50)
size = 25
columns = 8
rows = 6

hex_manager = HexManager(canvas, offset, size, columns, rows)

print('PI =', math.pi)
print('Square Root of Three =', math.sqrt(3))

root.mainloop()
