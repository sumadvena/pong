# Display Image & text on I2C driven SH1106 OLED display
from machine import I2C, Pin
from sh1106 import SH1106_I2C
from ball import Ball
from screen import Screen
from player import Player
# from time import sleep

WIDTH = 128  # oled display width
HEIGHT = 64  # oled display height

i2c = I2C(0, freq=400000)
print("I2C Address      : " + hex(i2c.scan()[0]).upper())  # Display device address
print("I2C Configuration: " + str(i2c))  # Display I2C config


oled = SH1106_I2C(WIDTH, HEIGHT, i2c)  # Init oled display

btn_white = Pin(0, Pin.IN, Pin.PULL_UP)
btn_blue = Pin(1, Pin.IN, Pin.PULL_UP)
buzz = Pin(2, Pin.OUT)

screen = Screen(oled, Player(0), Player(1), Ball())  # player bool is_bot


def white(pin):
    screen.player.paddle.move_down()


def blue(pin):
    screen.player.paddle.move_up()


btn_white.irq(trigger=Pin.IRQ_FALLING, handler=white)
btn_blue.irq(trigger=Pin.IRQ_FALLING, handler=blue)


while True:
    oled.fill(0)
    screen.ball.move()
    # Add some text
    oled.text("0:0", 50, 5)
    screen.draw()

    # Finally update the oled display so the image & text is displayed
    oled.show()
