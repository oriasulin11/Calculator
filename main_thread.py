

from infix_calculations import InfixCalc
from input_handling import InputHandler, StringProcessor
from logic_unit import PostFixConvertor
from parse import NumberParser
from postfix_evaluation import PostfixEvaluation


class MainThread:
    def start_program(self):
        while(True):
            input_handler = InputHandler()
            input_handler.take_input()
            proc = StringProcessor.string_process(input_handler.get_input())
            proc = NumberParser.parse_expression(proc)
            proc = InfixCalc.eval_expression(proc)
            proc = PostFixConvertor.convert(proc)
            proc = PostfixEvaluation.evaluate_postfix(proc)
            print(proc.get_value())




thread = MainThread()
thread.start_program()