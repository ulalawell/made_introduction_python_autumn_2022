import math


def find_roots(a, b, c):
    determinant = b * b - 4 * a * c
    if determinant < 0:
        return None
    first_root = (-b + math.sqrt(determinant)) / (2 * a)
    second_root = (-b - math.sqrt(determinant)) / (2 * a)
    return first_root, second_root


if __name__ == '__main__':
    assert find_roots(1, 2, -3) == (1, -3)
    assert find_roots(4, 4, 1) == (-0.5, -0.5)
    assert find_roots(1, 1, 10) is None

    print('ok')
