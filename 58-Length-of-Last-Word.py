class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s) -1
        length = 0
        while s[l] == \ \:
            l -= 1
        while l>=0 and s[l] != \ \:
            length += 1
            l -= 1
        return length