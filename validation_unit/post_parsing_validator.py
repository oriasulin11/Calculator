from validation_unit.exceptions import InvalidCharAfterTildaException, PostParseException
from calculation_unit.math_functions import Number


class AfterTildaValidation:
    """
    This class will validate that
    after tilda there is a valid expression
    """

    @staticmethod
    def after_tilda_validation(parsed_input: list):
        """
        This function validates that after every tilda
        comes either a Number a sign '-' or a '('
        """
        for index, char in enumerate(parsed_input):
            if char == '~' and not (isinstance(parsed_input[index + 1], Number) or parsed_input[index + 1] == '('
                                    or parsed_input[index + 1] == '-s'):
                raise InvalidCharAfterTildaException(parsed_input[index + 1])


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
