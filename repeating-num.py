class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                print('s[r] = ', s[r])
                print('l = ', l)
                print('charset = ', charSet)
                charSet.remove(s[l])
                print('charset removed = ', charSet)
                l += 1
            charSet.add(s[r])
            #print('res = ', res)
            res = max(res, r - l + 1)
            #print('res added = ', res)
        return res

sol = Solution()
s = "abcabcbb"
res = sol.lengthOfLongestSubstring(s)
print(res)