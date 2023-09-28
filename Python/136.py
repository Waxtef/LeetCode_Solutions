# 136 - Single Number
# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
# Example usage:
nums = [2, 2, 1, 1, 4]

for n in nums:
    count = nums.count(n)
    if count == 1:
        print(n)
