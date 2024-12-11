from machine import I2C
from sh1106 import SH1106_I2C
from ball import Ball
import math

# parameters for used oled display
WIDTH = 128
HEIGHT = 64


class Screen:
    def __init__(self, player_left, player_right):
        self.display = self.connection_init()
        self.player_left = player_left
        self.player_right = player_right
        self.ball = Ball()
        self.score = [0] * 2

    def connection_init(self):
        i2c = I2C(0, freq=400000)
        print("I2C Address: " + hex(i2c.scan()[0]).upper())  # Display device address
        print("I2C Configuration: " + str(i2c))  # Display I2C config
        return SH1106_I2C(WIDTH, HEIGHT, i2c)

    def handle_screen(self):
        self.display.fill(0)
        self.display.text(f"{self.score[0]}:{self.score[1]}", 50, 5)
        self.draw_objects()
        self.display.show()

    def draw_objects(self):
        self.player_left.draw(self.display)
        self.player_right.draw(self.display)
        self.ball.draw(self.display)
        self.detect_ball_collision()
        self.detect_win()

    def detect_ball_collision(self):
        """
        Hitbox:
            0: start_x, 1: end_x,
            2: start_y, 3: end_y
        """
        # wall collison
        if self.ball.hitbox[2] <= 1 or self.ball.hitbox[3] >= HEIGHT - 1:
            self.ball.velocity_y = -self.ball.velocity_y

        # paddle collision

        if (
            self.ball.hitbox[2] >= self.player_left.paddle.hitbox[2]
            and self.ball.hitbox[3] <= self.player_left.paddle.hitbox[3]
            and self.ball.hitbox[1] == self.player_left.paddle.hitbox[1]
        ):
            bounce_angle = self.bounce_angle()
            self.ball.velocity_x = int(self.ball.speed * math.cos(bounce_angle))
            self.ball.velocity_y = int(self.ball.speed * -math.sin(bounce_angle))

        if (
            self.ball.hitbox[2] >= self.player_right.paddle.hitbox[2]
            and self.ball.hitbox[3] <= self.player_right.paddle.hitbox[3]
            and self.ball.hitbox[1] == self.player_right.paddle.hitbox[0]
        ):
            bounce_angle = self.bounce_angle()
            self.ball.velocity_x = -int(self.ball.speed * math.cos(bounce_angle))
            self.ball.velocity_y = int(self.ball.speed * -math.sin(bounce_angle))

    def bounce_angle(self):
        # which player - doesn't matter
        relative_landing_point = (
            self.player_right.paddle.hitbox[2] + self.player_right.paddle.size_y / 2
        ) - self.ball.hitbox[2]
        normalized_rlp = relative_landing_point / (self.player_right.paddle.size_y / 2)
        return normalized_rlp * 1.04719755  # 60 degrees in radians

    def detect_win(self):
        if self.ball.position_x <= 0:
            self.score[1] += 1
            self.reset()
        if self.ball.position_x >= WIDTH:
            self.score[0] += 1
            self.reset()

    def reset(self):
        self.ball = Ball()
