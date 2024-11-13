from dataclasses import dataclass
from typing import Tuple

"""
Settings instead of configuration to avoid canvas.config confusion.
"""


@dataclass
class Settings:
	window_title: str = 'Hexagons in TKinter'
	window_theme: str = 'alt'
	window_width: int = 640
	window_height: int = 480
	window_canvas = None  # initialized in canvas manager
	"""
	FOUND ERROR
	scale confusion:
	 slider/mouse wheel directly update hex size,
	 then geometry does modifier math.
	 no modifier here.
	"""
	# Todo: this version shouldn't be used anywhere.
	zoom_scale: float = 1.0  # modifier for recalculating hex position, not for size
	zoom_minimum: int = 3
	zoom_maximum: int = 100  # somewhat arbitrary, does not mean 100%
	map_columns: int = 8
	map_rows: int = 6
	hexagon_offset = (50, 50)  # always doubled of size? not in case of non-square aspect ratio.
	hexagon_size = 25
	hexagon_color: Tuple[str, str] = ('#666', '#ccc')
	hexagon_shape = None  # Same format as canvas polygon shape,


# canvas scroll region and such here?


options = Settings()


# Canvas functions
def update_scroll_region():
	bbox = options.window_canvas.bbox("all")
	if bbox:
		options.window_canvas.configure(scrollregion=bbox)


def set_minimum_canvas_size():
	options.window_canvas.config(width=300, height=300)
