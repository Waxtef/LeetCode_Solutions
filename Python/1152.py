# 1512. Number of Good Pairs

# Example usage:
nums = [1, 2, 3, 1, 1, 3]


def numIdenticalPairs(nums):
    output = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  # To ensure i < j
            if nums[i] == nums[j]:
                output += 1

    return output


print(numIdenticalPairs(nums))
