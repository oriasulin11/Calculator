from exceptions import MissingOperandException, MissingOperatorException, SyntaxException
from infix_calculations import InfixCalc
from input_handling import InputHandler, StringProcessor
from postfix_conversion import PostFixConvertor
from parse import NumberParser
from postfix_evaluation import PostfixEvaluation
from syntax_validator import SyntaxValidator


class MainThread:
    def start_program(self):
        while True:
            try:
                # Taking input from user
                input_handler = InputHandler()

                input_handler.take_input()
                # process input to a list of chars
                initial_input = StringProcessor.string_process(input_handler.get_input())

                validator = SyntaxValidator(initial_input)
                # validate user input
                validator.validate()
                # Parse Numbers to objects
                parsed_input = NumberParser.parse_expression(initial_input)
                # Evaluate unary and sign minuses in infix form
                infix_evaluated_expression = InfixCalc.eval_expression(parsed_input)
                # Convert infix to postfix expression
                postfix_expression = PostFixConvertor.convert(infix_evaluated_expression)
                # Evaluate the result
                result = PostfixEvaluation.evaluate_postfix(postfix_expression)
                print(result.get_value())
            except SyntaxException as e:
                print(e)
            except MissingOperandException as e:
                print(e)
            except MissingOperatorException as e:
                print(e)
            except ValueError as e:
                print(e)
            except ZeroDivisionError as e:
                print(e)





thread = MainThread()
thread.start_program()