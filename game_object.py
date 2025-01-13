class Game_Object:
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.size_x = 0
        self.size_y = 0
        self.hitbox = [0] * 4
        self.calc_hitbox()

    def draw(self, display):
        self.calc_hitbox()
        display.fill_rect(self.position_x, self.position_y, self.size_x, self.size_y, 1)

    def calc_hitbox(self):
        self.hitbox[0] = self.position_x
        self.hitbox[1] = self.position_x + self.size_x
        self.hitbox[2] = self.position_y
        self.hitbox[3] = self.position_y + self.size_y
