import pytest
from rpn import to_rpn, evaluate_rpn, calculate

def test_manual_example():
    expr = "3 + 4 * 2 / (1 - 5) ^ 2"
    rpn_tokens = to_rpn(expr)
    assert " ".join(rpn_tokens) == "3 4 2 * 1 5 - 2 ^ / +"
    assert evaluate_rpn(rpn_tokens) == 3.5



def test_multi_digit_and_floats():
    rpn_str, res = calculate("12 + 3.5 * (4 - 2)")
    assert rpn_str == "12 3.5 4 2 - * +"
    assert res == 19.0



def test_nested_parentheses_and_power():
    rpn_str, res = calculate("((2 + 3) * 2) ^ 2 / 5")
    assert rpn_str == "2 3 + 2 * 2 ^ 5 /"
    assert res == 20.0



def test_unary_minus():
    _, res = calculate("-5 + 3 * (-2 + 4)")
    assert res == 1.0



def test_mismatched_parentheses():
    with pytest.raises(ValueError):
        calculate("(3 + 4 * 2")
    with pytest.raises(ValueError):
        calculate("3 + 4) * 2")



def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("10 / (5 - 5)")