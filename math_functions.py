from abc import ABC, abstractmethod

class Number:
    """
    An instance of this class represent a number,
    note that this class is immutable...
    once a number is generated its value can not be changed
    """
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

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
    SYMBOL = '+'
    def evaluate(self, first_operand: Number, second_operand : Number = None):
        return first_operand.get_value() + second_operand.get_value()
    def get_symbol(self):
        return self.SYMBOL
