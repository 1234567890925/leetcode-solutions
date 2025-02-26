#----------------------------------
'''
Brute force-
time complexity = o(n) -> str_x = str(x): O(log n)
space complexity = O(n)
Hash map -
time complexity = o(log n) -> while loop, runs half time
space complexity = O(1)
'''
#----------------------------------
#Brute force :
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        reversed = str_x[::-1]
        if reversed == str_x:
            return True
        else:
            return False
        
# Optimised:
'''
right = x%10
left = while loop
handle 0
(x%div) chops left
'''

        if x == 0:
            return False
        div = 1
        while x > 10* div:
            div *= 10
        while x:
            right = x % 10
            left = x // div
            
            if right != left:
                 return False
            x = (x%div) // 10
            div = div // 100
        return True
            