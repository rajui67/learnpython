def subtract_divide(dividend, x, y):
    """This function divides dividend with the result derived by subtracting y from x

    Input Arguments: dividend, x, y must be numbers.
    Returns: quotient.
    """

    try:
        z = x - y
        return dividend / z
    # except ZeroDivisionError:
    #     raise ZeroDivisionError
    except ZeroDivisionError:
        return f"this won't work, {x} - {y} is 0 or lower."