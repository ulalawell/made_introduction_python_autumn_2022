def divide_by_parity(numbers):
    even_numbers = []
    odd_numbers = []
    for element in numbers:
        if element % 2 == 0:
            even_numbers.append(element)
        else:
            odd_numbers.append(element)
    return even_numbers, odd_numbers


if __name__ == '__main__':
    assert divide_by_parity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
    assert divide_by_parity([1, 3, 5, 7, 9]) == ([], [1, 3, 5, 7, 9])
    assert divide_by_parity([2, 4, 6, 8, 10]) == ([2, 4, 6, 8, 10], [])

    print('ok')
