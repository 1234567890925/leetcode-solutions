class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        word = ''
        for idx, i in enumerate(haystack):
            word += i
            if needle in word:
                return idx - len(needle) + 1
        return -1