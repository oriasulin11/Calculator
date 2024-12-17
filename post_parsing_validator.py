from exceptions import InvalidCharAfterTildaException, PostParseException
from math_functions import PREFIX_OPERATORS, Number


class AfterTildaValidation:
    """
    This class will validate that
    after tilda there is a valid expression
    """

    @staticmethod
    def after_tilda_validation(parsed_input: list):
        for index, char in enumerate(parsed_input):
            if char == '~' and not (isinstance(parsed_input[index + 1], Number) or parsed_input[index + 1] == '('
                                    or parsed_input[index + 1] == '-s'):
                raise InvalidCharAfterTildaException(parsed_input[index + 1])


class InvalidCharAdjacentToOperatorValidator:
    @staticmethod
    def invalid_char_pre_operator(user_input):
        prev_char = None
        for index, char in enumerate(user_input):
            if char in PREFIX_OPERATORS and prev_char is not None:
                if not isinstance(prev_char, Number):
                    pass


class PostParsingValidator:
    """
    This class is a validator
    after the parsing process
    """

    def __init__(self, parsed_input):
        self._parsed_input = parsed_input

    def validate(self):
        try:
            AfterTildaValidation.after_tilda_validation(self._parsed_input)
        except InvalidCharAfterTildaException as e:
            raise PostParseException(e)

