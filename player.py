from paddle import Paddle


class Player:
    def __init__(self, left, y_axis):
        self.paddle = Paddle(y_axis)
        self.left = left

        if self.left:
            self.paddle.position_x = 5
        else:
            self.paddle.position_x = 122

    def draw(self, display):
        self.paddle.move()
        self.paddle.draw(display)
