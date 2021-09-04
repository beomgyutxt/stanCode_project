"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
There is a breakout game.
The game starts when user click the mouse.
The ball will go randomly and user has to use the paddle to rebound it.
Three boundaries of the window (top, left, right) can rebound the ball.
The number of lives decreases when the ball goes out of the window.
When the ball bumps into a brick, get one point.
The game finishes when there is no bricks (win) or there is no life of user (lose).
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 1000			# Number of attempts


def main():
    graphics = BreakoutGraphics()  # construct a graphic of breakout game

    vx = graphics.get_dx()         # get horizontal and vertical speed of the ball
    vy = graphics.get_dy()
    n = NUM_LIVES
    score = 0                      # total point

    while True:
        if graphics.start_game:    # when the game is on-going, the ball moves.
            graphics.ball.move(vx, vy)
        # Once the ball reaches boundaries (top, left, right) of the window, it rebounds.
        if 0 >= graphics.ball.x or graphics.ball.x >= graphics.window.width - graphics.ball.width:
            vx = -vx
        if 0 >= graphics.ball.y:
            vy = -vy

        bumped_obj = graphics.bump()
        if bumped_obj is not None and bumped_obj is not graphics.label:
            if bumped_obj != graphics.paddle:              # the ball bumps into a brick
                vy = -vy                                   # rebound
                graphics.window.remove(bumped_obj)         # remove the brick
                score += 1                                 # get one point
                graphics.label.text = f'Score: {score}'
            else:
                if vy > 0:                                 # the ball bumps into the paddle
                    vy = -vy

        if graphics.ball.y >= graphics.window.height:      # the ball is out of the window
            n -= 1                                         # the number of lives decreases
            graphics.start_game = False                    # reset the game
            graphics.window.add(graphics.ball, (graphics.window.width-graphics.ball.width)/2,
                                (graphics.window.height-graphics.ball.height)/2)

        if score == graphics.bricks_rn*graphics.bricks_cn:  # all bricks is removed
            graphics.label.text = 'You win'
            break

        if n == 0:                                          # no life
            graphics.label.text = 'You lose'
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
