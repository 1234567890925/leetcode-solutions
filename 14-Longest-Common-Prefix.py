#----------------------------------
'''
Brute force -
time complexity = o(m*n) -> 2 loops on diff lists
space complexity = O(1)

Optimised:
time complexity = o(n) -> 1 loop
space complexity = 0(1)
'''
#----------------------------------
#Brute force
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
    
# optimised:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
