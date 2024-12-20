import pytest

from exceptions import IllegalUnaryMinusException, IllegalSignMinusException, SyntaxException, \
    EmptyExpressionException,  PostParseException

from main_thread import MainThread


def test_basic_functionality_of_operators():
    """
    Test for basic functionality of operators
    """
    assert MainThread.evaluate("1+5") == 6
    assert MainThread.evaluate("1-5") == -4
    assert MainThread.evaluate("2*5") == 10
    assert MainThread.evaluate("10/2") == 5
    assert MainThread.evaluate("2^3") == 8
    assert MainThread.evaluate("10%8") == 2
    assert MainThread.evaluate("2@4") == 3
    assert MainThread.evaluate("1&5") == 1
    assert MainThread.evaluate("1$5") == 5
    assert MainThread.evaluate("~13") == -13
    assert MainThread.evaluate("5!") == 120
    assert MainThread.evaluate("15#") == 6


def test_for_precedence_functionality():
    """
    Test if the calculator can evaluate expressions
    With complex precedence
    """
    assert MainThread.evaluate("~((2+5)--3^2&11$12)#") == 20
    assert MainThread.evaluate("23#+3!-~4") == 15
    assert MainThread.evaluate("-5 % 2") == -1
    assert MainThread.evaluate("5*7&1!") == 5


def test_for_valid_binary_unary_and_sign_minus():
    """
    Test functionality and behavior of unary
    binary and sign minuses combinations
    """
    assert MainThread.evaluate("3+~-3") == 6
    assert MainThread.evaluate("~-3!") == 6
    assert MainThread.evaluate("-3!") == -6
    assert MainThread.evaluate("--3!") == 6
    assert MainThread.evaluate("2---3!") == -4
    assert MainThread.evaluate("2+--3!") == 8
    assert MainThread.evaluate("3+~-3") == 6
    assert MainThread.evaluate("3--(3-5)!") == 1


def test_for_invalid_unary_minus():
    """
    After any operator may come a sequence of '-'
    those will count as sign minuses as long as they are
    before a number or open parentheses
    """
    with pytest.raises(IllegalUnaryMinusException):
        MainThread.evaluate("--~--3")
        MainThread.evaluate("~--~-3")
        MainThread.evaluate("-(--~3!+1)")


def test_for_invalid_sign_minus():
    """
    Unary minus can only come before a number,
    open parentheses or another unary minus
    """
    with pytest.raises(IllegalSignMinusException):
        MainThread.evaluate("2---~3")
        MainThread.evaluate("2--~2")
        MainThread.evaluate("(2--(3--~2))")


def test_invalid_parentheses_errors():
    """
    Test for invalid syntax regarding parentheses
    """
    with pytest.raises(SyntaxException):
        MainThread.evaluate(")3+1")
        MainThread.evaluate("3+1(")
        MainThread.evaluate(")3+1(")
        MainThread.evaluate("(3+1))")
        MainThread.evaluate("((3+1)")
        MainThread.evaluate("(((22+1)*3)+1))")


def test_for_illegal_chars_errors():
    """
    In my amazing calculator the only characters
    allowed are digits operators '.' and '()'.
    """
    with pytest.raises(SyntaxException):
        MainThread.evaluate("a+b")
        MainThread.evaluate("omega > sigit")
        MainThread.evaluate("\tyh")
        MainThread.evaluate("\n1+34")
        MainThread.evaluate("\01+34")
        MainThread.evaluate("\r+34")
        MainThread.evaluate("\b+34")
        MainThread.evaluate("\00010+34")


def test_for_empty_expression():
    with pytest.raises(EmptyExpressionException):
        MainThread.evaluate("")
        MainThread.evaluate("     \n")
        MainThread.evaluate("\n")
        MainThread.evaluate("\r")
        MainThread.evaluate("\b")


def test_for_spacial_characters():
    """
    Test if the calculator can handle
    spacial characters(non UTF-8)
    """
    with pytest.raises(SyntaxException):
        MainThread.evaluate("1+™2")
        MainThread.evaluate("1+名字2")
        MainThread.evaluate("20°+1")
        MainThread.evaluate("1+€100")


def test_for_illegal_start():
    with pytest.raises(SyntaxException):
        MainThread.evaluate("!3+1")
        MainThread.evaluate("+1")
        MainThread.evaluate(")+1")
        MainThread.evaluate("#1+2")


def test_for_illegal_end():
    with pytest.raises(SyntaxException):
        MainThread.evaluate("3+1~")
        MainThread.evaluate("1+(")
        MainThread.evaluate("1+1-")
        MainThread.evaluate("1+2--")


def test_for_illegal_chars_after_tilda():
    """
    After the beloved tilda there can only be
    '-' sequence, a number or a '('
    """
    with pytest.raises(PostParseException):
        MainThread.evaluate("~~3")
        MainThread.evaluate("~+3")
        MainThread.evaluate("--~(~~3)")
        MainThread.evaluate("~(~--~3)")
        MainThread.evaluate("~--~3)")


def test_for_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        MainThread.evaluate("0/0")
        MainThread.evaluate("5/0")
        MainThread.evaluate("5%0")
        MainThread.evaluate("0%0")
        MainThread.evaluate("2/1000000000000000000*100000000000000")
        MainThread.evaluate("2%1000000000000000000*100000000000000")



