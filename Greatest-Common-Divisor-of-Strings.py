# Time complexity = O(n)
# Space complexity = O(1)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2)), 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                candidate = str1[:i]
                if str1 == candidate * (len(str1) // len(candidate)) and str2 == candidate * (len(str2) // len(candidate)):
                    return candidate
        return ""