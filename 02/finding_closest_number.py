def find_closest_number_to_zero(numbers):
    closest_numbers = []

    if not numbers:
        return closest_numbers
    min_abs_value = abs(min(numbers, key=abs))

    for element in numbers:
        if abs(element) == min_abs_value:
            closest_numbers.append(element)
    return closest_numbers


if __name__ == '__main__':
    assert find_closest_number_to_zero([-5, 9, 6, -8]) == ([-5])
    assert find_closest_number_to_zero([-1, 2, -5, 1, -1]) == ([-1, 1, -1])
    assert find_closest_number_to_zero([5, 5, 5, -5, -5, -5]) == ([5, 5, 5, -5, -5, -5])
    assert find_closest_number_to_zero([]) == ([])

    print('ok')

