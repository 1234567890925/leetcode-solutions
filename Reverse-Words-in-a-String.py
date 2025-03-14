'''
Time complexity = O(n)
Space complexity = O(n)
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        l, r = 0, len(words)-1
        while l<r:
            temp = words[l]
            words[l] = words[r]
            words[r] = temp
            r -= 1
            l += 1
        return " ".join(words)