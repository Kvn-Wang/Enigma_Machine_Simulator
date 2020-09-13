from MainFile.Classes.FunctionalClasses.Rotor.Rotor import Rotor


class RotorController:
    space_between_widget = 138

    def __init__(self, root, x_pos, y_pos, start_rotor_i, start_rotor_ii, start_rotor_iii):
        # creation of the rotors and bind the rotors (do -1 to bring the offset from 1 to 0)
        self.rotor1 = Rotor(root, x_pos - self.space_between_widget, y_pos, self.assign_rotor(start_rotor_i),
                            self.assign_rotor_name(start_rotor_i))
        self.rotor2 = Rotor(root, x_pos - self.space_between_widget * 2, y_pos, self.assign_rotor(start_rotor_ii),
                            self.assign_rotor_name(start_rotor_ii))
        self.rotor3 = Rotor(root, x_pos - self.space_between_widget * 3, y_pos, self.assign_rotor(start_rotor_iii),
                            self.assign_rotor_name(start_rotor_iii))

    def assign_rotor(self, rotor_number):
        # Rotor I: check wikipedia
        rotor_I = [(0, 4), (1, 10), (2, 12), (3, 5), (4, 11), (5, 6), (6, 3), (7, 16), (8, 21), (9, 25), (10, 13),
                  (11, 19), (12, 14), (13, 22), (14, 24), (15, 7), (16, 23), (17, 20), (18, 18), (19, 15), (20, 0),
                  (21, 8), (22, 1), (23, 17), (24, 2), (25, 9)]

        # Rotor II: check wikipedia
        rotor_II = [(0, 0), (1, 9), (2, 3), (3, 10), (4, 18), (5, 8), (6, 17), (7, 20), (8, 23), (9, 1), (10, 11),
                  (11, 7), (12, 22), (13, 19), (14, 12), (15, 2), (16, 16), (17, 6), (18, 25), (19, 13), (20, 15),
                  (21, 24), (22, 5), (23, 21), (24, 14), (25, 4)]

        # Rotor III: check wikipedia
        rotor_III = [(0, 1), (1, 3), (2, 5), (3, 7), (4, 9), (5, 11), (6, 2), (7, 15), (8, 17), (9, 19), (10, 23),
                  (11, 21), (12, 25), (13, 13), (14, 24), (15, 4), (16, 8), (17, 22), (18, 6), (19, 0), (20, 10),
                  (21, 12), (22, 20), (23, 18), (24, 16), (25, 14)]

        # Rotor IV: check wikipedia
        rotor_IV = [(0, 4), (1, 18), (2, 13), (3, 21), (4, 15), (5, 25), (6, 9), (7, 0), (8, 24), (9, 16), (10, 20),
                  (11, 8), (12, 17), (13, 7), (14, 23), (15, 11), (16, 13), (17, 5), (18, 19), (19, 6), (20, 10),
                  (21, 3), (22, 2), (23, 12), (24, 22), (25, 1)]

        # Rotor V: check wikipedia
        rotor_V = [(0, 21), (1, 25), (2, 1), (3, 17), (4, 6), (5, 8), (6, 19), (7, 24), (8, 20), (9, 15), (10, 18),
                  (11, 3), (12, 13), (13, 7), (14, 11), (15, 23), (16, 0), (17, 22), (18, 12), (19, 9), (20, 16),
                  (21, 14), (22, 5), (23, 4), (24, 2), (25, 10)]

        switcher = {
            1: rotor_I,
            2: rotor_II,
            3: rotor_III,
            4: rotor_IV,
            5: rotor_V
        }

        return switcher.get(rotor_number)

    def assign_rotor_name(self, rotor_number):
        switcher_name = {
            1: "rotor I",
            2: "rotor II",
            3: "rotor III",
            4: "rotor IV",
            5: "rotor V"
        }

        return switcher_name.get(rotor_number)

    def reverse_rotor_name(self, rotor_name):
        switcher_number = {
            "rotor I": 0,
            "rotor II": 1,
            "rotor III": 2,
            "rotor IV": 3,
            "rotor V": 4,
        }
        return switcher_number.get(rotor_name)

    def initial_encryption(self, letter, signal_inverted):
        return self.rotor3.encryption(
            self.rotor2.encryption(self.rotor1.encryption(letter, signal_inverted),
                                   signal_inverted), signal_inverted)

    def return_encryption(self, letter, signal_inverted):
        return self.rotor1.encryption(
            self.rotor2.encryption(self.rotor3.encryption(letter, signal_inverted),
                                   signal_inverted), signal_inverted)

    def update_rotors_offset(self):
        # update cycle
        cycle_completed = self.rotor1.update_offset()
        if cycle_completed:
            cycle_completed = self.rotor2.update_offset()
        if cycle_completed:
            self.rotor3.update_offset()

    def decrease_rotors_offset(self):
        # update cycle
        cycle_completed = self.rotor1.decrease_offset()
        if cycle_completed:
            cycle_completed = self.rotor2.decrease_offset()
        if cycle_completed:
            self.rotor3.decrease_offset()

    def change_rotor_1(self, number_replace_rotor):
        # swap the rotor
        self.rotor1.initialize_rotor(self.assign_rotor(number_replace_rotor),
                                     self.assign_rotor_name(number_replace_rotor))

    def change_rotor_2(self, number_replace_rotor):
        # swap the rotor
        self.rotor2.initialize_rotor(self.assign_rotor(number_replace_rotor),
                                     self.assign_rotor_name(number_replace_rotor))

    def change_rotor_3(self, number_replace_rotor):
        # swap the rotor
        self.rotor3.initialize_rotor(self.assign_rotor(number_replace_rotor),
                                     self.assign_rotor_name(number_replace_rotor))
