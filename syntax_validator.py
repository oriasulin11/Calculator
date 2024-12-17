from exceptions import IllegalCharsException, MismatchingParenthesesException, \
    ImbalancedParentheses, SyntaxException

class IllegalCharsValidator:
    """
    This class checks for illegal characters
    in the users input
    """
    LEGAL_CHARS = "1234567890.~!@$%^&*()-+/"

    @staticmethod
    def get_illegal_chars(user_input: list) -> list:
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
    def _is_matching_parentheses(user_input: list) -> bool:
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
    def get_parentheses_balance(user_input: list):
        """
        this function uses a variable - parentheses_balance
        to check if every '(' has a ')'
        """
        # not logical to check for parentheses balance for non-matching parentheses expressions
        if not MatchingParenthesesValidator._is_matching_parentheses(user_input):
            return None
        parentheses_balance = 0
        for char in user_input:
            if char == '(':
                parentheses_balance += 1
            elif char == ')':
                parentheses_balance -= 1
        return parentheses_balance


class SyntaxValidator:
    """
    This class will validate the processed input
    from the user.
    """
    def __init__(self, user_input: list):
        self._input = user_input
        # List of Exceptions found
        self._exceptions = []

    def validate(self):
        """
        this function checks the validity of the input
        and returns a list of exceptions which
        """
        illegal_chars = IllegalCharsValidator.get_illegal_chars(self._input)
        parentheses_balance = MatchingParenthesesValidator.get_parentheses_balance(self._input)

        if len(illegal_chars) > 0:
            self._exceptions.append(IllegalCharsException(illegal_chars))

        if parentheses_balance is None:
            self._exceptions.append(MismatchingParenthesesException())

        elif parentheses_balance != 0:
            self._exceptions.append(ImbalancedParentheses(parentheses_balance))

        self.handle_exceptions()

    def handle_exceptions(self):
        if self._exceptions:
            raise SyntaxException(self._exceptions)
