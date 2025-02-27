#----------------------------------
'''
Time Complexity: O(n log n) - Sorting dominates the time complexity.
Space Complexity: O(n) - Sorted strings require additional space proportional to input length.

Time Complexity: O(n)
Space Complexity: O(1)
'''
#----------------------------------
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s != sorted_t:
            return False
        return True
    
# Optimized:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = {}
        
        for char in s:
            #looks up value for char in hashmap, +1 adds the char to hashmap
            char_count[char] = char_count.get(char, 0) + 1 
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char] #char_count[] becomes 0, so we remove it
        
        return len(char_count) == 0
