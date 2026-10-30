# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)


    def __init__(self, name, birth):
        '''
            Constructor
        '''

        if not isinstance(name, str):
            raise TypeError("Name field must be of type string")
        elif name == "":
            raise ValueError("Name cannot be an empty string")
        
        if not isinstance(birth, date):
            raise TypeError("Date field must of of type date")

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    '''
        Methods on Person instance 
    '''

    def initials(self):
        '''
            Returns initials of given name in uppercase
            Inputs: person instance
            Outputs: String  with capitalized initials
        '''

        initial_arr = [item[0] for item in self.name.split(" ")]
        initials = "".join(initial_arr)

        return initials.upper()

    def is_birthday(self):
        '''
            Checks if current date is persons birthday
            Inputs: person instance
            Outputs: Boolean, True if birthday, False if not birthday
        '''

        if date.today().month == self.birth.month and date.today().day == self.birth.day:
            return True
        else:
            return False





