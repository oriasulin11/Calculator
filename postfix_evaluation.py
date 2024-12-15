from logic_unit import UNARY_OPERATORS, OPERATORS_DIC
from math_functions import Number


class PostfixEvaluation:

    def evaluate_postfix(self, postfix_expression):
        number_stack = []
        for char in postfix_expression:
            # push numbers to the stack
            if isinstance(char, Number):
                number_stack.append(char)
            elif char in UNARY_OPERATORS:
                operand1 = number_stack.pop()
                number_stack.append(Number(OPERATORS_DIC[char].evaluate(operand1)))
            # Is binary operator
            else:
                operand1 = number_stack.pop()
                operand2 = number_stack.pop()
                number_stack.append(Number(OPERATORS_DIC[char].evaluate(operand1,operand2)))
        return number_stack[0]


