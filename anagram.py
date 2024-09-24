class Solution:
    def checkAnagram(self, s1, s2) -> bool:
        s1 = s1.replace(" ", '').lower()
        s2 = s2.replace(" ", "").lower()

        return sorted(s1) == sorted(s2)


res = Solution()
print(res.checkAnagram('Listen', 'silent'))
print(res.checkAnagram('Hello', 'World'))
