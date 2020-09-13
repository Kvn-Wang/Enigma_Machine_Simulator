from tkinter import *


class CanvasDrawer:
    def __init__(self, frame, width, height, bg_color, border_thickness, placing_mode, x_pos=0, y_pos=0):
        self.wiring_designer = Canvas(frame, width=width, height=height, background=bg_color,
                                      highlightthickness=border_thickness)
        if placing_mode == "place":
            self.wiring_designer.place(x=x_pos, y=y_pos)
        if placing_mode == "pack":
            self.wiring_designer.pack()

    def initial_draw_line(self, right_value_y, left_value_y, color):
        # draw a line to highlight the label connection
        space_line_thickness = 8

        # refresh the canvas to get the corrects values of its width
        self.wiring_designer.update()

        # draw a straight line in the right widget to highlight the connection
        self.wiring_designer.create_line(self.wiring_designer.winfo_width(),
                                         right_value_y,
                                         self.wiring_designer.winfo_width() - space_line_thickness,
                                         right_value_y,
                                         fill=color, width=3)

        # draw the line from a widget to its correspondent widget pos
        self.wiring_designer.create_line(self.wiring_designer.winfo_width() - space_line_thickness,
                                         right_value_y,
                                         0 + space_line_thickness,
                                         left_value_y,
                                         fill=color, width=1)

        # draw a straight line in the left widget to highlight the connection
        self.wiring_designer.create_line(0,
                                         left_value_y,
                                         0 + space_line_thickness,
                                         left_value_y,
                                         fill=color, width=3)

    def return_draw_line(self, right_value_y, left_value_y, color):
        # draw a line to highlight the label connection
        space_line_thickness = 8

        # refresh the canvas to get the corrects values of its width
        self.wiring_designer.update()

        # draw a straight line in the right widget to highlight the connection
        self.wiring_designer.create_line(self.wiring_designer.winfo_width(),
                                         left_value_y,
                                         self.wiring_designer.winfo_width() - space_line_thickness,
                                         left_value_y,
                                         fill=color, width=3)

        # draw the line from a widget to its correspondent widget pos
        self.wiring_designer.create_line(self.wiring_designer.winfo_width() - space_line_thickness,
                                         left_value_y,
                                         0 + space_line_thickness,
                                         right_value_y,
                                         fill=color, width=1)

        # draw a straight line in the left widget to highlight the connection
        self.wiring_designer.create_line(0,
                                         right_value_y,
                                         0 + space_line_thickness,
                                         right_value_y,
                                         fill=color, width=3)

    # clear the canvas of all its lines
    def clear_canvas(self):
        self.wiring_designer.delete("all")
