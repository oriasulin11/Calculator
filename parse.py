from exceptions import InvalidOperandException
from math_functions import Number


class NumberParser:
    """
    This class will parse the numbers
    given by the user as input
    """

    @staticmethod
    def parse_number(number, is_decimal):
        try:
            operand = Number(float(number)) if is_decimal else Number(int(number))
        except ValueError as e:
            raise InvalidOperandException(number)
        return operand

    @staticmethod
    def parse_expression(user_input: list) -> list:
        """
        This function iterates over the input
        and parse numbers from strings to Number objs
        """
        parsed_expression = []
        number = ""
        is_decimal = False

        for char in user_input:

            if char.isdigit() or char == '.':
                number += char

                if char == '.':
                    is_decimal = True
                    # Operator or other character handling
            else:
                # Convert and add the current number if it exists
                if number:
                    parsed_expression.append(NumberParser.parse_number(number, is_decimal))
                    number = ""
                    is_decimal = False
                # Add non-numeric characters
                parsed_expression.append(char)

        # Handle the last number in the expression
        if number:
            parsed_expression.append(NumberParser.parse_number(number, is_decimal))
        return parsed_expression
