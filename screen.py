from machine import I2C, Pin
from sh1106 import SH1106_I2C
from ball import Ball
from player import Player
from paddle import Paddle
import math
import time

WIDTH = 128
HEIGHT = 64


class Screen:
    def __init__(self, display: SH1106_I2C, player_left: Player, player_right: Player):
        self.display = display
        self.player_left = player_left
        self.ball_reset()
        self.player_right = player_right
        self.buzzer = Pin(2, Pin.OUT)

    def ball_reset(self):
        self.ball = Ball()
        if self.player_left.is_bot:
            self.player_left.ball = self.ball

    def handle_screen(self):
        self.display.fill(0)
        self.display.text(f"{self.player_left.score}:{self.player_right.score}", 50, 5)
        self.draw_objects()
        self.display.show()

    def draw_objects(self):
        self.player_left.draw(self.display)
        self.player_right.draw(self.display)
        self.ball.draw(self.display)
        self.detect_ball_collision()

    def tick(self):
        self.buzzer.on()
        time.sleep_us(1000)
        self.buzzer.off()

    def detect_ball_collision(self):
        """Handle collisions with walls and paddles using AABB checks."""
        # Wall collision (top/bottom)
        if self.ball.hitbox[2] <= 0 or self.ball.hitbox[3] >= HEIGHT:
            self.ball.velocity_y = -self.ball.velocity_y

        # Paddle collision: left paddle
        if self.check_collision(self.player_left.paddle.hitbox):
            self.handle_paddle_bounce(self.player_left.paddle, is_left=True)
            self.tick()

        # Paddle collision: right paddle
        if self.check_collision(self.player_right.paddle.hitbox):
            self.handle_paddle_bounce(self.player_right.paddle, is_left=False)
            self.tick()

    def check_collision(self, checked_paddle_hitbox):
        # hitbox = [left, right, top, bottom]
        return (
            self.ball.hitbox[0] < checked_paddle_hitbox[1]
            and self.ball.hitbox[1] > checked_paddle_hitbox[0]
            and self.ball.hitbox[2] < checked_paddle_hitbox[3]
            and self.ball.hitbox[3] > checked_paddle_hitbox[2]
        )

    def handle_paddle_bounce(self, paddle: Paddle, is_left):
        bounce_angle = self.compute_bounce_angle(paddle)

        if bounce_angle < 0.75:
            bounce_angle = 0.75 if bounce_angle >= 0 else -0.75

        y_factor = math.sqrt(max(0.0, 1.0 - bounce_angle**2))
        if is_left:
            self.ball.velocity_x = int(abs(bounce_angle) * self.ball.speed)
            self.ball.velocity_y = (
                int(y_factor * self.ball.speed)
                if self.ball.velocity_y >= 0
                else int(-y_factor * self.ball.speed)
            )
            self.ball.position_x = paddle.hitbox[1]
        else:
            self.ball.velocity_x = int(-abs(bounce_angle) * self.ball.speed)
            self.ball.velocity_y = (
                int(y_factor * self.ball.speed)
                if self.ball.velocity_y >= 0
                else int(-y_factor * self.ball.speed)
            )
            self.ball.position_x = paddle.hitbox[0] - (
                self.ball.hitbox[1] - self.ball.hitbox[0]
            )

    def compute_bounce_angle(self, paddle: Paddle):
        paddle_center_y = (paddle.hitbox[2] + paddle.hitbox[3]) / 2.0
        ball_center_y = (self.ball.hitbox[2] + self.ball.hitbox[3]) / 2.0
        relative_intersect_y = ball_center_y - paddle_center_y

        normalized = relative_intersect_y / paddle.size_x / 2

        if normalized < -0.95:
            normalized = -0.95
        elif normalized > 0.95:
            normalized = 0.95

        return normalized

    def detect_win(self):
        if self.ball.position_x <= 0:
            self.player_right.score += 1
            return True
        if self.ball.position_x >= WIDTH - (self.ball.hitbox[1] - self.ball.hitbox[0]):
            self.player_left.score += 1
            return True

    def win_message(self, left_won=1):
        self.display.fill(0)
        if left_won:
            self.display.text("Left player has won!", 50, 30)
        else:
            self.display.text("Right player has won!", 50, 30)
        self.display.show()
        time.sleep(1)
        self.display.fill(0)
        self.display.show()

    def reset(self):
        self.ball_reset()
        self.display.fill(0)
        self.display.text(f"{self.player_left.score}:{self.player_right.score}", 50, 30)
        self.display.show()
        time.sleep_ms(500)
        self.display.fill(0)
        self.display.show()
