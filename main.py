from gui.main_gui import *
from game_manager import *
from redblob_hexagons import *


class Main:
	# TODO: clean up the lazy duplication here.
	offset = (50, 50)
	starting_size = 25  # do we need to maintain a copy of size here, or is starting value good enough?
	old_size = starting_size  # don't need this anymore, let tile and geometry worry about this stuff.
	columns = 8
	rows = 6
	color = ('#666', '#ccc')
	
	def __init__(self):
		self.GUI = MainGUI()
		self.hex_manager = HexManager(self.GUI.get_canvas(), self.offset, self.starting_size, self.columns, self.rows)
		self.GUI.connect_game_manager(self.hex_manager)
	
	def main_loop(self):
		print(constants.SEPARATOR)
		print('PI =', math.pi)
		print('Square Root of Three =', math.sqrt(3))
		test_all()
		
		self.GUI.root.mainloop()


main_game = Main()
main_game.main_loop()
