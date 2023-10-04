# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

import re


def isPalindrome(s):
    letras = "".join(re.sub(r"[^a-zA-Z0-9]", "", s)).lower()
    invert = letras[::-1]
    if letras == invert:
        return True
    return False


# Example usage:
s = "0P"
result = isPalindrome(s)
print(result)
