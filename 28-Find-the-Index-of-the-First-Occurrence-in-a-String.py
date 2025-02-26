#----------------------------------
'''
Brute force -
time complexity = o(nm) -> 2 strings
space complexity = O(1)

NO OPTIMIZED SOLUTION FOUND
AN ALTERNATE SOLUTION WITH WHILE IS WRITTER BELOW THE MAIN CODE
'''
#----------------------------------
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1