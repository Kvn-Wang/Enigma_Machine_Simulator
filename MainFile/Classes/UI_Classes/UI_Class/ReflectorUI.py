from tkinter import *
from string import *

class ReflectorUI:
    def __init__(self, title_bg, title_fg, title_font, root, x_pos, y_pos, reflector_name):
        self.create_frame(root, x_pos, y_pos)
        self.add_reflector_title_name(self.reflector_frame, reflector_name, title_bg, title_fg, title_font)
        self.initialize_frame(self.reflector_frame)
        self.draw_initial_canvas()

    def create_frame(self, root, x_value, y_value):
        self.reflector_frame = Frame(root, bg="black")
        self.reflector_frame.place(x=x_value, y=y_value)

    def add_reflector_title_name(self, rotor_frame, reflector_name, title_bg, title_fg, title_font):
        self.label_reflector_name = Label(rotor_frame, text=reflector_name, bg=title_bg, fg=title_fg,
                                          font=title_font, borderwidth=2, relief="ridge", width=15)
        self.label_reflector_name.pack(pady=3)

    def initialize_frame(self, rotor_frame):
        self.initialize_right_frame(rotor_frame)
        self.initialize_left_frame(rotor_frame)
        self.initialize_value_label()
        rotor_frame.update()

        self.initialize_canvas(rotor_frame)

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
        self.canvas_height = rotor_frame.winfo_height() - self.label_reflector_name.winfo_height() - 5

        self.wiring_designer = Canvas(rotor_frame, width=self.canvas_width, height=self.canvas_height, background='#4F4F4F')
        self.wiring_designer.pack(side=LEFT)

    def initialize_value_label(self):
        self.reversed_ascii_table = ascii_uppercase[::-1]

        for letter in range(0, len(self.reversed_ascii_table)):
            self.right_value.append(
                Label(self.right_value_frame, text=self.reversed_ascii_table[letter], borderwidth=1, relief="solid",
                      font=("Courier", 9), padx=3))
            self.left_value.append(
                Label(self.left_value_frame, text=self.right_value[letter].cget("text"), borderwidth=1, relief="solid",
                      font=("Courier", 9), padx=3))
            self.right_value[letter].grid(row=ord(ascii_uppercase[letter]), column=1, sticky=NSEW)
            self.left_value[letter].grid(row=ord(ascii_uppercase[letter]), column=0, sticky=NSEW)

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

    # draw the initial canvas (that is with only straight lines)
    def draw_initial_canvas(self):
        # reset
        self.wiring_designer.delete("all")

        for letter in range(0, len(self.right_value)):
            self.drawline(self.right_value[letter].winfo_y() + self.right_value[0].winfo_height() / 2,
                          self.left_value[letter].winfo_y() + self.left_value[0].winfo_height() / 2,
                          "black")

            self.right_value[letter].config(bg="white")
            self.left_value[letter].config(bg="white")

    # show how the signal is reflected by showing the link ui given the letter (it depends on the reflector wirings)
    def highlight_link(self, color_button_enter_signal, color_button_return_signal, color_link, starting_letter, end_letter):
        for first_letter in range(0, len(self.left_value)):
            if starting_letter == self.left_value[first_letter].cget("text"):
                # search the end letter input in the list of buttons
                for second_letter in range(0, len(self.left_value)):
                    if end_letter == self.left_value[second_letter].cget("text"):
                        self.hightlight_button(first_letter, color_button_enter_signal)
                        self.hightlight_button(second_letter, color_button_return_signal)

                        self.drawline(
                            self.right_value[first_letter].winfo_y() + self.right_value[0].winfo_height() / 2,
                            self.left_value[first_letter].winfo_y() + self.left_value[0].winfo_height() / 2,
                            color_button_enter_signal)

                        self.drawline(
                            self.right_value[second_letter].winfo_y() + self.right_value[0].winfo_height() / 2,
                            self.left_value[second_letter].winfo_y() + self.left_value[0].winfo_height() / 2,
                            color_button_return_signal)

                        self.draw_link_line(
                            self.left_value[first_letter].winfo_y() + self.left_value[0].winfo_height() / 2,
                            self.left_value[second_letter].winfo_y() + self.left_value[0].winfo_height() / 2,
                            color_link)

    def hightlight_button(self, button_number, color):
        self.right_value[button_number].config(bg=color)
        self.left_value[button_number].config(bg=color)

    def draw_link_line(self, start_left_value_y, end_left_value_y, color):
        # search the starting letter input in the list of buttons
        self.wiring_designer.create_line(10,
                                         start_left_value_y,
                                         10,
                                         end_left_value_y,
                                         fill=color, width=2)
    def reset_ui(self):
        self.draw_initial_canvas()
