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


assert merge([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7)) == ([1, 2, 7])
assert merge([1, 3, 5], ()) == ([])
assert merge([], (1, 3, 5)) == ([])
assert merge([], ()) == ([])
assert merge([1, 1, 1, 1], (1, 1, 1)) == ([1])

print('ok')
