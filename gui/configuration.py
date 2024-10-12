from dataclasses import dataclass
from typing import Tuple


@dataclass
class GUIConfig:
	title: str = 'Hexagons'
	theme: str = 'alt'
	window_width: int = 640
	window_height: int = 480
	zoom_minimum: int = 3
	zoom_maximum: int = 100


@dataclass  # todo: switch to using named tuple Point()
class Position:
	x: float = 0.0
	y: float = 0.0


@dataclass
class HexConfig:
	offset: Tuple[int, int] = (50, 50)
	starting_size: int = 25
	columns: int = 8
	rows: int = 6
	color: Tuple[str, str] = ('#666', '#ccc')
	