#1 - Two Sum
#Given an array of integers nums and an integer target, 
#return indices of the two numbers such that they add up to target.
def two_sum(nums, target):
    # Create a dictionary to store the complement of each number along with its index
    num_dict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            # If found, return the indices of the two numbers
            return ([num_dict[complement], i])
        
        # Otherwise, store the current number and its index in the dictionary
        num_dict[num] = i
    
    # If no solution is found, return an empty list or raise an exception as needed
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)