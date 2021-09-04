"""
File: bouncing_ball.py
Name: Hsuan Tung, Lin
-------------------------
The function imitates the process of a bouncing ball.
    At the beginning, the ball is at (START_X , START_Y).
    Once users clicks, the ball moves.
    The ball has a stable x velocity, VX, and y velocity is affected by gravity.
    When the ball hit the ground, it bounces and its y velocity reduces.
    When the ball is out of canvas, a new ball appears at (START_X , START_Y) and waits for user's click.
    The process(run) can repeat three times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# constants
VX = 3        # x velocity
DELAY = 20    # animation
GRAVITY = 1   # each moves, y velocity add a GRAVITY
SIZE = 20     # ball size
REDUCE = 0.9  # y velocity reduces
START_X = 30  # start point(START_X, START_Y)
START_Y = 40

# global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
runs = 0      # how many times the complete bouncing process happens


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball, START_X, START_Y)  # show a ball
    onmouseclicked(run)


def run(mouse):
    global runs
    here = window.get_object_at(START_X+SIZE/2, START_Y+SIZE/2)
    if here is not None and runs < 3:  # ball is at start point and complete run  < 3
        runs += 1
        bouncing()  # the ball starts to move


def bouncing():
    window.remove(ball)  # hiding a ball
    ball2 = GOval(SIZE, SIZE)  # constructs a moving ball
    window.add(ball2, START_X, START_Y)
    vy = 0
    while True:
        vy += GRAVITY  # each moves, y velocity add a GRAVITY
        ball2.move(VX, vy)
        if ball2.y + ball.height >= window.height and vy > 0:  # hit the ground
            vy = -vy * REDUCE  # bouncing and slowing the ball
        if ball2.x >= window.width:  # out of canvas
            break
        pause(DELAY)
    window.add(ball, START_X, START_Y)  # showing the ball, which is hiding before, at start point


if __name__ == "__main__":
    main()
