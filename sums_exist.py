from typing import List

"""
Problem description

Given a list of integers, check if the sum of any two integers in the list is not contained in the list.
For example with the list [4, 5, 15, 2, 8], there is no pair of integers where their sum is in the list. 
The list [8, 7, 5, 3] does not satisfy the criteria since the sum of 5 and 3 is in the list.
Write a python function which takes a list of integers and returns True if the list satisfies the criteria 
above, or False otherwise.
"""


def no_sums_exist(numbers_to_check: List[int]) -> bool:
    """ Are there any numbers in the input list which are the sum of two other numbers in the list?

    :param numbers_to_check: list of numbers to check against criteria
    :return: True if there are no sums in the input list
    """

    # the specification does not state what to do where the input list is None or empty
    # assume that this meets the criteria
    if not numbers_to_check:
        return True

    # sort in place
    numbers_to_check.sort()
    # to help with early termination, select the maximum input number
    max_number = numbers_to_check[-1]

    list_length = len(numbers_to_check)
    for left_index in range(list_length - 1):
        # index of the number which could be a sum matching a pair
        # to allow for negative numbers we need to start checking from 0
        candidate_index = 0
        for right_index in range(left_index + 1, list_length):
            # Number pairs must be at distinct indexes and constitute half the possible combinations
            assert left_index < right_index, f"Unexpected index pair {left_index}, {right_index}"

            pair_sum = numbers_to_check[left_index] + numbers_to_check[right_index]
            # if the sum of this pair is greater than the largest number in the list then all subsequent sums
            # will also be larger so we can stop looking at pairs with this left index now
            if pair_sum > max_number:
                break
            # move the candidate index through the list
            # until the sum of the current pair is the same or larger than the candidate
            while candidate_index < list_length and pair_sum >= numbers_to_check[candidate_index]:
                if numbers_to_check[candidate_index] == pair_sum:
                    return False
                candidate_index += 1
    return True
