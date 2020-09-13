from MainFile.Classes.FunctionalClasses.EnigmaController import EnigmaMachineMainFrame
from MainFile.Classes.FunctionalClasses.Rotor.RotorOption.RotorOption import RotorOption
from MainFile.Classes.FunctionalClasses.Rotor.RotorOption.RotorAvailability import RotorAvailability
from tkinter import *


class RotorController:
    def __init__(self, root, keyboard_frame_controller, start_rotor_i=1, start_rotor_ii=2, start_rotor_iii=3):
        # object that manage the mouse events
        self.drag_manager = DragManager(root)

        # object for displaying the list of the rotors to choose from
        self.rotor_option = RotorOption(root, self.drag_manager)

        # object that keeps track of which rotors has been used
        self.rotor_availability = RotorAvailability(start_rotor_i, start_rotor_ii, start_rotor_iii, self.rotor_option)

        # creation of the rotor class
        global rotors
        rotors = EnigmaMachineMainFrame(root, self.rotor_availability, keyboard_frame_controller, start_rotor_i,
                                        start_rotor_ii, start_rotor_iii)

    def rotor_encrypt_character(self, letter):
        return rotors.encrypt(letter)

    def return_rotors_class(self):
        return rotors


class DragManager:
    # variable that store which rotor the user has chosen
    rotor_option_selected = ""

    # variable that specify the color of the text and bg of the mimic label when its being dragged
    drag_mimic_label_color_bg = "#8298AF"
    drag_mimic_label_color_fg = "#004EAA"

    # names of the 3 rotor frame
    first_rotor_frame_name = ".!frame7"
    second_rotor_frame_name = ".!frame8"
    third_rotor_frame_name = ".!frame9"

    def __init__(self, root):
        self.root = root

        # initialize the image object that will be useful during the dragging of the mimic label,
        # the image are meant to visualize where the user could drop the label
        self.initialize_image_icon()

    def initialize_image_icon(self):
        image_zoom_value = 50

        self.image_prohibition_signal = PhotoImage(file="../ExternalResources/Images/ProhibitionSignal.png")
        self.image_prohibition_signal = self.image_prohibition_signal.subsample(image_zoom_value)

        self.image_add_icon = PhotoImage(file="../ExternalResources/Images/AddImageIcon.png")
        self.image_add_icon = self.image_add_icon.subsample(image_zoom_value)

    def add_dragable(self, widget):
        # binding the various function of the mouse left-click
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand2")

    def remove_dragable(self, widget):
        widget.unbind("<ButtonPress-1>")
        widget.unbind("<B1-Motion>")
        widget.unbind("<ButtonRelease-1>")
        widget.configure(cursor="arrow")

    def on_start(self, event):
        # find the widget under the cursor
        x, y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x, y)

        # store the name of the option selected and also show the user what option he has chosen though a mimic label
        self.rotor_option_selected = target.cget("text")

        self.mimic_label_drag_effect = Label(text=target.cget("text"), bg=self.drag_mimic_label_color_bg,
                                             fg=self.drag_mimic_label_color_fg, font=target.cget("font"),
                                             relief="ridge", borderwidth=1)

        self.mimic_label_image_icon = Label(bg=self.drag_mimic_label_color_bg)

    def on_drag(self, event):
        # find the widget under the cursor
        x, y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x, y)

        # if the cursor is on top of these frame that correspond to the 3 rotors,
        # show the add image that means that the user can drop the label on them
        if target.winfo_parent() == self.first_rotor_frame_name or target.winfo_parent() == self.second_rotor_frame_name \
                or target.winfo_parent() == self.third_rotor_frame_name:
            self.mimic_label_image_icon.config(image=self.image_add_icon)
            self.mimic_label_image_icon.image = self.image_add_icon
        # otherwise just show a prohibition signal that means the area where the cursor is actually in,
        # the user can't drop the label
        else:
            self.mimic_label_image_icon.config(image=self.image_prohibition_signal)
            self.mimic_label_image_icon.image = self.image_prohibition_signal

        # move the image icon near the mimic label, precisely in the bottom right
        self.mimic_label_image_icon.place(x=self.root.winfo_pointerx() - self.root.winfo_rootx() +
                                          self.mimic_label_drag_effect.winfo_width() / 2 - 5,
                                          y=self.root.winfo_pointery() - self.root.winfo_rooty() -
                                          self.mimic_label_drag_effect.winfo_height() / 2)

        # as long as the mouse is moving and the left click is pressed,
        # keep moving the mimic label position under the cursor
        self.mimic_label_drag_effect.place(x=self.root.winfo_pointerx() - self.root.winfo_rootx() -
                                           self.mimic_label_drag_effect.winfo_width() / 2 + 5,
                                           y=self.root.winfo_pointery() - self.root.winfo_rooty() -
                                           self.mimic_label_drag_effect.winfo_height() - 5)
        pass

    def on_drop(self, event):
        # delete the mimic, because it was only for visual purposes to show the drag and drop effect on the window
        self.mimic_label_drag_effect.place_forget()
        self.mimic_label_image_icon.place_forget()

        # find the widget under the cursor
        x, y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x, y)
        try:
            # if the mouse pointer is on the first rotor (his frame),
            # change the rotor with the selected option with the first rotor
            if target.winfo_parent() == self.first_rotor_frame_name:
                rotors.change_rotor(int(self.rotor_option_selected[6]), 1)

            # if the mouse pointer is on the second rotor (his frame),
            # change the rotor with the selected option with the second rotor
            elif target.winfo_parent() == self.second_rotor_frame_name:
                rotors.change_rotor(int(self.rotor_option_selected[6]), 2)

            # if the mouse pointer is on the third rotor (his frame),
            # change the rotor with the selected option with the third rotor
            elif target.winfo_parent() == self.third_rotor_frame_name:
                rotors.change_rotor(int(self.rotor_option_selected[6]), 3)
        except:
            pass
