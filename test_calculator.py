import pytest

from exceptions import IllegalUnaryMinusException, IllegalSignMinusException, SyntaxException
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


def test_for_invalid_unary_minus():
    with pytest.raises(IllegalUnaryMinusException):
        MainThread.evaluate("--~--3")
        MainThread.evaluate("~--~-3")
        MainThread.evaluate("-(--~3!+1)")


def test_for_invalid_sign_minus():
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
        MainThread.evaluate("3+1~")
        MainThread.evaluate(")3+1(")
        MainThread.evaluate("(3+1))")
        MainThread.evaluate("((3+1)")
        MainThread.evaluate("a+b")
        MainThread.evaluate("4+b)")
        MainThread.evaluate("4+b)")
