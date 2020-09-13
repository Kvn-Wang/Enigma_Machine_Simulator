from tkinter import *


class RotorOption:
    def __init__(self, root, drag_manager_class, pos_x=80, pos_y=15):
        # object that manage the mouse events
        self.drag_manager = drag_manager_class

        # initialize all object and widgets
        self.initialize(root, pos_x, pos_y)

    def initialize(self, root, pos_x, pos_y):
        # initializing the frame that will contain the list of the option available
        self.initialize_frame(root, pos_x, pos_y)

        # creating variable that will specify the number of rotors and the array of label
        self.create_variables()

        # initialize the label that will contain the options
        self.initialize_label()

        self.activate_draggable()

    def initialize_frame(self, root, pos_x, pos_y):
        self.frame_option_rotor = Frame(root, bg="black")
        self.frame_option_rotor.place(x=pos_x, y=pos_y)

    def create_variables(self):
        self.label_rotor_option = []
        self.number_rotor = 5

    def initialize_label(self):
        # create a label for visual only purposes
        Label(self.frame_option_rotor, text="Rotor Option:",
              bg="black", fg="#E5B96E", font=("Helvetica", 11), pady=4, padx=5).grid(column=0, row=0)

        # initializing the array of label
        for number in range(0, self.number_rotor):
            self.label_rotor_option.append(Label(self.frame_option_rotor, text="Rotor " + str(number + 1),
                                                 bg="black", fg="green", font=("Helvetica", 10), pady=4, padx=12))
            # put the widget in the column +1 ahead because of the label for visual purposes
            self.label_rotor_option[number].grid(column=number+1, row=0)

    def activate_draggable(self):
        for number in range(0, self.number_rotor):
            self.drag_manager.add_dragable(self.label_rotor_option[number])

    def deactivate_label(self, number_rotor):
        self.label_rotor_option[number_rotor].configure(fg="red")
        self.drag_manager.remove_dragable(self.label_rotor_option[number_rotor])

    def activate_label(self, number_rotor):
        self.label_rotor_option[number_rotor].configure(fg="green")
        self.drag_manager.add_dragable(self.label_rotor_option[number_rotor])
