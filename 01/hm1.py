import math


def divide_by_parity(numbers):
    even_numbers = []
    odd_numbers = []
    for element in numbers:
        if element % 2 == 0:
            even_numbers.append(element)
        else:
            odd_numbers.append(element)
    return even_numbers, odd_numbers


def find_roots(a, b, c):
    determinant = b * b - 4 * a * c
    if determinant < 0:
        return None
    first_root = (-b + math.sqrt(determinant)) / (2 * a)
    second_root = (-b - math.sqrt(determinant)) / (2 * a)
    return first_root, second_root


assert divide_by_parity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
assert divide_by_parity([1, 3, 5, 7, 9]) == ([], [1, 3, 5, 7, 9])
assert divide_by_parity([2, 4, 6, 8, 10]) == ([2, 4, 6, 8, 10], [])

assert find_roots(1, 2, -3) == (1, -3)
assert find_roots(4, 4, 1) == (-0.5, -0.5)
assert find_roots(1, 1, 10) is None

print('ok')