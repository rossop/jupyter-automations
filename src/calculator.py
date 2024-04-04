class Calculator:
    """
    A simple calculator class that supports basic arithmetic operations including 
    addition and subtraction.

    Attributes:
        val (int/float): The current value stored in the calculator, representing 
        the result of arithmetic operations.
    
    Methods:
        __init__(a): Initializes a new Calculator instance with a specified numeric value.
        add(b): Adds a number to the calculator's current value, ensuring 'b' is numeric.
        subtract(b): Subtracts a number from the calculator's current value, ensuring 'b' is numeric.
        __repr__(): Provides an official string representation of the calculator instance.
        __str__(): Returns a friendly string representation of the calculator instance.
    """

    def __init__(self, a):
        """
        Initializes a new instance of the Calculator with a specified value.

        Parameters:
            a (int/float): The initial value to store in the calculator.
        
        Raises:
            ValueError: If 'a' is not an integer or float.
        """
        if not isinstance(a, (int, float)):
            raise ValueError("Invalid input: 'a' must be an integer or float.")
        self.val = a

    def add(self, b):
        """
        Adds a number to the calculator's current value.

        Parameters:
            b (int/float): The number to be added to the current value.
        
        Raises:
            ValueError: If 'b' is not an integer or float.
        """
        if not isinstance(b, (int, float)):
            raise ValueError("Invalid input: 'b' must be an integer or float.")
        self.val += b

    def subtract(self, b):
        """
        Subtracts a number from the calculator's current value.

        Parameters:
            b (int/float): The number to be subtracted from the current value.
        
        Raises:
            ValueError: If 'b' is not an integer or float.
        """
        if not isinstance(b, (int, float)):
            raise ValueError("Invalid input: 'b' must be an integer or float.")
        self.val -= b

    def __repr__(self):
        """
        Returns an official string representation of the calculator instance.

        Returns:
            str: A string that can be used to recreate the calculator instance.
        """
        return f"Calculator({self.val})"
        
    def __str__(self):
        """
        Returns a friendly string representation of the calculator instance.

        Returns:
            str: A descriptive string indicating the current value of the calculator.
        """
        return f"Calculator instance with value = {self.val}"


