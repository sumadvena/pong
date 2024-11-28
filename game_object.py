class Game_Object:
    position_x = 0
    position_y = 0
    size_x = 0
    size_y = 0
    hitbox = []

    def __init__(self):
        self.hitbox[0] = self.position_x
        self.hitbox[1] = self.position_x + self.size_x
        self.hitbox[2] = self.position_y
        self.hitbox[3] = self.position_y + self.size_y

    def draw(self, display):
        display.fill_rect(self.position_x, self.position_y, self.size_x, self.size_y, 1)

    def calc_hitbox(self):
        self.hitbox[0] = self.position_x
        self.hitbox[1] = self.position_x + self.size_x
        self.hitbox[2] = self.position_y
        self.hitbox[3] = self.position_y + self.size_y
        return self.hitbox
