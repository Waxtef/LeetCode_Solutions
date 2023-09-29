# 905. Sort Array By Parity
# Given an integer array nums, move all the even integers at the beginning of the array
# followed by all the odd integers
# Example usage:
nums = [2, 1, 3, 4, 4, 6, 7]


def sortArrayByParity(nums):
    sorted_nums = sorted(nums, key=lambda x: x % 2 != 0)
    return sorted_nums


print(sortArrayByParity(nums))
