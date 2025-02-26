#----------------------------------
'''
optimised -
time complexity = o(log n) -> binary search
space complexity = O(1)

NO OPTIMIZED SOLUTION FOUND
AN ALTERNATE SOLUTION WITH WHILE IS WRITTER BELOW THE MAIN CODE
'''
#----------------------------------
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1  
            elif target < nums[mid]:
                right = mid - 1
        return left