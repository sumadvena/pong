from machine import Pin, ADC, I2C
from sh1106 import SH1106_I2C
from screen import Screen
from player import Player
from menu import Menu

right_player_joystick_y = ADC(Pin(27))
right_player_joystick_button = Pin(3, Pin.IN, Pin.PULL_UP)
i2c = I2C(0, freq=400000)
display = SH1106_I2C(128, 64, i2c)


def exit_to_menu():
    """
    Sets a flag (or performs an action) that breaks out of the main
    game loop so the user can return to the menu.
    """
    global in_game
    in_game = False


def main_loop(screen):
    """
    Your main game loop. The flag 'in_game' keeps it running until
    exit_to_menu() is called.
    """
    global in_game
    in_game = True

    while in_game:
        screen.handle_screen()
        screen.ball.move()
        if screen.detect_win():
            if screen.player_left.score == 10 or screen.player_right.score == 10:
                exit_to_menu()
            screen.reset()

    # Once the loop ends, you can run the menu again
    run_menu()


def run_menu():
    """
    Displays the menu, allowing the user to pick game mode or quit.
    """
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

    # Start the game after setting up
    main_loop(screen)


run_menu()
