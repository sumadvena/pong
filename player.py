from paddle import Paddle


class Player:
    def __init__(self, left, y_axis=None, is_bot=False, ball=None):
        self.score = 0
        self.paddle = Paddle(y_axis)
        self.left = left
        self.is_bot = is_bot
        self.ball = ball

        if self.left:
            self.paddle.position_x = 0
        else:
            self.paddle.position_x = 125

    def draw(self, display):
        if self.is_bot:
            self.bot_move()
        else:
            self.paddle.move()
        self.paddle.draw(display)

    def bot_move(self):
        follow_speed = 2
        # 'dead_zone' is how close the paddle center can get to ball center before bot stops moving
        dead_zone = 3
        ball_center_y = (self.ball.hitbox[2] + self.ball.hitbox[3]) // 2
        paddle_center_y = (self.paddle.hitbox[2] + self.paddle.hitbox[3]) // 2
        difference = ball_center_y - paddle_center_y
        # Only move if the difference is outside the dead zone
        if abs(difference) > dead_zone:
            step = follow_speed if difference > 0 else -follow_speed
            self.paddle.position_y += step

        if self.paddle.position_y < 0:
            self.paddle.position_y = 0
        if self.paddle.position_y + self.paddle.size_y > 64:
            self.paddle.position_y = 64 - self.paddle.size_y
