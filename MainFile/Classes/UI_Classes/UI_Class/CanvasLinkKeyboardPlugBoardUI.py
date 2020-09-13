from MainFile.Classes.UtilityComponent.CanvasDrawer import CanvasDrawer


class CanvasLinkKeyboardPlugBoardUI:
    def __init__(self, *args):
        self.initialize_canvas_between_keyboard_plug_board(*args)

    def initialize_canvas_between_keyboard_plug_board(self, root, plug_board, keyboard_frame_controller):
        self.keyboard_frame_controller = keyboard_frame_controller
        self.plug_board = plug_board

        # calculate the distance (x) between the plug board (that is the first component) and the keyboards
        width_between_keyboard_plug_board = keyboard_frame_controller.keyboard_lights_input_ui.get_keyboard_x() - \
                                            plug_board.plugboard_frame.winfo_x() - plug_board.get_plugboard_width() - 2

        # height of the components of the enigma machine (plug board, rotors, reflector)
        height_frame_component = keyboard_frame_controller.get_height_both_keyboard()

        self.canvas_link_keyboard_plug_board = CanvasDrawer(root, width_between_keyboard_plug_board,
                                                            height_frame_component, "black", 0, "place",
                                                            plug_board.plugboard_frame.winfo_x() +
                                                            plug_board.get_plugboard_width(),
                                                            plug_board.plugboard_frame.winfo_y())

    def highlight_link_keyboard_input_plug_board(self, color_highlight, character):
        # before drawing the lines, clear it first
        self.reset_ui()

        # draw a line that start from the input keyboard to the correspondent letter
        # (the same one that has been highlighted in the keyboard) in the plug board (right list)
        self.canvas_link_keyboard_plug_board.initial_draw_line(
            self.keyboard_frame_controller.keyboard_lights_input_ui.get_keyboard_center_y(),
            self.plug_board.get_pos_letter_right_list(character),
            color_highlight)

    def highlight_link_keyboard_output_plug_board(self, color_highlight, character):
        # draw a line that start from the the plug board (right list) to the output keyboard
        self.canvas_link_keyboard_plug_board.return_draw_line(
            self.plug_board.get_pos_letter_right_list(character),
            self.keyboard_frame_controller.keyboard_lights_output_ui.get_keyboard_center_y(),
            color_highlight)

    def reset_ui(self):
        self.canvas_link_keyboard_plug_board.clear_canvas()
