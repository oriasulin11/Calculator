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


class StartOfExpressionException(Exception):
    """
    This exception will be raised when an expression
    starts with invalid character
    """
    def __init__(self, char: str):
        super().__init__()
        self._invalid_char = char

    def __str__(self):
        return f"Cant start an expression with {self._invalid_char}"


class EndOfExpressionException(Exception):
    """
    This exception will be raised when an expression
    ends with invalid character
    """
    def __init__(self, char: str):
        super().__init__()
        self._invalid_char = char

    def __str__(self):
        return f"Cant end an expression with {self._invalid_char}"


class InvalidOperandException(Exception):
    def __init__(self, invalid_operand: str):
        super().__init__()
        self._invalid_operand = invalid_operand

    def __str__(self):
        return f"Found invalid operand: {self._invalid_operand}"


class InvalidCharAfterTildaException(Exception):
    def __init__(self, invalid_char):
        super().__init__()
        self._invalid_char = invalid_char

    def __str__(self):
        return f"The character {self._invalid_char} is not legal after ~"


class PostParseException(Exception):
    def __init__(self, exception):
        self._exception = exception

    def __str__(self):
        return str(self._exception)


class IllegalUnaryMinusException(Exception):
    """
    This exception will be raised when
    an illegal unary minus occurs
    """
    def __init__(self, index):
        super().__init__()
        self._index = index

    def __str__(self):
        return f"The unary '-' in index {self._index} is illegal"


class IllegalSignMinusException(Exception):
    """
    This exception will be raised when
    an illegal unary minus occurs
    """
    def __init__(self, index):
        super().__init__()
        self._index = index

    def __str__(self):
        return f"The sign '-' in index {self._index} is illegal"


class SyntaxException(Exception):
    def __init__(self, exceptions: list):
        super().__init__()
        self._exceptions = exceptions

    def __str__(self):
        exception_str = ""
        for exception in self._exceptions:
            exception_str += str(exception) + '\n'
        return exception_str
