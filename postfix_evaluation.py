from exceptions import MissingOperandException, MissingOperatorException
from postfix_conversion import UNARY_OPERATORS, OPERATORS_DIC
from math_functions import Number


class PostfixEvaluation:
    @staticmethod
    def evaluate_postfix(postfix_expression):
        number_stack = []
        for char in postfix_expression:
            # push numbers to the stack
            if isinstance(char, Number):
                number_stack.append(char)
            elif char in UNARY_OPERATORS:
                if len(number_stack) < 1:
                    raise MissingOperandException(1, len(number_stack))
                operand1 = number_stack.pop()
                number_stack.append(OPERATORS_DIC[char].evaluate(operand1))
            # Is binary operator
            else:
                if len(number_stack) < 2:
                    raise MissingOperandException(2, len(number_stack))
                operand1 = number_stack.pop()
                operand2 = number_stack.pop()
                number_stack.append(OPERATORS_DIC[char].evaluate(operand2,operand1))
        if len(number_stack) > 1:
            raise MissingOperatorException()
        return number_stack[0]


