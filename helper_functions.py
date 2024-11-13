import collections
import constants

Point = collections.namedtuple("Point", ["x", "y"])


def clamp(value, minimum, maximum):
	return max(minimum, min(value, maximum))


def flatten_list(list_of_tuples):
	"""Convert list of tuples to straight list."""
	return [item for sublist in list_of_tuples for item in sublist]


def extract_points(flattened_list):
	"""Convert straight list to list of paired tuples."""
	# could probably be a deque?
	flattened_list.reverse()
	new_list = []
	point_count = int(len(flattened_list) / 2)
	for i in range(point_count):
		x_value = flattened_list.pop()
		y_value = flattened_list.pop()
		new_list.append(Point(x_value, y_value))
	return new_list


def tuple_to_point(two_value_tuple):
	"""Convert a plain tuple to the named tuple 'Point'"""
	return Point(two_value_tuple[0], two_value_tuple[1])


# ----- Tuple math using list comprehensions -----

def tuple_times_value(modifier, input_tuple):
	"""Multiply each value in a set by a single variable (n * v for v in set)"""
	return tuple(modifier * float(unit) for unit in input_tuple)


def tuple_times_tuple(first_tuple, second_tuple):
	"""Multiply set components (offsets * positions for offsets, positions in zip(offset_tuples, position_tuples))"""
	return tuple(float(v1) * float(v2) for v1, v2 in zip(first_tuple, second_tuple))


def tuple_plus_value(increase, input_tuple):
	"""Add single variable to set (size + points for points in shape)"""
	return tuple(float(increase) + float(unit) for unit in input_tuple)


def tuple_plus_tuple(first_tuple, second_tuple):
	"""Add tuples (offsets + points for offsets, points in zip(offset_tuples, shape)"""
	return tuple(float(v1) + float(v2) for v1, v2 in zip(first_tuple, second_tuple))


def find_center(polygon_shape):
	# average points?
	points = extract_points(polygon_shape)
	points_total_x = 0.0
	points_total_y = 0.0
	# should probably be a list comprehension, but that shit is confusing.
	for point in points:
		points_total_x += point.x
		points_total_y += point.y
	print(constants.SEPARATOR)
	print('Total: ', points_total_x, points_total_y)
	return Point(float(points_total_x / 6),
				 float(points_total_y / 6))  # Magic numbers. extract count from shape or points?


def get_rgb_from_name(widget, color_name):
	rgb = widget.winfo_rgb(color_name)
	return tuple(int(x / 257) for x in rgb)


def get_hex_from_name(widget, color_name):
	rgb = widget.winfo_rgb(color_name)
	return '#{:02x}{:02x}{:02x}'.format(*[int(x / 257) for x in rgb])


def darker(color):
	return tuple_times_value(0.75, color)


def darken_hex_from_name(widget, color_name):
	rgb = widget.winfo_rgb(color_name)
	dimmed = tuple_times_value(0.75, rgb)
	return '#{:02x}{:02x}{:02x}'.format(*[int(x / 257) for x in dimmed])


if __name__ == "__main__":
	# tests
	pass
