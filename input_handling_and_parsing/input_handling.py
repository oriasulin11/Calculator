from validation_unit.exceptions import EmptyExpressionException


class InputHandler:
    """
    This class will take input from user
    """
    def __init__(self):
        self._input = ""

    def take_input(self):
        raw_input = input("\nEnter Arithmetic Expression To Evaluate, Enter exit to stop\n")
        if raw_input == "exit":
            exit()
        self._input = raw_input

    def get_input(self):
        return self._input


class StringProcessor:
    """
    This class converts a string of raw input from user,
    to a list where each element is a character
    """
    @staticmethod
    def string_process(raw_string: str) -> list:
        if len(raw_string) == 0:
            raise EmptyExpressionException()
        return [char for char in raw_string if char != ' ']
