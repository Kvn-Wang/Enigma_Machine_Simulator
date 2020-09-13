from tkinter import *
from string import *


class RotorUI:
    def __init__(self, rotor_title_bg, rotor_title_fg, rotor_title_font, rotor_offset_label_bg, rotor_offset_label_fg,
                 rotor_offset_label_font, wiring, offset, rotor_frame, rotor_name):
        self.rotor_frame = rotor_frame

        self.create_variables(wiring, offset)

        # initialize the various labels (the name and the current offset)
        self.initialize_visual_labels(rotor_name, rotor_title_bg, rotor_title_fg, rotor_title_font,
                                      rotor_offset_label_bg, rotor_offset_label_fg, rotor_offset_label_font)

        # initialize the structure of the frame (wirings, buttons ecc...)
        self.initialize_frame()

        # visualize the wirings and the letters
        self.draw_original_canvas()

    def create_variables(self, wiring, offset):
        self.wiring = wiring
        self.offset = offset

    def initialize_visual_labels(self, rotor_name, rotor_title_bg, rotor_title_fg, rotor_title_font,
                                 rotor_offset_label_bg, rotor_offset_label_fg, rotor_offset_label_font):
        # visualize the name of the current rotor
        self.add_rotor_title_name(self.rotor_frame, rotor_name, rotor_title_bg, rotor_title_fg, rotor_title_font)
        # visualize the offset in a label
        self.add_offset_label(self.rotor_frame, rotor_offset_label_bg, rotor_offset_label_fg, rotor_offset_label_font)

    def add_rotor_title_name(self, rotor_frame, rotor_name, rotor_title_bg, rotor_title_fg, rotor_title_font):
        self.label_rotor_name = Label(rotor_frame, textvariable=rotor_name, bg=rotor_title_bg, fg=rotor_title_fg,
                                      font=rotor_title_font, borderwidth=2, relief="ridge", width=15)
        self.label_rotor_name.pack(pady=3)

    def add_offset_label(self, rotor_frame, rotor_offset_label_bg, rotor_offset_label_fg, rotor_offset_label_font):
        self.label_offset = Label(rotor_frame, textvariable=self.offset, bg=rotor_offset_label_bg,
                                  fg=rotor_offset_label_fg, font=rotor_offset_label_font, borderwidth=2, relief="ridge",
                                  width=15)
        self.label_offset.pack(side=BOTTOM)

    def initialize_frame(self):
        self.initialize_right_frame(self.rotor_frame)
        self.initialize_left_frame(self.rotor_frame)
        self.initialize_value_label()
        self.rotor_frame.update()

        self.initialize_canvas(self.rotor_frame)

    def initialize_left_frame(self, rotor_frame):
        self.left_value_frame = Frame(rotor_frame)
        self.left_value_frame.pack(side=LEFT)
        self.left_value = []

    def initialize_right_frame(self, rotor_frame):
        self.right_value_frame = Frame(rotor_frame)
        self.right_value_frame.pack(side=RIGHT)
        self.right_value = []

    def initialize_canvas(self, rotor_frame):
        self.canvas_width = 100

        # the canvas height must be equal at the height of the various buttons
        self.canvas_height = rotor_frame.winfo_height() - self.label_rotor_name.winfo_height() \
                             - self.label_offset.winfo_height() - 5

        self.wiring_designer = Canvas(rotor_frame, width=self.canvas_width, height=self.canvas_height, background='#8A8A8A')
        self.wiring_designer.pack(side=LEFT)

    def initialize_value_label(self):
        self.reversed_ascii_table = ascii_uppercase[::-1]

        for letter in range(0 - self.offset.get(), len(self.reversed_ascii_table) - self.offset.get()):
            self.right_value.append(
                Label(self.right_value_frame, text=self.reversed_ascii_table[letter], borderwidth=1, relief="solid",
                      font=("Courier", 9), padx=3))
        for letter in range(0, len(ascii_uppercase)):
            self.right_value[letter].grid(row=ord(ascii_uppercase[letter]), column=1, sticky=NSEW)

        for letter in range(0, len(ascii_uppercase)):
            self.left_value.append(
                Label(self.left_value_frame, text=self.right_value[letter].cget("text"), borderwidth=1, relief="solid",
                      font=("Courier", 9), padx=3))
            self.left_value[letter].grid(row=ord(ascii_uppercase[letter]), column=1, sticky=NSEW)

    # function that draw only the links without any highlight
    def draw_original_canvas(self):
        self.wiring_designer.delete("all")
        # for every label with a character in it, search its correspondent in the wiring (first position)
        for number_element_label in range(0, len(self.right_value)):
            for number_element_rotor in range(0, len(self.wiring)):
                if ord(self.right_value[number_element_label].cget("text")) - 65 == self.wiring[number_element_rotor][0]:
                    # then search the correspondent wiring (second position) in the list of labels
                    for number_element_label1 in range(0, len(self.right_value)):
                        if (self.wiring[number_element_rotor][1] == ord(
                                self.right_value[number_element_label1].cget("text")) - 65):

                            self.drawline(
                                self.right_value[number_element_label].winfo_y() + self.right_value[0].winfo_height() / 2,
                                self.left_value[number_element_label1].winfo_y() + self.left_value[0].winfo_height() / 2,
                                "black")
        self.reset_button_color()

    def drawline(self, right_value_y, left_value_y, color):
        # draw a line to highlight the label connection
        space_line = 5

        # draw a straight line in the right label to highlight the connection
        self.wiring_designer.create_line(self.canvas_width,
                                    right_value_y,
                                    self.canvas_width - space_line,
                                    right_value_y,
                                    fill=color, width=3)

        # draw the line from a label with a character in it, to its correspondent character (see the wirings)
        self.wiring_designer.create_line(self.canvas_width - space_line,
                                    right_value_y,
                                    0 + space_line,
                                    left_value_y,
                                    fill=color, width=1)

        # draw a straight line in the left label to highlight the connection
        self.wiring_designer.create_line(0,
                                    left_value_y,
                                    0 + space_line,
                                    left_value_y,
                                    fill=color, width=3)

    # redraw everything when the rotor rotate
    def reset_ui(self):
        self.change_value_label()
        self.draw_original_canvas()

    def change_value_label(self):
        for letter in range(0, len(ascii_uppercase)):
            self.right_value[letter].config(text=self.reversed_ascii_table[0 - self.offset.get() + letter])
            self.left_value[letter].config(text=self.right_value[letter].cget("text"))

    def change_rotor_ui(self, wiring, offset):
        self.wiring = wiring
        self.offset = offset

        self.reset_ui()

    def draw_initial_encryption_line(self, letter, color_line):
        # find the correspondent button of the letter
        for number_button_right_label in range(0, len(self.right_value)):
            if letter == self.right_value[number_button_right_label].cget("text"):
                # find the correspondent letter searching through the wirings
                for position_wiring in range(0, len(self.wiring)):
                    if ord(letter)-65 == self.wiring[position_wiring][0]:
                        # given the result through the wiring, search the letter
                        for number_button_left_label in range(0, len(self.left_value)):
                            if chr(self.wiring[position_wiring][1]+65) == self.left_value[number_button_left_label].cget("text"):
                                self.drawline(self.right_value[number_button_right_label].winfo_y() + self.right_value[0].winfo_height() / 2,
                                              self.left_value[number_button_left_label].winfo_y() + self.left_value[0].winfo_height() / 2,
                                              color_line)

                                self.right_value[number_button_right_label].config(bg=color_line)
                                self.left_value[number_button_left_label].config(bg=color_line)

    def draw_return_encryption_line(self, letter, color_line):
        # find the correspondent button of the letter
        for number_button_left_label in range(0, len(self.left_value)):
            if letter == self.left_value[number_button_left_label].cget("text"):
                # find the correspondent letter searching through the wirings
                for position_wiring in range(0, len(self.wiring)):
                    if ord(letter) - 65 == self.wiring[position_wiring][1]:
                        # given the result through the wiring, search the letter
                        for number_button_right_label in range(0, len(self.right_value)):
                            if chr(self.wiring[position_wiring][0] + 65) == self.right_value[number_button_right_label].cget("text"):
                                self.drawline(self.right_value[number_button_right_label].winfo_y() + self.right_value[0].winfo_height() / 2,
                                              self.left_value[number_button_left_label].winfo_y() + self.left_value[0].winfo_height() / 2,
                                              color_line)

                                self.right_value[number_button_right_label].config(bg=color_line)
                                self.left_value[number_button_left_label].config(bg=color_line)

    def reset_button_color(self):
        for number in range(0, len(self.right_value)):
            self.right_value[number].config(bg="white")
            self.left_value[number].config(bg="white")