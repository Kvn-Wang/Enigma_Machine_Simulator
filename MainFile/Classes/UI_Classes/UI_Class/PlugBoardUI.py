from tkinter import *
from string import *


class PlugBoardUI:
    # variable that keeps track if any button of the correspondent list has been clicked
    # (-1 means, no button has been clicked yet)
    right_button_clicked = -1
    left_button_clicked = -1

    plug_settings_text = ""
    plug_settings = []

    def __init__(self, title_bg, title_fg, title_font, object_count_ui, frame, plug_settings_text, plug_settings, root):
        # assign the list of the all objects ui
        self.object_count_ui = object_count_ui
        # copy object main rotor frame
        self.frame = frame

        # max amount of settings (pair) allowed to set (default is 10 because is the same number used in the WW2)
        global max_settings
        max_settings = 10

        self.plug_settings_text = plug_settings_text
        self.plug_settings = plug_settings

        self.create_frame()
        self.initialize_label_result_text(root)

        self.add_plugboard_title_name(title_bg, title_fg, title_font)
        self.initialize_frame(self.plugboard_frame)

        self.draw_canvas()

    def create_frame(self, ):
        self.plugboard_frame = Frame(self.frame, bg="black")
        self.plugboard_frame.pack()

    def initialize_label_result_text(self, root):
        PlugBoardText(root, self.plug_settings_text)

    def add_plugboard_title_name(self, title_bg, title_fg, title_font, ):
        self.button_plug_board_title_name = Label(self.plugboard_frame, text="Plug Board", bg=title_bg, fg=title_fg,
                                                  font=title_font, borderwidth=2, relief="ridge", width=15)
        self.button_plug_board_title_name.pack(pady=3)

    def initialize_frame(self, plugboard_frame):
        # setup the frame for both the list of button
        self.initialize_right_frame(plugboard_frame)
        self.initialize_left_frame(plugboard_frame)

        # initialize the button value order
        self.initialize_value_label()
        plugboard_frame.update()

        # initialize the canvas, and display it
        self.initialize_canvas(plugboard_frame)

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
        self.canvas_height = rotor_frame.winfo_height() - self.button_plug_board_title_name.winfo_height() - 5

        self.wiring_designer = Canvas(rotor_frame, width=self.canvas_width,
                                      height=self.canvas_height, background='#4F4F4F')
        self.wiring_designer.pack(side=LEFT)

    def initialize_value_label(self):
        self.reversed_ascii_table = ascii_uppercase[::-1]

        for letter in range(0, len(self.reversed_ascii_table)):
            self.right_value.append(
                Button(self.right_value_frame, text=self.reversed_ascii_table[letter],
                       borderwidth=1, relief="solid",
                       font=("Microsoft", 7)))

            self.right_value[letter].config(command=lambda i=letter: self.right_button_click(i))

            self.left_value.append(
                Button(self.left_value_frame, text=self.right_value[letter].cget("text"), borderwidth=1, relief="solid",
                      font=("Microsoft", 7), command=lambda i=letter: self.left_button_click(i)))
            self.right_value[letter].grid(row=ord(ascii_uppercase[letter]), column=1, sticky=NSEW)
            self.left_value[letter].grid(row=ord(ascii_uppercase[letter]), column=0, sticky=NSEW)

    def drawline(self, right_value_y, left_value_y, color):
        # draw a line to highlight the label connection
        space_line = 8

        self.wiring_designer.update()

        # draw a straight line in the right label to highlight the connection
        self.wiring_designer.create_line(self.wiring_designer.winfo_width(),
                                         right_value_y,
                                         self.wiring_designer.winfo_width() - space_line,
                                         right_value_y,
                                         fill=color, width=3)

        # draw the line from a label with a character in it, to its correspondent character (see the wirings)
        self.wiring_designer.create_line(self.wiring_designer.winfo_width() - space_line,
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

    def draw_canvas(self):
        # reset
        self.wiring_designer.delete("all")

        # for each letter, draw its line to the correspondent character
        for letter in range(0, len(self.right_value)):
            # if the letter is in the pair setting...
            if self.check_letter_presence_setting(letter):
                # check each pair that has been set
                for pair in range(0, len(self.plug_settings)):
                    # if the letter has been paired, don't draw a straight line,
                    # but a line toward the correspondent character in the other list
                    if self.plug_settings[pair][0] == chr(letter+65):
                        for first_letter_pos in range(0, len(self.right_value)):
                            if chr(letter+65) == self.right_value[first_letter_pos].cget("text"):
                                for second_letter_pos in range(0, len(self.left_value)):
                                    if self.plug_settings[pair][1] == self.left_value[second_letter_pos].cget("text"):
                                        self.drawline(self.right_value[first_letter_pos].winfo_y() + self.right_value[0].winfo_height() / 2,
                                                      self.left_value[second_letter_pos].winfo_y() + self.left_value[0].winfo_height() / 2,
                                                      "black")
                                        self.drawline(self.right_value[second_letter_pos].winfo_y() + self.right_value[0].winfo_height() / 2,
                                                      self.left_value[first_letter_pos].winfo_y() + self.left_value[0].winfo_height() / 2,
                                                      "black")
            else:
                # draw a straight line, starts from the bottom because the alphabet is reversed in the list of button
                self.drawline(self.right_value[25-letter].winfo_y() + self.right_value[0].winfo_height() / 2,
                          self.left_value[25-letter].winfo_y() + self.left_value[0].winfo_height() / 2,
                          "black")

        # reset any highlighting of the opposed button list when setting the plug board
        if self.control_left_click():
            self.reset_color_right_buttons()
        if self.control_right_click():
            self.reset_color_left_buttons()

    def check_letter_presence_setting(self, letter):
        for pair in range(0, len(self.plug_settings)):
            for i in range(0, 2):
                if type(letter) == str:
                    if letter == self.plug_settings[pair][i]:
                        return True
                else:
                    if chr(letter+65) == self.plug_settings[pair][i]:
                        return True
        return False

    def right_button_click(self, right_button_number):
        # if a button of the plugboard has been clicked, reset all UI because the user is changing its settings
        self.redraw_all_canvas()

        # get the number of the button from the list that has been clicked, if yes, add the pair
        self.right_button_clicked = right_button_number

        # reset the bg color of all right buttons
        self.reset_color_right_buttons()

        # highlight the right button list that has been clicked
        self.right_value[right_button_number].config(bg="yellow")

        # check if the letter clicked in the right list is already paired, if yes, delete the pair
        if self.control_pair(self.right_value[self.right_button_clicked].cget("text")):
            # check also if any button in the left list has been clicked,
            # if yes, add the pair (the effect if that of a replacement)
            if self.control_left_click():
                self.add_pair(self.left_value[self.left_button_clicked].cget("text"),
                              self.right_value[self.right_button_clicked].cget("text"))
            # if not, reset everything after having deleted the pair
            else:
                self.reset_settings_lists()
        else:
            # check if any button of the left list has been clicked, if yes, add the pair
            if self.control_left_click():
                self.add_pair(self.left_value[self.left_button_clicked].cget("text"),
                              self.right_value[self.right_button_clicked].cget("text"))

        self.draw_canvas()

    def left_button_click(self, left_button_number):
        # if a button of the plugboard has been clicked, reset all UI because the user is changing its settings
        self.redraw_all_canvas()

        # get the number of the button from the list that has been clicked
        self.left_button_clicked = left_button_number

        # reset the bg color of all left buttons
        self.reset_color_left_buttons()

        # highlight the left button list that has been clicked
        self.left_value[left_button_number].config(bg="yellow")

        # check if the letter clicked in the right list is already paired, if yes, delete the pair
        if self.control_pair(self.left_value[self.left_button_clicked].cget("text")):
            # check also if any button in the left list has been clicked,
            # if yes, add the pair (the effect if that of a replacement)
            if self.control_right_click():
                self.add_pair(self.right_value[self.right_button_clicked].cget("text"),
                              self.left_value[self.left_button_clicked].cget("text"))
            else:
                # if not, reset everything after having deleted the pair
                self.reset_settings_lists()
        else:
            # check if any button of the left list has been clicked, if yes, add the pair
            if self.control_right_click():
                self.add_pair(self.right_value[self.right_button_clicked].cget("text"),
                              self.left_value[self.left_button_clicked].cget("text"))

        self.draw_canvas()

    def reset_color_right_buttons(self):
        for number in range(0, len(self.right_value)):
            self.right_value[number].config(bg="white")

    def reset_color_left_buttons(self):
        for number in range(0, len(self.left_value)):
            self.left_value[number].config(bg="white")

    def control_left_click(self):
        # check if any button of the left list has been clicked
        # if yes, return True
        if self.left_button_clicked >= 0:
            return True

        # if not, return False
        return False

    def control_right_click(self):
        # check if any button of the right list has been clicked
        # if yes, pair the 2 letters (the two letter will be unavailable for other pairing for both lists)
        if self.right_button_clicked >= 0:
            return True

        return False

    # pair the 2 letters (the two letter will be unavailable for other pairing for both lists)
    def add_pair(self, first_letter, second_letter):
        # allow the add settings, only if the current existing settings is under a specified number
        if len(self.plug_settings) != max_settings:
            # calling the function to pair the 2 letter
            self.add_setting(first_letter, second_letter)

        # after having set the pair, reset every option
        self.reset_settings_lists()

    # function that add the couple of letter in the variable
    def add_setting(self, first_letter, second_letter):
        # do not accept any couple that has the same letter
        if not (first_letter == second_letter):
            # add the couple(tuple) to the list
            self.plug_settings.append(tuple((first_letter, second_letter)))

            self.set_label_text()

    def delete_pair(self, pair_number):
        del self.plug_settings[pair_number]
        self.set_label_text()

    def set_label_text(self):
        # change the label text that this strVar is associated to
        self.plug_settings_text.set(self.plug_settings)

    def control_pair(self, letter):
        # check every pair
        for pair in range(0, len(self.plug_settings)):
            # check both letter of the pair because both can't be paired anymore
            for i in range(0, 2):
                # check if the button clicked correspond the letter in the list of pair
                if letter == self.plug_settings[pair][i]:
                    self.delete_pair(pair)
                    # return True, if the letter inserted, is already paired
                    return True
        # return False, if the letter inserted, hasn't been yet paired
        return False

    def reset_settings_lists(self):
        # reset the colors and values of the button list (-1 means no button has been clicked (reset))
        self.reset_color_right_buttons()
        self.right_button_clicked = -1
        self.reset_color_left_buttons()
        self.left_button_clicked = -1

    def hightlight_signal_wiring(self, colour, letter, signal_inverted):
        # for every button in the right list
        for i in range(0, len(self.right_value)):
            # search the one that is correspondent with the input
            if self.right_value[i].cget("text") == letter:
                # check if the letter is paired with any settings
                if self.check_letter_presence_setting(letter):
                    # if yes, search its correspondent
                    for pair in range(0, len(self.plug_settings)):
                        # if the letter in the setting pair, is in the first position
                        # go search its correspondent in the second position
                        if self.right_value[i].cget("text") == self.plug_settings[pair][0]:
                            # knowing the correspondent letter that has to be searched,
                            # go through the left list of buttons to find it
                            for i2 in range(0, len(self.left_value)):
                                if self.left_value[i2].cget("text") == self.plug_settings[pair][1]:
                                    # if the signal has been inverted, draw everything with the index swapped
                                    if signal_inverted:
                                        self.drawline(
                                            self.right_value[i2].winfo_y() + self.right_value[0].winfo_height() / 2,
                                            self.left_value[i].winfo_y() + self.left_value[0].winfo_height() / 2,
                                            colour)
                                        self.highlight_right_button(i2, colour)
                                        self.highlight_left_button(i, colour)
                                    else:
                                        self.drawline(
                                            self.right_value[i].winfo_y() + self.right_value[0].winfo_height() / 2,
                                            self.left_value[i2].winfo_y() + self.left_value[0].winfo_height() / 2,
                                            colour)
                                        self.highlight_right_button(i, colour)
                                        self.highlight_left_button(i2, colour)

                        # if the letter in the setting pair, is in the second position
                        # go search its correspondent in the first position
                        if self.right_value[i].cget("text") == self.plug_settings[pair][1]:
                            # knowing the correspondent letter that has to be searched,
                            # go through the left list of buttons to find it
                            for i2 in range(0, len(self.left_value)):
                                if self.left_value[i2].cget("text") == self.plug_settings[pair][0]:
                                    # if the signal has been inverted, draw everything with the index swapped
                                    if signal_inverted:
                                        self.drawline(
                                            self.right_value[i2].winfo_y() + self.right_value[0].winfo_height() / 2,
                                            self.left_value[i].winfo_y() + self.left_value[0].winfo_height() / 2,
                                            colour)
                                        self.highlight_right_button(i2, colour)
                                        self.highlight_left_button(i, colour)
                                    else:
                                        self.drawline(
                                            self.right_value[i].winfo_y() + self.right_value[0].winfo_height() / 2,
                                            self.left_value[i2].winfo_y() + self.left_value[0].winfo_height() / 2,
                                            colour)
                                        self.highlight_right_button(i, colour)
                                        self.highlight_left_button(i2, colour)
                else:
                    # draw a straight line, starts from the bottom
                    # because the alphabet is reversed in the list of button
                    self.drawline(self.right_value[i].winfo_y() + self.right_value[0].winfo_height() / 2,
                                  self.left_value[i].winfo_y() + self.left_value[0].winfo_height() / 2,
                                  colour)
                    self.highlight_right_button(i, colour)
                    self.highlight_left_button(i, colour)

    def highlight_right_button(self, number_button, colour):
        self.right_value[number_button].config(bg=colour)

    def highlight_left_button(self, number_button, colour):
        self.left_value[number_button].config(bg=colour)

    def reset_settings(self):
        self.reset_settings_lists()
        self.draw_canvas()

    def reset_ui(self):
        # reset the color bg of both lists of buttons
        self.reset_color_right_buttons()
        self.reset_color_left_buttons()

        # reset the canvas color
        self.draw_canvas()

    # redraw the entire ui of all graphical objects
    def redraw_all_canvas(self):
        for i in range(0, len(self.object_count_ui)):
            self.object_count_ui[i].reset_ui()

    def get_pos_letter_right_list(self, character):
        for i in range(0, len(self.right_value)):
            if self.right_value[i].cget("text") == character:
                # return the y (respect the initial pos of the frame) of the character in the right list
                return self.right_value[i].winfo_y() + self.button_plug_board_title_name.winfo_height() \
                       + self.right_value[0].winfo_height()

class PlugBoardText:
    def __init__(self, root, plugboard_wirings, x_pos=580, y_pos=15):
        self.initialize(root, x_pos, y_pos, plugboard_wirings)

    # initialize everything
    def initialize(self, root, x_pos, y_pos, plugboard_wirings):
        self.initialize_frame(root, x_pos, y_pos)
        self.initialize_label(plugboard_wirings)

    # initialize the frame that will contain the labels
    def initialize_frame(self, root, x_pos, y_pos):
        self.input_output_frame = Frame(root, bg="black")
        self.input_output_frame.place(x=x_pos, y=y_pos)

    # creation of 2 labels that permits to see the input and the output of the letters
    def initialize_label(self, plugboard_wirings):
        self.pluboard_text_label = Label(self.input_output_frame, text="Plug Wiring (max " +str(max_settings)+ " settings):", bg="black", fg="#E5B96E",
                                     font=("Helvetica", 11))
        self.pluboard_text_label.pack(side=LEFT)

        self.pluboard_wiring_label = Label(self.input_output_frame, textvariable=plugboard_wirings, bg="black", fg="white",
                                     font=("Helvetica", 11))
        self.pluboard_wiring_label.pack(side=RIGHT)
