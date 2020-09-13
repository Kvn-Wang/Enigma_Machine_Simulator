from tkinter import *


class SpeedAnimationSliderUI:
    def __init__(self, *args):
        self.initialize(*args)

    def initialize(self, root, initial_value_slider, max_value_slider, x_pos, y_pos, title_text, instruction_text,
                   label_bg, label_fg, label_font):
        self.initialize_frame(root, x_pos, y_pos)
        self.title_label(title_text, label_bg, label_fg, label_font)
        self.initialize_slider(initial_value_slider, max_value_slider)
        self.instruction_label(instruction_text, label_bg, label_fg, label_font)

    def initialize_frame(self, root, x_pos, y_pos):
        self.slider_frame = Frame(root, bg="black")
        self.slider_frame.place(x=x_pos, y=y_pos)

    def title_label(self, title_text, title_bg, title_fg, label_font):
        Label(self.slider_frame, text=title_text, bg=title_bg, fg=title_fg, font=label_font).pack()

    def initialize_slider(self, initial_value_slider, max_value_slider):
        self.slider = Scale(self.slider_frame, from_=initial_value_slider, to=max_value_slider, orient=HORIZONTAL)
        self.slider.pack()

    def instruction_label(self, instruction_text, title_bg, title_fg, label_font):
        Label(self.slider_frame, text=instruction_text, bg=title_bg, fg=title_fg, font=label_font).pack()
