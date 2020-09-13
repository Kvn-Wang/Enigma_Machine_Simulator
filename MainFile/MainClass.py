from tkinter import *
from MainFile.Classes.UI_Classes.UI_Class.InputOutputLabels import InputOutputLabels
from MainFile.Classes.FunctionalClasses.Rotor.RotorOption.RotorOptionController import RotorController
from MainFile.Classes.FunctionalClasses.KeyBoardFrameLight.KeyBoardsFrame import KeyBoardFrame


# defined a function that recognize every key that has been pressed
# and compare it to every letter in the ascii alphabet which has been linked to a button
def keypress(e):
    # store the letter that has been pressed on the keyboard
    keyboard_pressed_letter = e.char.upper()

    # store the original character
    original_character = keyboard_pressed_letter

    # if the program is currently encrypting a letter and the user pressed another key, discard it
    global encryption_in_progress
    if not encryption_in_progress:
        # set the variable to true, so that the other inputs that the user gives, the program will discard it
        encryption_in_progress = True

        # the try is needed in case the user inputs a special character that the program might return error
        try:
            # check if the symbol is within the ascii table values for char upper case
            if 65 <= ord(keyboard_pressed_letter) <= 90:
                # encrypt the letter through the rotors
                keyboard_pressed_letter = rotor_controller.rotor_encrypt_character(keyboard_pressed_letter)

                # updater the input and output labels by adding the character
                # to the existing string to show what the user has insert
                label_result_input_output_ui.update_input_label(original_character)
                label_result_input_output_ui.update_output_label(keyboard_pressed_letter)

                # light up the result on the keyboards to show what the user has pressed on keyboard,
                # and the result character after the encryption
                keyboard_frame_controller.input_signal_received(original_character, False)
                keyboard_frame_controller.output_signal_received(keyboard_pressed_letter, True)

            # if the key pressed is the del key
            if ord(keyboard_pressed_letter) == 8:
                # eliminate the last character typed, and if removal is successful...
                if label_result_input_output_ui.remove_character():
                    rotor_controller.return_rotors_class().decrease_rotor_offset()
        except:
            pass
        # set the variable to false, so that the user can input another character to be encrypted
        encryption_in_progress = False


# creation of the window
root = Tk()

# setting of the root window
root.configure(bg="black")
root.title("Enigma Machine")
root.geometry("1300x700")
root.bind("<KeyPress>", keypress)
root.resizable(False, False)
root.update()

# creation of object that will show the input and output of the user
label_result_input_output_ui = InputOutputLabels(root)

# creation of the controller for the keyboards light (input, output),
# that will lights up based on the input and output given
keyboard_frame_controller = KeyBoardFrame(root)

# initialize the object that will control everything about the rotors
rotor_controller = RotorController(root, keyboard_frame_controller)

# variable that keeps track, if the ui is occupied with an encryption or not
encryption_in_progress = False

root.mainloop()
