from MainFile.Classes.UI_Classes.ControllerUI import ControllerUI


class Reflector:

    # Reflector B: check wikipedia
    pairs = [(0, 24), (1, 17), (2, 20), (3, 7), (4, 16), (5, 18), (6, 11), (7, 3), (8, 15), (9, 23),
             (10, 13), (11, 6), (12, 14), (13, 10), (14, 12), (15, 8), (16, 4), (17, 1), (18, 5),
             (19, 25), (20, 2), (21, 22), (22, 21), (23, 9), (24, 0), (25, 19)]

    invert = False

    def __init__(self, root, x_pos, y_pos):
        self.reflector_ui = ControllerUI("reflector_ui", root, x_pos, y_pos, "Reflector B")

    def reflect(self, letter):
        # convert the letter to ascii value
        self.asciiValue = ord(letter)
        # offset 65 (the value start at the beginning of the ascii table for the upper letter)
        self.asciiValue -= 65

        # search whichever number, this value is associated with
        for i in range(0, len(self.pairs)):
            if self.asciiValue == self.pairs[i][0]:
                self.asciiValue = self.pairs[i][1]
                break

        self.invert = True

        # reset the ui
        self.reflector_ui.reflector_draw_initial_canvas()
        # display the link
        self.reflector_ui.reflector_highlight_link(letter, chr(self.asciiValue + 65))

        # add the offset, convert back to letter value from the int, and return the result
        return chr(self.asciiValue + 65)
