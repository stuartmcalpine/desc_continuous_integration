import my_simple_functions.arithmetic as xx

def test_add():
    a = 4
    b = 8

    ans = 12

    assert xx.add(a, b) == ans
