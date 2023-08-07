""" ! 5! = 1 * 2 * 3 * 4 * 5. """

def factorial(number: int) -> int:
    """
    factorial
    number : int
    return
    """

    if isinstance(number, int):
        if number <= 0:
            raise ValueError('Error: non work interval')
        if number == 1:
            return 1
        return number * factorial(number - 1)
    else:
        raise TypeError('Error: not int type')

print(factorial(1))
print(factorial(5))
