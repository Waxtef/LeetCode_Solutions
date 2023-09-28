# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
# Example usage:
nums = [2, 14, 1, 4, 4]


def containsDuplicate(nums):
    unique = set()
    for n in nums:
        if n in unique:
            return True
        unique.add(n)
    return False


print(containsDuplicate(nums))
