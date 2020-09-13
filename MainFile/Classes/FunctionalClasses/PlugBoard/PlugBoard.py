from tkinter import *
from MainFile.Classes.UI_Classes.ControllerUI import ControllerUI


class PlugBoard:
    def __init__(self, root, x_value, y_value):
        # string that contain all the wiring that has been set in text format
        self.plug_settings_text = StringVar()
        # list that contain all the wiring that has been set in tuple format
        self.plug_settings = []

        self.initialize_frame(root, x_value, y_value)

        self.plug_board_ui = ControllerUI("plugboard_ui", self.plugboard_frame, self.plug_settings_text, self.plug_settings, root)

    def initialize_frame(self, root, x_value, y_value):
        self.plugboard_frame = Frame(root, bg="black")
        self.plugboard_frame.place(x=x_value, y=y_value)

    def encrypt(self, letter, signal_inverted):
        # at the start of the encryption, reset the UI,
        # it understands that it is the start because the signal has yet to be inverted
        if not signal_inverted:
            # reset the UI (set the default bg of all buttons of the both lists)
            self.plug_board_ui.plugboard_reset_ui()

        # light up the wire and button that is interested in the encryption with a colour
        self.plug_board_ui.plugboard_highlight_signal_wiring(self.plugboard_frame, signal_inverted, letter, signal_inverted)

        for pair in range(0, len(self.plug_settings)):
            # if the letter has been found in the first position of the pair, return the second letter associated to it
            if self.plug_settings[pair][0] == letter:
                return self.plug_settings[pair][1]

            # if the letter has been found in the second position of the pair, return the first letter associated to it
            elif self.plug_settings[pair][1] == letter:
                return self.plug_settings[pair][0]

        # if there are not configuration for the input character, just return it without any variation
        return letter

    def get_plugboard_width(self):
        return self.plugboard_frame.winfo_width()

    def get_pos_letter_right_list(self, character):
        return self.plug_board_ui.get_pos_letter_right_list(character)
