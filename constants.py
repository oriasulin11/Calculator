PRECEDENCE_DIC = {'+': 1, '-': 1, '*': 2, '/': 2, '-u': 2.5, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6,
                  '#': 6, '-s': 7}
BINARY_OPERATORS = ['+', '-', '*', '/', '^', '@', '%', '$', '&']
PREFIX_OPERATORS = ['-u', '~', '-s']
POSTFIX_OPERATORS = ['!', '#', '#']
UNARY_OPERATORS = ['-u', '~', '!', '-s', '#']
DIGITS = list("1234567890")