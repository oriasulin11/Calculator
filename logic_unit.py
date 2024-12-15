from math_functions import Number, Plus, Operator, Minus, Multiplication, Division, MaxOperator, Modulo, \
    AverageOperator, UnaryNegation, Factorial

PRECEDENCE_DIC = {'+':1, '-':1, '*':2, '/':2, '-u' :2.5, '^':3, '%':4, '$':5, '&':5, '@':5 , '~':6, '!':6}
UNARY_OPERATORS = ['-u', '~', '!']
OPERATORS_DIC = {'+':Plus(), '-':Minus(), '-u':Minus(), '*':Multiplication(), '/':Division(), '$':MaxOperator(), '%':Modulo(), '@':AverageOperator(), '~':UnaryNegation(), '!':Factorial()}
class UnaryChecker:
    @staticmethod
    def is_unary(char : Operator, prev = None)->bool:
        return (char.get_symbol() in UNARY_OPERATORS and(
                prev is None or
                prev in PRECEDENCE_DIC or
                prev == '('))
class PostFixConvertor:


    @staticmethod
    def convert(infix_expression : list) -> list:
        operator_stack = []
        postfix_expression = []
        prev_char = None
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
                if UnaryChecker.is_unary(char,prev_char):
                    operator_stack.append(char)
                else:
                    while (operator_stack and
                           operator_stack != '(' and
                           PRECEDENCE_DIC[operator_stack[-1]] >= PRECEDENCE_DIC[char]):
                        postfix_expression.append(operator_stack.pop())
                    operator_stack.append(char)
            prev_char = char
            # Pop remaining operators
        while operator_stack:
            postfix_expression.append(operator_stack.pop())
        return postfix_expression




PostFixConvertor.convert(['~', '-','-',Number(3),'!'])

