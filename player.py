from paddle import Paddle


class Player:
    def __init__(self, left, y_axis):
        self.left = left
        self.paddle = Paddle(y_axis)
        self.reset()

    def draw(self, display):
        self.paddle.move()
        self.paddle.draw(display)

    def reset(self):
        if self.left:
            self.paddle.position_x = 4
        else:
            self.paddle.position_x = 122
