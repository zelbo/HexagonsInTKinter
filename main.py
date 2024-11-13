from gui.main_gui import *
from game_manager import *
from redblob_hexagons import *
# TODO: we broke zoom, probably when we removed the buttons. FIX IT!
import settings

options = settings.options


class Main:
	global options
	
	def __init__(self):
		self.GUI = MainGUI()
		# options.window_canvas = self.GUI.get_canvas()
		self.hex_manager = GameManager()
		self.GUI.connect_game_manager(self.hex_manager)
	
	def main_loop(self):
		print(constants.SEPARATOR)
		print('PI =', math.pi)
		print('Square Root of Three =', math.sqrt(3))
		
		print(constants.SEPARATOR)
		print(f'Game Settings {options}')
		test_all()
		
		self.GUI.root.mainloop()


main_game = Main()
main_game.main_loop()
