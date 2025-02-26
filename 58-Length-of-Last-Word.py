#----------------------------------
'''
optimised -
time complexity = o(k + n) -> k = number of spaces, n = length of the last word
space complexity = O(1)

NO OPTIMIZED SOLUTION FOUND
AN ALTERNATE SOLUTION WITH WHILE IS WRITTER BELOW THE MAIN CODE
'''
#----------------------------------
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s) -1
        length = 0
        while s[l] == " ":
            l -= 1
        while l>=0 and s[l] != " ":
            length += 1
            l -= 1
        return length