from exceptions import MissingOperandException, MissingOperatorException, SyntaxException, EmptyExpressionException, \
    InvalidOperandException, PostParseException, IllegalUnaryMinusException, IllegalSignMinusException
from infix_calculations import InfixCalc
from input_handling import InputHandler, StringProcessor
from post_parsing_validator import PostParsingValidator
from postfix_conversion import PostFixConvertor
from parse import NumberParser
from postfix_evaluation import PostfixEvaluation
from syntax_validator import SyntaxValidator


class MainThread:
    @staticmethod
    def start_program():
        while True:
            # Taking input from user
            try:
                input_handler = InputHandler()
                input_handler.take_input()
                result = MainThread.evaluate(input_handler.get_input())
                if result is not None:
                    print(result)

            except KeyboardInterrupt:
                print("Forced stop")
            except EmptyExpressionException as e:
                print(e)
            except SyntaxException as e:
                print(e)
            except MissingOperandException as e:
                print(e)
            except MissingOperatorException as e:
                print(e)
            except InvalidOperandException as e:
                print(e)
            except ValueError as e:
                print(e)
            except ZeroDivisionError as e:
                print(e)
            except OverflowError as e:
                print(e)
            except PostParseException as e:
                print(e)
            except IllegalUnaryMinusException as e:
                print(e)
            except IllegalSignMinusException as e:
                print(e)
            except EOFError:
                print("Nice try, almost got me")

    @staticmethod
    def evaluate(user_input: str):
        # process input to a list of chars
        initial_input = StringProcessor.string_process(user_input)

        validator = SyntaxValidator(initial_input)
        # validate user input
        validator.validate()
        # Parse Numbers to objects
        parsed_input = NumberParser.parse_expression(initial_input)

        # Evaluate unary and sign minuses in infix form
        infix_evaluated_expression = InfixCalc.eval_expression(parsed_input)
        # post parse validation
        post_parse_validator = PostParsingValidator(infix_evaluated_expression)
        post_parse_validator.validate()
        # Convert infix to postfix expression
        postfix_expression = PostFixConvertor.convert(infix_evaluated_expression)
        # Evaluate the result
        result = PostfixEvaluation.evaluate_postfix(postfix_expression)
        return result.get_value()


if __name__ == "__main__":
    MainThread.start_program()
