def safe_divide(a: float, b: float) -> float | None:
    """
    Safely divides two numbers, returning None if the denominator is zero.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float | None: The result of the division, or None if the denominator is zero.
    """
    if b == 0:
        return None
    return a / b