# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)

        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Inputs must be of type int")
        elif width<=0 or height<=0:
            raise ValueError("Inputs must be positive")

        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    '''
        Methods on rectangle instance
    '''

    def is_square(self):
        '''
        Check if rectangle is a square
        Inputs: Rectangle instance
        Outputs: True if square
                 False if not square
         '''
        if self.width == self.height:
            return True
        else:
            return False



    def area(self):

        '''
        Calculate area of square
        Inputs: instance of Rectangle
        Outputs: area of rectangle
        '''

        return self.width * self.height

    def perimeter(self):

        '''
        Calculate perimeter of rectangle
        Inputs: Rectangle instance
        Outputs: perimeter of rectangle
        '''

        return (self.width * 2) + (self.height * 2)

    
