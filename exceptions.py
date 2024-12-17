class MissingOperandException(Exception):
    """
    Exception raised when evaluating expression
    with missing operand
    """

    def __init__(self, expected, received):
        """
        getting how many operands are expected for the
        operation and how many where given
        """
        self._expected = expected
        self._received = received

    def __str__(self):
        return f"Missing operand, expected {self._expected} received {self._received}"


class MissingOperatorException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Missing operator"


class EmptyExpressionException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Cant preform calculation on empty expression"


class IllegalCharsException(Exception):
    def __init__(self, chars: list):
        super().__init__(chars)
        self._chars = chars

    def __str__(self):
        return f" Found illegal characters: {str(self._chars)}"


class MismatchingParenthesesException:
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "This Expression contains mismatching parentheses"


class ImbalancedParentheses:
    def __init__(self, balance):
        super().__init__()
        self._balance = balance

    def __str__(self):
        if self._balance > 0:
            return f"Missing {self._balance} closing parentheses"
        else:
            return f"Missing {self._balance} opening parentheses"


class SyntaxException(Exception):
    def __init__(self, exceptions: list):
        super().__init__(exceptions)
        self._exceptions = exceptions

    def __str__(self):
        exception_str = ""
        for exception in self._exceptions:
            exception_str += str(exception)
        return exception_str
