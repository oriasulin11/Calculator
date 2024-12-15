from infix_calculations import InfixCalc
from math_functions import Number


def test_infix_calc():
    proc = InfixCalc.eval_expression([Number(3), '+', '~', '-', Number(3)])