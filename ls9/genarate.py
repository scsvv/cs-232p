""" magic """
def square_generator(n: int) -> int:
    """ action """
    for i in range(n):
        yield i ** 2

squares = square_generator(5)
for square in squares:
    print(square)
