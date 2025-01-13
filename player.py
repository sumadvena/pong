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
        """
        Automatically move the paddle's position to track the ball's Y center.
        We add a small 'dead zone' to avoid jitter and a speed limit.
        """
        # Lower follow_speed to move gradually rather than jumping
        follow_speed = 3

        # 'dead_zone' is how close the paddle center can get to ball center before bot stops moving
        dead_zone = 2

        ball_center_y = (self.ball.hitbox[2] + self.ball.hitbox[3]) // 2
        paddle_center_y = (self.paddle.hitbox[2] + self.paddle.hitbox[3]) // 2

        difference = ball_center_y - paddle_center_y

        # Only move if the difference is outside the dead zone
        if abs(difference) > dead_zone:
            # Move up or down by 'follow_speed'
            step = follow_speed if difference > 0 else -follow_speed
            self.paddle.position_y += step

        # Clamp so the bot doesn't move off-screen
        if self.paddle.position_y < 0:
            self.paddle.position_y = 0
        if self.paddle.position_y + self.paddle.size_y > 64:
            self.paddle.position_y = 64 - self.paddle.size_y
