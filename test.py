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





