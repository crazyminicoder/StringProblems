import re
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Email checker:
# checks if the email entered is correct by matching the corresponding regex


class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        rev = res[::-1]
        if rev == res:
            return True
        else:
            return False

    def emailCheck(self, s: str) -> bool:
        emailRegex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z0-9-.]+$'
        if (re.match(emailRegex, s)):
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome('A man, a plan, a canal: Panama'))
print(s.emailCheck('name@domaincom'))
