import pytest
from testbook import testbook

@pytest.fixture(scope='module')
def tb():
    """
    A pytest fixture that sets up a Testbook environment by initialising a session
    with a specific Jupyter notebook. This fixture ensures the notebook is executed
    within a controlled test context, facilitating the testing of notebook cells and
    the Python objects they define. It's scoped to 'module', meaning the setup occurs
    once per test module, not for every test function, improving test suite efficiency.

    This fixture utilises the 'with' statement to manage the lifecycle of the Testbook
    client, ensuring resources are properly managed and the notebook session is closed
    after the tests complete. The 'execute' parameter explicitly lists the cells to run
    upon fixture initialisation, targeting only those necessary for the test context and
    thus optimising the test setup process.

    Returns:
        An instance of the Testbook client preconfigured with the notebook environment,
        ready for interaction in test cases.

    Usage:
        The fixture is automatically applied to test functions within the same module
        that declare 'tb' as an argument. It abstracts the notebook setup process,
        allowing test functions to focus on asserting behaviours and outcomes.

    Note:
        This fixture is designed for use in a testing suite focused on verifying the
        functionality and integrity of notebook-defined Python objects and their interactions.
        It is an integral part of a testing strategy that incorporates notebooks as first-class
        citizens in software development and testing practices.
    """
    with testbook('notebooks/calculator_nb.ipynb', execute=True) as tb_client:
        yield tb_client

@pytest.mark.parametrize("invalid_input", [
    "\"a string\"",
    "None",
    "[1, 2, 3]"
])
def test_calculator_invalid_initial_value(tb, invalid_input):
    """
    Tests Calculator initialisation with invalid inputs. The Calculator
    is expected to raise a ValueError when initialised with non-numeric
    inputs, ensuring robust input validation.
    
    Parameters:
        tb: The Testbook fixture for interacting with Jupyter notebooks.
        invalid_input: The input to test the Calculator with, expected to
                       be invalid for Calculator initialisation.
    """
    code = f"""
    try:
        calc = Calculator({invalid_input})
        print('Test failed: ValueError was expected but not raised.')
    except ValueError:
        print('ValueError raised successfully.')
    """
    tb.inject(code)
    output = tb.cell_output_text(-1)
    assert "ValueError raised successfully." in output, "Calculator should raise ValueError for invalid initial value"

@pytest.mark.parametrize("invalid_add_value", [
    "\"a string\"",
    "None",
    "[1, 2, 3]"
])
def test_calculator_add_invalid_input(tb, invalid_add_value):
    """
    Tests the add method of the Calculator with invalid inputs. Validates
    that the method raises a ValueError when attempting to add non-numeric
    values, preserving the integrity of the calculator's state.
    
    Parameters:
        tb: The Testbook fixture for interacting with Jupyter notebooks.
        invalid_add_value: The value to test the add method with, expected
                           to be invalid for the addition operation.
    """
    code = f"""
    try:
        calc = Calculator(10)
        calc.add({invalid_add_value})
        print('Test failed: ValueError was expected but not raised.')
    except ValueError:
        print('ValueError raised successfully for add operation.')
    """
    tb.inject(code)
    output = tb.cell_output_text(-1)
    assert "ValueError raised successfully for add operation." in output, "Calculator should raise ValueError for invalid add value"

@pytest.mark.parametrize("invalid_subtract_value", [
    "\"a string\"",
    "None",
    "[1, 2, 3]"
])
def test_calculator_subtract_invalid_input(tb, invalid_subtract_value):
    """
    Tests the subtract method of the Calculator with invalid inputs. This test
    ensures that attempting to subtract non-numeric values from the calculator's
    current value raises a ValueError, maintaining the calculator's accuracy.
    
    Parameters:
        tb: The Testbook fixture for interacting with Jupyter notebooks.
        invalid_subtract_value: The value to test the subtract method with,
                                expected to be invalid for the subtraction operation.
    """
    code = f"""
    try:
        calc = Calculator(10)
        calc.subtract({invalid_subtract_value})
        print('Test failed: ValueError was expected but not raised.')
    except ValueError:
        print('ValueError raised successfully for subtract operation.')
    """
    tb.inject(code)
    output = tb.cell_output_text(-1)
    assert "ValueError raised successfully for subtract operation." in output, "Calculator should raise ValueError for invalid subtract value"

@pytest.mark.parametrize("initial_value, add_value, subtract_value, expected_result", [
    (10, 5, 3, 12),
    (0, -2, -3, 1),
    (-5, 10, 5, 0)
])
def test_calculator_valid_operations(tb, initial_value, add_value, subtract_value, expected_result):
    """
    Tests valid operations on the Calculator, including initialisation, addition,
    and subtraction. This comprehensive test verifies the Calculator's basic arithmetic
    functionality works as expected with valid numeric inputs.

    Parameters:
        tb: The Testbook fixture for interacting with Jupyter notebooks.
        initial_value: The initial value to initialise the Calculator with.
        add_value: The numeric value to add to the Calculator's current value.
        subtract_value: The numeric value to subtract from the Calculator's current value.
        expected_result: The expected result after performing the addition and
                         subtraction operations.
    """
    code = f"""
    calc = Calculator({initial_value})
    calc.add({add_value})
    calc.subtract({subtract_value})
    assert calc.val == {expected_result}, 'Expected {expected_result}, got ' + str(calc.val)
    print('Valid operations passed.')
    """
    tb.inject(code)
    output = tb.cell_output_text(-1)
    assert "Valid operations passed." in output, f"Expected final result to be {expected_result}"
