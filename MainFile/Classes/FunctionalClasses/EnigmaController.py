from MainFile.Classes.FunctionalClasses.Reflector.Reflector import Reflector
from MainFile.Classes.FunctionalClasses.PlugBoard.PlugBoard import PlugBoard
from MainFile.Classes.UI_Classes.ControllerUI import ControllerUI
from MainFile.Classes.FunctionalClasses.Rotor.RotorController import RotorController


# class that manage anything of the encryption
class EnigmaMachineMainFrame:
    # this class is called by rotor option controller, it is not called directly because the rotor option controller,
    # needs the functionality of the enigma machine controller (specifically the change rotor one)
    def __init__(self, root, rotor_availability_class, keyboard_frame_controller, start_rotor_i, start_rotor_ii,
                 start_rotor_iii):
        # list that keeps track of which rotors has been used
        self.rotor_availability = rotor_availability_class

        # object that contain both input and output keyboard
        self.keyboard_frame_controller = keyboard_frame_controller

        # object that control any ui object
        self.ui_controller = ControllerUI("non_object")
        x_main_component_pos, y_main_component_pos = self.ui_controller.get_main_component_y()

        # space between each plug board/rotor/reflector
        space_between_widget = 138

        # create the object plug board
        self.plug_board = PlugBoard(root, x_main_component_pos, y_main_component_pos)

        # creation of the rotors and bind the rotors (do -1 to bring the offset from 1 to 0)
        self.rotor_controller = RotorController(root, x_main_component_pos, y_main_component_pos, start_rotor_i,
                                                start_rotor_ii, start_rotor_iii)

        # creation of the reflector, the space between widgets is multiplied by 4 because before there are 3 rotors
        self.reflector = Reflector(root, x_main_component_pos - space_between_widget * 4, y_main_component_pos)

        self.canvas_link_keyboard_plug_board = ControllerUI("canvas_link_keyboard_plug_board_ui", root, self.plug_board,
                                                            self.keyboard_frame_controller)

        # create a slide that will be used to control the velocity of the animation/encryption
        ControllerUI("slider_ui", root)

    def encrypt(self, not_encrypted_letter):
        self.reflector.invert = False

        # update the offsets while also updating the canvas
        self.update_rotors()

        # highlight the link between the input keyboard and to its correspondent char in the plug board
        self.canvas_link_keyboard_plug_board.canvas_link_highlight_link_input_keyboard_plug_board(not_encrypted_letter)

        # first go through the plug board
        encrypted_letter = self.plug_board.encrypt(not_encrypted_letter, self.reflector.invert)

        # first encryption -> reflect the signal -> second encryption
        encrypted_letter = self.second_encryption(
            self.reflector.reflect(self.first_encryption(encrypted_letter,
                                                         self.reflector.invert)), self.reflector.invert)

        # pass last time through the plug board
        encrypted_letter = self.plug_board.encrypt(encrypted_letter, self.reflector.invert)

        # highlight the link between the input keyboard and to its correspondent char in the plug board
        self.canvas_link_keyboard_plug_board.canvas_link_highlight_link_output_keyboard_plug_board(encrypted_letter)

        # and finally return the encrypted letter
        return encrypted_letter

    def first_encryption(self, *args):
        return self.rotor_controller.initial_encryption(*args)

    def second_encryption(self, *args):
        return self.rotor_controller.return_encryption(*args)

    def update_rotors(self):
        # update cycle
        self.rotor_controller.update_rotors_offset()

    def decrease_rotor_offset(self):
        # decrease rotors offset
        self.rotor_controller.decrease_rotors_offset()

    def change_rotor(self, number_replace_rotor, target_replace_rotor):
        # reset all canvas, because the user is changing the settings of the enigma machine
        self.ui_controller.redraw_all_canvas()

        if target_replace_rotor == 1:
            # unbind the rotor that has been replaced so that it can be chosen again
            # for later swap if the user wishes so
            self.unbind_motor(self.rotor_controller.reverse_rotor_name(self.rotor_controller.rotor1.get_rotor_name()))

            # swap the rotor 1
            self.rotor_controller.change_rotor_1(number_replace_rotor)

        elif target_replace_rotor == 2:
            # unbind the rotor that has been replaced so that it can be chosen again
            # for later swap if the user wishes so
            self.unbind_motor(self.rotor_controller.reverse_rotor_name(self.rotor_controller.rotor2.get_rotor_name()))

            # swap the rotor 2
            self.rotor_controller.change_rotor_2(number_replace_rotor)

        elif target_replace_rotor == 3:
            # unbind the rotor that has been replaced so that it can be chosen again
            # for later swap if the user wishes so
            self.unbind_motor(self.rotor_controller.reverse_rotor_name(self.rotor_controller.rotor3.get_rotor_name()))

            # swap the rotor 3
            self.rotor_controller.change_rotor_3(number_replace_rotor)

        # refresh the status of the availability of the rotors, bind the rotor so that it can't be assigned anymore
        # do -1 to bring the offset from 1 to 0
        self.bind_motor(number_replace_rotor-1)

    def bind_motor(self, number_rotor):
        self.rotor_availability.bind_rotor(number_rotor)

    def unbind_motor(self, number_rotor):
        self.rotor_availability.unbind_rotor(number_rotor)

    def reset_all_rotor_ui(self):
        # reset all canvas
        self.ui_controller.redraw_all_canvas()
