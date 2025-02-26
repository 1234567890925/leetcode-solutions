#----------------------------------
'''
Hash map -
time complexity = o(n) -> while loop, runs half time
space complexity = O(1)-> yes, hashmap has fixed number of element, and they are less
'''
#----------------------------------
class Solution:
    def romanToInt(self, s: str) -> int:
        letter_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        for i in range(len(s)-1):
            if letter_map[s[i]] < letter_map[s[i+1]]:
                total -= letter_map[s[i]]
            else:
                total += letter_map[s[i]]
        total += letter_map[s[-1]]
        return total