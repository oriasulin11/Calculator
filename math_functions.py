import math
from abc import ABC, abstractmethod

PRECEDENCE_DIC = {'+':1, '-':1, '*':2, '/':2, '-u' :2.5, '^':3, '%':4, '$':5, '&':5, '@':5 , '~':6, '!':6}

BINARY_OPERATORS = {'+','-','*','/','^','@','%','$','&'}
PREFIX_OPERATORS = {'-u','~'}
POSTFIX_OPERATORS = {'!','#'}
UNARY_OPERATORS = ['-u', '~', '!']

class Number:
    """
    An instance of this class represent a number
    """
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def set_value(self, new_value):
        self._value = new_value

    def get_value(self):
        return self._value
class Operator(ABC):
    """
    This abstract class represents an operator,
    each operator has its unique symbol and evaluation with
    either one or two operands.
    """
    def get_symbol(self):
        ...
    @abstractmethod
    def evaluate(self,first_operand :  Number, second_operand : Number = None) -> Number:
        ...

class Plus(Operator):
    """
    Binary addition.
    Adding two numbers
    """
    SYMBOL = '+'
    def evaluate(self, first_operand: Number, second_operand : Number = None) -> Number:
        if second_operand is None:
            raise ValueError("Addition requires two operands")
        return Number(first_operand.get_value() + second_operand.get_value())
    def get_symbol(self):
        return self.SYMBOL


class Minus(Operator):
    """
    Binary and unary subtraction operator.
    Supports both two-operand subtraction (a - b) and
    single-operand negation (-a) scenarios.
    """
    SYMBOL = '-'

    def evaluate(self, first_operand: Number, second_operand: Number = None) -> Number:
        # If only one operand is provided, perform unary negation
        if second_operand is None:
            return Number(-first_operand.get_value())

        # If two operands are provided, perform subtraction
        return Number(first_operand.get_value() - second_operand.get_value())

    def get_symbol(self):
        return self.SYMBOL


class Multiplication(Operator):
    """
    Binary multiplication operator.
    Multiplies two operands.
    """
    SYMBOL = '*'

    def evaluate(self, first_operand: Number, second_operand: Number = None) -> Number:
        if second_operand is None:
            raise ValueError("Multiplication requires two operands")
        return Number(first_operand.get_value() * second_operand.get_value())

    def get_symbol(self):
        return self.SYMBOL


class Factorial(Operator):
    """
    Unary factorial operator.
    Calculates the factorial of a non-negative integer.
    """
    SYMBOL = '!'

    def evaluate(self, first_operand: Number, second_operand: Number = None) -> Number:
        if second_operand is not None:
            raise ValueError("Factorial is a unary operator")

        value = first_operand.get_value()
        if int(value) != float(value):
            raise ValueError("Factorial is not defined for non-integer numbers")
        if value < 0:
            raise ValueError("Factorial is not defined for negative numbers")

        elif value > 100:
            raise ValueError("Cant preform factorial operation on numbers grater than 100")

        # Factorial calculation
        result = 1
        for i in range(1, int(value) + 1):
            result *= i

        return Number(result)

    def get_symbol(self):
        return self.SYMBOL


class Division(Operator):
    """
    Binary division operator.
    Divides first operand by second operand.
    Handles division by zero error.
    """
    SYMBOL = '/'

    def evaluate(self, first_operand: Number, second_operand: Number = None) -> Number:
        if second_operand is None:
            raise ValueError("Division requires two operands")

        denominator = second_operand.get_value()
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        return Number(first_operand.get_value() / denominator)

    def get_symbol(self):
        return self.SYMBOL


class MaxOperator(Operator):
    """
    Binary max operator (represented by $).
    Returns the maximum of two operands.
    """
    SYMBOL = '$'

    def evaluate(self, first_operand: Number, second_operand: Number = None) -> Number:
        if second_operand is None:
            raise ValueError("Max operator requires two operands")

        return Number(max(first_operand.get_value(), second_operand.get_value()))

    def get_symbol(self):
        return self.SYMBOL


class Modulo(Operator):
    """
    Binary modulo operator.
    Calculates the remainder of division.
    Handles division by zero.
    """
    SYMBOL = '%'

    def evaluate(self, first_operand: Number, second_operand: Number = None) -> Number:
        if second_operand is None:
            raise ValueError("Modulo requires two operands")

        denominator = second_operand.get_value()
        if denominator == 0:
            raise ZeroDivisionError("Cannot calculate modulo with zero")

        return Number(first_operand.get_value() % denominator)

    def get_symbol(self):
        return self.SYMBOL


class Power(Operator):
    """
    Binary power operator.
    Raises first operand to the power of second operand.
    """
    SYMBOL = '^'

    def evaluate(self, first_operand: Number, second_operand: Number = None) -> Number:
        if second_operand is None:
            raise ValueError("Power operator requires two operands")

        return Number(math.pow(first_operand.get_value(),second_operand.get_value()))

    def get_symbol(self):
        return self.SYMBOL


class AverageOperator(Operator):
    """
    Binary average operator (represented by @).
    Calculates the average of two operands.
    """
    SYMBOL = '@'

    def evaluate(self, first_operand: Number, second_operand: Number = None) -> Number:
        if second_operand is None:
            raise ValueError("Average operator requires two operands")

        return Number((first_operand.get_value() + second_operand.get_value()) / 2)

    def get_symbol(self):
        return self.SYMBOL


class UnaryNegation(Operator):
    """
    Unary negation operator (represented by ~).
    Changes the sign of the operand.
    """
    SYMBOL = '~'

    def evaluate(self, first_operand: Number, second_operand: Number = None) -> Number:
        if second_operand is not None:
            raise ValueError("Unary negation is a single-operand operator")

        return Number(-first_operand.get_value())

    def get_symbol(self):
        return self.SYMBOL


