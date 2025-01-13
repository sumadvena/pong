from game_object import Game_Object


class Paddle(Game_Object):
    def __init__(self, y_axis):
        super().__init__()
        self.y_axis = y_axis
        self.position_y = 26
        self.velocity = 0
        self.size_x = 3
        self.size_y = 18

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

    def move(self):
        self.velocity = self.calculate_velocity()
        new_y = self.position_y + self.velocity
        # Clamp the new Y position so the paddle stays fully on-screen
        if new_y < 0:
            new_y = 0
        if new_y + self.size_y > 64:
            new_y = 64 - self.size_y

        # Assign the safe, clamped position
        self.position_y = new_y
