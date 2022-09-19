def find_closest_number_to_zero(numbers):
    closest_numbers = []

    if not numbers:
        return closest_numbers
    min_abs_value = abs(min(numbers, key=abs))

    for element in numbers:
        if abs(element) == min_abs_value:
            closest_numbers.append(element)
    return closest_numbers


def merge(subsequence1, subsequence2):
    ptr1 = 0
    ptr2 = 0
    last_element = None
    merged_subsequence = []

    while ptr1 < len(subsequence1) and ptr2 < len(subsequence2):
        if subsequence1[ptr1] < subsequence2[ptr2]:
            ptr1 += 1
        elif subsequence1[ptr1] > subsequence2[ptr2]:
            ptr2 += 1
        else:
            if last_element != subsequence1[ptr1]:
                merged_subsequence.append(subsequence1[ptr1])
                last_element = subsequence1[ptr1]
            ptr1 += 1
            ptr2 += 1

    return merged_subsequence


assert find_closest_number_to_zero([-5, 9, 6, -8]) == ([-5])
assert find_closest_number_to_zero([-1, 2, -5, 1, -1]) == ([-1, 1, -1])
assert find_closest_number_to_zero([5, 5, 5, -5, -5, -5]) == ([5, 5, 5, -5, -5, -5])
assert find_closest_number_to_zero([]) == ([])

assert merge([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7)) == ([1, 2, 7])
assert merge([1, 3, 5], ()) == ([])
assert merge([], (1, 3, 5)) == ([])
assert merge([], ()) == ([])
assert merge([1, 1, 1, 1], (1, 1, 1)) == ([1])


print('ok')
