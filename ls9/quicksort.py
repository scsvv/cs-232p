"""  quick sort """
from random import randint

def quicksort(numbers: list[int]) -> list[int]:
    """
        quicksort 
    """
    if len(numbers) <=1:
        return numbers

    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]

    return quicksort(left) + middle + quicksort(right)

number = [randint(1, 100) for _ in range(10)]
print(number)
number = quicksort(number)
print(number)
