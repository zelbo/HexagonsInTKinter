import tkinter as tk
from tkinter import ttk
# import math  # already imported with other packages?
from HexManager import *
from RedBlobHexagons import *

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
test_all()

root.mainloop()

# https://docs.python.org/3/library/tkinter.html#bindings-and-events

# To interact with objects contained in a Canvas object you need to use tag_bind() which has this format:
# tag_bind(item, event=None, callback=None, add=None)
# The item parameter can be either a tag or an id.
# Here is an example to illustrate the concept:

# from tkinter import *
# def onObjectClick(event):
#     print('Got object click', event.x, event.y)
#     print(event.widget.find_closest(event.x, event.y))
# root = Tk()
# canvas = Canvas(root, width=100, height=100)
# obj1Id = canvas.create_line(0, 30, 100, 30, width=5, tags="obj1Tag")
# obj2Id = canvas.create_text(50, 70, text='Click', tags='obj2Tag')
# canvas.tag_bind(obj1Id, '<ButtonPress-1>', onObjectClick)
# canvas.tag_bind('obj2Tag', '<ButtonPress-1>', onObjectClick)
# print('obj1Id: ', obj1Id)
# print('obj2Id: ', obj2Id)
# canvas.pack()
# root.mainloop()
