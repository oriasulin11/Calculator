from exceptions import MissingOperandException, IllegalUnaryMinusException, IllegalSignMinusException
from math_functions import Number
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
        processed_input = []
        for index, char in enumerate(user_input):
            if char in ('(', ')'):
                processed_input.append(char)
            elif isinstance(char, Number):
                processed_input.append(Number(char.get_value()))
                found_operator = False
            else:
                if char == '-':
                    if isinstance(prev_char, Number) or prev_char in POSTFIX_OPERATORS or prev_char == ')':
                        processed_input.append(char)
                    elif found_operator and processed_input[-1] != '-u':
                        # Check if sign minus is legal
                        check_sign_index = index + 1
                        while user_input[check_sign_index] == '-':
                            check_sign_index += 1
                        if isinstance(user_input[check_sign_index], Number) or user_input[check_sign_index] == '(':
                            processed_input.append('-s')
                        else:
                            raise IllegalSignMinusException(index)
                    # Minus is not binary and not sign
                    else:
                        check_unary_index = index+1
                        # Check if the unary minus is valid
                        while user_input[check_unary_index] == '-':
                            check_unary_index += 1
                        if isinstance(user_input[check_unary_index], Number) or user_input[check_unary_index] == '(':
                            processed_input.append('-u')
                        else:
                            raise IllegalUnaryMinusException(index)
                else:
                    processed_input.append(char)
                if char in BINARY_OPERATORS or char in PREFIX_OPERATORS:
                    found_operator = True
            prev_char = char
        if len(processed_input) == 0:
            raise MissingOperandException(1, 0)
        return processed_input



