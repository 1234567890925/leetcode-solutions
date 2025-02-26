#----------------------------------
'''
Time Complexity: O(n log n) - Sorting dominates the time complexity.
Space Complexity: O(n) - Sorted strings require additional space proportional to input length.
'''
#----------------------------------
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s != sorted_t:
            return False
        return True