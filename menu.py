import time


class Menu:
    def __init__(self, display, joystick_y):
        self.display = display
        self.joystick_y = joystick_y
        self.selected_option = 0  # 0 = "2 Players", 1 = "vs Bot"

    def show(self):
        self.display.fill(0)

        if self.selected_option == 0:
            self.display.text("> 2 Players", 5, 15)
            self.display.text("  vs Bot", 5, 35)
        else:
            self.display.text("  2 Players", 5, 15)
            self.display.text("> vs Bot", 5, 35)

        self.display.show()

    def update_selection(self):
        val = self.joystick_y.read_u16()

        if val < 20000:
            self.selected_option = 0
        elif val > 45000:
            self.selected_option = 1

    def wait_for_confirm(self, button):
        while True:
            self.update_selection()
            self.show()
            if button.value() == 0:
                # Button pressed, break
                return self.selected_option
            time.sleep(0.1)
