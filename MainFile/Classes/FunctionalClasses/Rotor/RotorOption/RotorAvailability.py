class RotorAvailability:
    # list that keeps track of which rotors has been used
    rotor_availability = [True, True, True, True, True]

    def __init__(self, start_rotor_1, start_rotor_2, start_rotor_3, rotor_option_class):
        # create the object that will control the label option of the rotors
        self.rotor_option_class = rotor_option_class

        # bind the first 3 rotors
        self.initial_bind_rotor(start_rotor_1, start_rotor_2, start_rotor_3)

    # bind the initial 3 rotors
    def initial_bind_rotor(self, start_rotor_1, start_rotor_2, start_rotor_3):
        # do -1 to bring the offset from 1 to 0
        self.bind_rotor(start_rotor_1 - 1)
        self.bind_rotor(start_rotor_2 - 1)
        self.bind_rotor(start_rotor_3 - 1)

    def bind_rotor(self, rotor_number):
        self.rotor_availability[rotor_number] = False
        self.rotor_option_class.deactivate_label(rotor_number)

    def unbind_rotor(self, rotor_number):
        self.rotor_availability[rotor_number] = True
        self.rotor_option_class.activate_label(rotor_number)
