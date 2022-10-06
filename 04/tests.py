"""
Module with tests for CustomList from custom_list.py module
"""

from custom_list import CustomList


def check_equality(list1, list2):
    """
    Function for element-wise comparison
    """
    if len(list1) != len(list2):
        return False

    for element1, element2 in zip(list1, list2):
        if element1 != element2:
            return False

    return True


if __name__ == '__main__':
    subtraction_result = CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7])
    correct_result = CustomList([4, -1, -4, 7])
    assert check_equality(subtraction_result, correct_result)

    subtraction_result = CustomList([3, 4]) - [1, 2]
    correct_result = CustomList([2, 2])
    assert check_equality(subtraction_result, correct_result)

    subtraction_result = [1, 2] - CustomList([3, 4])
    correct_result = CustomList([-2, -2])
    assert check_equality(subtraction_result, correct_result)

    sum_result = CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])
    correct_result = CustomList([6, 3, 10, 7])
    assert check_equality(sum_result, correct_result)

    sum_result = CustomList([3, 4]) + [1, 2]
    correct_result = CustomList([4, 6])
    assert check_equality(sum_result, correct_result)

    sum_result = [1, 2] + CustomList([3, 4])
    correct_result = CustomList([4, 6])
    assert check_equality(sum_result, correct_result)

    assert CustomList([5, 1, 3, 7]) == CustomList([16])
    assert CustomList([5, 1]) == CustomList([3, 3])

    print('ok')
