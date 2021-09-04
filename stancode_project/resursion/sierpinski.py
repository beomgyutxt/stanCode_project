"""
File: sierpinski.py
Name: Hsuan TUng, Lin
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This program draws a Sierpinski Triangle through recursion, GObject and Gwindow.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: the order of a triangle
	:param length: the length of a triangle
	:param upper_left_x: the upper left x coordinate of the upper left triangle
	:param upper_left_y: the upper left y coordinate of the upper left triangle
	"""
	# base case
	if order == 0:
		return
	# recursive case
	else:
		# draw triangle
		line1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		window.add(line1)
		line2 = GLine(upper_left_x, upper_left_y, upper_left_x + length/2, upper_left_y + length*(3**0.5)/2)
		window.add(line2)
		line3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + length/2, upper_left_y + length*(3**0.5)/2)
		window.add(line3)
		# upper left
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		# upper right
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)
		# bottom
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 4, upper_left_y + length*(3**0.5)/4)


if __name__ == '__main__':
	main()