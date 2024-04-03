import pytest
from testbook import testbook

@testbook('notebooks/calculator_nb.ipynb', execute=True)
def test_calculator_initial_value(tb):
    """
    Test the Calculator's initialisation.

    Validates that the Calculator class initialises with the correct value.

    Parameters:
    - initial_value (int/float): The value to initialise the Calculator with.
    - expected (int/float): The expected initial value of the Calculator.
    """
    Calculator = tb.ref("Calculator")
    calc = Calculator(10)
    assert calc.val == 10, f"Initial value of the calculator should be {10}"
    

@testbook('notebooks/calculator_nb.ipynb', execute=True)
def test_calculator_add(tb):
    """
    Test the add function of the Calculator.

    Validates that the add method correctly increments the calculator's value.

    Parameters:
    - initial_value (int/float): The calculator's starting value.
    - add_value (int/float): The value to add to the calculator.
    - expected (int/float): The expected result after addition.
    """
    Calculator = tb.ref("Calculator")
    calc = Calculator(5)
    calc.add(3)
    assert calc.val == 8, f"Adding {3} to {5} should result in {8}"


@testbook('notebooks/calculator_nb.ipynb', execute=True)
def test_calculator_add_neg(tb):
    """
    Test the add function of the Calculator.

    Validates that the add method correctly increments the calculator's value.

    Parameters:
    - initial_value (int/float): The calculator's starting value.
    - add_value (int/float): The value to add to the calculator.
    - expected (int/float): The expected result after addition.
    """
    Calculator = tb.ref("Calculator")
    calc = Calculator(0)
    calc.add(-2)
    assert calc.val == -2, f"Adding {-2} to {0} should result in {-2}"


@testbook('notebooks/calculator_nb.ipynb', execute=True)
def test_calculator_add_big(tb):
    """
    Test the add function of the Calculator.

    Validates that the add method correctly increments the calculator's value.

    Parameters:
    - initial_value (int/float): The calculator's starting value.
    - add_value (int/float): The value to add to the calculator.
    - expected (int/float): The expected result after addition.
    """
    Calculator = tb.ref("Calculator")
    calc = Calculator(100)
    calc.add(100)
    assert calc.val == 200, f"Adding {100} to {100} should result in {200}"


@testbook('notebooks/calculator_nb.ipynb', execute=True)
def test_calculator_repr(tb):
    """
    Test the official string representation of the Calculator.
    
    Validates that invoking repr() on a Calculator instance returns the expected format.
    """
    Calculator = tb.ref("Calculator")
    calc = Calculator(1)
    expected_repr = f"'Calculator({1})'"  
    assert repr(calc) == expected_repr, f"repr should return {expected_repr}"



@testbook('notebooks/calculator_nb.ipynb', execute=True)
def test_calculator_repr_neg(tb):
    """
    Test the official string representation of the Calculator.
    
    Validates that invoking repr() on a Calculator instance returns the expected format.
    """
    Calculator = tb.ref("Calculator")
    calc = Calculator(-1)
    expected_repr = f"'Calculator({-1})'"
    assert repr(calc) == expected_repr, f"repr should return {expected_repr}"
