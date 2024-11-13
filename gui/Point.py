from dataclasses import dataclass


@dataclass  # todo: switch to using named tuple Point()
class Position:
	x: float = 0.0
	y: float = 0.0
