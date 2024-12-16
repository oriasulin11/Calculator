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
        return f"Missing operand expected: {self._expected} received {self._received}"

class MissingOperatorException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Missing operator"
