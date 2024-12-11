from game_object import Game_Object


class Paddle(Game_Object):
    def __init__(self, y_axis):
        super().__init__()
        self.y_axis = y_axis
        self.position_y = 26
        self.velocity = 0
        self.size_x = 2
        self.size_y = 15

    def calculate_velocity(self):
        y_value = self.y_axis.read_u16()
        if y_value < 25000:
            if y_value < 10000:
                if y_value < 5000:
                    return -6
                return -5
            return -4
        if y_value > 45000:
            if y_value > 55000:
                if y_value > 60000:
                    return 6
                return 5
            return 4
        else:
            return 0

    # def within_the_border(self):
    #     """
    #     Screen resolution is 128 x 64
    #     if the paddle is to high or to low -> return false
    #     """
    #     if self.hitbox[2] <= 0 or self.hitbox[3] >= 127:
    #         return False
    #     else:
    #         return True

    def move(self):
        self.velocity = self.calculate_velocity()
        if (
            self.hitbox[3] - self.velocity >= 6
            and self.hitbox[2] - self.velocity <= 120
        ):
            self.position_y += self.velocity
