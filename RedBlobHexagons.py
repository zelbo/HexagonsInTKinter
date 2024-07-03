# Generated code -- CC0 -- No Rights Reserved -- http://www.redblobgames.com/grids/hexagons/

from __future__ import division
from __future__ import print_function
import collections
import math

SQRT3 = math.sqrt(3.0)

Point = collections.namedtuple("Point", ["x", "y"])

_Hex = collections.namedtuple("hexagon", ["q", "r", "s"])


def hex_cel(q, r, s):
	assert not (round(q + r + s) != 0), "q + r + s must be 0"
	return _Hex(q, r, s)


def hex_add(a, b):
	return hex_cel(a.q + b.q, a.r + b.r, a.s + b.s)


def hex_subtract(a, b):
	return hex_cel(a.q - b.q, a.r - b.r, a.s - b.s)


def hex_scale(a, k):
	return hex_cel(a.q * k, a.r * k, a.s * k)


def hex_rotate_left(a):
	return hex_cel(-a.s, -a.q, -a.r)


def hex_rotate_right(a):
	return hex_cel(-a.r, -a.s, -a.q)


hex_directions = [hex_cel(1, 0, -1), hex_cel(1, -1, 0), hex_cel(0, -1, 1),
				  hex_cel(-1, 0, 1), hex_cel(-1, 1, 0), hex_cel(0, 1, -1)]


def hex_direction(direction):
	return hex_directions[direction]


def hex_neighbor(hexagon, direction):
	return hex_add(hexagon, hex_direction(direction))


hex_diagonals = [hex_cel(2, -1, -1), hex_cel(1, -2, 1), hex_cel(-1, -1, 2),
				 hex_cel(-2, 1, 1), hex_cel(-1, 2, -1), hex_cel(1, 1, -2)]


def hex_diagonal_neighbor(hexagon, direction):
	return hex_add(hexagon, hex_diagonals[direction])


def hex_length(hexagon):
	return (abs(hexagon.q) + abs(hexagon.r) + abs(hexagon.s)) // 2


def hex_distance(a, b):
	return hex_length(hex_subtract(a, b))


def hex_round(h):
	qi = int(round(h.q))
	ri = int(round(h.r))
	si = int(round(h.s))
	q_diff = abs(qi - h.q)
	r_diff = abs(ri - h.r)
	s_diff = abs(si - h.s)
	if q_diff > r_diff and q_diff > s_diff:
		qi = -ri - si
	else:
		if r_diff > s_diff:
			ri = -qi - si
		else:
			si = -qi - ri
	return hex_cel(qi, ri, si)


def hex_lerp(a, b, t):
	return hex_cel(a.q * (1.0 - t) + b.q * t, a.r * (1.0 - t) + b.r * t, a.s * (1.0 - t) + b.s * t)


def hex_line_draw(a, b):
	distance = hex_distance(a, b)
	a_nudge = hex_cel(a.q + 1e-06, a.r + 1e-06, a.s - 2e-06)
	b_nudge = hex_cel(b.q + 1e-06, b.r + 1e-06, b.s - 2e-06)
	results = []
	step = 1.0 / max(distance, 1)
	for i in range(0, distance + 1):
		results.append(hex_round(hex_lerp(a_nudge, b_nudge, step * i)))
	return results


offset_coordinates = collections.namedtuple("offset_coordinates", ["col", "row"])

EVEN = 1
ODD = -1


def q_offset_from_cube(offset, h):
	col = h.q
	row = h.r + (h.q + offset * (h.q & 1)) // 2
	if offset != EVEN and offset != ODD:
		raise ValueError("offset must be EVEN (+1) or ODD (-1)")
	return offset_coordinates(col, row)


def q_offset_to_cube(offset, h):
	q = h.col
	r = h.row - (h.col + offset * (h.col & 1)) // 2
	s = -q - r
	if offset != EVEN and offset != ODD:
		raise ValueError("offset must be EVEN (+1) or ODD (-1)")
	return hex_cel(q, r, s)


def r_offset_from_cube(offset, h):
	col = h.q + (h.r + offset * (h.r & 1)) // 2
	row = h.r
	if offset != EVEN and offset != ODD:
		raise ValueError("offset must be EVEN (+1) or ODD (-1)")
	return offset_coordinates(col, row)


def r_offset_to_cube(offset, h):
	q = h.col - (h.row + offset * (h.row & 1)) // 2
	r = h.row
	s = -q - r
	if offset != EVEN and offset != ODD:
		raise ValueError("offset must be EVEN (+1) or ODD (-1)")
	return hex_cel(q, r, s)


doubled_coordinates = collections.namedtuple("doubled_coordinates", ["col", "row"])


def q_doubled_from_cube(h):
	col = h.q
	row = 2 * h.r + h.q
	return doubled_coordinates(col, row)


def q_doubled_to_cube(h):
	q = h.col
	r = (h.row - h.col) // 2
	s = -q - r
	return hex_cel(q, r, s)


def r_doubled_from_cube(h):
	col = 2 * h.q + h.r
	row = h.r
	return doubled_coordinates(col, row)


def r_doubled_to_cube(h):
	q = (h.col - h.row) // 2
	r = h.row
	s = -q - r
	return hex_cel(q, r, s)


Orientation = collections.namedtuple("Orientation", ["f0", "f1", "f2", "f3", "b0", "b1", "b2", "b3", "start_angle"])

Layout = collections.namedtuple("Layout", ["orientation", "size", "origin"])

layout_pointy = Orientation(SQRT3, SQRT3 / 2.0, 0.0, 3.0 / 2.0, SQRT3 / 3.0, -1.0 / 3.0, 0.0, 2.0 / 3.0, 0.5)
layout_flat = Orientation(3.0 / 2.0, 0.0, SQRT3 / 2.0, SQRT3, 2.0 / 3.0, 0.0, -1.0 / 3.0, SQRT3 / 3.0, 0.0)


def hex_to_pixel(layout, h):
	orientation = layout.orientation
	size = layout.size
	origin = layout.origin
	x = (orientation.f0 * h.q + orientation.f1 * h.r) * size.x
	y = (orientation.f2 * h.q + orientation.f3 * h.r) * size.y
	return Point(x + origin.x, y + origin.y)


def pixel_to_hex(layout, p):
	orientation = layout.orientation
	size = layout.size
	origin = layout.origin
	pt = Point((p.x - origin.x) / size.x, (p.y - origin.y) / size.y)
	q = orientation.b0 * pt.x + orientation.b1 * pt.y
	r = orientation.b2 * pt.x + orientation.b3 * pt.y
	return hex_cel(q, r, -q - r)


def hex_corner_offset(layout, corner):
	orientation = layout.orientation
	size = layout.size
	angle = 2.0 * math.pi * (orientation.start_angle - corner) / 6.0
	return Point(size.x * math.cos(angle), size.y * math.sin(angle))


def polygon_corners(layout, h):
	corners = []
	center = hex_to_pixel(layout, h)
	for i in range(0, 6):
		offset = hex_corner_offset(layout, i)
		corners.append(Point(center.x + offset.x, center.y + offset.y))
	return corners


# Tests

def complain(name):
	print("FAIL {0}".format(name))


def equal_hex(name, a, b):
	if not (a.q == b.q and a.s == b.s and a.r == b.r):
		complain(name)


def equal_offset_coordinates(name, a, b):
	if not (a.col == b.col and a.row == b.row):
		complain(name)


def equal_doubled_coordinates(name, a, b):
	if not (a.col == b.col and a.row == b.row):
		complain(name)


def equal_int(name, a, b):
	if not (a == b):
		complain(name)


def equal_hex_array(name, a, b):
	equal_int(name, len(a), len(b))
	for i in range(0, len(a)):
		equal_hex(name, a[i], b[i])


def test_hex_arithmetic():
	equal_hex("hex_add", hex_cel(4, -10, 6), hex_add(hex_cel(1, -3, 2), hex_cel(3, -7, 4)))
	equal_hex("hex_subtract", hex_cel(-2, 4, -2), hex_subtract(hex_cel(1, -3, 2), hex_cel(3, -7, 4)))


def test_hex_direction():
	equal_hex("hex_direction", hex_cel(0, -1, 1), hex_direction(2))


def test_hex_neighbor():
	equal_hex("hex_neighbor", hex_cel(1, -3, 2), hex_neighbor(hex_cel(1, -2, 1), 2))


def test_hex_diagonal():
	equal_hex("hex_diagonal", hex_cel(-1, -1, 2), hex_diagonal_neighbor(hex_cel(1, -2, 1), 3))


def test_hex_distance():
	equal_int("hex_distance", 7, hex_distance(hex_cel(3, -7, 4), hex_cel(0, 0, 0)))


def test_hex_rotate_right():
	equal_hex("hex_rotate_right", hex_rotate_right(hex_cel(1, -3, 2)), hex_cel(3, -2, -1))


def test_hex_rotate_left():
	equal_hex("hex_rotate_left", hex_rotate_left(hex_cel(1, -3, 2)), hex_cel(-2, -1, 3))


def test_hex_round():
	a = hex_cel(0.0, 0.0, 0.0)
	b = hex_cel(1.0, -1.0, 0.0)
	c = hex_cel(0.0, -1.0, 1.0)
	rounded_lerp = hex_round(hex_lerp(hex_cel(0.0, 0.0, 0.0), hex_cel(10.0, -20.0, 10.0), 0.5))
	equal_hex("hex_round 1", hex_cel(5, -10, 5), rounded_lerp)
	equal_hex("hex_round 2", hex_round(a), hex_round(hex_lerp(a, b, 0.499)))
	equal_hex("hex_round 3", hex_round(b), hex_round(hex_lerp(a, b, 0.501)))
	equal_hex("hex_round 4", hex_round(a), hex_round(
		hex_cel(a.q * 0.4 + b.q * 0.3 + c.q * 0.3, a.r * 0.4 + b.r * 0.3 + c.r * 0.3,
				a.s * 0.4 + b.s * 0.3 + c.s * 0.3)))
	equal_hex("hex_round 5", hex_round(c), hex_round(
		hex_cel(a.q * 0.3 + b.q * 0.3 + c.q * 0.4, a.r * 0.3 + b.r * 0.3 + c.r * 0.4,
				a.s * 0.3 + b.s * 0.3 + c.s * 0.4)))


def test_hex_line_draw():
	equal_hex_array("hex_line_draw",
					[hex_cel(0, 0, 0), hex_cel(0, -1, 1), hex_cel(0, -2, 2), hex_cel(1, -3, 2),
					 hex_cel(1, -4, 3), hex_cel(1, -5, 4)], hex_line_draw(hex_cel(0, 0, 0), hex_cel(1, -5, 4)))


def test_layout():
	h = hex_cel(3, 4, -7)
	flat = Layout(layout_flat, Point(10.0, 15.0), Point(35.0, 71.0))
	equal_hex("layout", h, hex_round(pixel_to_hex(flat, hex_to_pixel(flat, h))))
	pointy = Layout(layout_pointy, Point(10.0, 15.0), Point(35.0, 71.0))
	equal_hex("layout", h, hex_round(pixel_to_hex(pointy, hex_to_pixel(pointy, h))))


def test_offset_roundtrip():
	a = hex_cel(3, 4, -7)
	b = offset_coordinates(1, -3)
	equal_hex("conversion_roundtrip even-q", a, q_offset_to_cube(EVEN, q_offset_from_cube(EVEN, a)))
	equal_offset_coordinates("conversion_roundtrip even-q", b, q_offset_from_cube(EVEN, q_offset_to_cube(EVEN, b)))
	equal_hex("conversion_roundtrip odd-q", a, q_offset_to_cube(ODD, q_offset_from_cube(ODD, a)))
	equal_offset_coordinates("conversion_roundtrip odd-q", b, q_offset_from_cube(ODD, q_offset_to_cube(ODD, b)))
	equal_hex("conversion_roundtrip even-r", a, r_offset_to_cube(EVEN, r_offset_from_cube(EVEN, a)))
	equal_offset_coordinates("conversion_roundtrip even-r", b, r_offset_from_cube(EVEN, r_offset_to_cube(EVEN, b)))
	equal_hex("conversion_roundtrip odd-r", a, r_offset_to_cube(ODD, r_offset_from_cube(ODD, a)))
	equal_offset_coordinates("conversion_roundtrip odd-r", b, r_offset_from_cube(ODD, r_offset_to_cube(ODD, b)))


def test_offset_from_cube():
	cel = hex_cel(1, 2, -3)
	equal_offset_coordinates("offset_from_cube even-q", offset_coordinates(1, 3), q_offset_from_cube(EVEN, cel))
	equal_offset_coordinates("offset_from_cube odd-q", offset_coordinates(1, 2), q_offset_from_cube(ODD, cel))


def test_offset_to_cube():
	equal_hex("offset_to_cube even-", hex_cel(1, 2, -3), q_offset_to_cube(EVEN, offset_coordinates(1, 3)))
	equal_hex("offset_to_cube odd-q", hex_cel(1, 2, -3), q_offset_to_cube(ODD, offset_coordinates(1, 2)))


def test_doubled_roundtrip():
	a = hex_cel(3, 4, -7)
	b = doubled_coordinates(1, -3)
	equal_hex("conversion_roundtrip doubled-q", a, q_doubled_to_cube(q_doubled_from_cube(a)))
	equal_doubled_coordinates("conversion_roundtrip doubled-q", b, q_doubled_from_cube(q_doubled_to_cube(b)))
	equal_hex("conversion_roundtrip doubled-r", a, r_doubled_to_cube(r_doubled_from_cube(a)))
	equal_doubled_coordinates("conversion_roundtrip doubled-r", b, r_doubled_from_cube(r_doubled_to_cube(b)))


def test_doubled_from_cube():
	cel = hex_cel(1, 2, -3)
	equal_doubled_coordinates("doubled_from_cube doubled-q", doubled_coordinates(1, 5), q_doubled_from_cube(cel))
	equal_doubled_coordinates("doubled_from_cube doubled-r", doubled_coordinates(4, 2), r_doubled_from_cube(cel))


def test_doubled_to_cube():
	cel = hex_cel(1, 2, -3)
	equal_hex("doubled_to_cube doubled-q", cel, q_doubled_to_cube(doubled_coordinates(1, 5)))
	equal_hex("doubled_to_cube doubled-r", cel, r_doubled_to_cube(doubled_coordinates(4, 2)))


def test_all():
	test_hex_arithmetic()
	test_hex_direction()
	test_hex_neighbor()
	test_hex_diagonal()
	test_hex_distance()
	test_hex_rotate_right()
	test_hex_rotate_left()
	test_hex_round()
	test_hex_line_draw()
	test_layout()
	test_offset_roundtrip()
	test_offset_from_cube()
	test_offset_to_cube()
	test_doubled_roundtrip()
	test_doubled_from_cube()
	test_doubled_to_cube()


if __name__ == '__main__':
	test_all()
