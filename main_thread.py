from exceptions import MissingOperandException, MissingOperatorException
from infix_calculations import InfixCalc
from input_handling import InputHandler, StringProcessor
from postfix_conversion import PostFixConvertor
from parse import NumberParser
from postfix_evaluation import PostfixEvaluation


class MainThread:
    def start_program(self):
        while(True):
            try:
                input_handler = InputHandler()
                input_handler.take_input()
                proc = StringProcessor.string_process(input_handler.get_input())
                proc = NumberParser.parse_expression(proc)
                proc = InfixCalc.eval_expression(proc)
                proc = PostFixConvertor.convert(proc)
                proc = PostfixEvaluation.evaluate_postfix(proc)
                print(proc.get_value())
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