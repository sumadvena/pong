from machine import Pin, ADC
from screen import Screen
from player import Player

buzz = Pin(2, Pin.OUT)

screen = Screen(
    Player(1, ADC(Pin(26))),
    Player(0, ADC(Pin(27))),
)  # player bool is_left


while True:
    screen.ball.move()
    screen.handle_screen()
