from tkinter import *


class InputOutputLabels:
    def __init__(self, root, x_pos=100, y_pos=630):
        self.initialize(root, x_pos, y_pos)

    # initialize everything
    def initialize(self, root, x_pos, y_pos):
        self.initialize_frame(root, x_pos, y_pos)
        self.initialize_label()

    # initialize the frame that will contain the labels
    def initialize_frame(self, root, x_pos, y_pos):
        self.input_output_frame = Frame(root, bg="black")
        self.input_output_frame.place(x=x_pos, y=y_pos)

    # creation of 2 labels that permits to see the input and the output of the letters
    def initialize_label(self):
        self.output_label = Label(self.input_output_frame, text="Output: ", bg="black", fg="white",
                                  font=("Lucida Console", 12))
        self.output_label.pack()

        self.input_label = Label(self.input_output_frame, text="Input:  ", bg="black", fg="white",
                                 font=("Lucida Console", 12))
        self.input_label.pack()

    # update the input label when a character is pressed on the keyboard
    def update_input_label(self, letter):
        self.input_label.config(text=self.input_label.cget("text") + letter)

    # update the input label, it will contain the encrypted character
    def update_output_label(self, letter):
        self.output_label.config(text=self.output_label.cget("text") + letter)

    # when the user press the del key, remove the last character in the labels
    def remove_character(self):
        # necessary control to avoid removing the initial text, if it's successful, return True
        if len(self.input_label.cget("text")) > 8:
            self.input_label.config(text=self.input_label.cget("text")[:-1])
            self.output_label.config(text=self.output_label.cget("text")[:-1])
            return True

        # return False if the removal of the character wasn't successful
        return False
