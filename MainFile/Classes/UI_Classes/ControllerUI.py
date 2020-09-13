from MainFile.Classes.UI_Classes.UI_Class.RotorUI import RotorUI
from MainFile.Classes.UI_Classes.UI_Class.PlugBoardUI import PlugBoardUI
from MainFile.Classes.UI_Classes.UI_Class.KeyBoardLayoutUI import KeyBoardLayout
from MainFile.Classes.UI_Classes.UI_Class.ReflectorUI import ReflectorUI
from MainFile.Classes.UI_Classes.UI_Class.CanvasLinkKeyboardPlugBoardUI import CanvasLinkKeyboardPlugBoardUI
from MainFile.Classes.UI_Classes.UI_Class.SpeedAnimationSliderUI import SpeedAnimationSliderUI


class ControllerUI:
    # list that keeps track of how many ui object has been created
    object_count = []

    # position of the main component of the enigma machine (plug board, rotors, reflector)
    main_component_x_pos = 650
    main_component_y_pos = 55

    # colors of the signal before and after being reflected
    initial_color_highlight = "#FECD63"
    return_color_highlight = "#6197CE"

    # color that highlight the link between two letter when the signal is being reflected
    reflector_color_link = "#93C6A0"

    # variables that specify the UI look of the widgets title label
    title_bg = "#65732F"
    title_fg = "white"
    title_font = "Courier 10 bold"

    # variables that specify the UI look of the offsets labels of the rotors
    rotor_offset_label_bg = "#2E4708"
    rotor_offset_label_fg = "white"
    rotor_offset_label_font = "Courier 10 bold"

    # variables that specify the UI look of the button, canvas and title color
    keyboard_button_color_bg = "#424242"
    keyboard_button_color_fg = "white"
    keyboard_frame_color_bg = "#635145"
    keyboard_title_color_bg = "#472337"
    keyboard_title_color_fg = "#E39634"
    keyboard_highlight_color_fg = "black"
    keyboard_x_pos = 900
    keyboard_input_y_pos = 400
    keyboard_output_y_pos = 100

    # animation speed in ms, it also influences the speed of typing, because during the animation,
    # the user can't type more character, it is a list so that it can be shared between classes
    speed_animation = []
    speed_animation.append(50)

    # configuration of the slider and text
    slider_initial_value = 30
    slider_max_value = 500
    slider_x_pos = keyboard_x_pos
    slider_y_pos = 280
    slider_title_text = "Animation Speed (in ms): "
    slider_instruction_text = "The faster the animation, the faster the Encryption.\n" \
                              "You can only encrypt a letter at time."
    slider_label_bg = "black"
    slider_label_fg = "red"
    slider_text_font = "Helvetica 8 bold"

    def __init__(self, object_type, *args):
        # don't give an id to the classes that want just access to the functions of the controller UI
        if object_type == "non_object":
            pass
        # don't initialize its ID, because it doesn't need it
        if object_type == "slider_ui":
            self.slider_ui = SpeedAnimationSliderUI(*args, self.slider_initial_value, self.slider_max_value,
                                                    self.slider_x_pos, self.slider_y_pos, self.slider_title_text,
                                                    self.slider_instruction_text, self.slider_label_bg,
                                                    self.slider_label_fg, self.slider_text_font)
            self.slider_ui.slider.config(command=self.change_animation_speed)
        else:
            # give an "id" (a number) to identify which object ui it is referred to
            self.initialize_id()

            # distinguish what type of object ui has been requested
            if object_type == "rotor_ui":
                self.object_count.append(RotorUI(self.title_bg, self.title_fg, self.title_font, self.rotor_offset_label_bg,
                                                 self.rotor_offset_label_fg, self.rotor_offset_label_font, *args))
            elif object_type == "plugboard_ui":
                self.object_count.append(PlugBoardUI(self.title_bg, self.title_fg, self.title_font, self.object_count, *args))
            elif object_type == "keyboard_ui":
                type_of_keyboard = args[0]
                if type_of_keyboard == "input_keyboard":
                    self.object_count.append(KeyBoardLayout(self.keyboard_button_color_bg,
                                                            self.keyboard_button_color_fg, self.keyboard_frame_color_bg,
                                                            self.keyboard_title_color_bg, self.keyboard_title_color_fg,
                                                            *args[1:], self.keyboard_x_pos, self.keyboard_input_y_pos))
                if type_of_keyboard == "output_keyboard":
                    self.object_count.append(KeyBoardLayout(self.keyboard_button_color_bg,
                                                            self.keyboard_button_color_fg, self.keyboard_frame_color_bg,
                                                            self.keyboard_title_color_bg, self.keyboard_title_color_fg,
                                                            *args[1:], self.keyboard_x_pos, self.keyboard_output_y_pos))

            elif object_type == "reflector_ui":
                self.object_count.append(ReflectorUI(self.title_bg, self.title_fg, self.title_font, *args))
            elif object_type == "canvas_link_keyboard_plug_board_ui":
                self.object_count.append(CanvasLinkKeyboardPlugBoardUI(*args))

    def initialize_id(self):
        # give a personal ID to recognize the object UI
        self.object_id = len(self.object_count)

    # redraw the entire ui of all graphical objects
    def redraw_all_canvas(self):
        for i in range(0, len(self.object_count)):
            self.object_count[i].reset_ui()

    # function to change a ui of a rotor with another one to simulate the change of the rotor
    def rotor_change_ui(self, *args):
        self.object_count[self.object_id].change_rotor_ui(*args)

    # reset the ui of a rotor
    def rotor_reset_ui(self):
        self.object_count[self.object_id].draw_original_canvas()

    # highlight a line in the canvas based on the character received and when the signal has not been yet inverted
    def rotor_draw_initial_encryption_line(self, rotorFrame, char):
        rotorFrame.after(self.speed_animation, self.object_count[self.object_id].draw_initial_encryption_line(char, self.initial_color_highlight))
        # update the ui, to see the highlight of the line
        rotorFrame.update()

    # highlight a line in the canvas based on the character received and when the signal has been inverted
    def rotor_draw_return_encryption_line(self, rotorFrame, char):
        rotorFrame.after(self.speed_animation, self.object_count[self.object_id].draw_return_encryption_line(char, self.return_color_highlight))
        # update the ui, to see the highlight of the line
        rotorFrame.update()

    # get the height of the title of the rotor
    def rotor_get_rotor_title_name_height(self):
        return self.object_count[self.object_id].label_rotor_name.winfo_height()

    # get the height of the offset label of the rotor
    def rotor_get_label_offset_height(self):
        return self.object_count[self.object_id].label_offset.winfo_height()

    # reset the ui of the plug board
    def plugboard_reset_ui(self):
        self.object_count[self.object_id].reset_settings()

    # highlight a connection in the plug board canvas
    def plugboard_highlight_signal_wiring(self, plug_board_frame, signal_inverted, *args):
        if not signal_inverted:
            self.object_count[self.object_id].hightlight_signal_wiring(self.initial_color_highlight, *args)
        else:
            self.object_count[self.object_id].hightlight_signal_wiring(self.return_color_highlight, *args)

        # update the frame to see the highlighting
        plug_board_frame.update()

    def get_pos_letter_right_list(self, character):
        return self.object_count[self.object_id].get_pos_letter_right_list(character)

    # highlight a label to indicate the input or output of a letter
    def keyboard_highlight_label(self, signal_inverted, letter):
        if not signal_inverted:
            self.object_count[self.object_id].lightup(letter, self.initial_color_highlight,
                                                      self.keyboard_highlight_color_fg)
        else:
            self.object_count[self.object_id].lightup(letter, self.return_color_highlight,
                                                      self.keyboard_highlight_color_fg)

    def get_keyboard_x(self):
        return self.object_count[self.object_id].get_keyboard_x()

    def get_height_keyboard(self):
        return self.object_count[self.object_id].get_height_keyboard()

    # return the y value of the center of the keyboard
    def get_absolute_y_keyboard(self):
        return self.object_count[self.object_id].get_absolute_y_keyboard()

    # return the y value of the center of a keyboard (input or output)
    def get_keyboard_center_y(self):
        return self.object_count[self.object_id].get_keyboard_center_y()

    # reset the canvas to its original state (with only straight lines)
    def reflector_draw_initial_canvas(self):
        self.object_count[self.object_id].draw_initial_canvas()

    # show how the signal is reflected by showing the link ui given the letter (it depends on the reflector wirings)
    def reflector_highlight_link(self, *args):
        self.object_count[self.object_id].highlight_link(self.initial_color_highlight, self.return_color_highlight,
                                                         self.reflector_color_link, *args)

    def canvas_link_highlight_link_input_keyboard_plug_board(self, character):
        self.object_count[self.object_id].highlight_link_keyboard_input_plug_board(self.initial_color_highlight,
                                                                                   character)

    def canvas_link_highlight_link_output_keyboard_plug_board(self, character):
        self.object_count[self.object_id].highlight_link_keyboard_output_plug_board(self.return_color_highlight,
                                                                                    character)

    def get_main_component_y(self):
        return self.main_component_x_pos, self.main_component_y_pos

    def get_y_main_component(self):
        return self.main_component_y_pos

    def change_animation_speed(self, current_slide_speed_value):
        self.speed_animation[0] = current_slide_speed_value
