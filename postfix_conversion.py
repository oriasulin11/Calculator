from constants import PRECEDENCE_DIC, UNARY_OPERATORS, POSTFIX_OPERATORS, PREFIX_OPERATORS
from math_functions import Number, Plus, Minus, Multiplication, Division, MaxOperator, Modulo, \
    AverageOperator, UnaryNegation, Factorial, Power, DigitSummation, MinimumOperator

OPERATORS_DIC = {'+': Plus(), '-': Minus(), '-u': Minus(), '*': Multiplication(), '/': Division(), '^': Power(),
                 '$': MaxOperator(), '&': MinimumOperator(), '%': Modulo(), '@': AverageOperator(), '~': UnaryNegation(), '!': Factorial(),
                 '-s': Minus(), '#': DigitSummation()}


class PostFixConvertor:
    """
    This class Converts Parsed expression
    to postfix form
    """

    @staticmethod
    def convert(infix_expression: list) -> list:
        operator_stack = []
        postfix_expression = []
        for char in infix_expression:
            # Char is a number
            if isinstance(char, Number):
                postfix_expression.append(char)
            # Handling open parenthesis
            elif char == '(':
                operator_stack.append(char)
            # Handling close parenthesis
            elif char == ')':
                while operator_stack and operator_stack[-1] != '(':
                    postfix_expression.append(operator_stack.pop())
                # Removing open parenthesis
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
            # Char is an operator
            else:
                # Handling Unary operator
                if char in UNARY_OPERATORS:
                    if char not in POSTFIX_OPERATORS:
                        operator_stack.append(char)
                    else:
                        # Pop all the higher precedence PreFix operators from the stack
                        while (operator_stack and operator_stack[-1] in PREFIX_OPERATORS and operator_stack[-1] != '('
                                and operator_stack[-1] != ')' and
                               PRECEDENCE_DIC[operator_stack[-1]] >= PRECEDENCE_DIC[char]):
                            postfix_expression.append(operator_stack.pop())
                        postfix_expression.append(char)
                # Handling binary operators
                else:
                    # Pop all the higher precedence operators from the stack
                    while (operator_stack and
                           operator_stack[-1] != '(' and
                           operator_stack != '(' and
                           PRECEDENCE_DIC[operator_stack[-1]] >= PRECEDENCE_DIC[char]):
                        postfix_expression.append(operator_stack.pop())
                    operator_stack.append(char)
            # Pop remaining operators
        while operator_stack:
            postfix_expression.append(operator_stack.pop())
        return postfix_expression
