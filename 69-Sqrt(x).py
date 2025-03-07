#----------------------------------
'''
optimised -
time complexity = o(log n) -> 1 while
space complexity = O(1)

NO OPTIMIZED SOLUTION FOUND
AN ALTERNATE SOLUTION WITH WHILE IS WRITTER BELOW THE MAIN CODE
'''
#----------------------------------
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            mid = l + ((r-l)//2)
            if mid**2 > x:
                r = mid - 1
            elif mid**2 < x:
                l = mid + 1
                res = mid
            else:
                return mid            
        return res