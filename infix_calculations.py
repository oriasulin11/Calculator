from constants import POSTFIX_OPERATORS, BINARY_OPERATORS, PREFIX_OPERATORS
from exceptions import MissingOperandException, IllegalUnaryMinusException, IllegalSignMinusException
from math_functions import Number


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
        # Iterating over the characters in the input
        for index, char in enumerate(user_input):
            # No spacial handling for parentheses
            if char == '(':
                found_operator = False
                processed_input.append(char)
            elif char == ')':
                processed_input.append(char)
            elif isinstance(char, Number):
                processed_input.append(char)
                # Reset the flag of found operator
                found_operator = False
            else:
                # Handle '-'
                if char == '-':
                    # Check for binary minus
                    if isinstance(prev_char, Number) or prev_char in POSTFIX_OPERATORS or prev_char == ')':
                        processed_input.append(char)
                    # Handel sign minus
                    elif found_operator and processed_input[-1] != '-u':
                        # Check if sign minus is legal
                        check_sign_index = index + 1
                        while user_input[check_sign_index] == '-':
                            check_sign_index += 1
                        if isinstance(user_input[check_sign_index], Number) or user_input[check_sign_index] == '(':
                            processed_input.append('-s')
                        else:
                            raise IllegalSignMinusException(index)
                    # Handle unary minus
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



