from math_functions import Number
from logic_unit import OPERATORS_DIC

class InfixCalc:
    """
    This class will handle initial calculations
    regarding ~ and unary -
    """
    @staticmethod
    def eval_expression(user_input: list) ->list:
        found_operator = False
        exceptions = []
        prev_char = None
        minus_count = 0
        processed_input = []
        for index , char in enumerate(user_input):
            if char in ('(', ')'):
                processed_input.append(char)
            elif isinstance(char, Number):
                if minus_count % 2 ==0:
                    processed_input.append(Number(char.get_value()))
                else:
                    processed_input.append(Number(-char.get_value()))
                minus_count = 0
            else:
                if char == '-':
                    if isinstance(prev_char, Number):
                        processed_input.append(char)
                    elif found_operator:
                        minus_count += 1
                    elif index != len(user_input)-1:
                        if isinstance(user_input[index +1], Number) or user_input[index+1] in ('(', '-u'):
                            processed_input.append('-u')
                else:
                    processed_input.append(char)
                found_operator = True
            prev_char = char
        return processed_input


pro = InfixCalc.eval_expression(['~', '-','-',Number(3),'!'])
for char in pro:
    print(char if isinstance(char,str) else char.get_value())




