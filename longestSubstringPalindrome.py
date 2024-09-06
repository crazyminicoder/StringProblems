def longestPalindrome(s: str) -> str:
    def isPalindrome(sub: str) -> bool:
        return sub == sub[::-1]

    ls = 0
    res = ''

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if isPalindrome(substring):
                if len(substring) > ls:
                    ls = len(substring)
                    res = substring

    return res


lss = longestPalindrome('absddsfg')
print(lss)
