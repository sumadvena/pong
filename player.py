from paddle import Paddle

class Player:
    def __init__(self, is_bot):
        self.is_bot = is_bot
        self.paddle = Paddle()

        if is_bot:
            self.paddle.position_x = 10
        else:
            self.paddle.position_x = 110

    def draw(self, display):
        self.paddle.draw(display)
