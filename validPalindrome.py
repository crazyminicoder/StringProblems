import re
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        rev = res[::-1]
        if rev == res:
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome('A man, a plan, a canal: Panamb'))
