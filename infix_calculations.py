from math_functions import Number
from postfix_conversion import OPERATORS_DIC
from math_functions import BINARY_OPERATORS, PREFIX_OPERATORS, POSTFIX_OPERATORS


class InfixCalc:
    """
    This class will handle initial calculations
    regarding ~ and unary -
    """

    @staticmethod
    def eval_expression(user_input: list) -> list:
        found_operator = False

        prev_char = None
        minus_count = 0
        processed_input = []
        for index, char in enumerate(user_input):
            if char in ('(', ')'):
                processed_input.append(char)
            elif isinstance(char, Number):
                if minus_count % 2 == 0:
                    processed_input.append(Number(char.get_value()))
                else:
                    processed_input.append(Number(-char.get_value()))
                minus_count = 0
                found_operator = False
            else:
                if char == '-':
                    if isinstance(prev_char, Number) or prev_char in POSTFIX_OPERATORS:
                        processed_input.append(char)
                    elif found_operator:
                        minus_count += 1
                    elif index != len(user_input) - 1:
                        if isinstance(user_input[index + 1], Number) or user_input[index + 1] in ('(', '-u'):
                            processed_input.append('-u')
                else:
                    processed_input.append(char)
                if char in BINARY_OPERATORS or char in PREFIX_OPERATORS:
                    found_operator = True
            prev_char = char
        return processed_input



