class Screen:
    def __init__(self, display, player, bot, ball):
        self.display = display
        self.player = player
        self.bot = bot
        self.ball = ball

    def draw(self):
        self.player.draw(self.display)
        self.bot.draw(self.display)
        self.ball.draw(self.display)

    def detect_collision(self):
        self.ball.calc_hitbox()
        pass
