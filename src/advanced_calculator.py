import import_ipynb
from calculator_nb import Calculator

class AdvancedCalculator(Calculator):
    """
    An advanced calculator class that extends the basic Calculator with additional 
    arithmetic operations including multiplication, division, exponentiation, and reset.

    Inherits from:
        Calculator: The base calculator class with basic arithmetic functionality.
    
    Methods:
        multiply(b): Multiplies the current value by a number.
        divide(b): Divides the current value by a number.
        exponentiate(b): Raises the current value to the power of a number.
        reset(): Resets the current value to zero.
    """

    def multiply(self, b):
        """
        Multiplies the calculator's current value by a specified number.

        Parameters:
            b (int/float): The number by which to multiply the current value.

        Raises:
            ValueError: If the input is not a number.
        """
        try:
            self.val *= b
        except TypeError:
            raise ValueError("Invalid input: multiplication expects a number.")

    def divide(self, b):
        """
        Divides the calculator's current value by a specified number.

        Parameters:
            b (int/float): The divisor.

        Raises:
            ValueError: If division by zero is attempted or if the input is not a number.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        try:
            self.val /= b
        except TypeError:
            raise ValueError("Invalid input: division expects a number.")

    def exponentiate(self, b):
        """
        Raises the calculator's current value to the power of a specified number.

        Parameters:
            b (int/float): The exponent value.

        Raises:
            ValueError: If the input is not a number.
        """
        try:
            self.val **= b
        except TypeError:
            raise ValueError("Invalid input: exponentiation expects a number.")

    def reset(self):
        """
        Resets the calculator's current value to zero.
        """
        self.val = 0

