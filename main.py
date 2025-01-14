from machine import Pin, ADC, I2C
from sh1106 import SH1106_I2C
from screen import Screen
from player import Player
from menu import Menu

right_player_joystick_y = ADC(Pin(27))
right_player_joystick_button = Pin(3, Pin.IN, Pin.PULL_UP)
i2c = I2C(0, freq=400000)
display = SH1106_I2C(128, 64, i2c)


# nwm czy potrzebne wgl
# def exit_to_menu():
#     """
#     Sets a flag (or performs an action) that breaks out of the main
#     game loop so the user can return to the menu.
#     """
#     global in_game
#     in_game = False


def main_loop(screen: Screen):
    in_game = True

    while in_game:
        screen.handle_screen()
        screen.ball.move()
        if screen.detect_win():
            if screen.player_left.score == 10:
                screen.win_message(left_won=1)
            elif screen.player_right.score == 10:
                screen.win_message(left_won=0)
            else:
                screen.reset()
            in_game = False
            # exit_to_menu()

    run_menu()


def run_menu():
    menu = Menu(display, right_player_joystick_y)
    selected_mode = menu.wait_for_confirm(right_player_joystick_button)

    if selected_mode == 0:
        screen = Screen(
            display,
            Player(1, ADC(Pin(26))),
            Player(0, ADC(Pin(27))),
        )  # player bool is_left
    else:
        screen = Screen(display, Player(1, None, is_bot=True), Player(0, ADC(Pin(27))))

    main_loop(screen)


run_menu()
