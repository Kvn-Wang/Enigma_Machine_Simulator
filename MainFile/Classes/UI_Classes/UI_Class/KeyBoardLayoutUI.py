from tkinter import *
from string import *


class KeyBoardLayout:
    # define the various row of the keyboard
    key_board_line1 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
    key_board_line2 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
    key_board_line3 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']

    def __init__(self, keyboard_button_color_bg, keyboard_button_color_fg, keyboard_frame_color_bg,
                 keyboard_title_color_bg, keyboard_title_color_fg, root, text, x_pos, y_pos):
        # creating a variable that will contain the name and the color of the keyboard that will displayed
        self.text = text

        # creation of the array and assignment of every letter in the ascii alphabet in the array of button
        self.label = []

        # initialize every necessary object
        self.initialize(keyboard_button_color_bg, keyboard_button_color_fg, keyboard_frame_color_bg,
                        root, x_pos, y_pos)

        self.display(keyboard_title_color_bg, keyboard_title_color_fg)

    def initialize(self, keyboard_button_color_bg, keyboard_button_color_fg, keyboard_frame_color_bg,
                   root, x_pos, y_pos):
        self.initialize_frame(root, x_pos, y_pos, keyboard_frame_color_bg)
        self.initialize_label(keyboard_button_color_bg, keyboard_button_color_fg)

    def initialize_frame(self, root, x_pos, y_pos, keyboard_frame_color_bg):
        self.frame = Frame(root, bg=keyboard_frame_color_bg, padx=5, pady=10, borderwidth=3, relief="groove")
        self.frame.place(x=x_pos, y=y_pos)

    def initialize_label(self, keyboard_button_color_bg, keyboard_button_color_fg):
        for letter in ascii_uppercase:
            self.label.append(Label(self.frame, text=letter,
                                    bg=keyboard_button_color_bg, fg=keyboard_button_color_fg,
                                    borderwidth=2, relief="ridge", font=("Microsoft 9 bold")))

    def display(self, keyboard_title_color_bg, keyboard_title_color_fg):
        # display a label that show the name of the functionality (visual only purposes)
        Label(self.frame, text=self.text, font=("Lucida 13 bold"),
              bg=keyboard_title_color_bg, fg=keyboard_title_color_fg, borderwidth=1,
              relief="solid").grid(row=1, columnspan=6, pady=10)

        # displaying every button in a keyboard pattern
        for line1 in range(0, len(self.key_board_line1)):
            for i1 in range(0, len(ascii_uppercase)):
                if self.key_board_line1[line1] == self.label[i1].cget("text"):
                    self.label[i1].grid(row=2, column=line1, ipadx=4, ipady=4, padx=5, pady=2)

        for line2 in range(0, len(self.key_board_line2)):
            for i2 in range(0, len(ascii_uppercase)):
                if self.key_board_line2[line2] == self.label[i2].cget("text"):
                    # add one more column when placing the widget for having more of the "keyboard" feel like
                    self.label[i2].grid(row=3, column=line2 + 1, ipadx=4, ipady=4, padx=6, pady=2)

        for line3 in range(0, len(self.key_board_line3)):
            for i3 in range(0, len(ascii_uppercase)):
                if self.key_board_line3[line3] == self.label[i3].cget("text"):
                    # add one more column when placing the widget for having more of the "keyboard" feel like
                    self.label[i3].grid(row=4, column=line3 + 2, ipadx=4, ipady=4, padx=5, pady=2)

    def lightup(self, letter, bg_color_lightup, fg_color_lightup):
        # go through every label to search the label to highlight
        # while also resetting the others that may be highlighted previously
        for i in range(0, len(self.label)):
            # if the letter that is requested to highlight is the same as the one in the label, highlight its background
            if letter == self.label[i].cget("text"):
                self.label[i].configure(bg=bg_color_lightup, fg=fg_color_lightup)
                self.frame.update()
            # if not, just color its background with a default color
            else:
                self.label[i].configure(bg="#424242", fg="white")

    # reset the bg of all labels to a default color
    def reset_ui(self):
        for i in range(0, len(self.label)):
            self.label[i].configure(bg="#424242", fg="white")

    # return the x pos of the keyboard
    def get_keyboard_x(self):
        return self.frame.winfo_x()

    def get_height_keyboard(self):
        return self.frame.winfo_height()

    # get the y of the keyboard (respect the entire window)
    def get_absolute_y_keyboard(self):
        return self.frame.winfo_rooty()

    # return the y value of the center of the keyboard (plus a constant just to better center the widget)
    def get_keyboard_center_y(self):
        return self.frame.winfo_y() + 20
