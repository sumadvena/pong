from game_object import Game_Object


class Paddle(Game_Object):
    def __init__(self, y_axis):
        super().__init__()
        self.y_axis = y_axis
        self.position_y = 20
        self.velocity = self.calculate_velocity()
        self.size_x = 2
        self.size_y = 15

    def calculate_velocity(self):
        y_value = self.y_axis.read_u16()
        if y_value < 25000:
            if y_value < 10000:
                if y_value < 5000:
                    return -4
                return -3
            return -2
        if y_value > 45000:
            if y_value > 55000:
                if y_value > 60000:
                    return 4
                return 3
            return 2
        else:
            return 0

    def move(self):
        self.velocity = self.calculate_velocity()
        self.position_y += self.velocity
