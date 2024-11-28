from game_object import Game_Object

class Paddle(Game_Object):

    def __init__(self):
        self.position_y = 20
        self.velocity = 2
        self.size_x = 2
        self.size_y = 15


    def move_down(self):
        self.position_y += self.velocity

    def move_up(self):
        self.position_y -= self.velocity

