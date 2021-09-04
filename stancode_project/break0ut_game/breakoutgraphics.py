"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION

The function composes a class 'BreakoutGraphics' which outputs the graphic of a breakout game.
The graphic consists of a ball(center), a paddle(bottom center) and lots of bricks.
User can construct own breakout game by using this class and adjusting key parameters.

There are 5 methods in this class.
1. start(): Once the mouse is clicked, the game starts.
2. paddle_move(): controlling the movement of the paddle
3. get_dx(): returning the horizontal speed of the ball
4. get_dy(): returning the vertical speed of the ball
5. bump(): returning the object bumped by the ball
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).

BALL_RADIUS = 10       # Radius of the ball (in pixels).

PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.x_paddle = (window_width-paddle_width)/2  # initial paddle position: bottom center of the window
        self.y_paddle = window_height-paddle_offset
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=self.x_paddle, y=self.y_paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True                       # initail ball position: center of the window
        self.window.add(self.ball, x=window_width/2 - ball_radius, y=window_height/2 - ball_radius)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)    # initial horizontal speed
        self.__dy = INITIAL_Y_SPEED                   # initial vertical speed
        if random.random() > 0.5:                     # the ball can go left or go right
            self.__dx = -self.__dx

        # Initialize our mouse listeners
        self.start_game = False                       # whether the game is on-going or not
        onmouseclicked(self.start)                    # click the mouse -> start game
        onmousemoved(self.paddle_move)                # the movement of the mouse determines the position of the paddle

        # Draw bricks
        self.bricks_w = brick_width
        self.bricks_h = brick_height
        self.bricks_s = brick_spacing
        self.bricks_rn = brick_rows
        self.bricks_cn = brick_cols
        self.bricks_o = brick_offset
        color = 'red'
        for i in range(self.bricks_rn):
            if i == 2:                                # the color of a brick is based on the row where the brick is.
                color = 'orange'
            elif i == 4:
                color = 'yellow'
            elif i == 6:
                color = 'green'
            elif i == 8:
                color = 'blue'
            for j in range(self.bricks_cn):
                x_brick = (self.bricks_w + self.bricks_s)*j                        # the position of bricks
                y_brick = self.bricks_o + (self.bricks_h + self.bricks_s) * i
                self.bricks = GRect(self.bricks_w, self.bricks_h)
                self.bricks.filled = True
                self.bricks.fill_color = color
                self.window.add(self.bricks, x=x_brick, y=y_brick)

        # draw score label
        self.label = GLabel(f'Score: ')
        self.label.font = '-20'
        self.window.add(self.label, 0, self.window.height)  # bottom left

    def paddle_move(self, event):
        """
        The method controls the movement of the paddle which is following the mouse movement.
        The whole paddle is always in the window wherever the mouse is.
        """
        if event.x <= 0:         # when the mouse is out of the window, the paddle stays at boundary of the window.
            self.x_paddle = 0
        elif event.x >= self.window.width - self.paddle.width:
            self.x_paddle = self.window.width - self.paddle.width
        else:
            self.x_paddle = event.x
        self.window.add(self.paddle, self.x_paddle, self.y_paddle)

    def start(self, event):
        """
        The method starts the game by sensing the mouse click.
        """
        self.start_game = True  # the game is on-going

    def get_dx(self):
        """
        the method provides the initial horizontal speed for user.
        """
        return self.__dx

    def get_dy(self):
        """
        the method provides the initial vertical speed for user
        """
        return self.__dy

    def bump(self):
        """
        The method will return an object, if the ball bumps into it, which means
        the four corners of the ball (x, y), (x+2r, y), (x, y+2r), (x+2r, y+2r)contact with it.
        :return: the object bumped by the ball
        """
        x_probe = self.ball.x
        y_probe = self.ball.y
        for i in range(2):
            for j in range(2):
                x_probe = x_probe + self.ball.width*i
                y_probe = y_probe + self.ball.height*j
                obj = self.window.get_object_at(x_probe, y_probe)
                return obj
