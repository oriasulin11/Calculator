from turtledemo.penrose import start


class InputHandler:
    """
    This class will take input from user
    """
    def __init__(self):
        self._input = ""

    def take_input(self):
        raw_input = input("\nEnter Arithmetic Expression To Evaluate\n")
        self._input = raw_input

    def get_input(self):
        return self._input

class StringProcessor:
    """
    This class converts a string of raw input from user,
    to a list where each element is a character
    """
    @staticmethod
    def string_process(raw_string : str)-> list:
        return [char for char in raw_string if char != ' ']

class IllegalCharsValidator:
    """
    This class checks for illegal characters
    in the users input
    """
    LEGAL_CHARS = "1234567890.~!@$%^&*()-+/"
    @staticmethod
    def get_illegal_chars(user_input : list)->list:
        """
        this function gets a list of characters and returns a list of illegal chars in the string
        """
        return [illegal_char for illegal_char in user_input if illegal_char not in IllegalCharsValidator.LEGAL_CHARS]

class MatchingParenthesesValidator:
    """
    This class validates that the given user input has
    matching parentheses.
    """
    @staticmethod
    def is_matching_parentheses(user_input : list) ->bool:
        """
        This function checks of mismatching parentheses
        in the given user input
        i.e : )3+5( ,in this instance the function will return false
        """
        parentheses_stack = []
        for char in user_input:
            if char == '(':
                parentheses_stack.append('(')
            elif char == ')':
                if not parentheses_stack:
                    return False
                parentheses_stack.pop()
        return True

    @staticmethod
    def get_parentheses_balance(user_input : list):
        """
        this function uses a variable - parentheses_balance
        to check if every '(' has a ')'
        """
        # not logical to check for parentheses balance for non-matching parentheses expressions
        if not MatchingParenthesesValidator.is_matching_parentheses(user_input):
            return None
        parentheses_balance = 0
        for char in user_input:
            if char == '(':
                parentheses_balance += 1
            elif char == ')':
                parentheses_balance -= 1
        return parentheses_balance

class InputValidator:
    """
    This class will validate the processed input
    from the user.
    """
    def __init__(self, user_input : list):
        self._input = user_input

    def validate(self):
        """
        this function checks the validity of the input
        and returns a list of exceptions which
        """
        exceptions = []
        illegal_chars = IllegalCharsValidator.get_illegal_chars(self._input)
        parentheses_balance = MatchingParenthesesValidator.get_parentheses_balance(self._input)

        if len(illegal_chars) > 0:
            exceptions.append(Exception(illegal_chars))# in the future will be custom exception

        if isinstance(parentheses_balance, str):#Mis
            exceptions.append(Exception(parentheses_balance))# in the future will be custom exception

            # There is parentheses inversion









inpt = InputHandler()
inpt.take_input()
print(StringProcessor.string_process(inpt.get_input()))





