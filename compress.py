class Solution:
    def compress(self, s) -> str:
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        s = ''
        for keys, values in dict.items():
            s += keys + str(values)
        return s


res = Solution()
print(res.compress('aabcccccaaa'))
