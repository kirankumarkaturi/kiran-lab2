from app.calculator import safe_divide


def test_safe_divide_normal_case() -> None:
    assert safe_divide(10, 2) == 5


def test_safe_divide_zero_division() -> None:
    assert safe_divide(10, 0) is None