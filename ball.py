from game_object import Game_Object

class Ball(Game_Object):

    def __init__(self):
        self.velocity_x = 1
        self.size_x = 2
        self.size_y = 2
        self.position_x = 50
        self.position_y = 25
        self.velocity_y = 0

    def move(self):
        self.position_x += self.velocity_x
        self.position_y += self.velocity_y

