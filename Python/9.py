# 9. Palindrome Number
def isPalindrome(x):
    x_list = str(x)
    invert = x_list[::-1]
    if x_list == invert:
        return True
    return False


x = 1213
print(isPalindrome(x))
