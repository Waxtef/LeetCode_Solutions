# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
def isPalindrome(s):
    letras = "".join(c for c in s if c.isalpha())
    invert = letras[::-1]
    print(letras)
    print(invert)
    if letras == invert:
        return True
    return False


# Example usage:
s = "A man, a plan, a canal: Panama"
result = isPalindrome(s)
print(result)
