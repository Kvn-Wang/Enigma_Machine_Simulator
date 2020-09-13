from MainFile.Classes.UI_Classes.ControllerUI import ControllerUI


class KeyBoardFrame:
    def __init__(self, root):
        # creation of the various lights (in the format of a keyboard) that will light up based on the given input
        self.keyboard_lights_input_ui = ControllerUI("keyboard_ui", "input_keyboard", root, "Key Board (Input)")

        # creation of the various lights (in the format of a keyboard) that will light up based on the given output
        self.keyboard_lights_output_ui = ControllerUI("keyboard_ui", "output_keyboard", root, "Light Board (Output)")

    def input_signal_received(self, letter, signal_inverted):
        self.keyboard_lights_input_ui.keyboard_highlight_label(signal_inverted, letter)

    def output_signal_received(self, letter, signal_inverted):
        self.keyboard_lights_output_ui.keyboard_highlight_label(signal_inverted, letter)

    def get_height_both_keyboard(self):
        return self.keyboard_lights_input_ui.get_absolute_y_keyboard() + \
               self.keyboard_lights_input_ui.get_height_keyboard() + \
               self.keyboard_lights_input_ui.get_y_main_component() - \
               self.keyboard_lights_output_ui.get_absolute_y_keyboard()
