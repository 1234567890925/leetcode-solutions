class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r-l+1) - max(count.values())>k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            print(f"Window: s[{l}:{r+1}] -> '{s[l:r+1]}', Length: {r-l+1}, Count: {count}, res: {res}")

        return res
sol = Solution()
s = "AAABABB"
k = 1
res = sol.characterReplacement(s, k)
print(res)