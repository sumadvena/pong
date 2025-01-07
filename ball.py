from game_object import Game_Object


class Ball(Game_Object):
    def __init__(self):
        super().__init__()
        self.size_x = 3
        self.size_y = self.size_x
        self.position_x = 63
        self.position_y = 31
        self.velocity_x = 3
        self.velocity_y = 1
        self.speed = 5

    def move(self):
        self.position_x += self.velocity_x
        self.position_y += self.velocity_y
