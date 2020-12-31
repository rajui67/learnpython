def subtract_divide(dividend, first_number, second_number):
    """This function divides dividend with the result derived by subtracting second_number from first_number

    Input Arguments: dividend, first_number, second_number must be numbers.
    Returns: quotient.
    """

    try:
        quotient = first_number - second_number
        return dividend / quotient
    # except ZeroDivisionError:
    #     raise ZeroDivisionError
    except ZeroDivisionError:
        return f"this won't work, {first_number} - {second_number} is 0 or lower."

