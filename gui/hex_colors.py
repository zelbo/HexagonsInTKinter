"""
Short for Hexagon Colors, but also using hexadecimal color codes. That's not confusing at all, right?
Instead of pre-made color sets, we could use a dimmer function for any given color.
Eventually, would like to incorporate a color picker for customization.
"""
from dataclasses import dataclass
# todo: This is overly complex, need to streamline our whole color system. It's getting out of hand.
# create array and enums?
# enum as key (RED = 1, ORANGE = 2...)
# array of structs?


@dataclass
class ColorSet:
	name: str = 'grey'  # for tile to use when requesting orb, would id# or key/value be better? or color_list[n]?
	dim: str = '#666'
	bright: str = '#ccc'
	border: str = '#000'


class Colors:
	red = ColorSet('red', '#900', '#c00', '#000')
	orange = ColorSet('orange', '#960', '#fc0', '#000')
	yellow = ColorSet('yellow', '#990', '#cc0', '#000')
	green = ColorSet('green', '#090', '#0c0', '#000')
	blue = ColorSet('blue', '#009', '#00c', '#000')
	indigo = ColorSet('indigo', '#306', '#90c', '#000')
	violet = ColorSet('violet', '#636', '#c6c', '#000')
	grey = ColorSet('grey', '#666', '#ccc', '#000')


color_list = [Colors.red,
			  Colors.orange,
			  Colors.yellow,
			  Colors.green,
			  Colors.blue,
			  Colors.indigo,
			  Colors.violet,
			  Colors.grey]
