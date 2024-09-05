# The goal is to fing the longest substring without repeating characters
# "abcabcbc" -> output is: 3 'abc' is unique without any repeating chars
def longestSubSteing(s: str) -> int:
    char_set = set()
    left = 0
    maxLength = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        maxLength = max(maxLength, right-left+1)

    return maxLength


res = longestSubSteing('pwwke')

print("The max length is: ", res)
