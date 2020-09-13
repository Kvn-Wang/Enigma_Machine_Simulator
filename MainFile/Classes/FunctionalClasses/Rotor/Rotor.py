from tkinter import *
from random import randrange
from MainFile.Classes.UI_Classes.ControllerUI import ControllerUI


class Rotor:
    # variable that will contain all the wiring/pairs
    wiring = []

    first_time_running = True

    def __init__(self, root, x_value, y_value, rotor_type_wiring, rotor_name):
        # initializing the frame that will contain all the necessary for the single motor
        self.initialize_frame(root, x_value, y_value)

        self.create_variables()

        self.initialize_rotor(rotor_type_wiring, rotor_name)

        self.rotor_ui = ControllerUI("rotor_ui", self.wiring, self.offset, self.rotorFrame, self.rotor_name_string)

        self.add_component()

    def initialize_frame(self, root, x_value, y_value):
        self.rotorFrame = Frame(root, bg="black")
        self.rotorFrame.place(x=x_value, y=y_value)

    def create_variables(self):
        # offsets variable that correspond at the rotation of the rotor
        self.offset = IntVar()
        self.rotor_name_string = StringVar()

    def initialize_rotor(self, rotor_type_wiring, rotor_name):
        self.wiring = rotor_type_wiring
        self.initialize_offset()
        self.set_rotor_name(rotor_name)

        if self.first_time_running:
            self.first_time_running = False
        else:
            self.rotor_ui.rotor_change_ui(self.wiring, self.offset)

    def initialize_offset(self):
        # initialize the various offsets, range: 0-25
        self.offset.set(randrange(26))

    def add_component(self):
        # zoom the image by 6 times
        image_zoom_value = 6
        button_bg_color = "#67817C"

        image_arrow_up = PhotoImage(file="../ExternalResources/Images/ArrowDown.png")
        image_arrow_up = image_arrow_up.subsample(image_zoom_value)
        # creating and displaying the button
        self.add_button = Button(self.rotorFrame, image=image_arrow_up,
                                 command=self.update_offset, bg=button_bg_color)
        self.add_button.photo = image_arrow_up
        # center the button in the bottom of the canvas
        self.add_button.place(x=self.rotorFrame.winfo_width() / 2 - 5,
                              y=self.rotorFrame.winfo_height() - self.rotor_ui.rotor_get_rotor_title_name_height()
                              - self.rotor_ui.rotor_get_label_offset_height() + 4)

        image_arrow_down = PhotoImage(file="../ExternalResources/Images/ArrowUp.png")
        image_arrow_down = image_arrow_down.subsample(image_zoom_value)
        # creating and displaying the button
        self.minus_button = Button(self.rotorFrame, image=image_arrow_down,
                                   command=self.decrease_offset, bg=button_bg_color)
        self.minus_button.photo = image_arrow_down
        # center the button in the upper of the canvas
        self.minus_button.place(x=self.rotorFrame.winfo_width() / 2 - 5,
                                y=0 + self.rotor_ui.rotor_get_rotor_title_name_height() + 9)

    # rotate the rotor, and check if any of the offsets reached the value 26 (if yes, reset to 0)
    # while still updating the others
    def update_offset(self):
        # if the principal offset has reached 26, it means that the rotor has done a cycle, then reset it
        # because after the 25 in the rotor, there is 0
        if self.offset.get() + 1 == 26:
            # reset offset
            self.offset.set(0)

            # redraw the entire ui
            self.rotor_ui.redraw_all_canvas()

            # return true if the rotor has completed its cycle
            return True
        else:
            self.offset.set(self.offset.get() + 1)

        # redraw the entire ui
        self.rotor_ui.redraw_all_canvas()

        # return false if the rotor haven't yet completed its cycle
        return False

    # check if any of the offsets reached the value -1 (if yes, reset to 25) while updating the others
    def decrease_offset(self):
        # if the principal rotor has reached 0, set its value to 25
        # because before the 0 in the rotor, there is 25
        if self.offset.get() - 1 == -1:
            # set the value of the offset to the max
            self.offset.set(25)

            # redraw the entire ui
            self.rotor_ui.redraw_all_canvas()

            # return true if the rotor has completed its cycle
            return True
        else:
            self.offset.set(self.offset.get() - 1)

        # redraw the entire ui
        self.rotor_ui.redraw_all_canvas()

        return False

    def encryption(self, letter, signal_inverted):
        # convert the letter to ascii value
        self.asciiValue = ord(letter)

        # offset 65 (the value start at the beginning of the ascii table for the upper letter)
        self.asciiValue -= 65

        self.support_value = self.asciiValue
        # add the current offset of the rotor and check if its higher than the max
        if self.support_value + self.offset.get() >= 26:
            self.support_value += self.offset.get()
            self.support_value -= 26
        else:
            self.support_value += self.offset.get()

        # highlight the wiring used
        if signal_inverted:
            # if the signal has been inverted...
            self.rotor_ui.rotor_draw_return_encryption_line(self.rotorFrame, chr(self.support_value + 65))
        else:
            self.rotor_ui.rotor_draw_initial_encryption_line(self.rotorFrame, chr(self.support_value + 65))

        # find the current wiring, knowing the offset, add everything and return the output
        self.find_wiring(signal_inverted)

        # after the 25 in the rotor, there is 0,1,2 and so on..., so do -26 to reset
        if self.asciiValue >= 26:
            self.asciiValue -= 26

        # add the offset, convert back to letter value from the int, and return the result
        return chr(self.asciiValue + 65)

    def find_wiring(self, signal_has_been_inverted):
        # if the signal has been inverted
        if signal_has_been_inverted:
            for i in range(0, len(self.wiring)):
                if self.support_value == self.wiring[i][1]:
                    if (self.asciiValue + (-self.wiring[i][1] + self.wiring[i][0])) < 0:

                        # before the 0 in the rotor, there is 25,24,23 and so on..., so do +26
                        self.asciiValue = self.asciiValue + (
                                -self.wiring[i][1] + self.wiring[i][0]) + 26
                    else:
                        self.asciiValue = self.asciiValue + (
                                -self.wiring[i][1] + self.wiring[i][0])
                    break
        else:
            if self.asciiValue + (-self.wiring[self.support_value][0] + self.wiring[self.support_value][1]) < 0:

                # before the 0 in the rotor, there is 25,24,23 and so on..., so do +26
                self.asciiValue = self.asciiValue + (
                        -self.wiring[self.support_value][0] + self.wiring[self.support_value][1]) + 26
            else:
                self.asciiValue = self.asciiValue + (
                        -self.wiring[self.support_value][0] + self.wiring[self.support_value][1])

    def get_rotor_name(self):
        return self.rotor_name_string.get()

    def set_rotor_name(self, name):
        self.rotor_name_string.set(name)

    def reset_rotor_ui_canvas(self):
        # reset the ui of the motor
        self.rotor_ui.rotor_reset_ui()
