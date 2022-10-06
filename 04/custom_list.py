"""
Module with implementation of custom list
"""

import itertools


class CustomList(list):
    """
    Implementation of custom list.
    Addition and subtraction operations are implemented element-wise.
    Comparison is made by the sum of the elements.
    Implemented method __str__
    """

    def __init__(self, data):
        super().__init__(data)

    def __add__(self, other):
        first_operand, second_operand = zip(*list(itertools.zip_longest(self, other, fillvalue=0)))
        return CustomList(map(sum, zip(first_operand, second_operand)))

    def __radd__(self, other):
        first_operand, second_operand = zip(*list(itertools.zip_longest(self, other, fillvalue=0)))
        return CustomList(map(sum, zip(first_operand, second_operand)))

    def __sub__(self, other):
        first_operand, second_operand = zip(*list(itertools.zip_longest(self, other, fillvalue=0)))
        return CustomList([x - y for x, y in zip(first_operand, second_operand)])

    def __rsub__(self, other):
        first_operand, second_operand = zip(*list(itertools.zip_longest(other, self, fillvalue=0)))
        return CustomList([x - y for x, y in zip(first_operand, second_operand)])

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        return f'({super().__str__()} sum is {sum(self)})'
