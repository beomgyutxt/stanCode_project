"""
File: draw_line.py
Name: Hsuan Tung, Lin
-------------------------
When user clicks the window twice, the function can draw a line on a canvas (window).
At the first click, a circle appears; at the second click, the circle disappears while a line appears.
The line is drawn from the position of first click to the position of second click.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# this constant determines size of circle
SIZE = 10

# global variables
window = GWindow()
origin_x = 0  # position of the the first click (origin_x, origin_y)
origin_y = 0
circle = GOval(SIZE, SIZE)

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(origin)  # the first click


def origin(click1):
    """
    At the first click, a circle appears at the position of the first click.
    """
    global origin_x, origin_y
    origin_x = click1.x  # position of the the first click (origin_x, origin_y)
    origin_y = click1.y
    window.add(circle, origin_x - SIZE/2, origin_y - SIZE/2)  # the central of the circle is where the mouse clicks
    onmouseclicked(final)  # the second click


def final(click2):
    """
    At the second click, the circle disappears and a line shows from the position of first click
    to  the position of second click.
    """
    window.remove(circle)  # the circle disappears
    line = GLine(origin_x, origin_y, click2.x, click2.y)
    window.add(line)  # the line shows
    onmouseclicked(origin)  # one more click --> show a new circle


if __name__ == "__main__":
    main()
